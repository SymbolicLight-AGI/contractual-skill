# Bulk Contact Import API — Reviewer Handoff

## 1. Context

We are designing an API for bulk contact import.

Known facts:

- Imports are asynchronous.
- Duplicate detection is required.
- Contact data contains PII.
- Frontend needs progress states.
- This handoff is for downstream review by:
  - Security
  - Frontend
  - QA
  - Documentation

Uncertainties / open inputs:

- Exact contact schema is not finalized.
- Import file formats are not specified.
- Duplicate matching rules are not finalized.
- Authorization model is not confirmed.
- Retention policy for uploaded files and import results is not confirmed.
- Maximum file size, row count, and rate limits are not confirmed.
- Whether partial success is allowed is not confirmed.

---

# 2. Proposed API Style

Use REST for this workflow.

Reasoning:

- The import is a resource-oriented asynchronous operation.
- Clients need to create an import job, poll or subscribe to status, review results, and possibly resolve duplicates.
- REST endpoints map cleanly to import jobs, progress, validation errors, and result artifacts.

---

# 3. Primary Consumers

## Frontend application

Needs to:

- Upload a file or submit contact records.
- Start an import.
- Display validation status.
- Display progress states.
- Show duplicate warnings.
- Show success, partial success, or failure outcomes.
- Let users download or review error reports.

## Backend workers

Need to:

- Process import jobs asynchronously.
- Validate contact data.
- Detect duplicates.
- Persist imported contacts.
- Emit progress and result updates.

## QA

Needs to:

- Validate edge cases.
- Test async state transitions.
- Test duplicate behavior.
- Test PII handling boundaries.
- Test failure and retry behavior.

## Security

Needs to:

- Review PII exposure.
- Validate authz/authn.
- Review upload handling.
- Review retention, logging, encryption, and audit requirements.

## Docs

Needs to:

- Explain lifecycle and states.
- Document request/response examples.
- Document duplicate detection semantics.
- Document errors and limits.

---

# 4. Proposed Resource Model

## Resource: Import Job

Represents an asynchronous bulk contact import.

Example fields:

```json
{
  "id": "imp_123",
  "status": "processing",
  "createdAt": "2026-05-24T12:00:00Z",
  "updatedAt": "2026-05-24T12:01:30Z",
  "createdBy": "user_456",
  "source": {
    "type": "file",
    "filename": "contacts.csv"
  },
  "progress": {
    "totalRows": 1000,
    "processedRows": 450,
    "successfulRows": 420,
    "failedRows": 20,
    "duplicateRows": 10,
    "percentComplete": 45
  },
  "result": null,
  "links": {
    "self": "/contact-imports/imp_123",
    "errors": "/contact-imports/imp_123/errors",
    "duplicates": "/contact-imports/imp_123/duplicates"
  }
}
```

---

# 5. Proposed Endpoints

## Create import job

```http
POST /contact-imports
```

Creates an asynchronous import job.

### Option A: File upload

If the API accepts multipart uploads:

```http
POST /contact-imports
Content-Type: multipart/form-data
```

Fields:

| Field | Required | Description |
|---|---:|---|
| `file` | Yes | CSV/XLSX/etc. contact file |
| `dedupeMode` | No | Duplicate handling strategy |
| `dryRun` | No | Validate only, do not persist |
| `metadata` | No | Optional client metadata |

Example response:

```http
202 Accepted
Location: /contact-imports/imp_123
```

```json
{
  "id": "imp_123",
  "status": "queued",
  "createdAt": "2026-05-24T12:00:00Z",
  "links": {
    "self": "/contact-imports/imp_123"
  }
}
```

### Option B: JSON payload

If the API accepts raw contact records:

```http
POST /contact-imports
Content-Type: application/json
```

```json
{
  "dedupeMode": "skip",
  "dryRun": false,
  "contacts": [
    {
      "firstName": "Asha",
      "lastName": "Rao",
      "email": "asha@example.com",
      "phone": "+15551234567"
    }
  ]
}
```

Response:

```http
202 Accepted
```

```json
{
  "id": "imp_123",
  "status": "queued",
  "links": {
    "self": "/contact-imports/imp_123"
  }
}
```

