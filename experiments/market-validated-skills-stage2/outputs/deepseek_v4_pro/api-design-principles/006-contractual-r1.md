# Bulk Contact Import API – Handoff to Downstream Reviewers

**Status:** Draft API contract for review.  
**Audience:** Security, Frontend, QA, Documentation teams.  
**Context:** Asynchronous bulk contact import with duplicate detection and PII. Frontend requires progress states.

---

## 1. Design Summary

- **Resource:** `BulkImport` represents an import job.
- **Async model:** Create job via `POST /bulk-imports`; track status via `GET /bulk-imports/{id}`.
- **Idempotency:** `POST` protected by `Idempotency-Key` header to prevent duplicate submissions.
- **Duplicate detection:** Handled server-side using configurable strategy (`error_on_duplicate`, `skip`, `overwrite`). Duplicate identification fields (e.g., `email`, `phone`) configurable per request.
- **PII:** Contact payload contains names, email addresses, phone numbers, and possibly other personally identifiable data. All responses must avoid leaking PII in logs or uncontrolled locations.
- **Progress:** Status includes lifecycle states (`pending`, `processing`, `completed`, `failed`) and metrics (`total_rows`, `processed_rows`, `duplicate_rows`, `error_rows`). Optionally, an errors endpoint for detailed feedback.
- **Observability:** `GET /bulk-imports/{id}/errors` to retrieve per-row errors (if any) with minimal PII exposure (error codes, row indices).

---

## 2. Proposed API Shape

### Create Import Job

```
POST /bulk-imports
Headers:
  Idempotency-Key: <client-generated unique key>
  Content-Type: application/json
  Authorization: Bearer <token>  (scope: contact:import)
```

**Request Body (illustrative):**
```json
{
  "file_url": "https://storage.example.com/imports/contacts.csv",   // secure, signed URL
  "mapping": {
    "first_name": "firstName",
    "last_name": "lastName",
    "email": "email",
    "phone": "phone",
    "company": "companyName"
  },
  "duplicate_strategy": "skip",           // or error_on_duplicate, overwrite
  "duplicate_fields": ["email", "phone"]  // fields to consider for match
}
```

**Response 201 Created:**
```json
{
  "id": "bui_3F7a9B2k",
  "status": "pending",
  "created_at": "2025-04-08T09:00:00Z",
  "links": {
    "self": "/bulk-imports/bui_3F7a9B2k",
    "errors": "/bulk-imports/bui_3F7a9B2k/errors"
  }
}
```

**Headers:** `Location: /bulk-imports/bui_3F7a9B2k`

**Possible errors:**
- 400: Bad Request (invalid mapping, unsupported strategy, missing file_url)
- 409: Idempotency conflict (same key, different body) – also indicate existing job id.
- 401/403: Unauthorized.
- 413: Payload too large for metadata (file itself is external)

### Track Import Status

```
GET /bulk-imports/{id}
Authorization: Bearer <token>
```

**Response 200 OK:**
```json
{
  "id": "bui_3F7a9B2k",
  "status": "processing",       // pending | processing | completed | failed
  "progress": {
    "total_rows": 5000,
    "processed_rows": 1200,
    "duplicate_rows": 45,
    "error_rows": 3
  },
  "error_summary": {
    "has_errors": true,
    "errors_url": "/bulk-imports/bui_3F7a9B2k/errors"
  },
  "created_at": "2025-04-08T09:00:00Z",
  "completed_at": null
}
```

### Retrieve Import Errors

```
GET /bulk-imports/{id}/errors
Authorization: Bearer <token>
Query: ?page=1&page_size=100
```

**Response 200 OK (paginated, with no PII in logs):**
```json
{
  "data": [
    {
      "row_index": 15,
      "error_code": "INVALID_EMAIL",
      "field": "email",
      "detail": "Value does not match email pattern"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_items": 3,
    "next_page": null
  }
}
```
> Note: The detail intentionally avoids echoing raw PII.

### Additional requirements
- **Authentication:** Bearer token with scope `contact:import` (exact permission model to be reviewed by Security).
- **Rate limiting:** TBD (likely per-account and per-user). Consider 429 response with `Retry-After`.
- **Versioning:** API path uses `/v1/` prefix if versioning is required; currently assumed `/bulk-imports` as first stable version. Human gate for breaking changes.
- **Schema validation:** All inputs validated against strict schemas. File URL must be HTTPS and signed; service must reject unsigned internal URLs.

