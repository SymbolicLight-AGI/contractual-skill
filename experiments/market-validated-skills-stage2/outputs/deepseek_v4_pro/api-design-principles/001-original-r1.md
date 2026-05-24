## Invoice Approval API Contract

### 1. Consumers, Use Cases & Constraints
- **Consumers**: Finance team (web dashboard), automated ERP systems, mobile clients for managers.
- **Use Cases**: View pending invoices, approve/reject individually, retry approvals safely (idempotency), audit all actions.
- **Constraints**: Must handle concurrent approval attempts, maintain complete audit trail, support large invoice volumes, and integrate with existing identity providers.

### 2. API Style & Resource Model
**Style**: RESTful JSON over HTTPS, chosen for its simplicity, caching, and broad tooling support.

**Primary Resource**: `Invoice`
```
{
  "id": "inv_4a7b3f",
  "amount": {"value": 1499.99, "currency": "USD"},
  "vendor": "Acme Corp",
  "description": "Q3 cloud services",
  "dueDate": "2025-12-01",
  "status": "pending",                  // pending | approved | rejected
  "createdAt": "2025-11-15T10:30:00Z",
  "updatedAt": "2025-11-15T10:30:00Z",
  "approvedAt": null,
  "approvedBy": null,
  "rejectedAt": null,
  "rejectedBy": null,
  "rejectionReason": null
}
```

**Audit metadata** is embedded in the resource: timestamps and actor identifiers for approval/rejection events.

### 3. Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/invoices` | List invoices, filter by status |
| `POST` | `/v1/invoices/{invoiceId}/approve` | Approve an invoice (idempotent) |
| `POST` | `/v1/invoices/{invoiceId}/reject` | Reject an invoice with reason |

#### 3.1 List Pending Invoices
`GET /v1/invoices?status=pending&limit=50&cursor=abc123`

- **Query Params**: `status` (required for pending: `pending`), `limit` (default 20, max 100), `cursor` (opaque cursor for pagination, omitted on first request).
- **Response** `200 OK`:
```json
{
  "data": [ { ... invoice objects ... } ],
  "pagination": {
    "nextCursor": "def456",
    "hasMore": true
  }
}
```

#### 3.2 Approve an Invoice (Idempotent)
`POST /v1/invoices/{invoiceId}/approve`

- **Headers**:
  - `Authorization: Bearer <token>`
  - `Idempotency-Key: <unique-client-key>` (required)
- **Request Body**: `{}` (no payload needed, or may include optional comment).
- **Responses**:
  - `200 OK` – Invoice already approved (idempotent retry). Body: current invoice state.
  - `201 Created` – Successfully approved. Body: updated invoice (status `approved`, `approvedAt`, `approvedBy`).
  - `409 Conflict` – Invoice not in a state that allows approval (e.g., already rejected).
  - `422 Unprocessable Entity` – Missing or invalid idempotency key.

**Idempotency Guarantee**: The server stores the response associated with the `Idempotency-Key` after the first successful execution. Subsequent requests with the same key return the cached response and do not alter the resource. Keys expire after 24 hours, and a new key must be generated per retry window.

#### 3.3 Reject an Invoice
`POST /v1/invoices/{invoiceId}/reject`

- **Headers**: `Authorization`, `Idempotency-Key` (recommended but not enforced; repeated rejections with same reason are harmless).
- **Request Body**:
```json
{
  "reason": "Duplicate invoice; already paid via PO #12345"
}
```
- `reason` is required, max 500 characters.
- **Responses**:
  - `200 OK` – Already rejected (idempotent). Returns current state.
  - `201 Created` – Rejected successfully. Body: updated invoice with `status: rejected`, `rejectedAt`, `rejectedBy`, `rejectionReason`.
  - `409 Conflict` – Invoice already approved (rejection not allowed).
  - `422` – Missing reason.

### 4. Error Format
All errors use `application/problem+json` per RFC 7807:
```json
{
  "type": "https://api.example.com/errors/invalid-status",
  "title": "Invalid invoice status",
  "status": 409,
  "detail": "Invoice inv_4a7b3f is already rejected and cannot be approved.",
  "instance": "/v1/invoices/inv_4a7b3f/approve"
}
```

### 5. Versioning
- URI path versioning: `/v1/` prefix.
- Breaking changes trigger a new major version; backwards-compatible additions (new fields, optional query parameters) do not.

### 6. Pagination
- Cursor-based pagination for `/v1/invoices` using opaque `cursor` parameter to avoid drift issues in rapidly changing lists.
- Response includes `nextCursor` and `hasMore` flag.

### 7. Authentication & Authorization
- All endpoints require a `Bearer` token in the `Authorization` header (OAuth 2.0 or JWT).
- Scopes: `invoices:read` for listing, `invoices:write` for approve/reject. The `approvedBy`/`rejectedBy` fields capture the user ID from the token.

### 8. Validation with Examples
**Success Flow** (First approval):
```
POST /v1/invoices/inv_123/approve
Idempotency-Key: key_abc
→ 201 Created
Response body shows status: approved, approvedAt: 2025-11-20T14:05:00Z, approvedBy: "user_42"
```

**Idempotent Retry**:
```
POST /v1/invoices/inv_123/approve
Idempotency-Key: key_abc   (same key)
→ 200 OK
Response body identical to the stored 201 response.
```

**Rejection**:
```
POST /v1/invoices/inv_123/reject
Body: { "reason": "Incorrect amount" }
→ 201 Created
Response: status rejected, rejectedAt, rejectedBy, rejectionReason: "Incorrect amount"
```

**Attempt to Approve a Rejected Invoice**:
```
POST /v1/invoices/inv_123/approve
→ 409 Conflict
Error detail: "Invoice inv_123 is already rejected."
```

### 9. Consistency Review
- **Idempotent retries**: Covered via `Idempotency-Key` header on the approval endpoint; rejection also accommodates it but requires reason resubmission.
- **Audit metadata**: Fully embedded in the resource; no separate endpoint needed. History of state changes can be derived from timestamps.
- **Separation of concerns**: List endpoint does not mix approvals; action endpoints are explicit sub-resources.
- **Scalability**: Cursor pagination prevents performance degradation with large datasets.

This contract provides a clear, self-documenting API that satisfies all stated requirements without exposing implementation details.
