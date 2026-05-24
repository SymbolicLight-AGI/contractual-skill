## Invoice Approval API Contract

### 1. Consumers, Use Cases & Constraints
- **Consumers:** Internal finance team, department managers, automated approval systems.
- **Use Cases:**
  1. Retrieve invoices awaiting review.
  2. Approve a specific invoice (idempotent retry safe).
  3. Reject an invoice with a mandatory reason.
  4. Audit all actions on an invoice.
- **Constraints:**
  - Idempotent approvals: repeating the same approval request must not change the outcome or create duplicate entries.
  - All state changes must record actor, timestamp, and reason (where applicable) for auditability.
  - Pagination required on list endpoints to handle growing invoice volumes.

---

### 2. API Style & Resource Modeling
- **Style:** REST (HTTP/1.1) with JSON payloads.
- **Base URL:** `https://api.example.com/v1`
- **Versioning:** URL path version (`/v1/...`); future breaking changes will increment the version.

**Core Resource:**
```
Invoice {
  id: string (UUID)
  status: "pending" | "approved" | "rejected"
  amount: { currency: string, value: string }
  vendor: { id: string, name: string }
  invoice_date: string (date)
  due_date: string (date)
  line_items: [...]
  audit_log: AuditEntry[]    // read-only, server-populated
}

AuditEntry {
  action: "approved" | "rejected"
  actor: { id: string, name: string }
  timestamp: string (ISO 8601)
  reason?: string             // mandatory for reject
  idempotency_key?: string    // present if provided
}
```

---

### 3. Endpoints & Contract

#### 3.1 List Pending Invoices
```
GET /v1/invoices?status=pending&limit=20&cursor=abc123
```
**Headers:**
- `Authorization: Bearer <token>` (scope: `invoice:read`)

**Query Parameters:**
- `status` (required for this use case) = `pending`
- `limit` (optional, default 20, max 100)
- `cursor` (optional, for pagination; returned in previous response)

**Response `200 OK`:**
```json
{
  "data": [
    {
      "id": "inv_9f8a7b",
      "status": "pending",
      "amount": { "currency": "USD", "value": "2500.00" },
      "vendor": { "id": "v_42", "name": "Acme Corp" },
      "due_date": "2026-03-15",
      "audit_log": []          // no approvals/rejections yet
    }
  ],
  "paging": {
    "next_cursor": "def456",
    "has_more": true
  }
}
```
**Errors:**
- `400` – Invalid `status` value
- `401` – Missing or invalid token
- `403` – Insufficient permissions

**Pagination:** Cursor-based. Response includes `paging.next_cursor` and `paging.has_more`. Client passes `cursor` for next page.

---

#### 3.2 Approve an Invoice (Idempotent)
```
POST /v1/invoices/{invoice_id}/approve
```
**Headers:**
- `Authorization: Bearer <token>` (scope: `invoice:approve`)
- `Idempotency-Key: <unique_client_key>` (required)

**Request Body:** empty

**Success Response `200 OK`:**
```json
{
  "id": "inv_9f8a7b",
  "status": "approved",
  "amount": { "currency": "USD", "value": "2500.00" },
  "vendor": { "id": "v_42", "name": "Acme Corp" },
  "audit_log": [
    {
      "action": "approved",
      "actor": { "id": "u_10", "name": "Jane Approver" },
      "timestamp": "2026-03-02T14:30:00Z",
      "idempotency_key": "ik_xyz789"
    }
  ]
}
```

**Idempotency Behavior:**
- First request with a given `Idempotency-Key` stores the outcome keyed on that key.
- Subsequent requests with the *same key* return `200 OK` with the original response, no state change.
- Different key on an already approved invoice returns `409 Conflict`.
- Keys expire after 24 hours; replay after expiry may re-execute, so clients must use fresh keys for new attempts.

**Errors:**
- `400` – Missing `Idempotency-Key`
- `401` / `403` – Auth errors
- `404` – Invoice not found
- `409 Conflict` – Invoice already approved or rejected. Body includes current status:
  ```json
  {
    "error": "conflict",
    "message": "Invoice already in terminal state.",
    "current_status": "approved"
  }
  ```
- `422 Unprocessable Entity` – Invoice has been deleted or is otherwise not actionable.

---

#### 3.3 Reject an Invoice
```
POST /v1/invoices/{invoice_id}/reject
```
**Headers:**
- `Authorization: Bearer <token>` (scope: `invoice:approve`)
- `Idempotency-Key: <unique_client_key>` (optional but recommended; supports idempotent rejection retries)

**Request Body:**
```json
{
  "reason": "Duplicate invoice – already paid via PO#1234."
}
```
`reason` is required, max 500 characters.

**Success Response `200 OK`:**
```json
{
  "id": "inv_9f8a7b",
  "status": "rejected",
  "amount": { "currency": "USD", "value": "2500.00" },
  "vendor": { "id": "v_42", "name": "Acme Corp" },
  "audit_log": [
    {
      "action": "rejected",
      "actor": { "id": "u_10", "name": "Jane Approver" },
      "timestamp": "2026-03-02T14:35:00Z",
      "reason": "Duplicate invoice – already paid via PO#1234.",
      "idempotency_key": "ik_abc111"
    }
  ]
}
```

- If `Idempotency-Key` is provided, the same idempotency guarantees as approval apply.
- If omitted, duplicate rejection attempts on an already rejected invoice return `409 Conflict`.

**Errors:**
- `400` – Missing `reason` field
- `401` / `403` – Auth errors
- `404` – Invoice not found
- `409` – Already approved/rejected
- `422` – Invoice invalid for rejection (e.g., already deleted)

---

### 4. Authentication & Authorization
- All endpoints require an OAuth 2.0 Bearer token via `Authorization` header.
- Token scopes:
  - `invoice:read` for list and individual invoice retrieval.
  - `invoice:approve` for approve and reject operations.
- Audit log entries automatically capture the authenticated user’s `id` and `name` from the token’s claims.

---

### 5. Validation Examples & Consistency Review

**Example flow:**
1. `GET /v1/invoices?status=pending` → returns two invoices.
2. User approves `inv_9f8a7b` with `Idempotency-Key: ik_xyz789` → success.
3. Network blip, client retries same request with same key → `200 OK` with original approval response.
4. Client tries to approve again with a **new** key → `409 Conflict` (already approved).
5. Manager rejects `inv_abc123` with reason “Incorrect PO line items” → success; audit log shows rejection with reason.
6. Subsequent `GET /v1/invoices?status=pending` no longer includes those two invoices.

**Consistency checks:**
- Idempotency protects against double processing for both approve and reject.
- Audit metadata is always present and read-only; no client can alter it.
- All terminal states (approved/rejected) are handled via `409` with clear messaging.
- Pagination cursors prevent missing or duplicate entries during list changes.
