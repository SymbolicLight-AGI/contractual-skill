<think>The user wants me to design an API contract for invoice approvals. Let me follow the skill instructions:

1. Define consumers, use cases, and constraints
2. Choose API style and model resources/types
3. Specify errors, versioning, pagination, and auth strategy
4. Validate with examples and review for consistency

This is a design task, so I should provide a clear API contract without implementation code.

Let me structure this:

**Consumers:**
- Finance team members (approvers)
- Automated systems (for bulk operations)
- Audit/compliance systems

**Use Cases:**
- List pending invoices for approval
- Approve a single invoice
- Reject an invoice with required reason
- Support idempotent retry for approvals
- Expose audit metadata for compliance

**API Style:** REST seems appropriate here given the resource-oriented nature (invoices, approvals)

Let me design the contract:

**Endpoints:**
1. GET /invoices?status=pending - List pending invoices
2. GET /invoices/{id} - Get invoice details
3. POST /invoices/{id}/approve - Approve invoice (idempotent)
4. POST /invoices/{id}/reject - Reject invoice with reason
5. GET /invoices/{id}/audit - Get audit metadata

**Key considerations:**
- Idempotency keys for approval retries
- Pagination for list endpoint
- Audit metadata (who, when, action, previous state)
- Error handling
- Authentication/Authorization

Let me create a comprehensive but concise API contract.
</think>

# Invoice Approval API Contract

## 1. Consumers & Use Cases

| Consumer | Use Case |
|----------|----------|
| Finance approvers | Review and approve/reject invoices |
| Automated workflows | Bulk approval with idempotent retries |
| Compliance systems | Audit trail retrieval |

---

## 2. Resource Model

### Invoice Resource

```json
{
  "id": "inv_abc123",
  "amount": 1500.00,
  "currency": "USD",
  "vendor": "Acme Corp",
  "submittedAt": "2026-01-15T10:30:00Z",
  "status": "pending",
  "metadata": {
    "poNumber": "PO-2024-001",
    "department": "Engineering"
  }
}
```

### Approval Action Resource

```json
{
  "action": "approved",
  "actor": "user_jane_doe",
  "timestamp": "2026-01-16T14:22:00Z",
  "idempotencyKey": "idem_xyz789"
}
```

### Audit Metadata Resource

```json
{
  "invoiceId": "inv_abc123",
  "history": [
    {
      "action": "submitted",
      "actor": "system",
      "timestamp": "2026-01-15T10:30:00Z"
    },
    {
      "action": "approved",
      "actor": "user_jane_doe",
      "timestamp": "2026-01-16T14:22:00Z",
      "previousStatus": "pending"
    }
  ]
}
```

---

## 3. API Endpoints

### 3.1 List Pending Invoices

```
GET /invoices?status=pending&page=1&limit=20
```

**Response:** `200 OK`
```json
{
  "data": [{ /* Invoice objects */ }],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 47,
    "hasMore": true
  }
}
```

---

### 3.2 Get Invoice Details

```
GET /invoices/{invoiceId}
```

**Response:** `200 OK` — Full Invoice resource

---

### 3.3 Approve Invoice (Idempotent)

```
POST /invoices/{invoiceId}/approve
Headers:
  Idempotency-Key: {client-generated-uuid}
  Authorization: Bearer {token}
```

**Request Body:** `{}` (empty)

**Response:** `200 OK` or `201 Created`
```json
{
  "id": "inv_abc123",
  "status": "approved",
  "action": {
    "actor": "user_jane_doe",
    "timestamp": "2026-01-16T14:22:00Z"
  }
}
```

> **Idempotency:** If `Idempotency-Key` matches a prior request, returns the original response without re-processing.

---

### 3.4 Reject Invoice

```
POST /invoices/{invoiceId}/reject
Headers:
  Authorization: Bearer {token}
```

**Request Body:**
```json
{
  "reason": "Budget exceeded for Q1"
}
```

**Response:** `200 OK`
```json
{
  "id": "inv_abc123",
  "status": "rejected",
  "action": {
    "actor": "user_jane_doe",
    "timestamp": "2026-01-16T14:25:00Z",
    "reason": "Budget exceeded for Q1"
  }
}
```

---

### 3.5 Get Audit Metadata

```
GET /invoices/{invoiceId}/audit
```

**Response:** `200 OK` — Audit Metadata resource

---

## 4. Error Responses

| Status | Condition |
|--------|-----------|
| `400 Bad Request` | Missing required `reason` on reject |
| `404 Not Found` | Invoice does not exist |
| `409 Conflict` | Invoice already approved/rejected |
| `422 Unprocessable` | Invoice not in `pending` status |
| `401 Unauthorized` | Invalid/missing token |
| `403 Forbidden` | User lacks approval permission |

---

## 5. Design Decisions Summary

| Aspect | Decision |
|--------|----------|
| **Style** | REST |
| **Idempotency** | `Idempotency-Key` header on approve |
| **Pagination** | Cursor-free page/limit with totals |
| **Versioning** | URL prefix (`/v1/invoices`) |
| **Auth** | Bearer token (JWT assumed) |
| **Audit** | Immutable event log per invoice |

---

## 6. Validation Checklist

- [ ] All endpoints return consistent JSON structure
- [ ] Reject requires non-empty `reason` field
- [ ] Approve is safe to retry with same `Idempotency-Key`
- [ ] Audit endpoint is read-only
- [ ] Status transitions enforced: `pending` → `approved` | `rejected`
