## Invoice Approvals API Contract

### 1. Consumers, Use Cases, Constraints

**Consumers**
- Internal finance approval UI
- Finance workflow automation services
- Audit/reporting tools

**Primary use cases**
- List invoices pending approval
- Approve an invoice
- Reject an invoice with a reason
- Retry approval requests safely using idempotency
- Expose audit metadata for approval decisions

**Assumptions**
- REST API
- JSON over HTTPS
- Authenticated users act as invoice approvers
- Invoices already exist in another invoice system
- This API only manages approval state, not invoice creation or payment

---

# REST API

Base URL:

```http
/api/v1
```

Authentication:

```http
Authorization: Bearer <access_token>
```

Content type:

```http
Content-Type: application/json
Accept: application/json
```

---

## Resource Model

### Invoice Approval

```json
{
  "invoiceId": "inv_123",
  "status": "pending",
  "supplierName": "Acme Supplies Ltd",
  "invoiceNumber": "ACME-2025-001",
  "amount": {
    "currency": "USD",
    "value": "1250.00"
  },
  "submittedAt": "2026-05-20T14:30:00Z",
  "dueDate": "2026-06-15",
  "approval": {
    "requiredBy": "2026-05-30T23:59:59Z",
    "assignedApproverId": "user_456"
  },
  "audit": {
    "createdAt": "2026-05-20T14:30:00Z",
    "createdBy": "user_123",
    "updatedAt": "2026-05-20T14:30:00Z",
    "updatedBy": "user_123",
    "decisionAt": null,
    "decisionBy": null,
    "decisionReason": null
  }
}
```

### Status Values

```text
pending
approved
rejected
cancelled
```

---

# Endpoints

## 1. List Pending Invoices

```http
GET /api/v1/invoice-approvals?status=pending
```

### Query Parameters

| Parameter | Type | Required | Description |
|---|---:|---:|---|
| `status` | string | Optional | Defaults to `pending`. For this use case, use `pending`. |
| `limit` | integer | Optional | Page size. Default `25`, max `100`. |
| `cursor` | string | Optional | Pagination cursor from previous response. |
| `assignedApproverId` | string | Optional | Filter by approver. |
| `dueBefore` | date | Optional | Filter invoices due before date. |

### Example Request

```http
GET /api/v1/invoice-approvals?status=pending&limit=25
Authorization: Bearer <token>
```

### Example Response

```json
{
  "data": [
    {
      "invoiceId": "inv_123",
      "status": "pending",
      "supplierName": "Acme Supplies Ltd",
      "invoiceNumber": "ACME-2025-001",
      "amount": {
        "currency": "USD",
        "value": "1250.00"
      },
      "submittedAt": "2026-05-20T14:30:00Z",
      "dueDate": "2026-06-15",
      "approval": {
        "requiredBy": "2026-05-30T23:59:59Z",
        "assignedApproverId": "user_456"
      },
      "audit": {
        "createdAt": "2026-05-20T14:30:00Z",
        "createdBy": "user_123",
        "updatedAt": "2026-05-20T14:30:00Z",
        "updatedBy": "user_123",
        "decisionAt": null,
        "decisionBy": null,
        "decisionReason": null
      }
    }
  ],
  "pagination": {
    "limit": 25,
    "nextCursor": "eyJpbnZvaWNlSWQiOiJpbnZfMTIzIn0="
  }
}
```

---

## 2. Approve an Invoice

```http
POST /api/v1/invoice-approvals/{invoiceId}/approve
```

### Headers

| Header | Required | Description |
|---|---:|---|
| `Authorization` | Yes | Bearer token |
| `Idempotency-Key` | Yes | Unique key supplied by client for safe retries |

### Request Body

```json
{
  "comment": "Approved for payment."
}
```

### Field Rules

| Field | Type | Required | Description |
|---|---:|---:|---|
| `comment` | string | No | Optional approval comment. Max 1000 characters. |

### Example Request

```http
POST /api/v1/invoice-approvals/inv_123/approve
Authorization: Bearer <token>
Idempotency-Key: approve-inv-123-20260524-001
Content-Type: application/json

{
  "comment": "Approved for payment."
}
```

### Success Response

```http
200 OK
```

