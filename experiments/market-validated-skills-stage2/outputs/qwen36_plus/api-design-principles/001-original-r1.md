# API Contract: Invoice Approval Service (v1)

## 1. Consumers, Use Cases & Constraints
- **Consumers:** Internal approval UI, automated finance workflows, third-party ERP integrations.
- **Use Cases:** View pending invoices, approve/reject with traceable reasoning, safely retry approval requests without side effects.
- **Constraints:** Strict idempotency for mutations, mandatory audit logging, role-based access control, RESTful resource modeling, no implementation code.

## 2. API Style & Resource Model
- **Style:** REST (JSON over HTTPS)
- **Resources:** `Invoice` (read), `ApprovalAction` (write), `AuditLog` (read)
- **Base Path:** `/v1`

## 3. Endpoints & Contract

### List Pending Invoices
- **Method/Path:** `GET /v1/invoices?status=pending&limit={int}&cursor={string}`
- **Response (200 OK):**
  - `data`: Array of `{ id, vendor_name, amount, currency, due_date, status, created_at }`
  - `pagination`: `{ next_cursor, has_more }`

### Approve or Reject Invoice
- **Method/Path:** `POST /v1/invoices/{invoice_id}/approval`
- **Required Header:** `Idempotency-Key: <UUID>`
- **Request Body:** `{ action: "approve" | "reject", reason?: string }`
  - `reason` is mandatory when `action` is `"reject"`.
- **Response (200 OK / 201 Created):**
  - `data`: `{ id, invoice_id, action, status, reason, approver_id, executed_at }`
  - `audit`: `{ created_by, created_at, ip_address, user_agent, idempotency_key }`

### Retrieve Audit Metadata
- **Method/Path:** `GET /v1/invoices/{invoice_id}/audit`
- **Response (200 OK):**
  - `data`: Array of `{ action, status, reason, actor_id, timestamp, metadata }` (chronological order)

## 4. Cross-Cutting Concerns
- **Authentication & Authorization:** Bearer JWT. Requires `invoice:read` for GET endpoints, `invoice:approve` for POST.
- **Idempotency Strategy:** Server caches the response for the provided `Idempotency-Key` for 24 hours. Subsequent identical requests return the cached `200` response without reprocessing or state mutation.
- **Versioning:** URI path versioning (`/v1/`). Additive changes are backward-compatible; breaking changes increment the major version.
- **Pagination:** Cursor-based for `/invoices` to guarantee stable ordering during concurrent approval operations.
- **Error Handling:** Consistent envelope `{ error: { code, message, details } }` with standard HTTP status codes:
  - `400`: Invalid payload (e.g., missing reason for reject)
  - `401/403`: Auth/permission failures
  - `404`: Invoice not found
  - `409`: Invoice already in terminal state (approved/rejected)
  - `422`: Business rule violation
  - `429`: Rate limit exceeded

## 5. Validation & Consistency Notes
- All timestamps use ISO 8601 UTC format.
- State transitions are strictly enforced: `pending` → `approved` | `rejected`.
- Idempotency keys must be unique per logical request; retries must reuse the exact same key and payload.
- Audit metadata is immutable and append-only.
- *Boundary Note:* This contract defines interface behavior only. Environment-specific validation, database schema design, and security testing are required before deployment.
