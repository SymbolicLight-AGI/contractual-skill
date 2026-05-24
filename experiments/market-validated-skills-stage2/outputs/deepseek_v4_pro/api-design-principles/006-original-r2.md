## Bulk Contact Import API – Draft Contract for Reviewer Handoff

### 1. Overview & Use Case Definition

- **Consumers**: Internal web frontend (primary), mobile apps (secondary), potential third‑party CRM integrations via partner keys.  
- **Use Cases**:  
  - Upload CSV/JSON files or provide a URL to a file containing contacts.  
  - Validate, deduplicate, and import contacts asynchronously.  
  - Surface real‑time progress and final outcome to frontend.  
  - Respect PII data‑handling requirements.  
- **Constraints**:  
  - Import must be asynchronous (files up to 100K rows).  
  - Duplicate detection against existing contacts (based on email/phone) must run before importing new records.  
  - All PII (names, emails, phones) must be encrypted in transit and at rest; access must be auditable.  
  - Frontend needs progress states (queued, processing, completed, failed) and summary counts.

### 2. API Style & Resource Model

**Style**: RESTful, using resource‑oriented URLs, JSON payloads, standard HTTP methods, and status codes.  

**Primary Resource**: `ContactImportJob`  

| Attribute       | Type      | Description |
|-----------------|-----------|-------------|
| `id`            | UUID      | Unique job identifier |
| `status`        | enum      | `PENDING`, `VALIDATING`, `IMPORTING`, `COMPLETED`, `FAILED`, `CANCELLED` |
| `progress`      | object    | `{ processed: int, total: int, percentage: float }` |
| `summary`       | object    | `{ created: int, updated: int, duplicates: int, errors: int }` |
| `error_details` | array     | List of per‑row errors (masked PII) |
| `created_at`    | timestamp | ISO‑8601 |
| `completed_at`  | timestamp | ISO‑8601 |
| `source`        | object    | Original file metadata (name, size) – no raw data stored after processing |

**Sub‑resource for results** (if needed later): `/jobs/{id}/results` – paginated list of processed contacts (PII‑aware).  

**Versioning**: URI prefix `/v1/` to allow safe evolution.

### 3. Endpoints

#### 3.1 Create Import Job
```
POST /v1/contact-import-jobs
```
**Request** (multipart/form-data or JSON with pre‑signed URL):
- `file`: binary file, or `source_url`: string (pre‑signed S3 URL).
- `options`: object
  - `dedup_strategy`: `"strict"` (email+phone) | `"email_only"` | `"phone_only"`
  - `field_mapping`: map of CSV columns to contact schema fields

