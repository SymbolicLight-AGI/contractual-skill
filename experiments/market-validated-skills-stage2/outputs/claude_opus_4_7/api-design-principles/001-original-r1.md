# Invoice Approvals API Contract

## 1. Consumers, Use Cases, Constraints

**Consumers:** Internal finance dashboard (primary), mobile approval app, audit/reporting service (read-only).

**Use cases:**
- Approver lists invoices awaiting their action.
- Approver approves or rejects an invoice (with reason).
- System retries approval calls safely after timeouts/network errors.
- Auditors read who/when/why for every state change.

**Constraints:**
- Approvals are financially material → must be **idempotent**, **auditable**, and **authenticated**.
- Concurrent approvers possible → need optimistic concurrency.
- Assumed: synchronous approval is acceptable (flag if async workflow is required).

## 2. API Style and Resources

**Style:** REST over HTTPS, JSON. REST fits the resource-centric, action-oriented, low-cardinality nature of approvals better than GraphQL.

**Base URL:** `https://api.example.com/v1`

**Primary resource:** `invoice` with sub-resource `approvals` capturing each decision event.

### Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/invoices?status=pending&assignee=me&page[cursor]=...&page[limit]=50` | List pending invoices for the caller |
| `GET` | `/invoices/{invoiceId}` | Retrieve a single invoice including current state and audit metadata |
| `POST` | `/invoices/{invoiceId}/approvals` | Record an approval or rejection decision |
| `GET` | `/invoices/{invoiceId}/approvals` | List the audit trail of decisions for that invoice |

Decisions are modeled as **appended events** rather than PATCHing `status`. This gives a natural audit log and clean idempotency semantics.

### Resource: Invoice (response shape)

```json
{
  "id": "inv_01HXYZ...",
  "vendor": { "id": "ven_123", "name": "Acme Corp" },
  "amount": { "value": "1250.00", "currency": "USD" },
  "issuedAt": "2026-02-20T10:00:00Z",
  "dueAt": "2026-03-20T00:00:00Z",
  "status": "pending",                // pending | approved | rejected | cancelled
  "assignee": { "id": "usr_42", "name": "J. Doe" },
  "version": 7,                       // for optimistic concurrency (ETag mirror)
  "audit": {
    "createdAt": "2026-02-20T10:00:00Z",
    "createdBy": "usr_system",
    "updatedAt": "2026-02-22T14:11:09Z",
    "updatedBy": "usr_42",
    "lastDecisionId": "dec_01HXY..."
  },
  "_links": {
    "self": "/v1/invoices/inv_01HXYZ",
    "approvals": "/v1/invoices/inv_01HXYZ/approvals"
  }
}
```

### Resource: Approval decision (event)

```json
{
  "id": "dec_01HXY...",
  "invoiceId": "inv_01HXYZ",
  "decision": "approved",             // approved | rejected
  "reason": null,                      // required when decision = rejected
  "actor": { "id": "usr_42", "name": "J. Doe", "role": "manager" },
  "decidedAt": "2026-02-22T14:11:09Z",
  "clientRequestId": "f3a1...-c9",   // echo of Idempotency-Key
  "ipAddress": "203.0.113.10",
  "userAgent": "FinanceApp/2.4 iOS"
}
```

## 3. Cross-Cutting Concerns

### Idempotent approval retries

- Clients **MUST** send `Idempotency-Key: <uuid>` on `POST /invoices/{id}/approvals`.
- Server stores `(invoiceId, idempotencyKey) → decisionId` for at least 24 hours.
- Retry with the **same key + same body** → returns the original `201` response.
- Retry with the **same key + different body** → `409 Conflict` (`idempotency_key_reuse`).
- New key on an already-decided invoice → `409 Conflict` (`invoice_not_pending`).

Additionally, send `If-Match: "<version>"` (ETag) to prevent stale-state overwrites; mismatch → `412 Precondition Failed`.

### Approve request

```
POST /v1/invoices/inv_01HXYZ/approvals
Idempotency-Key: 8b3c...e1
If-Match: "7"
Content-Type: application/json

{ "decision": "approved" }
```

### Reject request

```
POST /v1/invoices/inv_01HXYZ/approvals
Idempotency-Key: 8b3c...e2
If-Match: "7"
Content-Type: application/json

{
  "decision": "rejected",
  "reason": "Missing PO reference; please resubmit with PO #."
}
```

