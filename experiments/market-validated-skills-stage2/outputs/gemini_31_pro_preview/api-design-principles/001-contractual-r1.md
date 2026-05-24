### 1. Design Summary
This design provides a RESTful API contract for managing the invoice approval lifecycle. It utilizes a state-filtering approach for listing and explicit action endpoints (`/approve`, `/reject`) for state transitions. This ensures clear intent, strict validation (e.g., mandatory rejection reasons), safe retries via idempotency keys, and explicit exposure of audit metadata.

### 2. Proposed API Shape

**A. List Pending Invoices**
*   **Request:** `GET /v1/invoices?status=pending`
*   **Response:** `200 OK`
*   **Illustrative Schema:**
    ```json
    {
      "data": [
        {
          "id": "inv_12345",
          "status": "pending",
          "amount": 1500.00,
          "currency": "USD",
          "submitted_at": "2023-10-25T10:00:00Z",
          "submitted_by": "usr_789"
        }
      ],
      "pagination": {
        "next_cursor": "..."
      }
    }
    ```

**B. Approve Invoice**
*   **Request:** `POST /v1/invoices/{invoice_id}/approve`
*   **Headers:** `Idempotency-Key: <client-generated-uuid>`
*   **Response:** `200 OK` (Returned for both a successful new approval and a successful retry using the same idempotency key).
*   **Illustrative Schema:**
    ```json
    {
      "id": "inv_12345",
      "status": "approved",
      "audit_metadata": {
        "action": "approve",
        "acted_by": "usr_123",
        "acted_at": "2023-10-26T14:30:00Z",
        "ip_address": "192.168.1.1"
      }
    }
    ```

**C. Reject Invoice**
*   **Request:** `POST /v1/invoices/{invoice_id}/reject`
*   **Headers:** `Idempotency-Key: <client-generated-uuid>`
*   **Request Body:**
    ```json
    {
      "reason": "Amount exceeds departmental budget."
    }
    ```
*   **Response:** `200 OK`
*   **Illustrative Schema:**
    ```json
    {
      "id": "inv_12345",
      "status": "rejected",
      "audit_metadata": {
        "action": "reject",
        "acted_by": "usr_123",
        "acted_at": "2023-10-26T14:35:00Z",
        "reason": "Amount exceeds departmental budget.",
        "ip_address": "192.168.1.1"
      }
    }
    ```

**D. Standard Error Responses (Applicable to Writes)**
*   `400 Bad Request`: Missing rejection reason or malformed idempotency key.
*   `401 Unauthorized` / `403 Forbidden`: Missing or insufficient privileges to approve/reject.
*   `404 Not Found`: Invoice does not exist.
*   `409 Conflict`: Invoice is not in a `pending` state (if a different idempotency key is used).

### 3. Key Tradeoffs
*   **Action Endpoints vs. PATCH:** Using `/approve` and `/reject` instead of `PATCH /v1/invoices/{id}` (with `{"status": "approved"}`) prevents invalid state transitions and allows strict schema validation (e.g., requiring a `reason` payload *only* on rejection).
*   **Idempotency Header vs. State-based Idempotency:** Relying on an `Idempotency-Key` header allows the client to safely retry network timeouts and receive the exact same `200 OK` response with the audit payload, rather than receiving a `409 Conflict` or `400 Bad Request` because the invoice is already approved.

### 4. Risks and Human Gates
*   **Assumptions & Uncertainty:** The specific authentication model and authorization rules (e.g., role-based access control for who can approve specific invoices) are not provided in the requirements and must be defined.
*   **Concurrency Risk:** If two different users attempt to approve/reject simultaneously, the system must handle race conditions (e.g., via optimistic locking or database constraints) to ensure only the first action succeeds.
*   **Human Gates:** 
    *   **Security Approval:** Required for the authentication boundary and authorization rules governing who can approve/reject.
    *   **Product/Engineering Approval:** Required for public API commitments and data retention policies regarding the `audit_metadata`.

### 5. Verification Checklist
*   [ ] Method and resource consistency verified (RESTful action endpoints utilized).
*   [ ] Schema clarity and error handling defined (400, 401, 403, 404, 409).
*   [ ] Idempotency for writes confirmed via `Idempotency-Key` header.
*   [ ] Contract tests drafted for pending list, approval, and rejection flows.
*   [ ] Handoff to Security (auth review), Platform (standards alignment), and QA (contract tests) is ready.
