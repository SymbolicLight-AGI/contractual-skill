<think>The user wants me to design an API contract for invoice approvals. Let me follow the workflow from the skill:

1. Identify resources, actions, consumers, and lifecycle states
2. Separate public API contract, internal implementation, and migration concerns
3. Evaluate naming, methods, status codes, schema shape, errors, pagination, filtering, idempotency, and versioning
4. Recommend a design or compare alternatives with tradeoffs
5. Include examples only when they can be derived from the task
6. Surface security, compatibility, observability, and operational risks
7. Define verification criteria

Requirements from the task:
- List pending invoices
- Approve one invoice
- Reject with a reason
- Support idempotent approval retries
- Expose audit metadata

Let me design this:

**Resources:**
- Invoice (the main resource)
- ApprovalAction (audit trail)

**Actions:**
- List pending invoices (GET)
- Approve invoice (POST or PATCH)
- Reject invoice (POST with reason)
- Get audit metadata (part of invoice or separate endpoint)

**Design approach:**
I'll use REST since the task mentions REST/GraphQL and this is a straightforward resource-based API.

Let me structure the response according to the required output format:
1. Design summary
2. Proposed API shape
3. Key tradeoffs
4. Risks and human gates
5. Verification checklist
</think>

# Invoice Approvals API Contract

## 1. Design Summary

A RESTful API for managing invoice approval workflows. Supports listing pending invoices, approving/rejecting individual invoices with audit trails, and idempotent retry semantics for approvals.

---

## 2. Proposed API Shape

### Base URL
```
/v1/invoices
```

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/invoices?status=pending` | List pending invoices (paginated) |
| `GET` | `/v1/invoices/{invoiceId}` | Get invoice details with audit metadata |
| `POST` | `/v1/invoices/{invoiceId}/approve` | Approve an invoice (idempotent) |
| `POST` | `/v1/invoices/{invoiceId}/reject` | Reject an invoice with required reason |

---

### Request/Response Schemas

#### List Pending Invoices
```
GET /v1/invoices?status=pending&page=1&pageSize=20

Response 200:
{
  "data": [
    {
      "id": "inv_abc123",
      "amount": 1500.00,
      "currency": "USD",
      "vendor": "Acme Corp",
      "submittedAt": "2024-01-15T10:30:00Z",
      "status": "pending"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalCount": 45,
    "hasMore": true
  }
}
```

#### Approve Invoice
```
POST /v1/invoices/{invoiceId}/approve
Headers:
  Idempotency-Key: <client-generated-uuid>

Response 200 (already approved) or 201 (new approval):
{
  "id": "inv_abc123",
  "status": "approved",
  "approvedAt": "2024-01-16T14:22:00Z",
  "approvedBy": "user_jane_doe",
  "auditId": "audit_xyz789"
}
```

#### Reject Invoice
```
POST /v1/invoices/{invoiceId}/reject
Body:
{
  "reason": "Budget code invalid for Q1 project"
}

Response 200:
{
  "id": "inv_abc123",
  "status": "rejected",
  "rejectedAt": "2024-01-16T14:22:00Z",
  "rejectedBy": "user_jane_doe",
  "rejectionReason": "Budget code invalid for Q1 project",
  "auditId": "audit_xyz790"
}
```

#### Get Invoice with Audit Metadata
```
GET /v1/invoices/{invoiceId}

Response 200:
{
  "id": "inv_abc123",
  "amount": 1500.00,
  "currency": "USD",
  "vendor": "Acme Corp",
  "status": "approved",
  "submittedAt": "2024-01-15T10:30:00Z",
  "audit": {
    "createdAt": "2024-01-15T10:30:00Z",
    "createdBy": "system",
    "lastModifiedAt": "2024-01-16T14:22:00Z",
    "lastModifiedBy": "user_jane_doe",
    "history": [
      {
        "action": "submitted",
        "timestamp": "2024-01-15T10:30:00Z",
        "actor": "system"
      },
      {
        "action": "approved",
        "timestamp": "2024-01-16T14:22:00Z",
        "actor": "user_jane_doe"
      }
    ]
  }
}
```

### Error Responses
```
400 Bad Request:
{
  "error": "validation_error",
  "message": "Rejection reason is required",
  "field": "reason"
}

409 Conflict:
{
  "error": "invalid_state_transition",
  "message": "Invoice inv_abc123 is already approved",
  "currentStatus": "approved"
}

404 Not Found:
{
  "error": "not_found",
  "message": "Invoice inv_abc123 not found"
}
```

---

## 3. Key Tradeoffs

| Decision | Tradeoff |
|----------|----------|
| **Idempotency via header** | Clients must generate and store keys; adds complexity but guarantees safe retries. |
| **Reject requires reason** | Prevents ambiguous rejections; may slow workflow if reason field is misused. |
| **Audit in separate `audit` object** | Keeps invoice payload clean; requires extra fetch for full history. |
| **Status filter on list** | Simple but limited; consider adding `vendor`, `dateRange` filters if scale grows. |
| **Optimistic 200 on duplicate approval** | Idempotent by design; may confuse clients expecting 201 only on first approval. |

---

## 4. Risks and Human Gates

| Risk | Mitigation | Human Gate Required? |
|------|------------|---------------------|
| Approving already-rejected invoice | Return 409 with clear state message | No |
| Idempotency key collision | Use client-generated UUID; server stores keys with TTL | No |
| Sensitive audit data exposure | Filter fields based on caller role; review with security | **Yes** |
| Breaking change to rejection schema | Version endpoint (`/v2/`) if reason format changes | **Yes** |
| Rate limiting on list endpoint | Implement cursor-based pagination at scale | No |

---

## 5. Verification Checklist

- [ ] `GET /v1/invoices?status=pending` returns only pending invoices with pagination
- [ ] `POST /v1/invoices/{id}/approve` with same `Idempotency-Key` returns 200 and same `auditId`
- [ ] `POST /v1/invoices/{id}/approve` without key returns 400
- [ ] `POST /v1/invoices/{id}/reject` without `reason` returns 400
- [ ] Approving/rejecting already-processed invoice returns 409
- [ ] `GET /v1/invoices/{id}` includes `audit.history` with all state transitions
- [ ] Auth: endpoints require valid user context; reject anonymous requests with 401
- [ ] Schema validation: amounts are decimal, currency is ISO 4217, timestamps are ISO 8601
- [ ] Contract tests cover all error codes and state transitions
- [ ] Security review confirms audit metadata does not leak sensitive fields

---

## Handoff Notes

| Team | Items for Review |
|------|------------------|
| **Security** | Audit metadata field exposure; role-based access to history |
| **Platform** | Idempotency key storage TTL; rate limit configuration |
| **QA** | Contract tests for 409 conflicts; idempotency scenarios |
| **Docs** | Example `Idempotency-Key` generation; rejection reason guidelines |
| **Product** | Confirm rejection reason is required vs. optional for v1 |
