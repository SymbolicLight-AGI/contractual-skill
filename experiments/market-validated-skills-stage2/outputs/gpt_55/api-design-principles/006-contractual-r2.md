## 1. Design summary

### Supplied facts

- The API supports **bulk contact import**.
- Imports are **asynchronous**.
- **Duplicate detection is required**.
- Imported data includes **PII**.
- Frontend needs **progress states**.

### Proposed contract direction

Model bulk contact import as an asynchronous job resource:

- Client creates an import job.
- API returns a job identifier immediately.
- Frontend polls or subscribes to job status.
- Import results include aggregate counts and duplicate-detection outcomes.
- Sensitive contact data should not be exposed unnecessarily in job status or error payloads.

This handoff is for review by:

- **Security**: auth, authorization, PII handling, auditability, retention.
- **Frontend**: progress-state model and UX behavior.
- **QA**: contract tests, edge cases, error semantics.
- **Docs**: developer-facing examples, lifecycle explanation, and warnings.

---

## 2. Proposed API shape

The following is an illustrative contract proposal, not evidence of an implemented API.

### Create a bulk contact import

```http
POST /contact-imports
Content-Type: multipart/form-data
Idempotency-Key: <client-generated-key>
Authorization: Bearer <token>
```

Possible request fields:

```text
file: contacts.csv
deduplicationMode: strict | lenient
```

If JSON upload is preferred instead of file upload, the team should explicitly choose that contract. Do not support both unless there is a clear product requirement.

### Successful response

```http
202 Accepted
Location: /contact-imports/{importId}
```

```json
{
  "id": "imp_123",
  "status": "queued",
  "createdAt": "2026-05-24T12:00:00Z",
  "progress": {
    "totalRows": null,
    "processedRows": 0,
    "percent": 0
  }
}
```

### Get import status

```http
GET /contact-imports/{importId}
Authorization: Bearer <token>
```

Example response:

```json
{
  "id": "imp_123",
  "status": "processing",
  "createdAt": "2026-05-24T12:00:00Z",
  "startedAt": "2026-05-24T12:00:05Z",
  "completedAt": null,
  "progress": {
    "totalRows": 1000,
    "processedRows": 450,
    "percent": 45
  },
  "summary": {
    "createdCount": 400,
    "updatedCount": 20,
    "duplicateCount": 25,
    "failedCount": 5
  }
}
```

### Recommended import states

```text
queued
processing
completed
completed_with_errors
failed
cancelled
```

Optional additional state if needed:

```text
validating
```

Use this only if validation is meaningfully separate from processing and frontend needs to display it.

### Get import result details

```http
GET /contact-imports/{importId}/results
Authorization: Bearer <token>
```

Illustrative response:

```json
{
  "id": "imp_123",
  "summary": {
    "totalRows": 1000,
    "createdCount": 900,
    "updatedCount": 50,
    "duplicateCount": 40,
    "failedCount": 10
  },
  "errors": [
    {
      "rowNumber": 17,
      "code": "INVALID_EMAIL",
      "message": "Email address is invalid."
    }
  ],
  "duplicates": [
    {
      "rowNumber": 21,
      "code": "DUPLICATE_CONTACT",
      "resolution": "skipped"
    }
  ]
}
```

### Important PII constraint

Avoid returning raw contact PII in status or result payloads unless explicitly approved by security and product.

For example, prefer:

```json
{
  "rowNumber": 21,
  "code": "DUPLICATE_CONTACT",
  "resolution": "skipped"
}
```

Instead of:

```json
{
  "rowNumber": 21,
  "email": "person@example.com",
  "phone": "+15551234567",
  "code": "DUPLICATE_CONTACT"
}
```

If frontend needs to help the user fix rows, the exact safe fields require security review.

### Cancel an import

If cancellation is required by product, expose:

```http
POST /contact-imports/{importId}/cancel
Authorization: Bearer <token>
```

Response:

```http
202 Accepted
```

```json
{
  "id": "imp_123",
  "status": "cancelled"
}
```

If cancellation is not a product requirement, do not include this endpoint yet.

---

## 3. Key tradeoffs

### Asynchronous resource vs synchronous upload

Recommended: asynchronous resource.

Reasoning:

