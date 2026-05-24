# Bulk Contact Import API — Reviewer Handoff

## 1. Context & Constraints

- **Operation**: Bulk contact import (asynchronous)
- **Consumers**: Internal frontend (progress UI), downstream integrations (TBD — *uncertain*)
- **Known requirements**:
  - Async processing (job-based)
  - Duplicate detection (strategy *unspecified* — see open questions)
  - PII handling (names, emails, phones, etc. — *fields unconfirmed*)
  - Progress states surfaced to frontend

> ⚠️ Several inputs were not provided (auth model, scale limits, retention, dedupe rules). These are flagged as open questions per reviewer track below.

---

## 2. Proposed API Style

**REST** (job/resource pattern is well-suited to async + polling/eventing; lower client complexity than GraphQL for this single workflow).

### Resources

| Resource | Purpose |
|---|---|
| `POST /v1/contact-imports` | Create import job (accepts file ref or inline batch) |
| `GET /v1/contact-imports/{jobId}` | Job status + progress |
| `GET /v1/contact-imports/{jobId}/results` | Paginated row-level outcomes (created, updated, duplicate, error) |
| `GET /v1/contact-imports/{jobId}/errors` | Paginated error rows only |
| `DELETE /v1/contact-imports/{jobId}` | Cancel (if `status ∈ {queued, running}`) |

### Job State Machine (for frontend)

`queued → validating → running → (succeeded | partially_succeeded | failed | canceled)`

Progress payload:
```json
{
  "jobId": "imp_01H...",
  "status": "running",
  "progress": { "processed": 1240, "total": 5000, "percent": 24.8 },
  "counts": { "created": 1100, "updated": 80, "duplicates": 40, "errors": 20 },
  "startedAt": "...", "updatedAt": "...", "etaSeconds": 180
}
```

### Errors (RFC 9457 Problem Details)

```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Invalid contact row",
  "status": 422,
  "detail": "Row 42: email is malformed",
  "instance": "/v1/contact-imports/imp_01H.../results",
  "rowErrors": [{ "row": 42, "field": "email", "code": "invalid_format" }]
}
```

### Versioning
URI-versioned (`/v1/`). Additive changes only within major.

### Pagination
Cursor-based on results/errors endpoints: `?cursor=...&limit=100` → `{ items, nextCursor }`.

### Auth
*Uncertain* — assumed bearer token (OAuth2 client credentials for service-to-service, user token for UI-initiated). **Needs confirmation from security.**

---

## 3. Reviewer-Specific Handoff

### 🔒 Security Review
**Focus areas & open questions:**
- **PII inventory**: confirm which fields are PII (email, phone, address, custom fields?) and classification level.
- **Encryption**: at rest for staged import files + job result rows; TLS in transit assumed.
- **Auth & scopes**: required scope (e.g., `contacts:write`)? Tenant isolation on `jobId`?
- **Upload channel**: pre-signed URL vs. direct multipart? Virus scanning?
- **Retention**: how long are raw import payloads and per-row errors (which may contain PII) kept? Proposed: results 30d, raw payload 7d — **needs sign-off**.
- **Audit logging**: who initiated, row counts, dedupe outcomes.
- **Rate limiting / abuse**: max job size, max concurrent jobs/tenant.
- **Duplicate detection leakage**: if dedupe matches across tenants/users, response must not reveal existence of other records.

### 🎨 Frontend Review
**Contract for progress UI:**
- Polling: `GET /v1/contact-imports/{jobId}` with `Cache-Control: no-store`; recommended interval 2–5s with backoff.
- *Optional* webhook/SSE channel — **decision needed** (would remove polling).
- Progress payload (above) gives `percent`, `etaSeconds`, live counts → maps cleanly to progress bar + breakdown chips.
- Terminal states: `succeeded`, `partially_succeeded`, `failed`, `canceled` — UI must handle all four.
- Row-level outcomes via `/results` (paginated) for post-import summary screen.
- Error shape is consistent (Problem Details) — single error renderer reusable.
- **Open**: does UI need to display PII in error rows, or only row numbers + error codes? (security implication)

### ✅ QA Review
**Test surface:**
- **State transitions**: every legal + illegal path through the state machine.
- **Idempotency**: `Idempotency-Key` header on `POST /contact-imports` — retries must not create duplicate jobs.
- **Duplicate detection cases**: exact match, case-insensitive email, normalized phone, within-batch dupes, cross-batch dupes. *Rules unspecified — see open questions.*
- **Partial success**: e.g., 4,980/5,000 rows succeed → status `partially_succeeded`, errors retrievable.
- **Pagination**: cursor stability, limit bounds, empty pages.
- **Cancellation**: mid-run cancel, cancel after completion (should 409), cancel of unknown job (404).
- **Limits**: max rows/job, max file size, oversize → 413.
- **Auth/authz**: cross-tenant `jobId` access → 404 (not 403, to avoid existence leak).
- **Concurrency**: same idempotency key in parallel.
- **Backward compatibility**: contract tests against `/v1/`.

### 📘 Docs Review
**Deliverables needed:**
- OpenAPI 3.1 spec (source of truth) — *to be produced*.
- Quickstart: "Import 1,000 contacts in 5 minutes" with curl + one SDK.
- State diagram (visual) for the job lifecycle.
- Worked examples: success, partial success, validation failure, dedupe outcome.
- Error code catalog with remediation.
- PII & retention notice (coordinate with security copy).
- Pagination & idempotency conventions (link to platform-wide page).
- Changelog entry under `/v1/`.

---

## 4. Open Questions (blockers before sign-off)

1. **Duplicate detection rules** — match keys, precedence (skip / update / merge), cross-tenant scope?
2. **PII field list** and classification.
3. **Auth model and required scopes.**
4. **Scale targets** — max rows/job, max concurrent jobs, expected throughput (drives async SLAs and ETA accuracy).
5. **Delivery of progress** — polling only, or SSE/webhook?
6. **Retention policy** for raw payload, results, and error rows.
7. **Upload mechanism** — inline JSON, multipart, or pre-signed URL?
8. **Consumer list beyond frontend** (affects versioning rigor and SDK scope).

---

## 5. Next Steps

1. Resolve open questions with product + security (owner: API lead).
2. Publish OpenAPI 3.1 draft for line-by-line review.
3. Async review cycles with each track above; consolidate in design doc.
4. Validate with two example flows (happy path + partial failure) before implementation kickoff.

> **Boundary note**: This handoff covers API contract design only. Implementation choices (queue tech, dedupe algorithm internals, storage), threat modeling depth, and environment-specific validation are out of scope for this skill and should be handled in their respective review tracks.