Reviewer note: choose either file upload, JSON payload, or both. Supporting both increases surface area and QA burden.

---

## Get import job status

```http
GET /contact-imports/{importId}
```

Returns current job status and progress.

Example response:

```json
{
  "id": "imp_123",
  "status": "processing",
  "createdAt": "2026-05-24T12:00:00Z",
  "updatedAt": "2026-05-24T12:01:30Z",
  "progress": {
    "totalRows": 1000,
    "processedRows": 450,
    "successfulRows": 420,
    "failedRows": 20,
    "duplicateRows": 10,
    "percentComplete": 45
  },
  "links": {
    "self": "/contact-imports/imp_123",
    "errors": "/contact-imports/imp_123/errors",
    "duplicates": "/contact-imports/imp_123/duplicates"
  }
}
```

---

## List import jobs

```http
GET /contact-imports
```

Supports pagination and filtering.

Suggested query params:

| Param | Description |
|---|---|
| `status` | Filter by status |
| `createdAfter` | Filter by creation time |
| `createdBefore` | Filter by creation time |
| `limit` | Page size |
| `cursor` | Cursor for next page |

Example:

```http
GET /contact-imports?status=completed&limit=25
```

Response:

```json
{
  "data": [
    {
      "id": "imp_123",
      "status": "completed",
      "createdAt": "2026-05-24T12:00:00Z",
      "completedAt": "2026-05-24T12:04:00Z",
      "progress": {
        "totalRows": 1000,
        "processedRows": 1000,
        "successfulRows": 940,
        "failedRows": 40,
        "duplicateRows": 20,
        "percentComplete": 100
      }
    }
  ],
  "pagination": {
    "nextCursor": "cursor_abc"
  }
}
```

---

## Get import errors

```http
GET /contact-imports/{importId}/errors
```

Returns row-level validation or processing errors.

Suggested pagination:

```http
GET /contact-imports/imp_123/errors?limit=100&cursor=cursor_abc
```

Example response:

```json
{
  "data": [
    {
      "rowNumber": 12,
      "field": "email",
      "code": "INVALID_EMAIL",
      "message": "Email address is invalid."
    },
    {
      "rowNumber": 27,
      "field": "phone",
      "code": "INVALID_PHONE",
      "message": "Phone number is invalid."
    }
  ],
  "pagination": {
    "nextCursor": "cursor_def"
  }
}
```

Security note: avoid echoing full raw PII in error payloads unless absolutely required.

---

## Get duplicate candidates

```http
GET /contact-imports/{importId}/duplicates
```

Returns duplicate detection results.

Example response:

```json
{
  "data": [
    {
      "rowNumber": 42,
      "duplicateType": "email",
      "confidence": "exact",
      "action": "skipped",
      "matchedContact": {
        "id": "con_789",
        "displayName": "Asha R.",
        "maskedEmail": "a***@example.com",
        "maskedPhone": null
      }
    }
  ],
  "pagination": {
    "nextCursor": null
  }
}
```

Security note: duplicate responses should use masked PII where possible.

---

## Cancel import job

```http
POST /contact-imports/{importId}/cancel
```

Cancels a queued or processing import when possible.

Response:

```http
202 Accepted
```

```json
{
  "id": "imp_123",
  "status": "canceling"
}
```

Uncertainty: confirm whether cancellation is required.

---

# 6. Proposed Import Status Model

Recommended statuses:

| Status | Meaning |
|---|---|
| `queued` | Job accepted, not yet processing |
| `validating` | File or payload is being parsed and validated |
| `processing` | Valid records are being imported |
| `completed` | Import finished successfully |
| `completed_with_errors` | Import finished with partial failures |
| `failed` | Import failed and could not complete |
| `canceling` | Cancellation requested |
| `canceled` | Import was canceled |

Frontend should treat status as an enum and include a fallback for unknown future statuses.

---

# 7. Duplicate Detection Strategy

Duplicate detection is required, but matching rules are not finalized.

Proposed configurable modes:

| `dedupeMode` | Behavior |
|---|---|
| `skip` | Skip rows matching existing contacts |
| `update` | Update existing contacts with imported values |
| `create_anyway` | Create contacts even if duplicates are detected |
| `fail_on_duplicate` | Mark duplicate rows as errors |

