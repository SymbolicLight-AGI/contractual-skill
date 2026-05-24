## Invoice Approvals API Contract

### Assumptions

- API consumers are internal finance/admin web or mobile clients.
- Invoices already exist in the billing system.
- This API only covers approval workflow actions.
- REST is used for clarity, auditability, and simple resource-oriented operations.

---

# API Overview

Base URL:

```http
https://api.example.com/v1
```

Authentication:

```http
Authorization: Bearer <access_token>
```

Required scopes:

| Scope | Description |
|---|---|
| `invoices:read` | List and view invoice approval data |
| `invoices:approve` | Approve invoices |
| `invoices:reject` | Reject invoices |

---

# Resources

## Invoice Approval

```json
{
  "id": "inv_123",
  "status": "pending_approval",
  "vendor": {
    "id": "ven_456",
    "name": "Acme Supplies"
  },
  "amount": {
    "currency": "USD",
    "value": "1250.00"
  },
  "dueDate": "2026-06-15",
  "submittedAt": "2026-05-20T14:30:00Z",
  "submittedBy": {
    "id": "usr_111",
    "name": "Jane Smith"
  },
  "approval": {
    "status": "pending",
    "approvedBy": null,
    "approvedAt": null,
    "rejectedBy": null,
    "rejectedAt": null,
    "rejectionReason": null
  },
  "audit": {
    "createdAt": "2026-05-20T14:30:00Z",
    "createdBy": "usr_111",
    "updatedAt": "2026-05-20T14:30:00Z",
    "updatedBy": "usr_111",
    "version": 3
  }
}
```

### Invoice approval statuses

| Status | Description |
|---|---|
| `pending_approval` | Invoice is awaiting approval |
| `approved` | Invoice has been approved |
| `rejected` | Invoice has been rejected |

---

# Endpoints

## 1. List Pending Invoices

```http
GET /invoices?status=pending_approval
```

### Query parameters

| Parameter | Type | Required | Description |
|---|---:|---:|---|
| `status` | string | Optional | Use `pending_approval` to list pending invoices |
| `limit` | integer | Optional | Number of results, default `25`, max `100` |
| `cursor` | string | Optional | Pagination cursor |
| `vendorId` | string | Optional | Filter by vendor |
| `dueBefore` | date | Optional | Filter invoices due before date |
| `sort` | string | Optional | Example: `dueDate`, `-submittedAt` |

### Response

```http
200 OK
```

```json
{
  "data": [
    {
      "id": "inv_123",
      "status": "pending_approval",
      "vendor": {
        "id": "ven_456",
        "name": "Acme Supplies"
      },
      "amount": {
        "currency": "USD",
        "value": "1250.00"
      },
      "dueDate": "2026-06-15",
      "submittedAt": "2026-05-20T14:30:00Z",
      "submittedBy": {
        "id": "usr_111",
        "name": "Jane Smith"
      },
      "approval": {
        "status": "pending",
        "approvedBy": null,
        "approvedAt": null,
        "rejectedBy": null,
        "rejectedAt": null,
        "rejectionReason": null
      },
      "audit": {
        "createdAt": "2026-05-20T14:30:00Z",
        "createdBy": "usr_111",
        "updatedAt": "2026-05-20T14:30:00Z",
        "updatedBy": "usr_111",
        "version": 3
      }
    }
  ],
  "pagination": {
    "limit": 25,
    "nextCursor": "eyJpZCI6Imludl8xMjMifQ"
  }
}
```

---

## 2. Approve Invoice

Approves a pending invoice.

```http
POST /invoices/{invoiceId}/approval
```

### Headers

```http
Authorization: Bearer <access_token>
Idempotency-Key: 7f6d9b7a-1c47-4e41-9f5a-82fd9a7f9abc
Content-Type: application/json
```

`Idempotency-Key` is required for approval requests to safely support retries.

### Request body

```json
{
  "comment": "Approved for payment."
}
```

### Successful response

```http
200 OK
```

```json
{
  "id": "inv_123",
  "status": "approved",
  "approval": {
    "status": "approved",
    "approvedBy": {
      "id": "usr_789",
      "name": "Alex Manager"
    },
    "approvedAt": "2026-05-24T10:15:00Z",
    "rejectedBy": null,
    "rejectedAt": null,
    "rejectionReason": null,
    "comment": "Approved for payment."
  },
  "audit": {
    "createdAt": "2026-05-20T14:30:00Z",
    "createdBy": "usr_111",
    "updatedAt": "2026-05-24T10:15:00Z",
    "updatedBy": "usr_789",
    "version": 4
  }
}
```

### Idempotency behavior

If the same `Idempotency-Key` is retried with the same request body, the API returns the original successful response.

```http
200 OK
```

If the same `Idempotency-Key` is reused with a different request body:

```http
409 Conflict
```

```json
{
  "error": {
    "code": "IDEMPOTENCY_KEY_REUSED",
    "message": "This idempotency key was already used with a different request."
  }
}
```

---

## 3. Reject Invoice

Rejects a pending invoice with a required reason.

```http
POST /invoices/{invoiceId}/rejection
```

### Headers

```http
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request body

```json
{
  "reason": "Missing purchase order number.",
  "comment": "Please resubmit with the correct PO reference."
}
```

### Validation

| Field | Required | Description |
|---|---:|---|
| `reason` | Yes | Human-readable rejection reason |
| `comment` | No | Additional internal note |

### Successful response

```http
200 OK
```

```json
{
  "id": "inv_123",
  "status": "rejected",
  "approval": {
    "status": "rejected",
    "approvedBy": null,
    "approvedAt": null,
    "rejectedBy": {
      "id": "usr_789",
      "name": "Alex Manager"
    },
    "rejectedAt": "2026-05-24T10:20:00Z",
    "rejectionReason": "Missing purchase order number.",
    "comment": "Please resubmit with the correct PO reference."
  },
  "audit": {
    "createdAt": "2026-05-20T14:30:00Z",
    "createdBy": "usr_111",
    "updatedAt": "2026-05-24T10:20:00Z",
    "updatedBy": "usr_789",
    "version": 4
  }
}
```

---

# Error Format

All errors use a consistent envelope:

```json
{
  "error": {
    "code": "INVOICE_NOT_FOUND",
    "message": "Invoice was not found.",
    "details": {}
  }
}
```

## Common errors

| HTTP Status | Code | Description |
|---:|---|---|
| `400` | `VALIDATION_ERROR` | Request body or query parameters are invalid |
| `401` | `UNAUTHENTICATED` | Missing or invalid access token |
| `403` | `FORBIDDEN` | User lacks required permission |
| `404` | `INVOICE_NOT_FOUND` | Invoice does not exist |
| `409` | `INVALID_STATE_TRANSITION` | Invoice is already approved or rejected |
| `409` | `IDEMPOTENCY_KEY_REUSED` | Idempotency key reused with a different request |
| `429` | `RATE_LIMITED` | Too many requests |
| `500` | `INTERNAL_ERROR` | Unexpected server error |

Example invalid state response:

```http
409 Conflict
```

```json
{
  "error": {
    "code": "INVALID_STATE_TRANSITION",
    "message": "Only pending invoices can be approved or rejected.",
    "details": {
      "invoiceId": "inv_123",
      "currentStatus": "approved"
    }
  }
}
```

---

# Versioning

Version is included in the URL:

```http
/v1
```

Breaking changes require a new major version, for example:

```http
/v2
```

Non-breaking changes may be added to `v1`, such as new optional fields or new filter parameters.
