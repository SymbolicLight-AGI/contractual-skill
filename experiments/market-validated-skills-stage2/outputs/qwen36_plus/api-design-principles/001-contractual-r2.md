1. Design summary.
This contract defines a RESTful API for managing invoice approval workflows. The primary resource is `Invoice`, with a dedicated action sub-resource `/approvals` to handle state transitions. The design supports listing pending invoices via filtered, cursor-based pagination, and executing approve/reject actions with explicit idempotency controls. Audit metadata is embedded in resource representations to satisfy traceability requirements. Versioning uses URI prefixing (`/v1/`). All design choices prioritize explicit state transitions, predictable error semantics, and consumer-friendly ergonomics. Assumptions are explicitly marked where requirements are underspecified.

2. Proposed API shape.
**Versioning & Base Path:** `/v1/`
**Auth Boundary:** Bearer token required for all endpoints. Scope/role validation deferred to platform security review.

**List Pending Invoices**
- `GET /v1/invoices?status=pending&limit=20&cursor={opaque_token}`
- Success: `200 OK`
- Response Schema (illustrative):
  ```json
  {
    "data": [
      {
        "id": "inv_9f8e7d",
        "status": "pending",
        "amount": 1250.00,
        "currency": "USD",
        "audit": {
          "created_at": "2024-05-10T08:30:00Z",
          "last_action": null
        }
      }
    ],
    "pagination": {
      "next_cursor": "eyJpZCI6Imludl85ZjhlN2QifQ==",
      "has_more": true
    }
  }
  ```
- Errors: `400` (invalid filter/limit), `401/403` (auth/permission), `429` (rate limit).

**Approve or Reject Invoice**
- `POST /v1/invoices/{invoice_id}/approvals`
- Headers: `Idempotency-Key: <client-generated-uuid>` (required)
- Request Body (illustrative):
  ```json
  {
    "action": "approve",
    "reason": "Budget verified and vendor confirmed."
  }
  ```
- Success: `200 OK` (returns updated invoice state)
- Response Schema (illustrative):
  ```json
  {
    "id": "inv_9f8e7d",
    "status": "approved",
    "amount": 1250.00,
    "currency": "USD",
    "audit": {
      "created_at": "2024-05-10T08:30:00Z",
      "last_action": {
        "action": "approve",
        "actor_id": "usr_a1b2c3",
        "timestamp": "2024-05-12T14:22:00Z",
        "reason": "Budget verified and vendor confirmed."
      }
    }
  }
  ```
- Errors:
  - `400 Bad Request`: Missing `action`, invalid enum value, or `reason` omitted when `action=reject`.
  - `404 Not Found`: Invoice does not exist.
  - `409 Conflict`: Invoice already in terminal state (`approved`/`rejected`).
  - `422 Unprocessable Entity`: Schema validation failure.
  - `429 Too Many Requests`: Rate limit exceeded.
  - `500 Internal Server Error`: Unhandled platform failure.

**Idempotency Behavior:** Replaying the same `Idempotency-Key` within the retention window (assumed 24h) returns the identical `200 OK` response and does not mutate state. Missing or duplicate keys across different payloads return `400` or `409` per platform policy.

3. Key tradeoffs.
- **Action endpoint vs. PATCH on `/invoices/{id}`:** Chose `POST /approvals` to enforce explicit intent, simplify audit trail generation, and avoid partial-update ambiguity. Tradeoff: slightly more verbose routing, but clearer contract for state machines.
- **Cursor vs. Offset pagination:** Cursor selected for consistent performance at scale and safe resumption. Tradeoff: consumers cannot jump to arbitrary pages, which is acceptable for approval queues.
- **Embedded audit vs. separate `/audit` resource:** Embedded reduces round-trips and aligns with the requirement to "expose audit metadata." Tradeoff: payload size grows with history; mitigated by returning only `last_action` in list views and full history only if explicitly requested later.
- **Idempotency via header vs. body token:** Header aligns with REST conventions and simplifies client SDK generation. Tradeoff: requires proxy/gateway support for key storage and deduplication.

4. Risks and human gates.
- **Risks:**
  - *Concurrency:* Simultaneous approval attempts may race. Mitigated by `409 Conflict` on terminal states and idempotency key locking.
  - *Data Exposure:* `actor_id` and `reason` may contain PII or internal notes. Requires sanitization or role-based field masking.
  - *Schema Evolution:* Adding required fields to `reason` or `action` later breaks backward compatibility.
  - *Assumption/Uncertainty:* Auth model, actor resolution, and audit retention window are unspecified. Design assumes standard RBAC and 24h idempotency key retention.
- **Human Gates (require approval before implementation):**
  - Auth/permission boundaries (who can approve/reject, scope validation).
  - Public API commitment and versioning policy.
  - Data retention and privacy review for audit metadata.
  - Production migration plan if replacing legacy approval flows.

5. Verification checklist.
- [ ] Contract tests validate request/response schemas, status codes, and error payloads.
- [ ] Idempotency tests confirm identical responses and zero state mutation on key replay.
- [ ] Concurrency tests verify `409 Conflict` behavior for duplicate terminal-state requests.
- [ ] Pagination tests validate cursor encoding, boundary conditions, and `has_more` accuracy.
- [ ] Validation tests enforce `reason` requirement for `reject` and reject invalid `action` values.
- [ ] Security review confirms auth boundaries, sensitive field masking, and rate limit enforcement.
- [ ] Consumer review confirms DX clarity (predictable errors, consistent naming, documented idempotency window).
