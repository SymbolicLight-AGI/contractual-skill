### 1. Consumers, Use Cases, and Constraints
*   **Consumers:** Internal dashboards, mobile applications, or third-party ERP integrations.
*   **Use Cases:** Retrieve a list of invoices awaiting approval, approve an invoice, reject an invoice with a mandatory reason, and view audit trails.
*   **Constraints:** Must support safe retries (idempotency) for state-changing operations.

### 2. API Style and Resource Modeling
We will use a **RESTful API** style. 
*   **Base Resource:** `/v1/invoices`
*   **Sub-resources (State Transitions):** `/approve` and `/reject`. Using POST to these sub-resources is a standard REST pattern for explicit business actions/state transitions.

### 3. Global Strategies
*   **Authentication:** OAuth 2.0 Bearer Token (`Authorization: Bearer <token>`).
*   **Versioning:** URI-based (`/v1/`).
*   **Pagination:** Cursor-based pagination for listing invoices.
*   **Idempotency:** Required `Idempotency-Key` header for all `POST` requests. If a request is retried with the same key, the API will return the cached response of the original successful execution without re-processing the state change.

### 4. API Contract Specifications

#### A. List Pending Invoices
Retrieves a paginated list of invoices currently awaiting approval.

*   **Endpoint:** `GET /v1/invoices`
*   **Query Parameters:**
    *   `status=pending` (Filter by state)
    *   `limit=50` (Pagination limit)
    *   `cursor=cXVlcnk=` (Pagination cursor)
*   **Response (200 OK):**
```json
{
  "data": [
    {
      "id": "inv_01H8X",
      "amount": 5000.00,
      "currency": "USD",
      "status": "pending",
      "audit_metadata": {
        "created_at": "2023-10-24T08:00:00Z",
        "updated_at": "2023-10-24T08:00:00Z",
        "submitted_by": "usr_123"
      }
    }
  ],
  "pagination": {
    "next_cursor": "dG9rZW4=",
    "has_more": true
  }
}
```

#### B. Approve an Invoice
Approves a pending invoice.

*   **Endpoint:** `POST /v1/invoices/{id}/approve`
*   **Headers:**
    *   `Idempotency-Key: <UUID>` (Required)
*   **Response (200 OK):**
```json
{
  "id": "inv_01H8X",
  "status": "approved",
  "audit_metadata": {
    "created_at": "2023-10-24T08:00:00Z",
    "updated_at": "2023-10-25T10:15:00Z",
    "submitted_by": "usr_123",
    "processed_by": "usr_999",
    "action_taken": "approved"
  }
}
```

#### C. Reject an Invoice
Rejects a pending invoice. A rejection reason is required.

*   **Endpoint:** `POST /v1/invoices/{id}/reject`
*   **Headers:**
    *   `Idempotency-Key: <UUID>` (Required)
*   **Request Body:**
```json
{
  "reason": "Amount exceeds departmental budget limits."
}
```
*   **Response (200 OK):**
```json
{
  "id": "inv_01H8X",
  "status": "rejected",
  "rejection_reason": "Amount exceeds departmental budget limits.",
  "audit_metadata": {
    "created_at": "2023-10-24T08:00:00Z",
    "updated_at": "2023-10-25T10:20:00Z",
    "submitted_by": "usr_123",
    "processed_by": "usr_999",
    "action_taken": "rejected"
  }
}
```

### 5. Standard Error Responses
*   **`400 Bad Request`**: Missing `Idempotency-Key` header or invalid request body (e.g., missing rejection reason).
*   **`401 Unauthorized`**: Missing or invalid Bearer token.
*   **`403 Forbidden`**: User lacks approval permissions.
*   **`404 Not Found`**: Invoice ID does not exist.
*   **`409 Conflict`**: The invoice is no longer in a `pending` state (e.g., already approved or rejected).
*   **`422 Unprocessable Entity`**: The request is well-formed but semantically invalid.
