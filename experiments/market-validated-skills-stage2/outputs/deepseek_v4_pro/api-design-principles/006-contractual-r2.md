# API Design Handoff: Bulk Contact Import

## 1. Design Summary

The bulk contact import is modelled as an asynchronous job.  
A client creates an import job, receives an identifier, and polls for progress.  
Duplicate detection runs within the job; the result exposes counts of imported, duplicate, and errored contacts.  
Frontend progress states map to a small, well-defined job status machine.  
PII is present, requiring encryption in transit and at rest, and strict access control.

**Key decisions**  
- Asynchronous processing with polling (webhooks can be added later).  
- Idempotent creation using an `Idempotency-Key` header.  
- Versioned under `/v1/` to allow future breaking changes.  
- File upload is decoupled via a pre-signed object store URL (exact storage provider and signing mechanism are not defined here; security and platform must agree on the mechanism).

---

## 2. Proposed API Shape

All endpoints live under `/v1/contacts/imports`.  
No existing OpenAPI fragment was supplied—all schemas are illustrative.

### 2.1 Create an import  
`POST /v1/contacts/imports`  
**Request**  
- Headers: `Idempotency-Key` (required, UUID v4)  
- Content-Type: `application/json`  
```json
{
  "importFileUrl": "https://objectstore.example.com/files/abc.csv?signature=...",
  "duplicateDetection": {
    "strategy": "email",              // "email" | "phone" | "exact"
    "matchFields": ["email"],         // based on strategy; illustrative
    "action": "skip"                  // "skip" | "mark"
  }
}
```
**Response**  
`202 Accepted`  
`Location: /v1/contacts/imports/550e8400-e29b-41d4-a716-446655440000`  
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "createdAt": "2025-03-27T10:15:30Z",
  "sourceFile": "https://objectstore.example.com/files/abc.csv?signature=...",
  "progress": {
    "totalRows": null,
    "imported": 0,
    "duplicates": 0,
    "errors": 0
  }
}
```
**Errors**  
- `400 Bad Request` – invalid file URL, unsupported strategy  
- `409 Conflict` – idempotency key reused for a different payload (return existing job if identical)  
- `413 Payload Too Large` – file size beyond limit  
- `429 Too Many Requests` – rate limit  

### 2.2 Get import status  
`GET /v1/contacts/imports/{id}`  
**Response**  
`200 OK`  
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "processing",             // "pending" | "processing" | "completed" | "failed" | "cancelled"
  "createdAt": "2025-03-27T10:15:30Z",
  "updatedAt": "2025-03-27T10:16:05Z",
  "progress": {
    "totalRows": 5000,
    "imported": 3200,
    "duplicates": 150,
    "errors": 50
  },
  "errorSummary": {
    "message": null,
    "code": null
  }
}
```
- `404 Not Found` if id does not exist.  

### 2.3 Download results (optional, recommended)  
`GET /v1/contacts/imports/{id}/results?type=duplicates|errors`  
- Returns `200` with `Content-Type: text/csv` containing affected rows and reasons.  
- Intent: frontend can provide a link after job completion.

### 2.4 Common error shape  
RFC 7807 Problem Detail (`application/problem+json`):  
```json
{
  "type": "https://api.example.com/errors/invalid-request",
  "title": "Invalid file URL",
  "status": 400,
  "detail": "The import file URL must be a valid signed object store link.",
  "instance": "/v1/contacts/imports/..."
}
```

### 2.5 Security & authentication  
- All endpoints require a valid OAuth 2.0 access token with the scope `contacts:import`.  
- Missing/invalid token → `401 Unauthorized`; insufficient scope → `403 Forbidden`.  
- No sensitive PII is returned in the import status; only aggregate counts. The actual file content must be restricted to the internal processing pipeline.

---

## 3. Key Tradeoffs

| Decision | Alternative considered | Rationale |
|----------|------------------------|-----------|
| Polling for progress | Webhooks / Server-Sent Events | Polling is simpler for initial delivery; webhooks can be added later. Frontend teams prefer explicit control over polling and error handling. |
| File upload via signed URL | Direct multipart upload in the same request | Decouples large file handling, avoids oversized request issues, and lets the API stay lightweight. Signed URLs require extra platform agreement. |
| Duplicate detection inside the job | Client-side pre-detection | Server-side ensures consistent duplicate logic; client cannot be trusted to hold the full duplicate dataset. Adds latency but aligns with async design. |
| Idempotency via header | Separate deduplication endpoint | Header approach is standard, keeps resources clean, and aligns with IETF draft. Idempotency key stored for 24h; after that, a new job may be created. |
| Versioning in URL path | Content negotiation | Path versioning is visible, trivial to route, and easy for consumers. It does require human approval to introduce a new version. |

