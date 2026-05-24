<think>The user wants me to design an API contract for invoice approvals. Let me break down the requirements:

1. List pending invoices
2. Approve one invoice
3. Reject with a reason
4. Support idempotent approval retries
5. Expose audit metadata

No code is required - just the API contract/design.

Let me design a clean REST API for this:

**Resources:**
- Invoice (the main resource)
- Approval action (can be part of invoice or separate)

**Endpoints:**

1. `GET /invoices?status=pending` - List pending invoices
2. `GET /invoices/{id}` - Get invoice details with audit metadata
3. `POST /invoices/{id}/approve` - Approve an invoice (idempotent via idempotency key)
4. `POST /invoices/{id}/reject` - Reject with reason
5. `GET /invoices/{id}/audit` - Get audit trail

Let me structure this properly with request/response formats, status codes, headers, etc.
</think>

# Invoice Approval API Contract

## Base URL
```
/api/v1
```

---

## 1. List Pending Invoices

**Endpoint:** `GET /invoices`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter by status (`pending`, `approved`, `rejected`). Defaults to all. |
| `page` | integer | No | Page number (default: 1) |
| `pageSize` | integer | No | Items per page (default: 20, max: 100) |

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": "inv_abc123",
      "invoiceNumber": "INV-2024-0042",
      "amount": 1500.00,
      "currency": "USD",
      "vendor": "Acme Supplies",
      "submittedAt": "2024-01-15T09:30:00Z",
      "status": "pending"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 45,
    "totalPages": 3
  }
}
```

---

## 2. Get Invoice Details

**Endpoint:** `GET /invoices/{invoiceId}`

**Response:** `200 OK`
```json
{
  "id": "inv_abc123",
  "invoiceNumber": "INV-2024-0042",
  "amount": 1500.00,
  "currency": "USD",
  "vendor": {
    "id": "vnd_789",
    "name": "Acme Supplies",
    "email": "billing@acme.com"
  },
  "lineItems": [
    { "description": "Office supplies", "quantity": 10, "unitPrice": 150.00 }
  ],
  "submittedAt": "2024-01-15T09:30:00Z",
  "status": "pending",
  "audit": {
    "createdAt": "2024-01-15T09:30:00Z",
    "createdBy": "user_jane",
    "lastModifiedAt": "2024-01-15T09:30:00Z",
    "lastModifiedBy": "user_jane"
  }
}
```

**Error Responses:**
- `404 Not Found` — Invoice does not exist

---

## 3. Approve Invoice (Idempotent)

**Endpoint:** `POST /invoices/{invoiceId}/approve`

**Headers:**
| Header | Required | Description |
|--------|----------|-------------|
| `Idempotency-Key` | Yes | Unique key for safe retry support (UUID recommended) |
| `Authorization` | Yes | Bearer token |

**Request Body:** *(optional)*
```json
{
  "notes": "Approved for Q1 budget"
}
```

**Response:** `200 OK` *(or `201 Created` on first approval)*
```json
{
  "id": "inv_abc123",
  "status": "approved",
  "approvedAt": "2024-01-16T14:22:00Z",
  "approvedBy": "user_john",
  "idempotencyKey": "key_xyz789",
  "audit": {
    "createdAt": "2024-01-15T09:30:00Z",
    "createdBy": "user_jane",
    "lastModifiedAt": "2024-01-16T14:22:00Z",
    "lastModifiedBy": "user_john"
  }
}
```

**Idempotency Behavior:**
- Same `Idempotency-Key` returns the original response without re-processing
- Keys expire after 24 hours
- Duplicate approval of already-approved invoice returns `200` with current state

**Error Responses:**
- `404 Not Found` — Invoice does not exist
- `409 Conflict` — Invoice already rejected (cannot approve)
- `422 Unprocessable Entity` — Invoice not in `pending` state

---

## 4. Reject Invoice

**Endpoint:** `POST /invoices/{invoiceId}/reject`

**Headers:**
| Header | Required | Description |
|--------|----------|-------------|
| `Idempotency-Key` | Yes | Unique key for safe retry support |
| `Authorization` | Yes | Bearer token |

**Request Body:** *(required)*
```json
{
  "reason": "Budget exceeded for Q1. Please resubmit with reduced scope."
}
```

**Response:** `200 OK`
```json
{
  "id": "inv_abc123",
  "status": "rejected",
  "rejectedAt": "2024-01-16T14:22:00Z",
  "rejectedBy": "user_john",
  "rejectionReason": "Budget exceeded for Q1. Please resubmit with reduced scope.",
  "idempotencyKey": "key_abc456",
  "audit": {
    "createdAt": "2024-01-15T09:30:00Z",
    "createdBy": "user_jane",
    "lastModifiedAt": "2024-01-16T14:22:00Z",
    "lastModifiedBy": "user_john"
  }
}
```

**Error Responses:**
- `400 Bad Request` — Missing `reason` field
- `404 Not Found` — Invoice does not exist
- `409 Conflict` — Invoice already approved (cannot reject)
- `422 Unprocessable Entity` — Invoice not in `pending` state

---

## 5. Get Audit Trail

**Endpoint:** `GET /invoices/{invoiceId}/audit`

**Response:** `200 OK`
```json
{
  "invoiceId": "inv_abc123",
  "events": [
    {
      "event": "created",
      "timestamp": "2024-01-15T09:30:00Z",
      "actor": "user_jane",
      "details": {}
    },
    {
      "event": "status_changed",
      "timestamp": "2024-01-16T14:22:00Z",
      "actor": "user_john",
      "previousStatus": "pending",
      "newStatus": "approved",
      "notes": "Approved for Q1 budget"
    }
  ]
}
```

---

## Summary of Design Decisions

| Concern | Decision |
|---------|----------|
| **Style** | REST with resource-based URLs |
| **Idempotency** | `Idempotency-Key` header for approve/reject actions |
| **Audit Metadata** | Embedded in resource + dedicated `/audit` endpoint |
| **Error Handling** | Semantic HTTP status codes with structured error body |
| **Versioning** | URL path (`/api/v1`) |
| **Pagination** | Offset-based with `page`/`pageSize` |

---

## Common Error Format

```json
{
  "error": {
    "code": "INVOICE_ALREADY_APPROVED",
    "message": "This invoice has already been approved and cannot be modified.",
    "details": {
      "invoiceId": "inv_abc123",
      "currentStatus": "approved",
      "approvedAt": "2024-01-16T14:22:00Z"
    }
  }
}
```
