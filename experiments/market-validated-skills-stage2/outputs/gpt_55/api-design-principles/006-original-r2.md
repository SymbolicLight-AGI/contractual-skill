# Bulk Contact Import API Contract Handoff

## 1. Context

We are designing an API for **bulk contact import**.

Known facts:

- Imports are **asynchronous**.
- **Duplicate detection** is required.
- Imported data includes **PII**.
- Frontend needs clear **progress states**.
- This handoff is for:
  - Security
  - Frontend
  - QA
  - Documentation

Open uncertainties are called out where decisions are still needed.

---

# 2. Intended Consumers

## Primary consumers

### Frontend application

Needs to:

- Upload or submit contact import data.
- Start an import job.
- Display import progress.
- Show success, failure, duplicate, and partial-completion states.
- Allow users to review duplicate or invalid rows if supported.
- Surface actionable errors.

### Backend workers

Need to:

- Process import jobs asynchronously.
- Validate contacts.
- Detect duplicates.
- Persist valid contacts.
- Produce import summaries and row-level results.

### Admin/support tooling

Potentially needs to:

- Inspect import status.
- Debug failed imports.
- View sanitized summaries.
- Avoid unnecessary PII exposure.

Uncertainty: Whether admin/support tooling is in scope for v1.

---

# 3. Core Use Cases

## Required use cases

1. User starts a bulk contact import.
2. API creates an asynchronous import job.
3. Frontend polls or subscribes to progress.
4. Backend validates rows.
5. Backend detects duplicates.
6. Backend imports valid contacts.
7. Frontend displays final results.
8. User can retrieve an import summary.
9. User can retrieve row-level errors or duplicate records, subject to PII/security constraints.

## Possible future use cases

- Cancel an import.
- Retry a failed import.
- Resume a partially processed import.
- Download an error report.
- Manually resolve duplicates before import.
- Webhook notification when import completes.

Uncertainty: These are not confirmed for the initial version.

---

# 4. Recommended API Style

Use **REST** for this workflow.

Reasoning:

- The import is a resource-oriented asynchronous operation.
- Job lifecycle maps naturally to REST resources.
- Frontend can poll job status using predictable endpoints.
- Security and audit requirements are easier to reason about with explicit resources and permissions.

---

# 5. Proposed Resource Model

## Main resources

### `ContactImport`

Represents an asynchronous import job.

Example fields:

```json
{
  "id": "imp_123",
  "status": "processing",
  "progress": {
    "totalRows": 1000,
    "processedRows": 425,
    "validRows": 390,
    "invalidRows": 20,
    "duplicateRows": 15,
    "percentComplete": 42
  },
  "createdAt": "2026-05-24T12:00:00Z",
  "startedAt": "2026-05-24T12:00:05Z",
  "completedAt": null,
  "createdBy": "user_123",
  "source": {
    "type": "csv",
    "filename": "contacts.csv"
  },
  "result": null,
  "links": {
    "self": "/contact-imports/imp_123",
    "errors": "/contact-imports/imp_123/errors",
    "duplicates": "/contact-imports/imp_123/duplicates"
  }
}
```

### `ContactImportError`

Represents a validation or processing error for a row.

Example:

```json
{
  "rowNumber": 42,
  "code": "INVALID_EMAIL",
  "message": "Email address is invalid.",
  "field": "email"
}
```

### `ContactImportDuplicate`

Represents a detected duplicate.

Example:

```json
{
  "rowNumber": 57,
  "duplicateType": "existing_contact",
  "matchedFields": ["email"],
  "resolution": "skipped"
}
```

Important: Avoid exposing full existing contact PII unless strictly required and authorized.

---

# 6. Proposed Endpoints

## Create import

```http
POST /contact-imports
```

Creates an asynchronous import job.

### Request option A: JSON payload

Use if contacts are submitted directly as JSON.

```json
{
  "contacts": [
    {
      "firstName": "Ada",
      "lastName": "Lovelace",
      "email": "ada@example.com",
      "phone": "+15551234567"
    }
  ],
  "duplicatePolicy": "skip"
}
```