---

## 4. Risks and Human Gates

**Risks requiring review before production commit**

| Risk | Owner(s) | Mitigation |
|------|----------|------------|
| PII exposure in transit/at rest | Security | Enforce TLS 1.2+, require AES-256 at rest, review signed URL expiry and access logging. |
| PII leaking through error messages or progress counters | Security + QA | Audit response payloads; aggregate counts only, never expose raw PII fields. |
| Duplicate detection algorithm may reveal existence of contacts | Security + Legal | Match on hashed tokens / bloom filters if needed; review strategy with privacy team. |
| Frontend mis-interprets progress states (e.g., missing “retrying”) | Frontend + QA | Explicit state machine: pending → processing → completed / failed / cancelled. Add `retrying` only if transient failures are surfaced; keep it lean. |
| Idempotency key reuse conflict | Platform | Clearly define conflict resolution: identical payload returns 200 (existing job), different payload returns 409 and rejects. |
| Rate limiting exhaustion | Platform | Apply per-client and per-user rate limits on creation endpoint; return `429` with Retry-After. |
| Breaking changes to status model or error codes | Product + Engineering | Respect semantic versioning; hold a human review for any change that breaks existing polling logic. |

**Human gates (explicit approval required)**  
- Introduction of a new API version (e.g., `/v2/`).  
- Changes to authentication/authorization scopes.  
- Adding or removing PII-related fields in responses.  
- Changing idempotency semantics.  
- Altering duplicate detection strategies that impact existing customer data.  
- Commitment to a public SLA for polling responsiveness.  
- Any production migration of this API to a different domain/path.

---

## 5. Verification Checklist

### For Security  
- [ ] Review data flow: how file is uploaded, stored, and accessed by the processing pipeline.  
- [ ] Confirm all endpoints require appropriate OAuth scopes and reject unauthorized access.  
- [ ] Validate that no raw PII appears in API responses (status, error, or result download).  
- [ ] Verify signed URL expiration, permissions, and audit logging are in place.  
- [ ] Check that error messages in the Problem Detail body do not disclose internal paths or data.  
- [ ] Sign off on duplicate detection side-channel risks.

### For Frontend  
- [ ] Provide an OpenAPI specification and a mock server exposing the full status lifecycle.  
- [ ] Agree on polling interval and back-off strategy (e.g., 2 seconds while processing, exponential backoff on error).  
- [ ] Test all status transitions (pending → processing → completed, failed, cancelled) including network interruptions.  
- [ ] Verify error rendering for 401, 403, 404, 409, 413, 429, and 5xx.  
- [ ] Review whether a “download results” link is needed and coordinate UX.

### For QA  
- [ ] Create contract tests for all endpoints using the OpenAPI spec.  
- [ ] Idempotency: same key with same body returns the existing job; different body returns 409.  
- [ ] Status polling: verify progress counters increase and become final when status is terminal.  
- [ ] Duplicate detection: feed a known CSV with duplicates for `email` and `phone` strategies; assert counts.  
- [ ] Error scenarios: expired signed URL, malformed CSV, oversized file, missing scope, missing idempotency key.  
- [ ] Rate limiting: trigger 429 and confirm Retry-After header.

### For Documentation  
- [ ] Write a developer guide covering:  
   - Authentication and scopes.  
   - Creating a job (idempotency key usage).  
   - File upload flow (pre-signed URL) and supported formats.  
   - Polling for status and interpreting the state machine.  
   - Downloading duplicate/error reports.  
   - Rate limits and error handling.  
- [ ] Provide request/response examples for each endpoint, including common failure cases.  
- [ ] Clarify idempotency key lifetime (24h) and conflict behavior.

---

**Note** All examples above are illustrative, derived from the stated requirements and general design patterns. No API has been deployed, tested, or approved. The exact duplicate detection fields, file upload mechanism, and auth model must be confirmed with the owning teams before finalising the contract.
