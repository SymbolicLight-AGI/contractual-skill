## 1. Design summary

### Supplied facts

- The API supports **bulk contact import**.
- Imports are **asynchronous**.
- **Duplicate detection is required**.
- The workflow involves **PII**.
- The frontend needs **progress states**.

### Recommended contract direction

Model bulk import as an asynchronous **import job** resource:

- Client creates an import job.
- Server validates and processes the uploaded contacts asynchronously.
- Client polls or subscribes to job status for progress.
- Duplicate detection results are exposed in a controlled, privacy-aware way.
- Import results are available after completion, with clear success, partial failure, and failure states.

This handoff should be reviewed by:

- **Security** for PII handling, authorization, retention, duplicate visibility, audit logging, and abuse controls.
- **Frontend** for progress state ergonomics and error/result rendering.
- **QA** for contract, state-machine, duplicate, and failure-case testing.
- **Docs** for developer-facing examples, lifecycle explanation, and privacy caveats.

---

## 2. Proposed API shape

The following is an illustrative API contract proposal, not a deployed or approved design.

### Resource model

Primary resource:

```text
ContactImport
```

Represents a bulk contact import job.

Related concepts:

```text
ContactImportItem
DuplicateCandidate
ImportError
```

These may be separate resources or embedded summaries depending on privacy and scale requirements.

---

### Create an import job

```http
POST /contact-imports
```

Creates an asynchronous contact import job.

#### Request body, illustrative

```json
{
  "source": "csv_upload",
  "file_id": "file_123",
  "duplicate_strategy": "skip_existing",
  "metadata": {
    "original_filename": "contacts.csv"
  }
}
```

#### Notes

- If contacts are uploaded as a file, prefer referencing a previously uploaded `file_id` rather than sending large contact arrays directly in this endpoint.
- If direct JSON import is required, define a separate shape and size limits.
- Because this is a write API, support **idempotency**.

#### Required headers

```http
Idempotency-Key: 2f4b8e3a-9b4e-4d2a-9a41-...
```

#### Response

```http
202 Accepted
Location: /contact-imports/import_123
```

```json
{
  "id": "import_123",
  "status": "queued",
  "progress": {
    "total": null,
    "processed": 0,
    "succeeded": 0,
    "failed": 0,
    "duplicates": 0
  },
  "created_at": "2026-05-24T12:00:00Z",
  "updated_at": "2026-05-24T12:00:00Z"
}
```

#### Status code guidance

- `202 Accepted` when the job is accepted for async processing.
- `400 Bad Request` for malformed requests.
- `401 Unauthorized` if caller is not authenticated.
- `403 Forbidden` if caller lacks permission to import contacts.
- `404 Not Found` if referenced upload/file does not exist or is inaccessible.
- `409 Conflict` for conflicting duplicate/idempotency conditions if applicable.
- `413 Payload Too Large` if direct upload exceeds limits.
- `415 Unsupported Media Type` if upload format is unsupported.
- `422 Unprocessable Entity` if request is syntactically valid but semantically invalid.
- `429 Too Many Requests` for rate or abuse limits.

---

### Get import status

```http
GET /contact-imports/{import_id}
```

Returns the current state and progress of an import.

#### Response, illustrative

```json
{
  "id": "import_123",
  "status": "processing",
  "progress": {
    "total": 1000,
    "processed": 450,
    "succeeded": 420,
    "failed": 10,
    "duplicates": 20
  },
  "duplicate_detection": {
    "status": "in_progress",
    "strategy": "skip_existing"
  },
  "created_at": "2026-05-24T12:00:00Z",
  "started_at": "2026-05-24T12:00:05Z",
  "updated_at": "2026-05-24T12:01:30Z",
  "completed_at": null,
  "links": {
    "self": "/contact-imports/import_123",
    "errors": "/contact-imports/import_123/errors",
    "duplicates": "/contact-imports/import_123/duplicates"
  }
}
```

---

### Suggested status lifecycle

Use an explicit state machine.

```text
queued
validating
processing
completed
completed_with_errors
failed
cancelled
```

Optional states if useful:

```text
duplicate_review_required
expired
```

#### State guidance