`reason` is required when `decision = "rejected"`, min 5 / max 500 chars.

### Errors (RFC 7807 Problem Details)

```json
{
  "type": "https://api.example.com/errors/invoice_not_pending",
  "title": "Invoice is not in a pending state",
  "status": 409,
  "code": "invoice_not_pending",
  "detail": "Invoice inv_01HXYZ was already approved at 2026-02-22T14:11:09Z.",
  "instance": "/v1/invoices/inv_01HXYZ/approvals",
  "traceId": "01HXY..."
}
```

| HTTP | code | Meaning |
|---|---|---|
| 400 | `validation_error` | Malformed body, missing `reason`, etc. |
| 401 | `unauthenticated` | Missing/invalid token |
| 403 | `forbidden` | Caller cannot approve this invoice |
| 404 | `invoice_not_found` | Unknown invoice ID |
| 409 | `invoice_not_pending` | Already decided |
| 409 | `idempotency_key_reuse` | Same key, different body |
| 412 | `version_conflict` | `If-Match` failed |
| 422 | `self_approval_forbidden` | Approver = submitter |
| 429 | `rate_limited` | Backoff via `Retry-After` |

### Versioning

- URI-based major version: `/v1/...`.
- Additive, non-breaking changes deploy without version bump.
- Breaking changes → `/v2/...` with a published deprecation window (min 6 months) and `Sunset` + `Deprecation` headers on `/v1`.

### Pagination

- Cursor-based: `?page[cursor]=<opaque>&page[limit]=50` (max 200).
- Response envelope:

```json
{
  "data": [ /* invoices */ ],
  "page": { "nextCursor": "eyJ...", "hasMore": true }
}
```

Filtering: `status`, `assignee`, `vendorId`, `minAmount`, `maxAmount`, `issuedAfter`, `issuedBefore`. Sorting: `sort=-issuedAt`.

### Auth

- OAuth 2.1 bearer tokens (`Authorization: Bearer ...`).
- Scopes: `invoices:read`, `invoices:approve`.
- Approve/reject additionally requires the caller to be the invoice `assignee` or hold `invoices:approve_any`.
- All decision endpoints require fresh auth (`auth_time` within 15 min) for step-up assurance.

### Audit metadata exposure

- Every invoice response includes the `audit` block above.
- Full immutable history available via `GET /invoices/{id}/approvals` (append-only, returns decisions in chronological order, paginated).
- Server also records (but does not return to non-admin callers): request headers hash, geo, MFA assurance level.

## 4. Validated Examples

**List pending for me**
```
GET /v1/invoices?status=pending&assignee=me&page[limit]=25
→ 200 OK
{ "data": [ {...invoice...} ], "page": { "nextCursor": null, "hasMore": false } }
```

**Approve, success**
```
POST /v1/invoices/inv_01HXYZ/approvals    (Idempotency-Key: K1, If-Match: "7")
{ "decision": "approved" }
→ 201 Created
Location: /v1/invoices/inv_01HXYZ/approvals/dec_01HXY
ETag: "8"
{ ...decision event... }
```

**Approve, network retry with same key/body**
```
POST ... (Idempotency-Key: K1, same body)
→ 201 Created   (identical response, no duplicate side effect)
```

**Reject without reason**
```
POST ... { "decision": "rejected" }
→ 400 validation_error  ("reason is required when decision=rejected")
```

**Stale version**
```
POST ... (If-Match: "6")
→ 412 version_conflict
```

### Consistency review checklist ✅

- Resources are nouns; actions modeled as sub-resource events.
- Plural collection names, kebab-free, camelCase JSON fields throughout.
- Idempotency, concurrency, errors, pagination, and auth are uniform across endpoints.
- Audit data is first-class and immutable.
- Versioning strategy is explicit with deprecation policy.

## Open Questions / Uncertainties

- **Async vs sync decisions:** assumed synchronous. If approvals trigger long-running workflows (e.g., multi-step routing), switch to `202 Accepted` + status polling or webhooks.
- **Multi-approver policies** (e.g., dual approval over $10k) are not modeled; would extend `approvals` with a `policy` field and keep `status=pending` until quorum.
- **Bulk approval** not included; can be added as `POST /invoices/approvals:batch` if needed.
- **PII/retention rules** for `ipAddress`/`userAgent` in audit need confirmation with compliance.