```json
{
  "invoiceId": "inv_123",
  "status": "approved",
  "audit": {
    "createdAt": "2026-05-20T14:30:00Z",
    "createdBy": "user_123",
    "updatedAt": "2026-05-24T10:15:00Z",
    "updatedBy": "user_456",
    "decisionAt": "2026-05-24T10:15:00Z",
    "decisionBy": "user_456",
    "decisionReason": "Approved for payment."
  }
}
```

### Idempotency Behavior

- The client must send an `Idempotency-Key` for approval requests.
- If the same key is retried with the same request body, the API returns the original successful response.
- If the same key is reused with a different request body or different invoice, the API returns `409 Conflict`.
- Recommended idempotency key retention: at least 24 hours.

---

## 3. Reject an Invoice

```http
POST /api/v1/invoice-approvals/{invoiceId}/reject
```

### Headers

| Header | Required | Description |
|---|---:|---|
| `Authorization` | Yes | Bearer token |

### Request Body

```json
{
  "reason": "Invoice amount does not match purchase order."
}
```

### Field Rules

| Field | Type | Required | Description |
|---|---:|---:|---|
| `reason` | string | Yes | Rejection reason. Min 3, max 1000 characters. |

### Example Request

```http
POST /api/v1/invoice-approvals/inv_123/reject
Authorization: Bearer <token>
Content-Type: application/json

{
  "reason": "Invoice amount does not match purchase order."
}
```

### Success Response

```http
200 OK
```

```json
{
  "invoiceId": "inv_123",
  "status": "rejected",
  "audit": {
    "createdAt": "2026-05-20T14:30:00Z",
    "createdBy": "user_123",
    "updatedAt": "2026-05-24T10:20:00Z",
    "updatedBy": "user_456",
    "decisionAt": "2026-05-24T10:20:00Z",
    "decisionBy": "user_456",
    "decisionReason": "Invoice amount does not match purchase order."
  }
}
```

---

# Error Format

All errors use a consistent response envelope.

```json
{
  "error": {
    "code": "invoice_not_found",
    "message": "Invoice approval was not found.",
    "details": {
      "invoiceId": "inv_123"
    },
    "requestId": "req_abc123"
  }
}
```

---

## Error Responses

| HTTP Status | Code | Description |
|---:|---|---|
| `400` | `invalid_request` | Malformed request or invalid query parameter. |
| `400` | `missing_rejection_reason` | Reject request did not include a reason. |
| `401` | `unauthorized` | Missing or invalid token. |
| `403` | `forbidden` | User is not allowed to approve or reject this invoice. |
| `404` | `invoice_not_found` | Invoice approval record does not exist. |
| `409` | `invoice_not_pending` | Invoice has already been approved, rejected, or cancelled. |
| `409` | `idempotency_key_conflict` | Same idempotency key was reused with a different request. |
| `422` | `validation_failed` | Request body is syntactically valid but violates field rules. |
| `429` | `rate_limited` | Too many requests. |
| `500` | `internal_error` | Unexpected server error. |

---

# Versioning

Use URL-based major versioning:

```http
/api/v1
```

Backward-compatible changes may be added within `v1`, including:
- New optional response fields
- New filter parameters
- New enum values, if documented as extensible

Breaking changes require a new major version:

```http
/api/v2
```

---

# Authorization Model

Suggested scopes or permissions:

| Permission | Allows |
|---|---|
| `invoice_approvals:read` | List pending invoice approvals |
| `invoice_approvals:approve` | Approve invoices |
| `invoice_approvals:reject` | Reject invoices |
| `invoice_approvals:audit:read` | View audit metadata |

Approval and rejection should also verify business rules, such as:
- Invoice is assigned to the current approver or their approval group
- Invoice is currently `pending`
- Approver has sufficient authority for invoice amount or department

---

# Summary of Contract

```http
GET  /api/v1/invoice-approvals?status=pending
POST /api/v1/invoice-approvals/{invoiceId}/approve
POST /api/v1/invoice-approvals/{invoiceId}/reject
```

This design supports listing pending invoices, approval, rejection with required reason, safe idempotent approval retries, consistent pagination, consistent errors, versioning, authorization, and audit visibility.