| Status | Meaning |
|---|---|
| `queued` | Job accepted but not started. |
| `validating` | File or payload is being parsed and validated. |
| `processing` | Contacts are being imported. |
| `completed` | All valid contacts processed successfully. |
| `completed_with_errors` | Some contacts imported, some failed or were skipped. |
| `failed` | Import could not complete due to job-level error. |
| `cancelled` | User or system cancelled the import. |
| `duplicate_review_required` | Optional state if duplicates require user decision. |
| `expired` | Optional state if job/result details are no longer available due to retention limits. |

Frontend should not infer behavior from progress counters alone. It should rely on the `status` field as the source of truth.

---

### List import jobs

```http
GET /contact-imports
```

Returns import jobs visible to the caller.

#### Query parameters, illustrative

```text
status=processing
created_after=2026-05-01T00:00:00Z
created_before=2026-05-24T00:00:00Z
limit=50
cursor=abc123
```

#### Response

```json
{
  "data": [
    {
      "id": "import_123",
      "status": "completed_with_errors",
      "progress": {
        "total": 1000,
        "processed": 1000,
        "succeeded": 930,
        "failed": 40,
        "duplicates": 30
      },
      "created_at": "2026-05-24T12:00:00Z",
      "completed_at": "2026-05-24T12:05:00Z"
    }
  ],
  "pagination": {
    "next_cursor": null
  }
}
```

Use cursor pagination rather than offset pagination if import history can grow or change during paging.

---

### Get import errors

```http
GET /contact-imports/{import_id}/errors
```

Returns item-level validation or processing errors.

#### Query parameters

```text
limit=50
cursor=abc123
```

#### Response, illustrative

```json
{
  "data": [
    {
      "row_number": 42,
      "code": "invalid_email",
      "message": "Email address is invalid.",
      "field": "email"
    }
  ],
  "pagination": {
    "next_cursor": "def456"
  }
}
```

#### PII caution

Avoid returning full contact records in errors unless explicitly approved by security and product. Prefer:

- `row_number`
- field name
- error code
- sanitized message

---

### Get duplicate results

```http
GET /contact-imports/{import_id}/duplicates
```

Returns duplicate detection outcomes for the import.

#### Response, illustrative

```json
{
  "data": [
    {
      "row_number": 17,
      "duplicate_type": "existing_contact",
      "resolution": "skipped",
      "matched_contact_id": "contact_789"
    }
  ],
  "pagination": {
    "next_cursor": "ghi789"
  }
}
```

#### PII caution

The duplicate endpoint is security-sensitive. It may reveal that a person or email already exists in the system. Review whether `matched_contact_id` is safe to expose to the caller. Consider returning only counts or masked identifiers if necessary.

---

### Cancel an import job

Optional, if product requires cancellation.

```http
POST /contact-imports/{import_id}:cancel
```

Alternative REST shape:

```http
POST /contact-imports/{import_id}/cancellation
```

#### Response

```json
{
  "id": "import_123",
  "status": "cancelled"
}
```

#### Notes

Cancellation behavior must be explicit:

- Is cancellation best-effort?
- Can already-imported contacts be rolled back?
- Is partial import acceptable?
- What status is returned if cancellation is requested after completion?

This requires product and backend approval before commitment.

---

### Error response model

Use a consistent error envelope.

```json
{
  "error": {
    "code": "invalid_import_file",
    "message": "The uploaded file could not be parsed.",
    "details": [
      {
        "field": "file_id",
        "reason": "File format is unsupported."
      }
    ],
    "request_id": "req_123"
  }
}
```

#### Error contract requirements

- `code`: stable, machine-readable.
- `message`: safe for display or explicitly marked internal.
- `details`: optional structured field errors.
- `request_id`: required for support and observability.

Do not include raw PII in error messages.

---

## 3. Key tradeoffs

### Polling versus push updates

#### Polling with `GET /contact-imports/{id}`

Pros:

- Simple to implement.
- Easy to test.
- Works across most clients.

Cons:

- Can increase load.
- Frontend must manage polling interval and backoff.

#### Server-sent events, WebSockets, or webhooks

Pros:

- Better real-time progress.
- Less repeated polling.

