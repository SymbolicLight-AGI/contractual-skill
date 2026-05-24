# Invoice Approvals API — Contract Design

## 1. Consumers, Use Cases, Constraints

**Consumers**
- Internal finance/approver web UI
- Mobile approver app (latency-sensitive)
- Workflow automation services (retry-prone, must be idempotent)

**Use cases**
- List invoices awaiting my approval
- Approve a single invoice (with retry safety)
- Reject a single invoice with a reason
- View who did what, when (audit trail)

**Constraints / assumptions** *(uncertain — confirm with stakeholders)*
- Authenticated users with role `approver`
- Invoices already exist in the system (creation is out of scope)
- Decisions are terminal but auditable

---

## 2. Style & Resources

**Style:** REST over HTTPS, JSON, resource-oriented. (GraphQL not chosen — needs are narrow, mutations are well-bounded, and idempotency semantics are clearer in REST.)

**Base:** `/v1`

**Primary resource:** `invoice` with sub-resource `approval` representing the decision.

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/v1/invoices?status=pending` | List pending invoices |
| `GET` | `/v1/invoices/{id}` | Retrieve invoice + current approval state |
| `POST` | `/v1/invoices/{id}/approval` | Approve the invoice |
| `POST` | `/v1/invoices/{id}/rejection` | Reject the invoice with a reason |
| `GET` | `/v1/invoices/{id}/audit` | Retrieve audit trail |

Using two distinct sub-resource endpoints (`/approval`, `/rejection`) keeps each action’s schema and semantics explicit and avoids overloading a single endpoint with conditional fields.

---

## 3. Resource Schemas

### Invoice (summary)
```
{
  "id": "inv_01HXYZ...",
  "vendor": "Acme Corp",
  "amount": { "currency": "USD", "value": "1240.00" },
  "submitted_at": "2026-02-20T14:02:11Z",
  "status": "pending" | "approved" | "rejected",
  "approval": {
    "decided_by": "user_123" | null,
    "decided_at": "2026-02-21T09:00:00Z" | null,
    "reason": "string" | null
  }
}
```

### Audit entry
```
{
  "event_id": "evt_...",
  "invoice_id": "inv_...",
  "actor_id": "user_123",
  "action": "viewed" | "approved" | "rejected" | "reopened",
  "reason": "string" | null,
  "at": "2026-02-21T09:00:00Z",
  "request_id": "req_...",
  "idempotency_key": "..." | null
}
```

---

## 4. Key Endpoint Specs

### List pending invoices
`GET /v1/invoices?status=pending&assignee=me&cursor=<opaque>&limit=50`

- Filters: `status`, `assignee`, `min_amount`, `max_amount`, `submitted_after`
- Response: `{ "data": [Invoice], "next_cursor": "..." }`
- Cursor-based pagination (stable under inserts).

### Approve
`POST /v1/invoices/{id}/approval`

Headers:
- `Idempotency-Key: <client-generated-uuid>` *(required)*
- `If-Match: "<etag>"` *(optional, for optimistic concurrency)*

Body: `{}` (no fields required; approver inferred from auth token)

Responses:
- `200 OK` — already approved with same idempotency key; returns prior result
- `201 Created` — newly approved
- `409 Conflict` — invoice in terminal non-approved state, or idempotency key reused with different payload
- `412 Precondition Failed` — stale `If-Match`

### Reject
`POST /v1/invoices/{id}/rejection`

Headers: `Idempotency-Key` required.

Body:
```
{
  "reason_code": "missing_po" | "duplicate" | "amount_mismatch" | "other",
  "reason_note": "Free-text explanation (required when reason_code = other)"
}
```
- `reason_code` required; `reason_note` length-capped (e.g., 1000 chars).

---

## 5. Idempotency

- Clients send `Idempotency-Key` on every `POST` to `/approval` and `/rejection`.
- Server stores `(key, route, request_hash, response)` for at least 24h *(retention period — confirm)*.
- Same key + same payload → replay stored response (`200`).
- Same key + different payload → `409 Conflict` with `code: idempotency_key_reuse`.
- Keys are scoped per invoice + route to avoid cross-contamination.

---

## 6. Errors

Uniform error envelope (RFC 7807-style):
```
{
  "type": "https://errors.example.com/invoice_already_decided",
  "title": "Invoice already decided",
  "status": 409,
  "code": "invoice_already_decided",
  "detail": "Invoice inv_01HXYZ was rejected at 2026-02-20T...",
  "request_id": "req_..."
}
```

Standard codes used:
- `400` validation, `401` unauth, `403` forbidden, `404` not found, `409` state conflict / idempotency reuse, `412` precondition, `422` semantic validation, `429` rate-limited, `5xx` server.

---

## 7. Versioning

- URI-based major version (`/v1`) for breaking changes.
- Additive changes (new fields, new optional filters) are non-breaking and shipped within the same major version.
- Deprecations announced via `Deprecation` and `Sunset` response headers with a minimum 6-month window *(policy — confirm)*.

---

## 8. Pagination

- Cursor-based (`cursor`, `next_cursor`), `limit` default 50, max 200.
- Avoid offset pagination — invoice lists mutate frequently as approvals happen.

---

## 9. Auth

- OAuth 2.0 bearer tokens (or session-derived service token).
- Scopes: `invoices:read`, `invoices:approve`, `invoices:reject`, `invoices:audit:read`.
- Authorization enforced server-side: only assigned approvers (or delegates) can decide; self-approval (approver == submitter) is rejected with `403`.

---

## 10. Audit Metadata

- Every state-changing call emits an immutable audit record (see schema above).
- Exposed via `GET /v1/invoices/{id}/audit` returning chronological events.
- Audit records include `actor_id`, `request_id`, and `idempotency_key` to support traceability and replay investigation.
- Audit endpoint is read-only; no mutation or deletion path.

---

## 11. Worked Example

1. UI calls `GET /v1/invoices?status=pending&assignee=me` → list returned.
2. User clicks Approve on `inv_01HXYZ`. UI generates `Idempotency-Key: 4f1c...`.
3. `POST /v1/invoices/inv_01HXYZ/approval` with that key → `201 Created`.
4. Network blip — UI retries with the **same** key → `200 OK`, same body. No duplicate audit entry beyond the original.
5. Later, `GET /v1/invoices/inv_01HXYZ/audit` shows one `approved` event with the actor, timestamp, request_id, and idempotency_key.

---

## 12. Consistency Review Checklist

- [x] Plural, lowercase, hyphen-free resource names
- [x] Verbs expressed via HTTP methods, not paths
- [x] Approve/reject are POSTs to sub-resources (not PATCH on parent) — explicit intent
- [x] All POSTs accept `Idempotency-Key`
- [x] Errors use a single envelope with stable `code` values
- [x] Pagination, versioning, auth strategies uniform across endpoints
- [x] Audit is queryable but not mutable

---

## Open Questions (flagged uncertainty)

1. Can a rejected invoice be reopened/resubmitted? If yes, that's a separate endpoint (`POST /invoices/{id}/reopen`) — out of current scope.
2. Multi-approver workflows (e.g., amount thresholds requiring N approvals)? Current design assumes single-decider.
3. Idempotency key retention window and audit retention period — needs compliance input.
4. Should partial approvals (line-item level) be supported? Current design is whole-invoice only.