---

## 3. Key Tradeoffs

1. **Direct file upload vs. file_url:**  
   - **Chosen:** file_url to keep import service stateless and avoid handling large request bodies. Requires secure, pre-signed storage.  
   - **Tradeoff:** Adds coupling to a file store; frontend must first upload file.

2. **Polling vs. webhooks for progress:**  
   - **Chosen:** polling via `GET /bulk-imports/{id}`. Simpler to implement, no callback infrastructure needed.  
   - **Tradeoff:** Higher network churn for frontend, potential for stale views. Webhooks could be added later as an enhancement.

3. **Duplicate detection granularity:**  
   - **Chosen:** Configurable `duplicate_fields` per request.  
   - **Tradeoff:** Flexibility for different customer data formats, but complex server logic and potential inconsistency if fields are misconfigured.

4. **Error detail exposure:**  
   - **Chosen:** Structured error codes, row index, field name, generic detail; original PII values omitted.  
   - **Tradeoff:** Debugging may require file-level correlation; operators may need access to raw data under controlled conditions.

---

## 4. Risks and Human Gates (per team)

### Security
- **PII stored and processed:** Contacts contain personally identifiable data.  
  - **Risk:** Exposure in logs, error messages, or unintentional return values.  
  - **Gates:**  
    - Human approval required on auth scopes and any granting of raw data access.  
    - Review encryption in transit (TLS) and at rest.  
    - Review logging and monitoring to ensure PII redaction.  
    - Audit file storage access (signed URLs with expiration).  
- **Idempotency key handling:** Must validate that repeated keys with mismatched body are rejected safely.  
- **Injection attacks:** Validate all inputs against schema; reject unexpected parameters.

### Frontend
- **Progress states:** Need to map status values (`pending`, `processing`, `completed`, `failed`) to UI.  
  - **Gate:** Human approval for any UI that displays raw error details or exposes PII inadvertently (e.g., showing full email in error toast).  
- **Polling interval and backoff:** Must implement exponential backoff to avoid hammering the server.  
- **File upload flow:** Frontend must upload file to storage, receive signed URL, then POST import. This sequence must be secure and handle failures gracefully.

### QA
- **Contract tests:** All endpoints must have contract tests covering happy path, auth failures, idempotency conflicts, missing fields, invalid duplicate strategies, and error scenarios.  
- **PII test data:** Test data must not contain real PII; use synthetic profiles.  
- **Performance:** Validate that progress tracking remains accurate under concurrent imports and large files.  
- **Verification criteria:**  
  - Async job completes in reasonable time.  
  - Duplicate detection matches specification.  
  - Errors are returned with correct row indices and codes.  
  - Idempotency prevents duplicate jobs.  
  - No PII leaks in API responses or error details.

### Documentation
- **Developer examples:** Provide clear request/response examples (using illustrative data, no real PII).  
  - **Gate:** Human review of public-facing examples to ensure no real data.  
- **Authentication/authorization flows:** Document how to obtain `contact:import` scope.  
- **Error codes catalog:** List all possible error codes and remediation steps.  
- **File format requirements:** Document accepted column mappings, supported file formats (CSV with headers), size limits.

---

## 5. Verification Checklist (before implementation proceeds)

### General (all teams)
- [ ] API design approved by architecture/platform owner.
- [ ] Breaking changes declared or avoided; versioning strategy confirmed.
- [ ] No assumption of deployed/tested status; contract tests created.

### Security
- [ ] Auth model and scopes approved.
- [ ] PII handling plan (encryption, masking, log redaction) verified.
- [ ] File URL validation prevents SSRF.
- [ ] Rate limiting and abuse prevention defined.

### Frontend
- [ ] UI progress states and error display reviewed (no PII exposure).
- [ ] File upload + import creation sequence fails safely.
- [ ] Polling strategy with backoff implemented.

### QA
- [ ] Contract tests written for all endpoints, covering idempotency, error edges, and auth.
- [ ] Test data is synthetic, not real PII.
- [ ] Performance/scalability baselines established.

### Documentation
- [ ] Public documentation examples reviewed for PII risk.
- [ ] Error catalog and mapping requirements published.
- [ ] Developer quickstart prepared for internal/external consumers.

---

*This handoff contains draft API contract proposals. It is not a claim of deployment, testing, or final approval. All human gates must be satisfied before committing to the public API.*
