## API Design Contract for Invoice Approvals

### 1. Design Summary
A RESTful API that lets a client list invoices pending approval, approve an invoice, or reject it with a reason. Writes use **idempotency keys** so retries are safe. Each invoice response includes an **audit log** capturing who acted, when, and the outcome. The API is versioned (`/v1/`) and uses standard HTTP status codes.

---

### 2. Proposed API Shape

**Base URL**: `https://api.example.com/v1`

**Authentication**: Bearer token or equivalent (not part of this design, but required).

**Idempotency**: All state‑changing requests (`approve`, `reject`) **must** include an `Idempotency-Key` header. The server stores the response of the first successful processing and replays it for duplicate keys within a retention window (e.g., 24 hours). The key is per‑operation (approve/reject), not shared across endpoints.

---

#### 2.1 List Pending Invoices
`GET /v1/invoices?status=pending&page=1&limit=20`

**Query parameters**:
| Parameter | Type    | Required | Description                  |
|-----------|---------|----------|------------------------------|
| `status`  | string  | yes      | `pending` (only value)       |
| `page`    | integer | no       | Default 1                    |
| `limit`   | integer | no       | Default 20, max 100          |

**Response** `200 OK`:
```json
{
  "data": [
    {
      "id": "inv_123",
      "status": "pending",
      "amount": { "currency": "USD", "value_cents": 1099 },
      "due_date": "2026-03-01",
      "vendor": "Acme Corp",
      "approval_chain": ["manager_id_1", "director_id_2"],
      "audit_trail": [
        {
          "id": "aud_001",
          "action": "created",
          "actor": "submitter_id",
          "timestamp": "2026-02-15T10:30:00Z"
        }
      ]
    }
    // … more invoices
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total_count": 47,
    "next": "/v1/invoices?status=pending&page=2&limit=20"
  }
}
```

**Errors**:
| Code | Meaning                              |
|------|--------------------------------------|
| 400  | Invalid `status` or pagination       |
| 401  | Unauthenticated                      |
| 403  | Not authorized to list invoices      |

---

#### 2.2 Approve an Invoice
`POST /v1/invoices/{invoiceId}/approve`
**Headers**: `Idempotency-Key: client-generated-unique-key`

**Request body**: none (or optional comment – not required).

**Response** `200 OK` – full invoice object with updated status and appended audit entry:
```json
{
  "id": "inv_123",
  "status": "approved",
  "amount": { "currency": "USD", "value_cents": 1099 },
  "due_date": "2026-03-01",
  "approved_by": "current-actor-id",
  "audit_trail": [
    { "id": "aud_001", "action": "created", "actor": "submitter_id", "timestamp": "2026-02-15T10:30:00Z" },
    { "id": "aud_002", "action": "approved", "actor": "current-actor-id", "timestamp": "2026-02-20T09:00:00Z", "idempotency_key": "abc-123" }
  ]
}
```

**Idempotency behaviour**:  
- If the same `Idempotency-Key` is retried, the server **re‑emits the stored 200 response** (no side‑effect).  
- If the invoice is already in a terminal state (`rejected` or `approved`) and the **key is different**, return `409 Conflict` with a detailed error explaining the current state.  
- If the invoice is still `pending` and the key is new, process the approval atomically.

**Errors**:
| Code | Scenario                                      |
|------|-----------------------------------------------|
| 404  | Invoice not found                             |
| 400  | Missing `Idempotency-Key` header              |
| 409  | Invoice already approved/rejected (new key)   |
| 422  | Business rule violation (e.g., not in approval chain) |
| 429  | Too many requests                             |

---

#### 2.3 Reject an Invoice
`POST /v1/invoices/{invoiceId}/reject`
**Headers**: `Idempotency-Key: client-generated-unique-key`

**Request body**:
```json
{
  "reason": "Vendor tax ID missing – policy requires validation"
}
```
- `reason` is required, max 1000 characters.

**Response** `200 OK`:
```json
{
  "id": "inv_123",
  "status": "rejected",
  "amount": { "currency": "USD", "value_cents": 1099 },
  "rejection_reason": "Vendor tax ID missing – policy requires validation",
  "audit_trail": [
    ...,
    { "id": "aud_003", "action": "rejected", "actor": "current-actor-id", "timestamp": "2026-02-21T11:15:00Z", "reason": "...", "idempotency_key": "def-456" }
  ]
}
```

**Idempotency** and error semantics mirror the approve endpoint (409 for conflicting terminal state, 200 replay on duplicate key).

---

### 3. Key Tradeoffs

| Decision                           | Alternative                            | Why chosen                                                  |
|------------------------------------|----------------------------------------|-------------------------------------------------------------|
| Action endpoints (`/approve`, `/reject`) instead of `PATCH /invoices/{id}` with a status field | Single resource update with a partial document | Clear intent, simpler idempotency scoping, and ability to enforce required fields per action (e.g., `reason` for rejection). |
| `POST` for approve/reject rather than `PUT` | Idempotent `PUT` with a client‑chosen transaction ID | `POST` with `Idempotency-Key` is widely adopted and avoids coupling client‑generated resource IDs to the server’s state model. |
| Embedded audit trail in invoice | Separate `/audit` sub‑resource | Reduces round‑trips; the audit is logically part of the invoice’s lifecycle. A separate endpoint could be added later if pagination or filtering on audit events is needed. |
| `status=pending` filter on `/invoices` | Dedicated `/invoices/pending` endpoint | More flexible for future filters (e.g., `status=approved`). |
| Version prefix `/v1/`              | Content‑negotiation (`Accept: version=…`) | Simple, explicit in URL, easy to route.                   |

---

### 4. Risks and Human Gates

**Risks**  
- **Concurrent conflicting approvals**: Two actors may both try to approve while the invoice is pending. The server must use optimistic locking (e.g., a version or ETag) or serializable isolation to prevent both from succeeding. The idempotency key alone does not prevent this if keys are different.  
- **Idempotency key storage**: Must be persisted with a TTL; ensure the store is resilient and keys are not re‑used across tenants.  
- **Audit trail exposure**: May contain actor identifiers; ensure the caller has permission to view the full trail.  
- **Rejection reason length**: Validation on `reason` must not allow injection (e.g., oversized payloads).  

**Human Gates** (require approval before production rollout)  
- Breaking changes to the API contract (field removal, new required fields, path changes).  
- Changes to authentication/authorization model (e.g., who can approve).  
- Public commitment to this version (`v1`) – once public, deprecation policy must be defined.  
- Any change that alters the semantic meaning of the idempotency key.  

---

### 5. Verification Checklist

- [ ] **Contract tests** for all endpoints (200, 400, 404, 409, 422 responses).  
- [ ] **Idempotency test suite**:  
   - Same key for approve returns identical response and only one audit entry.  
   - Different key after approval returns 409.  
   - Replay of reject with same key returns original response.  
   - Keys with expired TTL are rejected (if applicable).  
- [ ] **Schema validation** against a published OpenAPI document – ensure request/response bodies match.  
- [ ] **Pagination**: verify `next` link when there are more results, `total_count` accuracy.  
- [ ] **Concurrency test**: Simultaneous approve requests with different idempotency keys; only one succeeds, others get 409 (or queue appropriately).  
- [ ] **Consumer review** by integration teams to confirm the contract satisfies their workflows (UI, partners).  
- [ ] **Observability**: Logs/metrics capture idempotency key reuse, conflict rates, and latency.  

---
