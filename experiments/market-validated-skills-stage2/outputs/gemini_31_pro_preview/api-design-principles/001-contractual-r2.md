### 1. Design Summary
This design proposes a RESTful API contract for managing invoice approvals. It models the approval and rejection processes as state-transition actions on an `invoice` resource. The design supports listing pending invoices via query filtering, enforces idempotent approvals using client-provided idempotency keys, requires a reason for rejections, and embeds audit metadata in the resource representation. 

*Note: As the specific authentication model, pagination strategy, and underlying data schema were not provided, standard assumptions have been made and marked as illustrative.*

### 2. Proposed API Shape

**A. List Pending Invoices**
*   **Endpoint:** `GET /v1/invoices`
*   **Query Parameters:** 
    *   `status=pending` (Filters for pending invoices)
    *   `limit`, `cursor` (Illustrative pagination parameters)
*   **Response (200 OK):**
    ```json
    {
      "data": [
        {
          "id": "inv_12345",
          "status": "pending",
          "amount": 1000.00,
          "audit_metadata": {
            "created_at": "2023-10-24T10:00:00Z",
            "created_by": "usr_789",
            "last_modified_at": "2023-10-24T10:00:00Z"
          }
        }
      ],
      "next_cursor": "..."
    }
    ```

**B. Approve Invoice**
*   **Endpoint:** `POST /v1/invoices/{invoice_id}/approve`
*   **Headers:** 
    *   `Idempotency-Key: <UUID>` (Required for safe retries)
*   **Request Body:** Empty
*   **Response (200 OK):** Returns the updated invoice.
    ```json
    {
      "id": "inv_12345",
      "status": "approved",
      "audit_metadata": {
        "created_at": "2023-10-24T10:00:00Z",
        "created_by": "usr_789",
        "last_modified_at": "2023-10-25T14:30:00Z",
        "actioned_by": "usr_999",
        "actioned_at": "2023-10-25T14:30:00Z"
      }
    }
    ```
*   **Error Semantics:** 
    *   `400 Bad Request` (Missing Idempotency-Key)
    *   `409 Conflict` (Invoice is not in a `pending` state)

**C. Reject Invoice**
*   **Endpoint:** `POST /v1/invoices/{invoice_id}/reject`
*   **Request Body:**
    ```json
    {
      "reason": "Amount exceeds departmental budget."
    }
    ```
*   **Response (200 OK):** Returns the updated invoice.
    ```json
    {
      "id": "inv_12345",
      "status": "rejected",
      "rejection_reason": "Amount exceeds departmental budget.",
      "audit_metadata": {
        "created_at": "2023-10-24T10:00:00Z",
        "last_modified_at": "2023-10-25T15:00:00Z",
        "actioned_by": "usr_999",
        "actioned_at": "2023-10-25T15:00:00Z"
      }
    }
    ```

### 3. Key Tradeoffs
*   **Action Sub-resources vs. PATCH:** Using `POST /approve` and `POST /reject` instead of `PATCH /invoices/{id}` with a status payload. *Tradeoff:* While PATCH is more strictly CRUD, POST to an action sub-resource is preferred here because state transitions require specific side-effects, distinct validation (e.g., rejection reason is required *only* on reject), and explicit idempotency handling.
*   **Header-based Idempotency vs. Natural Idempotency:** Requiring an `Idempotency-Key` header for approvals. *Tradeoff:* Places the burden of key generation and storage on the API consumer, but guarantees that network timeouts during approval do not result in duplicate downstream side-effects (e.g., triggering duplicate ledger entries or payment workflows).
*   **Query Filtering vs. Dedicated Endpoint:** Using `GET /v1/invoices?status=pending` rather than `GET /v1/invoices/pending`. *Tradeoff:* Query filtering is more extensible if consumers later need to filter by multiple statuses or other attributes, though it requires the backend to enforce proper indexing on the `status` field.

### 4. Risks and Human Gates
*   **Security & Auth Boundary Risk:** The prompt does not define the authorization model. There is a risk of unauthorized users approving invoices or viewing sensitive audit metadata.
*   **Concurrency Risk:** Race conditions may occur if two authorized users attempt to approve/reject the same invoice simultaneously.
*   **Human Gates:** 
    *   **Security Approval:** Required to define and validate the authorization boundary (RBAC/ABAC) for who can list, approve, and reject invoices.
    *   **Product Approval:** Required to finalize the public API commitment, specifically regarding the visibility of audit metadata and data retention policies for rejection reasons.

### 5. Verification Checklist
*   [ ] **Idempotency Tests:** Verify that submitting the same `Idempotency-Key` to `/approve` multiple times yields the exact same response without triggering duplicate downstream business logic.
*   [ ] **Schema Validation:** Ensure the `reason` field in the `/reject` endpoint is strictly required and has defined length constraints.
*   [ ] **State Machine Enforcement:** Verify that `/approve` and `/reject` return a `409 Conflict` if the invoice is already approved, rejected, or otherwise not in a `pending` state.
*   [ ] **Auth Boundary Tests:** Confirm that consumers without the explicit "approver" role receive a `403 Forbidden` when attempting to call POST endpoints.
*   [ ] **Pagination & Filtering:** Verify that `GET /v1/invoices?status=pending` correctly paginates and does not leak invoices in other states.
