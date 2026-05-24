<think>The user is asking me to prepare a handoff API contract for downstream reviewers (security, frontend, QA, and docs) for a bulk contact import API. Let me analyze what I need to do based on the skill under test.

Key facts provided:
- Bulk contact import API
- Imports are asynchronous
- Duplicate detection is required
- PII is involved
- Frontend needs progress states

I need to create a handoff document that covers:
1. Design summary
2. Proposed API shape
3. Key tradeoffs
4. Risks and human gates
5. Verification checklist

And I need to hand off to:
- Security (for auth and sensitive data review)
- Frontend (for developer experience)
- QA (for contract tests)
- Documentation (for developer examples)
- Product (for compatibility tradeoffs)

Let me structure this properly as a handoff document for these downstream teams.

Since I don't have specific details about the actual API design, I'll need to make reasonable assumptions based on the facts provided and clearly mark them as assumptions. I should design a RESTful API for bulk contact import that addresses:
- Async processing
- Duplicate detection
- PII handling
- Progress tracking

Let me create a comprehensive handoff document.
</think>

# Bulk Contact Import API — Handoff to Downstream Reviewers

---

## 1. Design Summary

**Purpose:** Enable authenticated clients to submit bulk contact imports for asynchronous processing with duplicate detection, progress tracking, and PII-safe handling.

**Assumptions (derived from requirements):**
- Contacts contain name, email, phone, and optional custom fields
- Duplicate detection uses email as primary key (configurable)
- Import jobs have a defined lifecycle: `pending` → `processing` → `completed` | `failed` | `partial_failure`
- Progress is reported via percentage and optional per-record status
- PII fields require redaction in logs and responses unless explicitly authorized

**API Style:** REST with JSON payloads

---

## 2. Proposed API Shape

### 2.1 Create Import Job

```
POST /v1/contacts/imports
Authorization: Bearer <token>
Content-Type: application/json

{
  "duplicate_strategy": "skip" | "replace" | "error",
  "contacts": [
    {
      "email": "user@example.com",
      "first_name": "Jane",
      "last_name": "Doe",
      "phone": "+1-555-0100",
      "custom_fields": {}
    }
  ]
}
```

**Response (202 Accepted):**
```json
{
  "job_id": "imp_abc123",
  "status": "pending",
  "total_records": 150,
  "created_at": "2024-01-15T10:30:00Z",
  "status_url": "/v1/contacts/imports/imp_abc123"
}
```

### 2.2 Get Import Job Status

```
GET /v1/contacts/imports/{job_id}
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "job_id": "imp_abc123",
  "status": "processing",
  "progress_percent": 45,
  "total_records": 150,
  "processed_records": 67,
  "duplicates_skipped": 3,
  "errors": [],
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:31:15Z"
}
```

**Status Values:**
| Status | Description |
|--------|-------------|
| `pending` | Job queued, not yet started |
| `processing` | Active import in progress |
| `completed` | All records imported successfully |
| `partial_failure` | Import done, some records failed |
| `failed` | Import aborted due to system error |

### 2.3 Get Import Results (on completion)

```
GET /v1/contacts/imports/{job_id}/results
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "job_id": "imp_abc123",
  "status": "partial_failure",
  "results": [
    { "index": 0, "status": "created", "contact_id": "cnt_001" },
    { "index": 1, "status": "duplicate_skipped", "original_id": "cnt_002" },
    { "index": 2, "status": "error", "error_code": "INVALID_PHONE", "message": "Phone format invalid" }
  ]
}
```

### 2.4 Cancel Import Job

```
POST /v1/contacts/imports/{job_id}/cancel
Authorization: Bearer <token>
```

**Constraints:**
- Only cancellable when `status` is `pending` or `processing`
- Returns `409 Conflict` if already completed/failed

---

## 3. Key Tradeoffs

| Decision | Tradeoff | Rationale |
|----------|----------|-----------|
| **Async via polling** | Extra round-trips vs. Webhook complexity | Simpler client integration; avoids callback reliability concerns |
| **Duplicate strategy per-job** | Less granular than per-record | Reduces payload size; clients can split jobs if needed |
| **Full error details in results** | Larger response payload | Enables client-side retry/display without follow-up calls |
| **Email as duplicate key** | Assumes email uniqueness | Industry norm; configurable if business requires compound keys |
| **No streaming progress** | Polling latency up to 5s | Acceptable for bulk operations; revisit if <100ms needed |

---

## 4. Risks and Human Gates

### Security Review Required
- [ ] **PII handling:** Confirm field redaction in logs and error messages
- [ ] **Authorization scope:** Verify callers can only access their own import jobs
- [ ] **Rate limits:** Define per-user and per-organization limits to prevent abuse
- [ ] **Input validation:** Sanitize all contact fields; prevent injection in custom fields

### Human Gates (require approval before production)
- [ ] Breaking changes to `duplicate_strategy` enum values
- [ ] Changes to PII exposure in error messages
- [ ] Modifications to job retention period (data lifecycle)
- [ ] Public documentation of this API surface

### Operational Risks
| Risk | Mitigation |
|------|------------|
| Large payload causes timeout | Enforce max batch size (e.g., 10,000 records) |
| Stale polling state | Include `updated_at`; clients should handle out-of-order updates |
| Duplicate detection race condition | Use database-level upsert with unique constraint |
| PII in logs | Audit log scrubbing; exclude contact fields from default logging |

---

## 5. Verification Checklist

### For QA
- [ ] Contract tests for all status transitions
- [ ] Validate `duplicate_strategy` enum rejects unknown values
- [ ] Verify `409` returned when cancelling completed job
- [ ] Test pagination/filtering on results endpoint (if >1,000 results)
- [ ] Negative tests: unauthorized access, malformed JSON, oversized payload

### For Security
- [ ] Confirm no PII in response headers or error stack traces
- [ ] Verify job_id is opaque (no sequential enumeration)
- [ ] Audit token scopes required for each endpoint

### For Frontend
- [ ] Confirm progress polling interval guidance (recommend 5s)
- [ ] Validate error state display for `partial_failure` vs `failed`
- [ ] Check that duplicate_skipped records are distinguishable from errors

### For Documentation
- [ ] Include example payloads for each endpoint
- [ ] Document retry guidance for `partial_failure` jobs
- [ ] Clarify idempotency: POST to `/imports` is idempotent if `job_id` provided in `Idempotency-Key` header

---

## 6. Handoff Assignments

| Team | Items for Review | Deadline |
|------|------------------|----------|
| **Security** | PII handling, auth scope, rate limits, log scrubbing | Before implementation |
| **Frontend** | Progress UX, error states, polling strategy | After schema freeze |
| **QA** | Contract tests, negative cases, results pagination | After API implementation |
| **Docs** | Example payloads, retry guidance, idempotency usage | After review cycle |
| **Product** | Confirm duplicate_strategy options, batch size limits | Immediate |

---

**Next Step:** Security review of PII handling and auth boundaries before implementation begins.
