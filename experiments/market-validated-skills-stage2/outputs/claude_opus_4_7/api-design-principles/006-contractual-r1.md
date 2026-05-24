# Handoff: Bulk Contact Import API

## 1. Design Summary

Bulk contact import is an **asynchronous, job-oriented** operation. Clients submit a batch, receive a job handle, and poll (or subscribe to) status. Duplicate detection is part of per-record processing and surfaces in the job's per-record results. PII handling, auth, and progress semantics need explicit reviewer sign-off before implementation.

**Supplied facts:** asynchronous processing, duplicate detection required, PII involved, frontend needs progress states.
**Inferred (assumptions, not given):** REST style, job/resource model, polling as baseline. Mark as illustrative.

## 2. Proposed API Shape (illustrative)

### Submit import
```
POST /v1/contact-imports
Idempotency-Key: <client-generated UUID>
Content-Type: application/json

{
  "source": "<string, optional>",
  "duplicate_strategy": "skip | merge | error",   // assumption — confirm with product
  "contacts": [ { ...contact fields... } ]
}

201 Created
{
  "import_id": "imp_123",
  "status": "queued",
  "submitted_count": 2500,
  "created_at": "..."
}
```

### Poll status
```
GET /v1/contact-imports/{import_id}

200 OK
{
  "import_id": "imp_123",
  "status": "queued | running | completed | completed_with_errors | failed | canceled",
  "progress": {
    "total": 2500,
    "processed": 1800,
    "succeeded": 1700,
    "duplicates": 80,
    "failed": 20
  },
  "started_at": "...",
  "completed_at": null
}
```

### Per-record results (paginated)
```
GET /v1/contact-imports/{import_id}/results?status=duplicate|failed|succeeded&cursor=...&limit=100

200 OK
{
  "items": [
    {
      "row_index": 42,
      "status": "duplicate",
      "matched_contact_id": "con_999",
      "match_reason": "email"
    },
    {
      "row_index": 51,
      "status": "failed",
      "error": { "code": "invalid_email", "message": "..." }
    }
  ],
  "next_cursor": "..."
}
```

### Cancel (optional, human-gate)
```
POST /v1/contact-imports/{import_id}:cancel
```

### Error model (illustrative)
```
{ "error": { "code": "validation_error", "message": "...", "details": [...] } }
```

**Status semantics**
- `201` on submission accepted (job created), not on completion.
- `200` on status reads.
- `409` if `Idempotency-Key` collides with a different payload.
- `413` on payload too large; document a max batch size (value not supplied — confirm).

## 3. Key Tradeoffs

| Decision | Option A | Option B | Note |
|---|---|---|---|
| Progress delivery | Polling `GET` | Webhook / SSE / WebSocket push | Polling is simplest; push reduces latency for frontend. Frontend should weigh in. |
| Duplicate strategy | Per-request flag | Account-wide policy | Per-request is more flexible; account-wide is simpler. Product decision. |
| Result delivery | Inline in status | Separate paginated results endpoint (recommended) | Large jobs make inline impractical. |
| Submission format | JSON array | Multipart CSV upload | CSV matters for large imports; not specified in task. |
| Idempotency | Header-based key | Natural key dedup | Header recommended for safe retries on submit. |

## 4. Risks and Human Gates

**Risks**
- **PII exposure**: contact payloads, error logs, and per-record results may contain emails/phones/names. Logging, retention, and access scoping unspecified.
- **Duplicate detection semantics undefined**: matching keys (email? phone? normalized?), cross-tenant scope, and merge behavior are not in the task.
- **Result retention**: how long `import_id` and per-record results remain queryable is unspecified.
- **Backpressure / batch size limits** not defined.
- **Auth boundary** not specified — who can submit, view, cancel another user's import?
- **Observability**: no specified metrics, tracing, or audit trail for PII access.

**Human gates required**
- Auth and permission model (security + product).
- PII retention and result-endpoint access policy (security + legal if applicable).
- Public versioning commitment (`/v1`) and breaking-change policy (product).
- Duplicate strategy default and whether it is customer-visible (product).
- Webhook/push delivery commitment if chosen (platform).

## 5. Verification Checklist

- [ ] Contract tests cover: submit, poll, results pagination, cancel, idempotency replay, 409 on key collision.
- [ ] Schema validation on submission (per-record and batch-level limits).
- [ ] Error code catalog reviewed and stable.
- [ ] Duplicate detection rules documented and tested with fixtures.
- [ ] PII fields classified; logging redaction verified.
- [ ] AuthZ tests: cross-tenant access to `import_id` denied.
- [ ] Progress monotonicity test (`processed` never decreases).
- [ ] Terminal states are final (no transitions out of `completed`/`failed`/`canceled`).
- [ ] Backward-compatibility review for any later field additions.

---

## Reviewer Handoff

### → Security
Please review:
- Auth model for submit/read/cancel and cross-tenant isolation on `import_id`.
- PII handling in request bodies, results endpoint, logs, and error messages (redaction policy).
- Retention of import payloads and per-record results.
- Idempotency-Key storage (may itself be sensitive if derived from PII).
- Audit logging for access to per-record results.
- Rate limits and abuse protection on bulk submit.

### → Frontend
Please confirm:
- Progress UX needs: is polling acceptable, or is push (SSE/WebSocket/webhook-to-BFF) required?
- Required progress fields (`total`, `processed`, `succeeded`, `duplicates`, `failed`) — anything missing?
- Whether per-row error surfacing in UI needs additional fields (e.g., original row echo).
- Cancellation UX expectations and partial-success display.
- Expected batch sizes from the UI (drives pagination/limits).

### → QA
Please plan:
- Contract tests against the OpenAPI spec (spec not yet supplied — flag as prerequisite).
- Idempotency replay scenarios (same key + same body, same key + different body).
- State-machine tests for `status` transitions and terminality.
- Duplicate-detection fixtures once rules are confirmed by product.
- Large-batch and boundary tests (max size, empty batch, all-duplicates, all-failures).
- AuthZ negative tests.

### → Docs
Please prepare:
- Endpoint reference for submit / status / results / cancel.
- Async lifecycle diagram and status state machine.
- Idempotency-Key usage guide with examples.
- Duplicate strategy explanation (pending product confirmation).
- Error code reference.
- Quickstart: submit → poll → fetch results.
- Clear note that examples shown here are **illustrative**; finalize against the implemented OpenAPI spec.

---

## Boundary Notes

- No OpenAPI fragment, existing conventions, auth model, scale numbers, or duplicate-matching rules were supplied. Concrete field names, limits, and status codes above are **illustrative** and require confirmation.
- This Skill cannot publish docs, create tickets, or notify reviewers. Next step: a human owner should route this handoff to each team (e.g., via the team's tracker) and attach the eventual OpenAPI draft.
