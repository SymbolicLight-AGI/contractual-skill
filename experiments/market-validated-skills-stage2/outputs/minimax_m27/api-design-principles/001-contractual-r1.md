# Invoice Approval API Contract

## 1. Design Summary

This contract models invoice approvals as a **workflow resource** with state transitions (pending → approved/rejected). The API exposes the approval action as a first-class resource to support idempotency, auditability, and explicit rejection reasons. All write operations are idempotent via client-supplied idempotency keys.

---

## 2. Proposed API Shape

### 2.1 List Pending Invoices

```
GET /invoices?status=pending&page=1&pageSize=20

Response 200:
{
  "data": [
    {
      "id": "inv_abc123",
      "vendor": "Acme Corp",
      "amount": 1500.00,
      "currency": "USD",
      "dueDate": "2024-02-15",
      "status": "pending",
      "submittedAt": "2024-01-20T10:30:00Z",
      "createdBy": "user_xyz"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalCount": 45,
    "hasNext": true
  }
}
```

### 2.2 Get Invoice Detail

```
GET /invoices/{invoiceId}

Response 200:
{
  "id": "inv_abc123",
  "vendor": "Acme Corp",
  "amount": 1500.00,
  "currency": "USD",
  "dueDate": "2024-02-15",
  "status": "pending",
  "lineItems": [...],
  "submittedAt": "2024-01-20T10:30:00Z",
  "submittedBy": "user_xyz",
  "approvalHistory": [
    {
      "action": "submitted",
      "actor": "user_xyz",
      "timestamp": "2024-01-20T10:30:00Z"
    }
  ]
}
```

### 2.3 Approve Invoice

```
POST /invoices/{invoiceId}/approvals
Idempotency-Key: {client-generated-uuid}
Authorization: Bearer {token}

Request body (optional):
{
  "comment": "Approved per Q1 budget"
}

Response 200 (approval succeeded or already approved):
{
  "invoiceId": "inv_abc123",
  "status": "approved",
  "approvedAt": "2024-01-25T14:00:00Z",
  "approvedBy": "user_current",
  "idempotencyKey": "client-key-here"
}

Response 409 (invoice already rejected):
{
  "error": {
    "code": "INVALID_STATE_TRANSITION",
    "message": "Cannot approve a rejected invoice",
    "details": {
      "currentStatus": "rejected",
      "rejectedAt": "2024-01-22T09:00:00Z",
      "rejectedBy": "user_other",
      "rejectionReason": "Budget exceeded"
    }
  }
}
```

### 2.4 Reject Invoice

```
POST /invoices/{invoiceId}/rejections
Idempotency-Key: {client-generated-uuid}
Authorization: Bearer {token}

Request body:
{
  "reason": "Budget exceeded for Q1",
  "comment": "See Jira ticket INV-456"
}

Response 200:
{
  "invoiceId": "inv_abc123",
  "status": "rejected",
  "rejectedAt": "2024-01-25T14:00:00Z",
  "rejectedBy": "user_current",
  "reason": "Budget exceeded for Q1",
  "idempotencyKey": "client-key-here"
}

Response 409 (already approved):
{
  "error": {
    "code": "INVALID_STATE_TRANSITION",
    "message": "Cannot reject an already approved invoice",
    "details": { "currentStatus": "approved" }
  }
}
```

### 2.5 Get Audit Trail

```
GET /invoices/{invoiceId}/audit

Response 200:
{
  "invoiceId": "inv_abc123",
  "entries": [
    {
      "timestamp": "2024-01-20T10:30:00Z",
      "action": "submitted",
      "actor": "user_xyz",
      "actorRole": "submitter"
    },
    {
      "timestamp": "2024-01-25T14:00:00Z",
      "action": "approved",
      "actor": "user_current",
      "actorRole": "approver",
      "comment": "Approved per Q1 budget",
      "metadata": {
        "ipAddress": "192.168.1.1",
        "userAgent": "Mozilla/5.0..."
      }
    }
  ]
}
```

### 2.6 Error Response Schema

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "requestId": "req_abc123",
    "details": {}
  }
}
```

---

## 3. Key Tradeoffs

| Decision | Rationale | Tradeoff |
|----------|-----------|----------|
| Separate `/approvals` and `/rejections` endpoints | Explicit rejection reason required; cleaner semantically than generic PATCH | Consumers must call different endpoints for each action |
| POST for state transitions | Approval/rejection are irreversible actions with side effects; POST is appropriate for non-CRUD operations | Less RESTful-orthodox than using PUT/PATCH on the invoice resource |
| `Idempotency-Key` header on write ops | Enables safe client retries without duplicate approvals/rejections | Requires clients to generate and track keys; server must deduplicate within a time window |
| Audit trail as separate endpoint | Separates read-only audit data from invoice resource; supports compliance access patterns | Extra network call if consumers need both invoice and audit in one request |
| 409 on invalid state transitions | Fail fast rather than silently ignoring action; consumer can handle idempotency and state errors differently | Requires clients to handle conflict errors explicitly |
| Embedded approval history in invoice | Reduces round-trips for simple approval status checks | Increases payload size for list operations |

---

## 4. Risks and Human Gates

| Risk | Mitigation | Human Gate Required? |
|------|------------|---------------------|
| **Rejection reason lost or empty** | Require `reason` field; return 400 if missing | No—validation handles |
| **Double approval via retry** | Idempotency key deduplication; return 200 with current state | No—server enforces |
| **Unauthorized approval** | Auth token required; enforce role-based access control (RBAC) | **Yes**—security review |
| **Audit tampering** | Immutable audit log; append-only writes | **Yes**—security + compliance |
| **Rate limit abuse on approvals** | Per-user rate limits on write endpoints | No—platform handles |
| **Breaking change: add required fields** | Version prefix (`/v1/`); additive changes only for minor versions | **Yes**—public API commitment |

**Human Gates Required:**
- Security review for RBAC and audit access control
- Public API commitment before versioning freeze

---

## 5. Verification Checklist

### Contract Validation
- [ ] All endpoints return documented status codes (200, 400, 401, 404, 409, 500)
- [ ] Error responses include `code`, `message`, and `requestId`
- [ ] Idempotency key handling tested (retry → same response, no duplicate state change)
- [ ] Pagination metadata present for list endpoint

### Schema Clarity
- [ ] Field names consistent (camelCase)
- [ ] Amount uses decimal type, not float
- [ ] Timestamps in ISO 8601 UTC

### Auth & Permissions
- [ ] All write endpoints require Bearer token
- [ ] Role-based access enforced (approver role required)
- [ ] Unauthorized attempts return 401/403

### Idempotency & Safety
- [ ] Duplicate approval returns 200 with current approved state
- [ ] Duplicate rejection returns 200 with current rejected state
- [ ] Idempotency key collision within 24h window returns original response

### Observability
- [ ] Audit entries capture actor, timestamp, action, and metadata
- [ ] All errors include `requestId` for tracing

### Compatibility
- [ ] No breaking changes to existing response shapes (additive only)
- [ ] Version prefix in base URL for future extensibility

---

**Handoff:** Route to security for RBAC and audit integrity, platform for standards alignment, QA for contract test coverage, documentation for developer examples, and product for rejection reason requirements validation.