- Bulk import can take an unknown amount of time.
- Frontend needs progress states.
- `202 Accepted` accurately represents accepted-but-not-complete work.
- Job resource supports retries, observability, and result retrieval.

### Polling vs push updates

Default recommendation: start with polling.

Example:

```http
GET /contact-imports/{importId}
```

Tradeoff:

- Polling is simpler and easier to test.
- Push mechanisms such as WebSocket or Server-Sent Events can improve UX but add operational complexity.

If real-time progress is required, the team should explicitly review that with frontend and platform.

### Duplicate handling model

Required, but unspecified.

Open decision:

- Should duplicates be skipped?
- Should they update existing contacts?
- Should the import fail on duplicates?
- Should duplicate behavior be configurable?

Possible modes:

```text
skip_duplicates
update_existing
fail_on_duplicate
```

This needs product approval because it affects user-visible behavior and data mutation semantics.

### Idempotency

Recommended for create-import endpoint:

```http
Idempotency-Key: <client-generated-key>
```

Reasoning:

- Upload/import submission is a write operation.
- Network retries could otherwise create multiple import jobs.
- Duplicate imports may create duplicate contacts or conflicting results.

The idempotency behavior should be explicit:

- Same key and same payload returns the same import job.
- Same key and different payload returns a conflict error.
- Keys expire after a documented period.

Exact retention period is unknown and requires platform/product input.

---

## 4. Risks and human gates

### Security handoff

Security review is required before public commitment or implementation if the API exposes customer contact data.

Security should review:

- Authentication and authorization boundary:
  - Who can create imports?
  - Who can view import status?
  - Who can view failed-row details?
  - Can one user see another user’s import job?
- PII exposure:
  - Request body contains contacts.
  - Result payloads may reveal emails, names, phone numbers, addresses, or other sensitive data.
  - Error messages must not leak unnecessary PII.
- Data retention:
  - How long uploaded files are stored.
  - How long import results are stored.
  - Whether failed rows are retained.
- Audit logging:
  - Import created.
  - Import completed.
  - Import failed.
  - Duplicate handling result.
  - Import viewed or downloaded, if applicable.
- Rate limiting and abuse controls:
  - File size limits.
  - Row count limits.
  - Frequency limits.
- Malware/content scanning if files are uploaded.
- Encryption in transit and at rest.
- Access to temporary files or processing queues.

Human gate:

- Security approval is required for PII handling, result visibility, retention, and access control.

---

### Frontend handoff

Frontend should review whether the following state model is sufficient:

```text
queued
processing
completed
completed_with_errors
failed
cancelled
```

Frontend needs clarity on:

- Whether `progress.totalRows` can be unknown at first.
- Whether `percent` is always available.
- Whether progress is exact or approximate.
- Whether users can leave the page and return to the import.
- Whether cancellation is supported.
- Whether partial success is allowed.
- How duplicates should be displayed.
- Whether failed rows can be downloaded or corrected.
- Whether polling interval guidance is needed.

Recommended status response fields for frontend:

```json
{
  "id": "imp_123",
  "status": "processing",
  "progress": {
    "totalRows": 1000,
    "processedRows": 450,
    "percent": 45
  },
  "summary": {
    "createdCount": 400,
    "updatedCount": 20,
    "duplicateCount": 25,
    "failedCount": 5
  }
}
```

Human gate:

- Product/frontend approval is required for user-visible duplicate behavior, progress semantics, and partial-success UX.

---

### QA handoff

QA should prepare contract and behavior tests for:

#### Create import

- Valid import request returns `202 Accepted`.
- Response includes import ID.
- `Location` header points to status endpoint.
- Missing auth returns `401 Unauthorized`.
- Insufficient permission returns `403 Forbidden`.
- Invalid file format returns `400 Bad Request` or `422 Unprocessable Entity`.
- Oversized file returns `413 Payload Too Large`.
- Unsupported media type returns `415 Unsupported Media Type`.

#### Idempotency

- Retrying the same request with the same `Idempotency-Key` returns the same import job.
- Reusing the same key with a different payload returns `409 Conflict`.
- Missing idempotency key behavior is explicitly tested according to the chosen policy.

#### Status lifecycle