### Request option B: file upload

Use if frontend uploads CSV or spreadsheet files.

```http
POST /contact-imports
Content-Type: multipart/form-data
```

Fields:

- `file`
- `duplicatePolicy`

Uncertainty: The team needs to decide whether v1 supports JSON, file upload, or both.

### Response

```http
202 Accepted
Location: /contact-imports/imp_123
```

```json
{
  "id": "imp_123",
  "status": "queued",
  "progress": {
    "totalRows": null,
    "processedRows": 0,
    "validRows": 0,
    "invalidRows": 0,
    "duplicateRows": 0,
    "percentComplete": 0
  },
  "createdAt": "2026-05-24T12:00:00Z",
  "links": {
    "self": "/contact-imports/imp_123"
  }
}
```

---

## Get import status

```http
GET /contact-imports/{importId}
```

Returns current status and progress.

### Response

```json
{
  "id": "imp_123",
  "status": "processing",
  "progress": {
    "totalRows": 1000,
    "processedRows": 425,
    "validRows": 390,
    "invalidRows": 20,
    "duplicateRows": 15,
    "percentComplete": 42
  },
  "createdAt": "2026-05-24T12:00:00Z",
  "startedAt": "2026-05-24T12:00:05Z",
  "completedAt": null,
  "result": null
}
```

---

## Get final import summary

Can be the same endpoint as `GET /contact-imports/{importId}` once completed.

Example completed response:

```json
{
  "id": "imp_123",
  "status": "completed_with_errors",
  "progress": {
    "totalRows": 1000,
    "processedRows": 1000,
    "validRows": 900,
    "invalidRows": 50,
    "duplicateRows": 50,
    "percentComplete": 100
  },
  "createdAt": "2026-05-24T12:00:00Z",
  "startedAt": "2026-05-24T12:00:05Z",
  "completedAt": "2026-05-24T12:02:30Z",
  "result": {
    "createdContacts": 900,
    "skippedRows": 100,
    "failedRows": 50,
    "duplicateRows": 50
  },
  "links": {
    "errors": "/contact-imports/imp_123/errors",
    "duplicates": "/contact-imports/imp_123/duplicates"
  }
}
```

---

## Get row-level errors

```http
GET /contact-imports/{importId}/errors
```

Supports pagination.

### Query parameters

```http
?pageSize=100&pageToken=abc
```

### Response

```json
{
  "items": [
    {
      "rowNumber": 42,
      "code": "INVALID_EMAIL",
      "message": "Email address is invalid.",
      "field": "email"
    }
  ],
  "nextPageToken": "def"
}
```

---

## Get duplicate rows

```http
GET /contact-imports/{importId}/duplicates
```

Supports pagination.

### Response

```json
{
  "items": [
    {
      "rowNumber": 57,
      "duplicateType": "existing_contact",
      "matchedFields": ["email"],
      "resolution": "skipped"
    }
  ],
  "nextPageToken": "ghi"
}
```

---

## Optional: Cancel import

```http
POST /contact-imports/{importId}:cancel
```

Response:

```json
{
  "id": "imp_123",
  "status": "canceling"
}
```

Uncertainty: Cancellation support is not confirmed. If not supported, omit from v1.

---

# 7. Import Status Model

Recommended statuses:

| Status | Meaning | Frontend behavior |
|---|---|---|
| `queued` | Job accepted but not started | Show waiting state |
| `processing` | Rows are being validated/imported | Show progress |
| `completed` | Import finished successfully | Show success summary |
| `completed_with_errors` | Import finished with invalid/skipped rows | Show partial success and report links |
| `failed` | Import could not complete | Show failure message and retry guidance |
| `canceling` | Cancellation requested | Show stopping state |
| `canceled` | Job canceled | Show canceled state |

If cancellation is not supported, remove `canceling` and `canceled`.

---

# 8. Duplicate Detection Strategy

## API-level contract

The client should be able to specify a duplicate handling policy.

Recommended field:

```json
{
  "duplicatePolicy": "skip"
}
```