Cons:

- More operational complexity.
- Harder auth/session handling.
- More edge cases for reconnects.

Recommendation: start with polling unless real-time updates are a strict requirement. Define safe polling guidance such as every few seconds with exponential backoff, but final limits should align with platform rate-limit standards.

---

### Duplicate result detail versus privacy

More detailed duplicate information helps users resolve import issues, but it can expose sensitive relationship or existence data.

Options:

1. Return only counts.
2. Return row-level duplicate status without matched contact identifiers.
3. Return matched internal contact IDs.
4. Return masked contact hints.
5. Return full matched contact details.

Recommendation: default to the least sensitive form that supports the product need. Security must approve any matched identifiers or contact details.

---

### Synchronous validation versus async validation

The create endpoint can perform lightweight synchronous validation, such as checking request shape and file existence, while heavy validation should happen asynchronously.

Recommendation:

- Synchronous: auth, permissions, idempotency, file existence, supported type, basic request validity.
- Asynchronous: file parsing, row validation, duplicate detection, contact creation.

---

### Partial success behavior

The API must clearly define whether a job can partially succeed.

Recommended statuses:

- `completed` for full success.
- `completed_with_errors` for partial success.
- `failed` for job-level failure where import did not complete.

Product must confirm whether partial import is acceptable and whether rollback is required.

---

### Idempotency

Because import creation can create many records, the create endpoint should require or strongly support `Idempotency-Key`.

Expected behavior:

- Same key and same request returns the original job.
- Same key and different request returns an idempotency conflict.
- Idempotency key retention period must be defined by platform/product.

This needs platform alignment.

---

## 4. Risks and human gates

### Security handoff

Security should review and approve:

- Which PII fields may be accepted, stored, logged, returned, or masked.
- Authorization model:
  - Who can create imports?
  - Who can view import status?
  - Who can view errors?
  - Who can view duplicate results?
  - Are permissions scoped by workspace, account, tenant, or owner?
- Whether duplicate detection leaks existence of contacts.
- Whether `matched_contact_id` or other duplicate identifiers are safe to expose.
- File upload scanning requirements.
- Rate limits and abuse prevention for bulk imports.
- Audit logging requirements.
- Data retention for uploaded files, parsed rows, import errors, and duplicate results.
- Whether raw uploaded files should be encrypted, quarantined, or deleted after processing.
- Whether PII is excluded from application logs, metrics, traces, and error reports.
- Access boundaries for support/admin tooling.

Human gate: security approval is required before exposing duplicate details, storing uploaded contact files, or returning any PII in API responses.

---

### Frontend handoff

Frontend should review:

- Whether the proposed status lifecycle supports the desired UX.
- Which statuses need user-facing copy.
- Whether progress counters are sufficient:
  - `total`
  - `processed`
  - `succeeded`
  - `failed`
  - `duplicates`
- How to render unknown totals while validation is still in progress.
- Whether users need to cancel imports.
- Whether users need to download or view row-level errors.
- Whether duplicate resolution is automatic or requires user review.
- Polling interval, timeout, retry, and backoff behavior.
- How to handle terminal states:
  - `completed`
  - `completed_with_errors`
  - `failed`
  - `cancelled`
  - `expired`

Human gate: product/frontend approval is required before finalizing progress states and user-visible import lifecycle copy.

---

### QA handoff

QA should prepare contract and behavior tests for:

#### Create import

- Valid import request returns `202 Accepted`.
- Response includes job ID, initial status, timestamps, and location.
- Missing or invalid file ID returns expected error.
- Unsupported file type returns expected error.
- Unauthorized caller receives `401`.
- Caller without permission receives `403`.
- Oversized import returns expected error.
- Idempotency key reuse with same request returns same job.
- Idempotency key reuse with different request returns conflict.

#### Status lifecycle

- Job transitions through allowed states only.
- Terminal states do not transition unexpectedly.
- Progress counters are internally consistent.
- Unknown total is represented consistently.
- Partial success results in `completed_with_errors`.
- Job-level failure results in `failed`.

#### Duplicate detection

