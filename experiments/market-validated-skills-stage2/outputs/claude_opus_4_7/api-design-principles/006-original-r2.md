# Bulk Contact Import API — Handoff Package

## 1. Consumers, Use Cases, Constraints

**Consumers**
- Internal frontend (progress UI, status polling)
- Customer admins via authenticated session
- Possibly downstream CRM integrations (assumed — **uncertain**, confirm scope)

**Primary use cases**
- Upload a batch of contacts (CSV/JSON) for asynchronous processing
- Poll/subscribe to import job progress
- Retrieve results: imported, skipped (duplicates), failed rows
- Cancel an in-flight import (assumed — **confirm with product**)

**Constraints**
- Async processing (job-based, not request/response)
- Duplicate detection required (criteria **uncertain** — email? phone? composite? confirm)
- PII handling (names, emails, phones — possibly addresses)
- Frontend requires intermediate progress states
- Max batch size **unspecified** — recommend defining (e.g., 10k rows)

---

## 2. Proposed API Style and Resource Model

**Style:** REST with job resource (best fit for async + polling; GraphQL subscriptions optional later).

### Resources

| Resource | Path | Purpose |
|---|---|---|
| Import Job | `POST /v1/contact-imports` | Create import job (returns 202 + job id) |
| Import Job | `GET /v1/contact-imports/{id}` | Retrieve job status/progress |
| Import Job Items | `GET /v1/contact-imports/{id}/items?status=failed\|duplicate` | Paginated row-level results |
| Import Job | `DELETE /v1/contact-imports/{id}` | Cancel (if supported) |

### Job state machine (frontend progress states)
`queued → validating → processing → completed`
Branches: `failed`, `cancelled`, `partially_completed`

Progress payload:
```json
{
  "id": "imp_01H...",
  "state": "processing",
  "progress": { "total": 5000, "processed": 3120, "imported": 2980, "duplicates": 110, "failed": 30 },
  "created_at": "...", "updated_at": "...",
  "estimated_completion_at": "..."
}
```

---

## 3. Cross-Cutting Concerns

### Errors (RFC 7807-style)
```json
{ "type": "about:blank/validation_error", "title": "Invalid row", "status": 422,
  "detail": "Row 42 missing required field 'email'", "row": 42, "field": "email" }
```
Codes to define: `validation_error`, `duplicate_detected`, `payload_too_large`, `rate_limited`, `forbidden_pii_field`.

### Versioning
- URI versioning (`/v1/`) for clarity; deprecation via `Sunset` header.

### Pagination
- Cursor-based for `/items` (stable under long-running jobs): `?cursor=...&limit=100`.

### AuthN/Z
- Bearer token (OAuth2) + scope `contacts:import`.
- Per-tenant isolation enforced on job id lookup.
- Idempotency: `Idempotency-Key` header on `POST` to prevent duplicate submissions.

### PII handling (flag for Security)
- Upload via pre-signed URL **or** direct multipart — **decision needed**.
- Encrypt at rest; redact PII in logs and error payloads (return row index, not row content).
- TTL on raw upload artifact (recommend ≤24h post-completion).
- Audit log: who imported, when, row counts (no PII values).

### Duplicate detection (flag for Product/Security)
- Match key(s) **uncertain** — confirm.
- Policy on match: `skip` | `update` | `error`. Recommend `skip` default with per-request override.

---

## 4. Example Flow

```http
POST /v1/contact-imports
Idempotency-Key: 8f3...
Content-Type: application/json

{ "source": "csv", "upload_id": "up_123", "on_duplicate": "skip" }

→ 202 Accepted
Location: /v1/contact-imports/imp_01H...
{ "id": "imp_01H...", "state": "queued" }
```

```http
GET /v1/contact-imports/imp_01H...
→ 200 { "state": "processing", "progress": { ... } }
```

---

## 5. Reviewer-Specific Handoff

### → Security
- Confirm PII-in-transit/at-rest model and upload mechanism (pre-signed vs multipart).
- Review log redaction rules and audit event schema.
- Validate `Idempotency-Key` storage TTL and tenant scoping on job ids.
- Confirm retention for raw upload + per-row results.
- **Open question:** is PII row content ever returned in error responses? Recommend: no.

### → Frontend
- States to render: `queued, validating, processing, completed, partially_completed, failed, cancelled`.
- Polling cadence recommendation: 2s while `processing`, backoff to 10s; or adopt SSE/WebSocket later.
- Progress fields are additive and monotonic except on retry.
- Use `Location` header from `POST` to drive polling URL.
- **Open question:** is cancel exposed in UI?

### → QA
- Test matrix: empty file, oversized file, malformed rows, all-duplicates, partial duplicates, mid-job cancel, idempotency replay, auth/scope failures, cross-tenant access attempt.
- Verify no PII appears in error payloads or logs.
- State machine transitions — assert no illegal transitions.
- Pagination stability while job still writing items.

### → Docs
- Document: lifecycle diagram, all states, error catalog, idempotency semantics, duplicate policy options, rate limits, max batch size, retention windows.
- Provide curl + one SDK example per endpoint.
- Add a "PII & compliance" section summarizing what is and is not stored/returned.

---

## 6. Open Questions Blocking Sign-Off

1. Duplicate match key definition and override policy.
2. Max batch size and rate limits.
3. Upload mechanism (pre-signed URL vs multipart).
4. Cancellation supported in v1?
5. Retention windows for raw uploads and item-level results.
6. Are third-party/CRM consumers in scope for v1?

---

*Boundary note: this skill covers API contract design and handoff. Implementation details (framework, queue choice, DB schema) and environment-specific security validation are out of scope — route those to the respective owning teams after contract sign-off.*
