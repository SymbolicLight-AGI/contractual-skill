### 1. Consumers, Use Cases, and Constraints
*   **Consumers:** Internal financial dashboards, automated approval workflows, and mobile approval apps.
*   **Use Cases:** Retrieve a list of invoices awaiting action, approve an invoice, reject an invoice with justification, and view audit trails.
*   **Constraints:** Must handle network retries safely (idempotency), enforce strict state transitions (only pending invoices can be approved/rejected), and maintain a concise contract.

### 2. API Style and Resource Modeling
*   **Style:** REST
*   **Resource:** `/invoices`
*   **Modeling Strategy:** We will use standard CRUD for listing, but treat state transitions (approve/reject) as sub-resources (`/approve`, `/reject`) using the `POST` method. This explicitly captures the business intent and makes implementing idempotency straightforward.

### 3. Specifications
*   **Versioning:** URI-based (e.g., `/v1/invoices`).
*   **Authentication:** OAuth2 Bearer Token (`Authorization: Bearer <token>`).
*   **Pagination:** Cursor-based pagination for listing pending invoices to handle large datasets efficiently.
*   **Idempotency:** Required `Idempotency-Key` header for all `POST` requests. If a request is retried with the same key, the API will return the cached response of the original successful execution without re-processing the approval.
*   **Errors:** 
    *   `400 Bad Request`: Missing rejection reason or invalid parameters.
    *   `401 Unauthorized` / `403 Forbidden`: Authentication/Authorization failures.
    *   `404 Not Found`: Invoice ID does not exist.
    *   `409 Conflict`: Invoice is no longer in a `pending` state.

### 4. API Contract Examples

#### A. List Pending Invoices
**Request:**
`GET /v1/invoices?status=pending&limit=50&cursor={cursor_token}`

**Response (200 OK):**
```json
{
  "data": [
    {
      "id": "inv_10485",
      "amount": 5000.00,
      "currency": "USD",
      "status": "pending",
      "vendor_name": "Acme Corp",
      "audit_metadata": {
        "created_at": "2023-10-24T10:00:00Z",
        "created_by": "sys_billing",
        "last_updated_at": "2023-10-24T10:00:00Z"
      }
    }
  ],
  "pagination": {
    "next_cursor": "cXdlcnR5dWlvcA==",
    "has_more": true
  }
}
```

#### B. Approve an Invoice
**Request:**
`POST /v1/invoices/{id}/approve`
`Idempotency-Key: 8f9b2a4c-1d3e-4f5a-9b8c-7d6e5f4a3b2c`

**Response (200 OK):**
```json
{
  "id": "inv_10485",
  "status": "approved",
  "audit_metadata": {
    "created_at": "2023-10-24T10:00:00Z",
    "created_by": "sys_billing",
    "last_updated_at": "2023-10-25T14:30:00Z",
    "action_by": "usr_9928",
    "action_timestamp": "2023-10-25T14:30:00Z",
    "action_reason": null
  }
}
```

#### C. Reject an Invoice
**Request:**
`POST /v1/invoices/{id}/reject`
`Idempotency-Key: 4a3b2c1d-5e6f-7a8b-9c0d-1e2f3a4b5c6d`

**Request Body:**
```json
{
  "reason": "Amount exceeds the authorized departmental budget."
}
```

**Response (200 OK):**
```json
{
  "id": "inv_10485",
  "status": "rejected",
  "audit_metadata": {
    "created_at": "2023-10-24T10:00:00Z",
    "created_by": "sys_billing",
    "last_updated_at": "2023-10-25T15:45:00Z",
    "action_by": "usr_9928",
    "action_timestamp": "2023-10-25T15:45:00Z",
    "action_reason": "Amount exceeds the authorized departmental budget."
  }
}
```
