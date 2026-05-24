# Invoice Approvals API — Design Recommendation

## 1. Design Summary

A small REST contract focused on the invoice-approval lifecycle. Approvals and rejections are modeled as explicit state-transition actions on an invoice resource rather than generic `PATCH` updates, because they have distinct semantics (reason required for reject, idempotency required for approve, and audit trail emission). Idempotency is handled via a client-supplied `Idempotency-Key` header so retries do not double-apply approvals. Audit metadata is exposed read-only on the invoice and via a dedicated audit sub-resource.

Supplied facts: list pending, approve one, reject with reason, idempotent approval retries, expose audit metadata. Everything else below is **inferred** or **illustrative** and should be confirmed by product/platform owners.

## 2. Proposed API Shape

Base path: `/v1` (assumed; versioning policy not supplied).

### 2.1 List pending invoices
```
GET /v1/invoices?status=pending&limit=50&cursor=<opaque>
```
- Query params:
  - `status` (filter; defaults to `pending` for this endpoint's primary use case — confirm default).
  - `limit` (cursor pagination, max assumed 100 — confirm).
  - `cursor` (opaque, forward-only).
- Response `200`:
  ```json
  {
    "data": [
      {
        "id": "inv_01HX...",
        "status": "pending",
        "amount": { "value": "1234.56", "currency": "USD" },
        "submitted_by": "user_123",
        "submitted_at": "2025-01-10T12:00:00Z",
        "audit": {
          "created_at": "...",
          "updated_at": "...",
          "last_actor_id": "user_123",
          "last_action": "submitted"
        }
      }
    ],
    "next_cursor": "..."
  }
  ```
- Illustrative fields only; actual invoice schema must come from the domain model.

### 2.2 Approve an invoice (idempotent)
```
POST /v1/invoices/{invoice_id}/approve
Headers:
  Idempotency-Key: <client-generated UUID>   (required)
  Authorization: Bearer ...
Body: {}    // or { "note": "optional reviewer note" }
```
- Semantics:
  - First successful call transitions `pending → approved` and records audit entry.
  - Retries with the **same** `Idempotency-Key` and same request body return the original response (same status, same body).
  - Retries with the same key but a **different** body return `409 Conflict` with code `idempotency_key_reuse_mismatch`.
  - Keys assumed scoped per-invoice and retained for at least 24h — confirm with platform.
- Responses:
  - `200 OK`: invoice in `approved` state with audit metadata.
  - `409 Conflict`: invoice not in `pending` state (e.g., already approved/rejected), or idempotency conflict.
  - `403 Forbidden`: caller lacks approval permission.
  - `404 Not Found`: invoice id unknown to caller.

### 2.3 Reject an invoice (with reason)
```
POST /v1/invoices/{invoice_id}/reject
Headers:
  Idempotency-Key: <client-generated UUID>   (recommended; see tradeoffs)
Body:
  {
    "reason_code": "missing_receipt",
    "reason_note": "Receipt PDF not attached."
  }
```
- `reason_code` required; `reason_note` optional free text. Allowed `reason_code` values not supplied — must come from product.
- Responses mirror approve: `200`, `409`, `403`, `404`, plus `422` if `reason_code` is missing or invalid.

### 2.4 Audit metadata

Two surfaces:

1. Embedded on the invoice (`audit` object as shown above) — lightweight, last-action only.
2. Dedicated endpoint for full history:
   ```
   GET /v1/invoices/{invoice_id}/audit-events?limit=50&cursor=...
   ```
   Returns ordered events:
   ```json
   {
     "data": [
       {
         "event_id": "evt_...",
         "invoice_id": "inv_...",
         "action": "approved",            // submitted | approved | rejected
         "actor_id": "user_456",
         "actor_role": "approver",
         "occurred_at": "2025-01-10T12:05:00Z",
         "reason_code": null,
         "reason_note": null,
         "request_id": "req_...",
         "idempotency_key": "..."
       }
     ],
     "next_cursor": null
   }
   ```
- Illustrative. Whether `idempotency_key` should be exposed externally is a security decision — flagged as a risk.

### 2.5 Error envelope (consistent across endpoints)
```json
{
  "error": {
    "code": "invoice_not_pending",
    "message": "Invoice is already approved.",
    "details": { "current_status": "approved" },
    "request_id": "req_..."
  }
}
```

## 3. Key Tradeoffs

- **Action endpoints (`/approve`, `/reject`) vs `PATCH /invoices/{id}` with `status` field.** Chose action endpoints because (a) reject requires a `reason_code`, (b) approve needs idempotency-key semantics that read awkwardly on `PATCH`, and (c) audit/permissions are clearer per-action. Cost: slightly less "pure" REST; two endpoints instead of one.
- **Idempotency on reject.** Not in the explicit requirements. Recommending it for symmetry and safe retries, but it can be omitted if product wants reject to be strictly single-shot.
- **Cursor vs offset pagination.** Cursor recommended for stable iteration over a changing pending queue; offset would drift as invoices are approved during paging. Cost: clients cannot jump to page N.
- **Embedded `audit` summary vs dedicated audit-events endpoint.** Provided both. Embedded is convenient for list views; full history endpoint avoids bloating the invoice payload.
- **Conflict on wrong state → `409` vs `422`.** Used `409` because the resource state, not the request body, is the source of conflict. Confirm against existing platform conventions.

## 4. Risks and Human Gates

Risks:
- **Reason taxonomy unknown.** `reason_code` values are not supplied; an open string would harm reporting, and a hardcoded enum may not match product needs. **Conflict to resolve with product.**
- **Permission model unspecified.** Who can approve vs reject, and whether self-approval is allowed, is not given. Must be defined before implementation.
- **Idempotency-key scope and retention** not supplied — needed to make retry semantics precise.
- **Audit exposure of `idempotency_key` and `actor_id`** may leak internal identifiers; needs security review.
- **`status=pending` filter assumes a single pending state.** Real lifecycles often have `submitted`, `in_review`, `pending_secondary_approval`, etc. State machine must be confirmed.
- **No supplied versioning policy**; `/v1` is an assumption.

Human gates required per Skill:
- Approval/rejection authorization rules (auth/permission change).
- Public commitment to the `/v1` contract, error codes, and `reason_code` enum.
- Audit field visibility (data exposure).
- Any future breaking change to state machine or action endpoints.

## 5. Verification Checklist

- [ ] Resources and actions match the confirmed invoice state machine.
- [ ] `POST /approve` is idempotent: same key + same body → identical response; same key + different body → `409`.
- [ ] `POST /reject` requires `reason_code`; rejects unknown codes with `422`.
- [ ] State-transition conflicts return `409` with a stable `error.code`.
- [ ] Pagination is cursor-based and stable under concurrent state changes.
- [ ] Audit events are emitted for every successful approve/reject and are queryable.
- [ ] AuthZ enforced per action; unauthorized callers get `403`, not `404`-leak vs `403` policy is consistent.
- [ ] Contract tests cover: happy path approve, idempotent retry, conflicting retry, reject with/without reason, approve on non-pending invoice, list pagination boundary.
- [ ] Security review of audit payload fields (especially `idempotency_key`, internal ids).
- [ ] Schema published (OpenAPI) and reviewed by at least one consumer team.

---

**Evidence note:** Supplied by task = list pending, approve, reject-with-reason, idempotent approval retries, audit metadata exposure. All field names, status codes, error codes, pagination limits, reason codes, and the `/v1` prefix are **illustrative inferences** and should be confirmed before implementation. No code, deployment, documentation publication, or testing has occurred — this is a design proposal only.
