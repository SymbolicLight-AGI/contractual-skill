# Invoice Approvals API — Design Recommendation

## 1. Design Summary

A small REST contract over an `invoices` resource with approval/rejection modeled as **state-transition sub-actions**. Idempotency is handled via a client-supplied `Idempotency-Key` header on write operations. Audit metadata is exposed as a read-only block on the invoice and, optionally, via a dedicated audit sub-resource.

Supplied facts: list pending invoices, approve, reject with reason, idempotent approval retries, expose audit metadata.
Inferred (assumptions, flagged): authn/authz exists; invoices have an `id`, status lifecycle, and timestamps; rejection reason is free-text with a bounded length; consumers are internal/back-office first.

## 2. Proposed API Shape

Base path: `/v1/invoices` (versioning assumption — see §3).

### 2.1 List pending invoices
```
GET /v1/invoices?status=pending&cursor=<opaque>&limit=50
```
- Filtering: `status` (required for this use case; default not assumed).
- Pagination: cursor-based (`cursor`, `limit`, response `next_cursor`). Illustrative.
- Response (illustrative):
```json
{
  "data": [
    {
      "id": "inv_01H...",
      "status": "pending",
      "amount": { "value": "1234.56", "currency": "USD" },
      "submitted_at": "2025-01-10T12:00:00Z",
      "audit": {
        "created_at": "2025-01-10T12:00:00Z",
        "created_by": "user_abc",
        "last_updated_at": "2025-01-10T12:00:00Z",
        "last_updated_by": "user_abc",
        "version": 1
      }
    }
  ],
  "next_cursor": "eyJ..."
}
```
Note: amount/currency fields are illustrative; not specified in the task.

### 2.2 Approve an invoice
```
POST /v1/invoices/{id}/approve
Headers:
  Idempotency-Key: <client-generated UUID>   # required
  If-Match: "<etag>"                          # optional optimistic concurrency
Body: {}    # empty or optional { "note": "..." }
```
- Returns `200 OK` with the updated invoice; `409 Conflict` if state transition is invalid; `412 Precondition Failed` on stale `If-Match`.
- Idempotency: server stores the result keyed by `(actor, invoice_id, Idempotency-Key)` for a defined retention window (assumption: 24h; confirm with platform). Replays return the original response.

### 2.3 Reject an invoice
```
POST /v1/invoices/{id}/reject
Headers:
  Idempotency-Key: <client-generated UUID>   # required
Body:
  { "reason": "string, 1..1000 chars" }
```
- `reason` is required and non-empty.
- Same idempotency and concurrency semantics as approve.

### 2.4 Audit metadata
- Inline `audit` block on every invoice response (see §2.1).
- Optional dedicated endpoint for full history:
```
GET /v1/invoices/{id}/audit-events?cursor=&limit=
```
Each event (illustrative): `{ id, type: "approved"|"rejected"|"created"|..., actor, occurred_at, reason?, idempotency_key, request_id }`.

### 2.5 Error model
Consistent envelope (illustrative):
```json
{
  "error": {
    "code": "invalid_state_transition",
    "message": "Invoice is not in 'pending' state.",
    "details": { "current_status": "approved" },
    "request_id": "req_..."
  }
}
```
Suggested codes:
- `400 invalid_request` (missing reason, bad cursor)
- `401 unauthenticated` / `403 forbidden`
- `404 not_found`
- `409 invalid_state_transition` or `idempotency_key_conflict` (key reused with a different request body)
- `412 precondition_failed`
- `422 validation_failed`
- `429 rate_limited`

### 2.6 Status codes for writes
- `200 OK` — action applied (or idempotent replay).
- `409` — state conflict or idempotency-key reuse with mismatched payload.
- `422` — semantic validation failure (e.g., empty `reason`).

## 3. Key Tradeoffs

- **Action sub-resources (`/approve`, `/reject`) vs. PATCH on status.** Chosen sub-actions because rejection carries a required `reason` and approval needs distinct idempotency/audit semantics; PATCH would conflate fields and complicate authorization. Tradeoff: less "pure REST," more explicit verbs.
- **Cursor vs. offset pagination.** Cursor scales better and avoids skew as invoices change state; offset is simpler for UIs needing page numbers. Recommend cursor; revisit if product needs page jumps.
- **Idempotency-Key required vs. optional.** Required reduces accidental double-approval at the cost of client effort. Strongly recommended for financial state transitions.
- **Inline audit vs. separate endpoint.** Inline covers the stated "expose audit metadata" need cheaply; separate endpoint adds history depth. Offering both keeps list payloads small while supporting investigations.
- **Single `reason` string vs. structured reason (code + note).** Structured improves analytics and policy enforcement; free-text is simpler. Requirements only mandate "a reason" — flagged for product input.

## 4. Risks and Human Gates

Risks:
- **Authorization model unspecified.** Who can approve vs. reject, self-approval rules, segregation of duties — unknown. Must be defined before implementation.
- **State machine unspecified.** Allowed transitions (e.g., can a rejected invoice be re-approved?) not provided.
- **PII / financial data exposure.** Listing endpoints may leak sensitive fields; field-level filtering needs review.
- **Idempotency window and storage.** Retention and scoping rules affect correctness of retries across actors/devices.
- **Audit immutability and retention.** Compliance (SOX, regional finance regs) likely applies — not specified.
- **Rate limits and abuse vectors** on list and write endpoints — not specified.

Human gates required:
- Approval/rejection authorization policy (security + product).
- Public-vs-internal API commitment and versioning policy.
- Audit retention and immutability guarantees (compliance).
- Any breaking changes to existing invoice endpoints (assumption: none exist; confirm).
- Customer-visible error code taxonomy.

## 5. Verification Checklist

- [ ] Resource and method choices reviewed against existing org API conventions (not supplied).
- [ ] State machine for invoice statuses documented and enforced server-side.
- [ ] Contract tests for: list filter by `status`, approve happy path, reject requires `reason`, invalid state transition returns `409`, idempotent replay returns identical response, idempotency-key reuse with different body returns `409`.
- [ ] Schema validation (OpenAPI) for requests and responses, including error envelope.
- [ ] AuthN/AuthZ checks: only permitted roles can approve/reject; segregation-of-duties rule confirmed.
- [ ] Audit events written atomically with state change; include actor, timestamp, reason, idempotency key, request id.
- [ ] Observability: per-endpoint metrics, structured logs with `request_id`, alerts on elevated `409`/`422` rates.
- [ ] Pagination tested for stability under concurrent status changes.
- [ ] Backward-compatibility review (assumption: greenfield; confirm).
- [ ] Security review of response fields for sensitive data exposure.

---

**Boundary note:** This contract is a design proposal only. No OpenAPI document, code, tests, or deployment has been produced or executed. Examples shown are illustrative and should be confirmed against real domain fields, auth model, and org API standards before implementation. Handoffs: security (authz, sensitive fields), platform (conventions, idempotency storage), QA (contract tests), docs (developer examples), product (reason structure, state machine, versioning).