Possible values:

| Value | Meaning |
|---|---|
| `skip` | Do not import duplicates |
| `update` | Update existing contacts if duplicate found |
| `create_anyway` | Create even if duplicate exists |
| `fail_import` | Fail the import if duplicates are detected |

Recommended v1 default: `skip`.

Uncertainty: Product/business rules need to confirm allowed duplicate policies.

## Duplicate matching

Potential matching fields:

- Email
- Phone number
- External ID
- Name plus company

Uncertainty: Exact duplicate matching rules are not provided and must be defined before QA can complete test coverage.

---

# 9. Error Model

Use a consistent error envelope.

## Error response shape

```json
{
  "error": {
    "code": "IMPORT_NOT_FOUND",
    "message": "The requested contact import was not found.",
    "requestId": "req_123",
    "details": []
  }
}
```

## Recommended API errors

| HTTP status | Code | Scenario |
|---|---|---|
| `400` | `INVALID_REQUEST` | Malformed request |
| `400` | `UNSUPPORTED_FILE_TYPE` | File type is not supported |
| `400` | `INVALID_DUPLICATE_POLICY` | Duplicate policy is unsupported |
| `401` | `UNAUTHENTICATED` | Missing or invalid credentials |
| `403` | `FORBIDDEN` | User cannot access this import |
| `404` | `IMPORT_NOT_FOUND` | Import does not exist or is not accessible |
| `409` | `IMPORT_ALREADY_FINALIZED` | Mutating a completed import |
| `413` | `IMPORT_TOO_LARGE` | File or row count exceeds allowed limit |
| `415` | `UNSUPPORTED_MEDIA_TYPE` | Incorrect content type |
| `422` | `VALIDATION_FAILED` | Submitted contact data failed validation |
| `429` | `RATE_LIMITED` | Too many requests/imports |
| `500` | `INTERNAL_ERROR` | Unexpected server error |
| `503` | `IMPORT_SERVICE_UNAVAILABLE` | Worker/import service unavailable |

---

# 10. Pagination

Use cursor-based pagination for row-level errors and duplicates.

Recommended query parameters:

```http
?pageSize=100&pageToken=abc
```

Recommended response:

```json
{
  "items": [],
  "nextPageToken": null
}
```

Guidelines:

- Define a maximum `pageSize`.
- Use stable ordering, preferably by `rowNumber`.
- Avoid offset pagination for large imports.

Uncertainty: Maximum page size and retention period are not yet defined.

---

# 11. Versioning

Recommended approach:

- Start with unversioned internal route only if this is not public.
- If this API is public or used by third-party clients, use URL or header versioning from v1.

Example:

```http
/api/v1/contact-imports
```

Versioning rules:

- Additive fields are allowed.
- Do not change enum meanings without a new version.
- Do not remove response fields without a new version.
- New statuses require frontend compatibility review.

Uncertainty: Public vs internal API status is not specified.

---

# 12. Authentication and Authorization

## Required

- All endpoints require authentication.
- Users can only access import jobs they created or are authorized to view.
- Authorization must be enforced on:
  - Import creation
  - Status retrieval
  - Error retrieval
  - Duplicate retrieval
  - Cancellation, if supported

## Suggested authorization checks

- User has permission to create contacts.
- User has permission to import contacts in the target workspace/account.
- User has permission to view contact import results.
- User has permission to view any returned PII.

---

# 13. PII and Data Handling Requirements

Because contact imports contain PII, the API should minimize exposure.

## Required considerations

- Do not return full imported contact rows by default.
- Do not expose existing matched contact details in duplicate responses unless required.
- Mask sensitive values where practical.
- Log only metadata, not raw contact data.
- Ensure import files and raw rows have retention limits.
- Ensure row-level reports do not expose unnecessary PII.
- Include audit logging for import creation and access to result reports.
- Ensure authorization boundaries across accounts/workspaces.
- Define encryption requirements for stored files and processed rows.
- Define deletion behavior for abandoned, failed, and completed imports.

---

# 14. Frontend Handoff

