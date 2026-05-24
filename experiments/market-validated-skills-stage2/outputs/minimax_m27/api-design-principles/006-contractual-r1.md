# Bulk Contact Import API — Handoff to Downstream Reviewers

## 1. Design Summary

A RESTful endpoint for initiating bulk contact imports with an asynchronous job model. Supports tracking import progress, reporting duplicate outcomes, and handling PII securely throughout the lifecycle.

**Resource model:** `POST /contacts/imports` creates an import job; `GET /contacts/imports/{jobId}` returns status and results; `GET /contacts/imports/{jobId}/errors` surfaces validation failures.

**Assumptions inferred (not confirmed):**
- File upload via multipart/form-data or URL-based fetch
- Duplicate detection uses email as primary key (unless a custom dedup key is specified)
- PII is encrypted at rest; transit uses TLS 1.2+
- Progress states: `pending` → `processing` → `completed` | `failed` | `partial`

---

## 2. Proposed API Shape

### Create Import Job

```
POST /contacts/imports
Content-Type: multipart/form-data
Authorization: Bearer {token}

-- Request body (form fields) --
file: <CSV/JSON>
deduplication_key: email | phone | external_id (default: email)
notify_webhook_url: <optional URL>

-- Response 202 Accepted --
{
  "job_id": "imp_abc123",
  "status": "pending",
  "estimated_total_records": 1500,
  "created_at": "2024-01-15T10:30:00Z",
  "_links": {
    "self": "/contacts/imports/imp_abc123",
    "errors": "/contacts/imports/imp_abc123/errors"
  }
}
```

### Poll Job Status

```
GET /contacts/imports/{jobId}
Authorization: Bearer {token}

-- Response 200 OK --
{
  "job_id": "imp_abc123",
  "status": "processing",
  "progress": {
    "total_records": 1500,
    "processed": 820,
    "imported": 795,
    "duplicates_skipped": 20,
    "validation_errors": 5,
    "percent_complete": 54
  },
  "duplicate_detection": {
    "rule": "email",
    "action": "skip"
  },
  "completed_at": null
}
```

### Fetch Validation Errors

```
GET /contacts/imports/{jobId}/errors?page=1&per_page=100
Authorization: Bearer {token}

-- Response 200 OK --
{
  "errors": [
    {
      "row": 42,
      "field": "email",
      "value": "invalid-format",
      "message": "Email address is malformed"
    }
  ],
  "pagination": {
    "total_errors": 5,
    "page": 1,
    "per_page": 100,
    "has_more": false
  }
}
```

### Terminal States

```
-- Completed --
{
  "job_id": "imp_abc123",
  "status": "completed",
  "progress": {
    "total_records": 1500,
    "processed": 1500,
    "imported": 1490,
    "duplicates_skipped": 5,
    "validation_errors": 5
  },
  "completed_at": "2024-01-15T10:35:22Z"
}

-- Partial (if errors are non-blocking) --
{
  "status": "partial",
  "note": "2 records failed due to system errors. See /contacts/imports/imp_abc123/errors"
}
```

---

## 3. Key Tradeoffs

| Decision | Tradeoff |
|----------|----------|
| **Polling vs. Webhooks** | Chose polling (`GET /imports/{id}`) over webhooks for simplicity. Webhooks add reliability but require receiver infrastructure; polling is easier for frontend but adds load. Consider webhooks if import jobs exceed 5 min. |
| **Dedup action: skip vs. update** | Default is `skip` (ignore duplicates). Alternative `update` would overwrite existing records but introduces risk of accidental data loss. The contract should make the behavior explicit. |
| **Partial completion** | A `partial` state acknowledges that some records succeeded while others failed. This is honest but may confuse consumers expecting all-or-nothing semantics. Document clear retry guidance. |
| **Error granularity** | Providing per-row error details enables targeted fixes but increases storage and response size. Page errors to avoid unbounded responses. |
| **File size limits** | Not specified; expect a practical limit (e.g., 50 MB, 500k rows). This should be documented and enforced with a clear `413 Payload Too Large` response. |

---

## 4. Risks and Human Gates

### Security Gate Required
- **PII handling:** Contact records likely include name, email, phone—consider GDPR/CCPA implications. Confirm encryption at rest, field-level access controls, and audit logging for who accessed import jobs.
- **Webhook URL validation:** If `notify_webhook_url` is supported, validate URL ownership to prevent SSRF or redirect to internal services.
- **Upload scanning:** File uploads must be scanned for malware before parsing.

### Compatibility Concerns
- If deduplication key changes post-import, existing duplicates may re-enter the system. Version the dedup policy in the job response.
- If the import job schema changes (new required fields), in-flight jobs may fail silently. Document schema versioning or lock fields for active jobs.

### Operational Risks
- **Large file DoS:** Without limits, a malicious user could upload enormous files and exhaust parse workers. Enforce limits and return `429` with `Retry-After` when throttled.
- **Zombie jobs:** Jobs stuck in `processing` for >1 hour without progress may indicate a worker crash. Implement a stale-job watchdog.

---

## 5. Verification Checklist

### Contract Tests (QA)
- [ ] `POST /contacts/imports` returns `202` with valid job_id on valid file upload
- [ ] `POST /contacts/imports` returns `400` on malformed CSV, `413` on oversized file, `401` on missing/invalid token
- [ ] `GET /contacts/imports/{jobId}` returns correct progress for `pending`, `processing`, `completed`, `failed`, `partial`
- [ ] `GET /contacts/imports/{jobId}/errors` returns paginated errors with row numbers and field names
- [ ] Duplicate detection: importing same email twice results in `duplicates_skipped` increment and only one record in system
- [ ] Idempotency: retrying the same `POST /contacts/imports` with identical file creates new job (no cached response)

### Security Review
- [ ] PII fields are not logged in plain text
- [ ] Import job responses do not expose raw record content without explicit permission
- [ ] Webhook URL validates against SSRF (block internal IPs, require HTTPS)
- [ ] File upload size limits enforced before parsing begins

### Frontend Review
- [ ] Poll interval: recommend 5–10 seconds; confirm UI handles `pending` state gracefully on slow connections
- [ ] Error page links work from `partial` or `failed` states
- [ ] Progress bar handles `percent_complete` rounding (e.g., 99.9% may display as 99% or 100%)

### Documentation Review
- [ ] Describe deduplication key behavior and how to choose `email` vs. `phone`
- [ ] Include sample CSV with headers matching expected field names
- [ ] Document `Retry-After` semantics for `429` and `503` responses
- [ ] Clarify that job results (imported records) are available via standard `GET /contacts` after job completes—not embedded in job response

---

## Handoff Routing

| Reviewer | Focus Areas |
|----------|-------------|
| **Security** | PII handling, webhook SSRF, file upload size limits, audit logging |
| **Frontend** | Poll timing, error state UX, progress state handling, webhook vs. polling preference |
| **QA** | Contract tests above, dedup scenario coverage, error response schema validation |
| **Docs** | Sample files, dedup key explanation, rate limit / throttle behavior, migration guidance if schema evolves |

---

**Status:** Draft awaiting review from security gate before further iteration. No deployment or test evidence supplied; all items above are proposed design, not confirmed implementation.