- Duplicates are counted.
- Duplicate strategy is applied consistently.
- Duplicate details do not expose disallowed PII.
- Caller cannot view duplicates for another tenant/account/workspace.

#### Error results

- Row-level errors are paginated.
- Error messages are sanitized.
- Error codes are stable and documented.
- PII is not present in logs or API error messages, subject to security-approved test strategy.

#### Pagination and filtering

- List endpoints support cursor pagination.
- Pagination handles concurrent updates.
- Filters return expected subsets.
- Invalid cursors return a clear error.

#### Observability

- Responses include request IDs.
- Job IDs are traceable in logs without exposing PII.
- Failure cases are diagnosable by support using non-sensitive identifiers.

Human gate: QA should not mark the contract ready until state-machine behavior, idempotency, duplicate handling, and PII-safe error behavior are testable.

---

### Documentation handoff

Docs should cover:

- End-to-end import flow:
  1. Upload or provide contact data.
  2. Create import job.
  3. Poll job status.
  4. Retrieve errors or duplicate results.
  5. Handle terminal states.
- Status lifecycle table.
- Progress field definitions.
- Duplicate detection behavior and strategies.
- Error code reference.
- Idempotency behavior.
- Pagination behavior.
- Rate-limit guidance, if defined by platform.
- PII and privacy notes.
- Example requests and responses.
- Recommended frontend polling behavior.
- Retention windows for import results, once approved.

Docs should avoid promising behavior not approved by product, security, and platform.

Human gate: documentation should not publish public examples containing real or realistic sensitive contact data unless approved and sanitized.

---

## 5. Verification checklist

Before implementation or public commitment, verify the following.

### Contract consistency

- [ ] Resource names are consistent: `contact-imports`, `errors`, `duplicates`.
- [ ] Async creation uses `202 Accepted`.
- [ ] `Location` header points to the job status endpoint.
- [ ] Status lifecycle is explicit and finite.
- [ ] Terminal states are defined.
- [ ] Partial success behavior is defined.

### Schema clarity

- [ ] Request body shape is finalized.
- [ ] Response fields are documented.
- [ ] Required versus optional fields are clear.
- [ ] Timestamps use a consistent format.
- [ ] Progress counters are clearly defined.
- [ ] Unknown totals have a defined representation, such as `null`.

### Error handling

- [ ] Error envelope is consistent across endpoints.
- [ ] Error codes are stable and machine-readable.
- [ ] Error messages do not leak PII.
- [ ] Row-level errors are separated from job-level errors.
- [ ] Request IDs are returned for support.

### Security and privacy

- [ ] Auth and permission boundaries are approved.
- [ ] PII fields accepted by the API are explicitly listed.
- [ ] PII fields returned by the API are explicitly approved.
- [ ] Duplicate result visibility is approved.
- [ ] File retention and result retention are approved.
- [ ] Logs, traces, and metrics avoid raw PII.
- [ ] Rate limiting and abuse controls are defined.

### Idempotency

- [ ] `POST /contact-imports` supports idempotency.
- [ ] Idempotency conflict behavior is defined.
- [ ] Idempotency retention period is defined.
- [ ] Duplicate submissions do not create duplicate contacts.

### Pagination and scale

- [ ] List endpoints are paginated.
- [ ] Error and duplicate result endpoints are paginated.
- [ ] Large files and large result sets have defined limits.
- [ ] Cursor behavior is documented.

### Frontend readiness

- [ ] Frontend can render all statuses.
- [ ] Frontend knows when to stop polling.
- [ ] Frontend can handle unknown totals.
- [ ] Frontend can render duplicate and error summaries.
- [ ] Cancellation behavior is either supported or explicitly not supported.

### QA readiness

- [ ] Contract tests exist for success and failure cases.
- [ ] State-machine tests cover valid and invalid transitions.
- [ ] Duplicate detection scenarios are covered.
- [ ] PII leakage tests are included where feasible.
- [ ] Idempotency tests are included.
- [ ] Authorization boundary tests are included.

### Documentation readiness

- [ ] Developer flow is documented.
- [ ] Example payloads are sanitized.
- [ ] Error codes are documented.
- [ ] Status lifecycle is documented.
- [ ] Privacy and retention caveats are included.