## Frontend should implement

### Create import

Call:

```http
POST /contact-imports
```

Expect:

```http
202 Accepted
```

Store returned `id`.

### Poll progress

Call:

```http
GET /contact-imports/{importId}
```

Recommended polling behavior:

- Poll while status is `queued` or `processing`.
- Stop polling when status is terminal:
  - `completed`
  - `completed_with_errors`
  - `failed`
  - `canceled`, if supported
- Use backoff to avoid excessive polling.

### Display states

Frontend should handle:

- Uploading
- Queued
- Processing with percent complete
- Completed successfully
- Completed with errors
- Failed
- Canceled, if supported

### Progress fields

Use:

```json
{
  "totalRows": 1000,
  "processedRows": 425,
  "validRows": 390,
  "invalidRows": 20,
  "duplicateRows": 15,
  "percentComplete": 42
}
```

### Final results

Use `result` from the completed import.

### Error and duplicate reports

Use:

```http
GET /contact-imports/{importId}/errors
GET /contact-imports/{importId}/duplicates
```

Both are paginated.

## Frontend open questions

- Should users be able to cancel imports?
- Should users be able to retry failed imports?
- Should duplicate rows be resolvable in the UI?
- Should row-level reports be downloadable?
- How much PII can be shown in error and duplicate reports?

---

# 15. Security Handoff

## Security review focus

### PII exposure

Please review:

- Request payloads and file uploads.
- Response payloads for status, errors, and duplicates.
- Logs and telemetry.
- Worker storage.
- Error reports.
- Duplicate result payloads.

### Access control

Confirm:

- Only authorized users can create imports.
- Users cannot view imports from other tenants/accounts/workspaces.
- Users cannot infer existence of contacts outside their authorized scope.
- Duplicate detection does not leak unauthorized contact details.
- Row-level results are protected.

### File and payload safety

If file upload is supported, review:

- Allowed MIME types.
- File extension validation.
- Maximum file size.
- Maximum row count.
- Malware scanning requirements.
- CSV/spreadsheet formula injection handling.
- Encoding handling.
- Zip/archive support, if any.

### Abuse prevention

Review:

- Rate limits.
- Maximum concurrent imports per user/account.
- Maximum rows per import.
- Worker queue protection.
- Idempotency requirements.
- Replay behavior.
- Audit logging.

### Data retention

Define:

- Raw file retention period.
- Parsed row retention period.
- Error/duplicate report retention period.
- Deletion behavior on user/account deletion.
- Access logging requirements.

## Security open questions

- Are imported raw files stored? If yes, where and for how long?
- Are row-level errors allowed to include original field values?
- Should PII in reports be masked?
- Are duplicate matches allowed to include existing contact identifiers?
- Is malware scanning required before processing files?
- Are there regulatory constraints for contact PII in this product context?

---

# 16. QA Handoff

## QA should validate

### Import creation

- Valid import returns `202 Accepted`.
- Response includes import `id`.
- `Location` header points to status endpoint.
- Invalid payload returns appropriate `400` or `422`.
- Unsupported file type returns `400` or `415`.
- Oversized import returns `413`.
- Invalid duplicate policy returns `400`.

### Status lifecycle

Validate transitions:

```text
queued -> processing -> completed
queued -> processing -> completed_with_errors
queued -> processing -> failed
queued -> canceling -> canceled, if cancellation is supported
```

Ensure invalid transitions cannot occur.

### Progress behavior

- `processedRows` never exceeds `totalRows`.
- `percentComplete` stays between `0` and `100`.
- Terminal states have `percentComplete = 100`, except possibly `failed` depending on failure timing.
- Counts add up consistently.
- Unknown `totalRows` is handled if row count is not known immediately.

### Duplicate detection

Test:

- Duplicate within the same file.
- Duplicate against existing contacts.
- Duplicate by email.
- Duplicate by phone, if supported.
- Case-insensitive email matching, if required.
- Normalized phone matching, if required.
- Duplicate policy behavior:
  - `skip`
  - `update`
  - `create_anyway`
  - `fail_import`