- New import starts as `queued` or `processing`.
- Import eventually reaches terminal state:
  - `completed`
  - `completed_with_errors`
  - `failed`
  - `cancelled`, if supported
- Terminal imports do not regress to non-terminal states.
- Progress values are valid:
  - `processedRows <= totalRows`, when `totalRows` is known.
  - `percent` is between `0` and `100`.
  - `percent` does not decrease unless approximate progress is explicitly documented.

#### Duplicate detection

- Duplicate contacts are detected.
- Duplicate result count is correct.
- Duplicate resolution behavior matches the chosen product rule:
  - skipped
  - updated
  - failed
  - merged
- Duplicate result payload does not expose unauthorized PII.

#### Result retrieval

- Results are available only to authorized users.
- Results include summary counts.
- Row-level errors include stable error codes.
- Sensitive fields are redacted or omitted unless approved.
- Pagination is used if result lists can be large.

#### Failure scenarios

- Malformed rows.
- Empty file.
- Header-only file.
- Mixed valid and invalid rows.
- Duplicate rows within the file.
- Duplicates against existing contacts.
- Backend processing failure.
- Import job not found.
- Accessing another user’s import job.

---

### Docs handoff

Docs should explain:

- Import lifecycle.
- Required permissions.
- File or payload format.
- Maximum file size and row count, once defined.
- Async behavior and polling.
- Import states.
- Duplicate-detection behavior.
- Error codes.
- Idempotency behavior.
- PII and privacy considerations.
- Result retention period, once approved.

Docs should include examples for:

#### Create import

```http
POST /contact-imports
Idempotency-Key: 4d6f2b7a-6a5c-4f0a-9b21-example
```

#### Poll status

```http
GET /contact-imports/imp_123
```

#### Completed response

```json
{
  "id": "imp_123",
  "status": "completed_with_errors",
  "progress": {
    "totalRows": 1000,
    "processedRows": 1000,
    "percent": 100
  },
  "summary": {
    "createdCount": 900,
    "updatedCount": 50,
    "duplicateCount": 40,
    "failedCount": 10
  }
}
```

Docs should not publish exact examples containing real PII.

Human gate:

- Documentation should not be published until product, security, and API owners approve the duplicate-handling behavior, error model, limits, and retention language.

---

## 5. Verification checklist

### API contract

- [ ] `POST /contact-imports` returns `202 Accepted`, not `200 OK`, for asynchronous processing.
- [ ] Response includes import job ID.
- [ ] Status endpoint exists.
- [ ] Terminal and non-terminal states are clearly defined.
- [ ] Duplicate-detection behavior is explicit.
- [ ] Partial-success behavior is explicit.
- [ ] Error response schema is consistent.
- [ ] Large result sets are paginated or otherwise bounded.

### Security and privacy

- [ ] Auth required for all endpoints.
- [ ] Authorization scoped to the correct owner/account/workspace.
- [ ] PII is not exposed in status payloads unnecessarily.
- [ ] Row-level error details are reviewed for PII leakage.
- [ ] Uploaded files and result artifacts have a retention policy.
- [ ] Sensitive operations are audit logged.
- [ ] Rate limits and file size limits are defined.
- [ ] Malware/content scanning decision is made for uploads.

### Frontend readiness

- [ ] Progress states cover all UX needs.
- [ ] Frontend knows whether progress is exact or approximate.
- [ ] Frontend knows whether `totalRows` can be `null`.
- [ ] Polling interval guidance is defined.
- [ ] Duplicate and failed-row display behavior is approved.
- [ ] Cancellation behavior is either supported or explicitly out of scope.

### QA readiness

- [ ] Contract tests cover success, validation, auth, and failure paths.
- [ ] Idempotency tests are defined.
- [ ] Duplicate-detection test cases are defined.
- [ ] PII redaction/omission tests are defined.
- [ ] State transition tests are defined.
- [ ] Result pagination or bounding tests are defined.

### Documentation readiness

- [ ] Lifecycle documented.
- [ ] Request format documented.
- [ ] Response schemas documented.
- [ ] Error codes documented.
- [ ] Duplicate behavior documented.
- [ ] Idempotency documented.
- [ ] Security and privacy notes documented.
- [ ] Examples avoid real PII.