**Response**: `201 Created`  
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "PENDING",
  "links": {
    "self": "/v1/contact-import-jobs/550e8400-...",
    "cancel": "/v1/contact-import-jobs/550e8400-.../cancel"
  }
}
```

**Auth**: OAuth2 bearer token with scope `contacts:write`.  
**Rate limit**: 10 jobs per minute per tenant.

#### 3.2 Get Job Status (Progress)
```
GET /v1/contact-import-jobs/{id}
```
**Response**: `200 OK`  
```json
{
  "id": "550e8400-...",
  "status": "IMPORTING",
  "progress": { "processed": 1200, "total": 5000, "percentage": 24.0 },
  "summary": null,
  "created_at": "2026-03-15T10:00:00Z"
}
```
When `status` is `COMPLETED` or `FAILED`, `summary` is populated. `error_details` may be included if errors occurred (row index + sanitized message, no raw PII).

**Auth**: Bearer token, scope `contacts:read`.  

#### 3.3 Cancel Job
```
POST /v1/contact-import-jobs/{id}/cancel
```
**Response**: `200 OK` with updated status `CANCELLED`.

### 4. Error Handling Strategy

All errors follow [RFC 7807 Problem Details](https://datatracker.ietf.org/doc/html/rfc7807).  
Example:
```json
{
  "type": "https://api.example.com/errors/invalid-file",
  "title": "Invalid file format",
  "status": 422,
  "detail": "Uploaded file must be a valid CSV or JSON.",
  "instance": "/v1/contact-import-jobs/550e8400-..."
}
```

For async processing failures, the job object itself will contain `error_details` with sanitized messages (never exposing raw PII).

### 5. Pagination

- **List jobs**: `GET /v1/contact-import-jobs` returns cursor‑based pagination (next/prev links).  
- **Job results** (future): offset/limit with max page size 100, scoped to job.

### 6. Authentication & Authorization

- All endpoints require OAuth2 tokens.
- Scopes: `contacts:read`, `contacts:write`, `contacts:admin` (for bulk operations).
- API key option for server‑to‑server integrations (scoped, short‑lived, IP‑restricted).
- All tokens transmitted via `Authorization: Bearer` header; no PII in query strings.

### 7. PII & Privacy Guardrails

- Files uploaded are encrypted in transit (TLS 1.2+), stored temporarily with AES‑256 at rest, and deleted after processing.
- Access logs omit PII; only job IDs are logged.
- Response objects never return raw PII from the original file; only validation errors with masked data (e.g., `j***@domain.com`) when absolutely necessary.
- Data retention policy: original files deleted immediately after import completion; job metadata retained for 30 days.

---

## Handoff Notes to Downstream Reviewers

### 🔒 For Security Review
1. **AuthZ scopes**: Validate that the proposed scopes (`contacts:read`, `contacts:write`, `contacts:admin`) are granular enough and do not over‑privilege the frontend.
2. **PII handling**: Ensure the contract enforces encryption at rest for uploaded files, immediate deletion after processing, and no PII leakage in logs or error responses.
3. **Duplicate detection**: Confirm that the deduplication logic (email/phone matching) does not inadvertently expose existing PII to unauthorized callers.
4. **URL pre‑signed upload**: Review the temporary URL mechanism; ensure it is hardened against path traversal, CSRF, and replay.
5. **Rate limiting & abuse**: Validate job creation limits (10/min) and consider payload size limits (max 100K rows, 10 MB file) to prevent resource exhaustion.
6. **Token handling**: Verify that OAuth2 and API key flows are consistent with the existing IAM service; no PII in tokens or audit trails.
7. **Data retention**: Sign off on file deletion and metadata retention (30 days). Ensure compliance with data protection regulations.

### 🎨 For Frontend Review
1. **Progress states**: The job status enum and `progress` object cover all UI states: pending → validating → importing → completed/failed/cancelled. Please confirm this maps to your loading indicators and progression UI.
2. **Polling vs WebSocket**: The contract assumes polling via `GET /jobs/{id}`. If real‑time updates are needed, we can add a WebSocket event stream later (not in v1). Is polling acceptable for the MVP?
3. **Error summaries**: After completion, the `summary` and `error_details` provide counts and row‑level errors (with masked PII). Does the error detail format (`row_index`, `message`) work for displaying in an error summary table?
4. **File upload**: The multipart/file upload or pre‑signed URL approach – which does the frontend prefer? We recommend pre‑signed URLs for large files to offload bandwidth from API server.
5. **Cancellation**: The `cancel` endpoint allows immediate stop; ensure the UI can handle the transition to `CANCELLED` state without confusion.
6. **Field mapping flexibility**: The `options.field_mapping` allows mapping CSV columns to contact fields. Does the UI need a preview step to let users adjust mapping? If yes, we may need a separate validation endpoint (`POST …/validate`).

### 🔍 For QA Review
1. **Test scenarios**:
   - Happy path: upload a valid CSV, verify status transitions, summary counts.
   - Duplicate handling: file with all duplicates → summary shows duplicates, no new contacts created.
   - Mixed duplicates/new: verify correct counts.
   - Large payload (100K rows): performance and timeout handling.
   - Malformed file: 422 response with descriptive Problem Details.
   - Unauthorized access: 401/403 responses.
   - Rate limiting: exceed limit → 429.
   - Cancel during processing: job status becomes `CANCELLED`, no partial import.
2. **Async contract**: No synchronous return of full result; test that polling consistently returns correct progress and final summary.
3. **Error format compliance**: Ensure all error responses adhere to RFC 7807 and have consistent `type` URIs.
4. **PII leakage**: Negative tests to confirm that error responses, logs, and job status responses never expose raw email/phone/names from the source file.
5. **Idempotency**: If the same file is uploaded twice, what happens? Should be documented; QA should validate that duplicate upload does not create duplicates if dedup is on (or returns `409 Conflict` with existing job ID if detected as identical file).

### 📚 For Documentation Review
1. **Developer onboarding**: The contract already defines resource model, endpoints, authentication, errors, and pagination. Please structure the public API docs around:
   - “Quickstart” – creating first import job with cURL examples.
   - Authentication section with scope requirements.
   - Full endpoint reference (request/response examples, including error shapes).
   - A guide on field mapping supported by the import.
   - A “Status and Progress” concept page explaining polling and state machine.
2. **PII safety warnings**: Explicitly state that the API never returns raw PII from the upload file and that error details are masked. Add a note about data retention.
3. **Code samples**: Provide snippets for JavaScript fetch and a Python SDK if applicable.
4. **Glossary**: Define “Contact Import Job”, “Deduplication Strategy”, “Pre‑signed URL”, “Problem Details”.
5. **Changelog**: Version prefix `/v1` should be documented with a changelog placeholder for future breaking changes.

---

**Next Steps**

- Please review the sections relevant to your domain and add feedback as comments or requests for change in this document.
- Any missing requirements (e.g., webhooks for completion, batch abort, RBAC)? Raise them now so we can incorporate them before implementation.
- Once all reviews are approved, the contract will be frozen for `v1` implementation.

*End of handoff.*