Only test policies confirmed for v1.

### Validation errors

Test row-level errors for:

- Missing required fields.
- Invalid email.
- Invalid phone.
- Field too long.
- Malformed row.
- Unsupported characters, if applicable.
- Duplicate row.
- Mixed valid and invalid rows.

### Pagination

Test:

- First page.
- Middle page.
- Last page.
- Empty result set.
- Invalid `pageToken`.
- Excessive `pageSize`.
- Stable ordering by `rowNumber`.

### Authorization

Test:

- Unauthenticated access returns `401`.
- Unauthorized access returns `403` or `404`, depending on security decision.
- User cannot access another user/account import.
- User cannot retrieve duplicate/error reports without permission.

### Failure modes

Test:

- Worker failure.
- Partial processing failure.
- Import service unavailable.
- Timeout.
- Repeated polling.
- Retry behavior, if supported.
- Cancellation, if supported.

## QA open questions

- What is the maximum file size?
- What is the maximum row count?
- Which contact fields are required?
- What formats are supported?
- What duplicate matching rules are authoritative?
- Are duplicate policies configurable?
- What is the expected behavior for partial success?
- Are row-level reports retained after completion?

---

# 17. Documentation Handoff

## Docs should include

### Overview

Explain that contact imports are asynchronous:

1. Create an import.
2. Poll status.
3. Fetch errors or duplicates if needed.
4. Review final summary.

### Endpoint reference

Document:

- `POST /contact-imports`
- `GET /contact-imports/{importId}`
- `GET /contact-imports/{importId}/errors`
- `GET /contact-imports/{importId}/duplicates`
- Optional: `POST /contact-imports/{importId}:cancel`

### Status enum

Document all statuses and terminal states.

### Duplicate policy

Document supported policies and default behavior.

### Error model

Document shared error envelope and common error codes.

### Pagination

Document cursor pagination for errors and duplicates.

### Security notes

Document:

- Required authentication.
- Authorization scope.
- PII handling expectations.
- Data retention if externally visible.

### Examples

Include examples for:

- Successful import creation.
- Polling progress.
- Completed import.
- Completed import with errors.
- Failed import.
- Retrieving validation errors.
- Retrieving duplicates.
- Handling pagination.

## Docs open questions

- Is this API public, partner-facing, or internal?
- Should docs include file upload examples, JSON examples, or both?
- Should duplicate matching rules be fully documented?
- Should data retention timelines be included?
- Are SDK examples required?

---

# 18. Consistency Checklist Before Implementation

Before finalizing the contract, confirm:

- [ ] Supported request format: JSON, file upload, or both.
- [ ] Required contact fields.
- [ ] Maximum file size.
- [ ] Maximum row count.
- [ ] Duplicate matching rules.
- [ ] Supported duplicate policies.
- [ ] Whether cancellation is supported.
- [ ] Whether retry is supported.
- [ ] Whether downloadable reports are supported.
- [ ] Whether row-level reports may include PII.
- [ ] Retention period for files, rows, errors, and duplicates.
- [ ] Public/internal versioning strategy.
- [ ] Auth scopes and tenant boundaries.
- [ ] Rate limits and concurrency limits.
- [ ] Frontend polling interval/backoff guidance.
- [ ] Final enum list for statuses and error codes.

---

# 19. Recommended Initial Contract Summary

If we need a conservative v1, recommend:

- REST API.
- File upload or JSON, but not both unless required.
- `POST /contact-imports` returns `202 Accepted`.
- `GET /contact-imports/{id}` for polling.
- Cursor-paginated:
  - `GET /contact-imports/{id}/errors`
  - `GET /contact-imports/{id}/duplicates`
- Statuses:
  - `queued`
  - `processing`
  - `completed`
  - `completed_with_errors`
  - `failed`
- Duplicate policy:
  - Default `skip`
- Do not return raw PII in duplicate/error reports by default.
- Require auth and tenant-scoped authorization on every endpoint.
- Use consistent error envelope.
- Add versioning if this API is public or partner-facing.