Recommended default: `skip`, unless product requires manual resolution or strict data integrity.

Potential duplicate keys:

- Email exact match
- Phone exact match
- External/contact source ID
- Name + phone/email composite match

Uncertainty: final matching rules need product, data, and security review.

---

# 8. Error Format

Use a consistent error envelope.

Example:

```json
{
  "error": {
    "code": "IMPORT_NOT_FOUND",
    "message": "Import job was not found.",
    "requestId": "req_123"
  }
}
```

Validation error example:

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "The request contains invalid fields.",
    "details": [
      {
        "field": "dedupeMode",
        "code": "INVALID_VALUE",
        "message": "dedupeMode must be one of: skip, update, create_anyway, fail_on_duplicate."
      }
    ],
    "requestId": "req_123"
  }
}
```

Suggested HTTP status codes:

| HTTP Status | Use |
|---:|---|
| `202` | Import accepted for async processing |
| `200` | Read status/results successfully |
| `400` | Invalid request |
| `401` | Missing or invalid authentication |
| `403` | Authenticated but not allowed |
| `404` | Import job not found or not visible to caller |
| `409` | Conflict, such as invalid state transition |
| `413` | File or payload too large |
| `415` | Unsupported media type/file type |
| `422` | Semantically invalid import content |
| `429` | Rate limit exceeded |
| `500` | Unexpected server error |

---

# 9. Pagination

Use cursor pagination for list endpoints and row-level result endpoints.

Applies to:

- `GET /contact-imports`
- `GET /contact-imports/{importId}/errors`
- `GET /contact-imports/{importId}/duplicates`

Recommended params:

| Param | Description |
|---|---|
| `limit` | Max records to return |
| `cursor` | Opaque cursor from previous response |

Example response shape:

```json
{
  "data": [],
  "pagination": {
    "nextCursor": "cursor_abc"
  }
}
```

---

# 10. Versioning

Recommended options:

## Preferred

Use path versioning if public or cross-team API stability is required:

```http
/v1/contact-imports
```

## Alternative

Use header-based versioning for internal APIs where gateway/client tooling supports it:

```http
Accept: application/vnd.company.contact-imports.v1+json
```

Uncertainty: existing platform API versioning standard should be followed.

---

# 11. Auth and Authorization

Recommended baseline:

- Require authentication for all endpoints.
- Authorize access to import jobs by tenant/workspace/account.
- Users should only view imports they are allowed to access.
- Consider separate permissions:
  - `contacts:import`
  - `contacts:read`
  - `contacts:write`
  - `contact_imports:read`
  - `contact_imports:cancel`

Security must confirm:

- Whether admins can view all user imports.
- Whether row-level result data can expose PII.
- Whether service accounts can create imports.
- Whether imports require audit events.

---

# 12. PII and Security Review Notes

Because contact data contains PII, review the following:

## Upload handling

- Allowed file types.
- File size limits.
- Malware scanning requirement.
- CSV formula injection handling.
- Encoding normalization.
- Rejection of malformed files.
- Temporary storage encryption.

## Data exposure

- Avoid returning raw imported rows by default.
- Mask email and phone in duplicate result previews where possible.
- Avoid including PII in logs, metrics, traces, and error messages.
- Ensure `requestId` and job IDs are non-sensitive.

## Retention

Need confirmed policy for:

- Uploaded files.
- Parsed staging records.
- Error reports.
- Duplicate reports.
- Completed import job metadata.

## Audit

Consider audit events for:

- Import created.
- Import completed.
- Import failed.
- Import canceled.
- Contacts created or updated by import.

## Abuse controls

- Rate limits per user/tenant.
- Max concurrent imports.
- Max file size.
- Max row count.
- Backpressure behavior.
- Quotas for failed/retried imports.

---

# 13. Frontend Review Notes

Frontend should verify:

## Required states

- Initial upload selected
- Uploading
- Queued
- Validating
- Processing
- Completed
- Completed with errors
- Failed
- Canceling
- Canceled

## Required UI data

- `status`
- `progress.totalRows`
- `progress.processedRows`
- `progress.successfulRows`
- `progress.failedRows`
- `progress.duplicateRows`
- `progress.percentComplete`
- Links to errors and duplicates
- Final summary

## Polling

If no realtime mechanism is available, frontend can poll:

```http
GET /contact-imports/{importId}
```

Recommended behavior:

- Poll faster during `queued`, `validating`, and `processing`.
- Stop polling on terminal states:
  - `completed`
  - `completed_with_errors`
  - `failed`
  - `canceled`
- Handle unknown statuses gracefully.
- Handle temporary `429` and `5xx` with backoff.

Uncertainty: whether WebSocket/SSE/event-based updates are available.

---

# 14. QA Review Checklist

QA should cover:

## Happy paths

- Valid file import completes.
- Valid JSON payload import completes, if supported.
- Progress updates from queued to completed.
- Import summary counts are correct.

## Validation

- Missing required fields.
- Invalid email.
- Invalid phone.
- Unsupported file type.
- Empty file.
- Malformed CSV.
- Extra columns.
- Missing headers.
- Duplicate headers.
- Oversized file.
- Too many rows.

## Duplicate handling

- Exact email duplicate.
- Exact phone duplicate.
- Duplicate within same import file.
- Duplicate against existing contact.
- Duplicate with different casing/formatting.
- Behavior for each supported `dedupeMode`.

## Async behavior

- Job queued.
- Job processing.
- Partial failure.
- Full failure.
- Worker crash/retry behavior.
- Idempotency/retry of create request, if supported.
- Cancel queued job.
- Cancel processing job, if supported.

## Permissions

- User cannot access another tenant’s import.
- User without import permission cannot create import.
- User without read permission cannot view results.
- Expired/invalid token returns `401`.

## PII/security

- PII is not leaked in logs-visible error messages.
- Duplicate endpoint masks sensitive fields.
- Error report does not expose unnecessary raw data.
- Uploaded malicious-looking content is rejected or sanitized according to policy.

---

# 15. Docs Review Checklist

Docs should include:

- Overview of async import lifecycle.
- Endpoint reference.
- Request examples.
- Response examples.
- Status enum definitions.
- Progress field definitions.
- Duplicate detection behavior.
- Error codes.
- File format requirements.
- Limits:
  - Max file size
  - Max row count
  - Max concurrent imports
  - Rate limits
- Authentication and permissions.
- Retention expectations.
- Polling guidance.
- Troubleshooting guide.

Docs should clearly state whether imports are:

- All-or-nothing, or
- Partial success with row-level errors.

Uncertainty: partial success behavior must be finalized.

---

# 16. Key Open Questions for Reviewers

## Product / API owners

1. Which input modes are supported: file upload, JSON records, or both?
2. What file formats are supported?
3. What is the contact schema?
4. Are imports partial success or atomic?
5. Is cancellation required?
6. Are dry runs required?
7. Are manual duplicate resolutions required, or is dedupe automatic?

## Security

1. What is the retention period for uploaded files and import reports?
2. Should duplicate previews include masked PII only?
3. Is malware scanning required for uploads?
4. What audit events are required?
5. What are the required permissions?
6. Are there regulatory constraints for contact PII?

## Frontend

1. Is polling acceptable, or is realtime progress required?
2. What minimum progress fields are needed?
3. Does the UI need row-level duplicate resolution?
4. Should users be able to download error reports?

## QA

1. What are target limits for file size and row count?
2. What async timeout behavior should be expected?
3. What retry/idempotency behavior should be validated?
4. What duplicate scenarios are in scope for launch?

## Docs

1. Which endpoints are final for initial release?
2. What examples should be included?
3. Are there customer-facing limits or beta caveats?
4. What terminology should be used: import, upload, job, batch, or contact import?

---

# 17. Recommended Next Step

Before implementation, reviewers should align on these contract decisions:

1. Supported input format.
2. Contact field schema.
3. Duplicate matching and handling rules.
4. Partial success vs all-or-nothing behavior.
5. PII masking and retention policy.
6. Auth permissions.
7. Progress state model.
8. Limits and rate limiting.
9. API versioning convention.

Once these are resolved, the API contract can be converted into a formal OpenAPI specification for final review.
