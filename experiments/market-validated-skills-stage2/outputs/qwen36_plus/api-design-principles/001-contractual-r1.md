1. Design summary.
A RESTful, versioned API (`/v1/`) centered on the `Invoice` resource. Pending invoices are retrieved via a filtered `GET` endpoint with cursor pagination. Approval and rejection are modeled as explicit actions via `POST /invoices/{id}/approvals` to maintain clear intent, enforce required rejection reasons, and capture immutable audit metadata. Idempotency is enforced via the standard `Idempotency-Key` request header to safely support retry semantics. All responses include structured audit fields. Auth, permissions, and data retention policies are treated as external boundaries requiring human review.

2. Proposed API shape.
**Endpoints & Methods**
- `GET /v1/invoices?status=pending&limit={int}&cursor={string}`
  - Purpose: List pending invoices.
  - Response: `200 OK` with array of invoice summaries and pagination metadata.
- `POST /v1/invoices/{invoice_id}/approvals`
  - Purpose: Approve or reject a specific invoice.
  - Required Header: `Idempotency-Key: <uuid>`
  - Request Body: `{ "action": "approve" | "reject", "reason": "string (required if action=reject)" }`
  - Response: `200 OK` with updated invoice state and audit record.

**Status Codes & Error Semantics**
- `200 OK`: Successful action or list retrieval.
- `400 Bad Request`: Invalid `action` value, missing `reason` for rejection, or malformed payload.
- `404 Not Found`: `invoice_id` does not exist or is inaccessible.
- `409 Conflict`: Invoice already approved/rejected, or `Idempotency-Key` reused with a different payload.
- `422 Unprocessable Entity`: Business rule violation (e.g., insufficient permissions, invoice locked).
- `429 Too Many Requests`: Rate limit exceeded.
- Error Response Shape: `{ "error": { "code": "string", "message": "string", "details": "object?" } }`

**Schema & Audit Metadata (Illustrative)**
```json
// GET /v1/invoices?status=pending response item
{
  "id": "inv_9f8a7b",
  "status": "pending",
  "amount": 1250.00,
  "currency": "USD",
  "audit": {
    "created_at": "2024-05-10T08:30:00Z",
    "last_action": null
  }
}

// POST /v1/invoices/{id}/approvals response
{
  "id": "inv_9f8a7b",
  "status": "approved",
  "amount": 1250.00,
  "currency": "USD",
  "audit": {
    "created_at": "2024-05-10T08:30:00Z",
    "last_action": {
      "action": "approve",
      "actor_id": "usr_4c2d",
      "timestamp": "2024-05-12T14:15:00Z",
      "reason": null,
      "idempotency_key": "req_88e1f2"
    }
  }
}
```
*Note: Schemas are illustrative and derived from stated requirements. Actual field names, types, and actor resolution depend on internal data models.*

3. Key tradeoffs.
- **Action endpoint vs. PATCH on `/invoices/{id}`**: Chose `POST /approvals` to explicitly separate state transitions from partial updates, simplify validation (e.g., mandatory `reason` on reject), and naturally capture audit trails without overloading `PATCH` semantics.
- **Idempotency via header vs. payload token**: Header aligns with HTTP standards and prevents payload mutation during retries. Requires server-side key storage and TTL management.
- **Cursor vs. offset pagination**: Cursor avoids performance degradation and duplicate/missing items on large, frequently updated pending queues. Slightly more complex for simple UI implementations.
- **Embedded audit vs. separate `/audit` resource**: Embedded reduces round-trips and satisfies the requirement to "expose audit metadata" in the same response. If audit history grows large, a separate paginated endpoint will be needed later.

4. Risks and human gates.
- **Risks**:
  - *Concurrency*: Simultaneous approval attempts may race. Mitigated by `409 Conflict` on state change and idempotency key validation.
  - *Data Exposure*: `actor_id` and `reason` may contain sensitive or PII data. Requires security review before public exposure.
  - *Backward Compatibility*: Adding new actions or making `reason` universally required later would be breaking.
  - *Uncertainty*: Auth model (RBAC/ABAC), actor identity resolution, and audit retention windows are unspecified and assumed external.
- **Human Gates**:
  - Security/Compliance: Auth boundaries, permission scoping, and sensitive field masking.
  - Platform/Standards: Alignment with existing versioning, pagination, and error conventions.
  - Product: Public API commitment, backward compatibility guarantees, and audit retention policy.
  - QA/Docs: Contract test coverage and developer-facing examples.

5. Verification checklist.
- [ ] Contract tests validate request/response schemas, required fields, and enum constraints.
- [ ] Idempotency tests confirm identical responses and state for repeated `Idempotency-Key` usage, and `409` for key reuse with differing payloads.
- [ ] Concurrency tests verify `409 Conflict` on simultaneous approvals of the same invoice.
- [ ] Pagination tests validate cursor consistency, boundary conditions, and `limit` enforcement.
- [ ] Error handling tests cover missing `reason` on reject, invalid `action`, non-existent IDs, and rate limits.
- [ ] Security review confirms `actor_id` and `reason` exposure aligns with data classification policies.
- [ ] Consumer review confirms clear error messages, predictable field names, and retry-safe behavior.
