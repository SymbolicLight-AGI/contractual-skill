# API Contract: Invoice Approval Service (v1)

## 1. Consumers, Use Cases & Constraints
- **Consumers:** Internal approval UI, automated finance workflows, third-party ERP integrations.
- **Use Cases:** View pending invoices, approve/reject with traceable audit data, safely retry approval requests without duplicate processing.
- **Constraints:** Strict idempotency for mutations, mandatory audit logging, role-based access control, immutable audit records, no direct infrastructure or DB exposure.

## 2. API Style & Resource Model
- **Style:** RESTful, resource-oriented.
- **Primary Resource:** `Invoice`
- **Action Resource:** `Approval` (modeled as a POST action on the invoice resource to capture state transitions, enforce business rules, and generate audit metadata).

## 3. Endpoint Contract

### List Pending Invoices
- **Method/Path:** `GET /v1/invoices?status=pending&limit={int}&cursor={string}`
- **Response (`200 OK`):**
  - `data[]`: Array of invoice summaries (`id`, `vendor_name`, `amount`, `currency`, `due_date`, `status`, `created_at`)
  - `pagination`: `next_cursor`, `has_more`

### Approve or Reject Invoice
- **Method/Path:** `POST /v1/invoices/{invoice_id}/approval`
- **Required Header:** `Idempotency-Key: <UUID>`
- **Request Body:**
  - `action`: `"approve"` | `"reject"`
  - `reason`: `string` (Required when `action` is `"reject"`, optional for `"approve"`)
- **Response (`200 OK`):**
  - `id`: Approval record ID
  - `invoice_id`: Target invoice
  - `action`: `"approve"` | `"reject"`
  - `status`: `"completed"`
  - `reason`: Provided reason (if any)
  - `audit`: Object containing `actor_id`, `actor_role`, `timestamp`, `ip_address`, `idempotency_key`, `previous_status`, `new_status`

### Retrieve Audit Metadata
- **Method/Path:** `GET /v1/invoices/{invoice_id}/audit`
- **Response (`200 OK`):**
  - `history[]`: Chronological array of audit entries (matches `audit` object structure above)

## 4. Cross-Cutting Concerns
- **Versioning:** URL path versioning (`/v1/`). Breaking changes require `/v2/`.
- **Authentication & Authorization:** Bearer JWT. Requires `invoice:read` for GET endpoints, `invoice:approve` for POST.
- **Pagination:** Cursor-based for list endpoint to guarantee stable ordering during concurrent state changes.
- **Idempotency Strategy:** Server stores the `Idempotency-Key` + request payload hash for 24 hours. Identical retries return the cached `200 OK` response without re-evaluating business rules or duplicating side effects.
- **Error Handling:** Standard HTTP status codes with `error_code` and `message` fields.
  - `400`: Invalid payload (e.g., missing reason for reject)
  - `401/403`: Missing/invalid token or insufficient scope
  - `404`: Invoice not found
  - `409`: Invoice already in terminal state (approved/rejected)
  - `422`: Business rule violation (e.g., amount exceeds approver limit)
  - `500`: Internal server error

## 5. Validation & Consistency Notes
- All timestamps use ISO 8601 UTC format.
- Currency codes follow ISO 4217.
- Audit metadata is append-only and immutable once persisted.
- Idempotency validation occurs before state transition checks to prevent race conditions on retries.
- **Boundary Note:** This contract defines interface behavior and data shapes only. Environment-specific validation, database schema design, queueing mechanisms, and exact auth provider configuration are outside this skill's scope and require implementation-level review.
