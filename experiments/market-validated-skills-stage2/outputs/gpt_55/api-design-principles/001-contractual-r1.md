## 1. Design summary

Design a REST API centered on the `invoice` resource and its approval lifecycle.

Supplied requirements:

- List pending invoices.
- Approve one invoice.
- Reject one invoice with a reason.
- Support idempotent approval retries.
- Expose audit metadata.
- No code required.

Assumptions, to be validated:

- Invoices already exist before approval.
- Approval state is part of an invoice lifecycle.
- Consumers are authenticated internal or partner clients with permission to approve/reject invoices.
- Audit metadata should expose operationally useful fields without leaking sensitive internal data.

Recommended model:

- Use `GET /invoices?status=pending_approval` to list pending invoices.
- Use action subresources for lifecycle transitions:
  - `POST /invoices/{invoiceId}/approval`
  - `POST /invoices/{invoiceId}/rejection`
- Require an `Idempotency-Key` header for approval and preferably for rejection as well.
- Include audit metadata on invoice responses and transition responses.

---

## 2. Proposed API shape

### Resource: Invoice

Illustrative response shape:

```json
{
  "id": "inv_123",
  "status": "pending_approval",
  "amount": {
    "currency": "USD",
    "value": "1250.00"
  },
  "vendor": {
    "id": "ven_456",
    "name": "Example Vendor"
  },
  "submittedAt": "2026-05-24T10:00:00Z",
  "audit": {
    "createdAt": "2026-05-20T09:00:00Z",
    "createdBy": "user_111",
    "updatedAt": "2026-05-24T10:00:00Z",
    "updatedBy": "user_222",
    "approval": {
      "approvedAt": null,
      "approvedBy": null,
      "rejectedAt": null,
      "rejectedBy": null,
      "rejectionReason": null
    }
  }
}
```

Notes:

- Field names are illustrative.
- Avoid exposing sensitive user details unless explicitly approved.
- `createdBy`, `updatedBy`, `approvedBy`, and `rejectedBy` may be user IDs, service account IDs, or actor references depending on the auth model.

---

### List pending invoices

```http
GET /invoices?status=pending_approval&limit=50&pageToken=abc
```

#### Query parameters

| Parameter | Required | Description |
|---|---:|---|
| `status` | Optional or required by convention | Use `pending_approval` to list pending invoices. |
| `limit` | Optional | Maximum number of invoices to return. |
| `pageToken` | Optional | Cursor for pagination. |

#### Response

```http
200 OK
```

```json
{
  "data": [
    {
      "id": "inv_123",
      "status": "pending_approval",
      "amount": {
        "currency": "USD",
        "value": "1250.00"
      },
      "vendor": {
        "id": "ven_456",
        "name": "Example Vendor"
      },
      "submittedAt": "2026-05-24T10:00:00Z",
      "audit": {
        "createdAt": "2026-05-20T09:00:00Z",
        "createdBy": "user_111",
        "updatedAt": "2026-05-24T10:00:00Z",
        "updatedBy": "user_222"
      }
    }
  ],
  "pagination": {
    "nextPageToken": "def",
    "hasMore": true
  }
}
```

#### Behavior

- Returns invoices visible to the authenticated caller.
- Should support pagination from the start to avoid compatibility issues.
- If no pending invoices exist, return:

```http
200 OK
```

```json
{
  "data": [],
  "pagination": {
    "nextPageToken": null,
    "hasMore": false
  }
}
```

---

### Approve an invoice

```http
POST /invoices/{invoiceId}/approval
Idempotency-Key: 8f9a2c2e-3d5b-4a8a-9b5a-example
```

#### Request body

```json
{
  "comment": "Reviewed and approved"
}
```

`comment` is optional unless the product requires approval comments.

#### Response: newly approved

```http
200 OK
```

```json
{
  "id": "inv_123",
  "status": "approved",
  "audit": {
    "updatedAt": "2026-05-24T11:00:00Z",
    "updatedBy": "user_789",
    "approval": {
      "approvedAt": "2026-05-24T11:00:00Z",
      "approvedBy": "user_789",
      "approvalComment": "Reviewed and approved",
      "rejectedAt": null,
      "rejectedBy": null,
      "rejectionReason": null
    }
  }
}
```

#### Idempotency behavior

Approval should be idempotent when the same `Idempotency-Key` is retried for the same invoice and same request payload.

Recommended behavior:

| Scenario | Response |
|---|---|
| First valid approval request | `200 OK` with approved invoice |
| Retry with same key and same payload | `200 OK` with same effective approval result |
| Retry with same key but different payload | `409 Conflict` or `422 Unprocessable Entity` |
| Invoice already approved by same completed operation | `200 OK` |
| Invoice already rejected | `409 Conflict` |
| Invoice does not exist | `404 Not Found` |
| Caller lacks permission | `403 Forbidden` |
| Missing idempotency key | `400 Bad Request` |

Alternative: use `201 Created` for the first creation of an approval subresource. However, `200 OK` is simpler for consumers because approval is a state transition on an existing invoice.

---

### Reject an invoice

```http
POST /invoices/{invoiceId}/rejection
Idempotency-Key: 59a2c1ee-1122-43de-bc4a-example
```

#### Request body

```json
{
  "reason": "Invoice amount does not match purchase order"
}
```

#### Validation

- `reason` is required.
- Enforce a maximum length, for example 1,000 characters.
- If structured rejection reasons are needed later, add `reasonCode` in a backward-compatible way.

#### Response

```http
200 OK
```

```json
{
  "id": "inv_123",
  "status": "rejected",
  "audit": {
    "updatedAt": "2026-05-24T11:15:00Z",
    "updatedBy": "user_789",
    "approval": {
      "approvedAt": null,
      "approvedBy": null,
      "rejectedAt": "2026-05-24T11:15:00Z",
      "rejectedBy": "user_789",
      "rejectionReason": "Invoice amount does not match purchase order"
    }
  }
}
```

#### Behavior

| Scenario | Response |
|---|---|
| Valid rejection request | `200 OK` |
| Missing rejection reason | `422 Unprocessable Entity` |
| Invoice already approved | `409 Conflict` |
| Invoice already rejected by same idempotent operation | `200 OK` |
| Invoice does not exist | `404 Not Found` |
| Caller lacks permission | `403 Forbidden` |

Although the requirement only explicitly mentions idempotent approval retries, rejection should also support idempotency to protect against duplicate client retries and network failures.

---

### Optional: Get one invoice

Not explicitly required, but useful for clients after approval/rejection.

```http
GET /invoices/{invoiceId}
```

#### Response

```http
200 OK
```

```json
{
  "id": "inv_123",
  "status": "approved",
  "amount": {
    "currency": "USD",
    "value": "1250.00"
  },
  "vendor": {
    "id": "ven_456",
    "name": "Example Vendor"
  },
  "submittedAt": "2026-05-24T10:00:00Z",
  "audit": {
    "createdAt": "2026-05-20T09:00:00Z",
    "createdBy": "user_111",
    "updatedAt": "2026-05-24T11:00:00Z",
    "updatedBy": "user_789",
    "approval": {
      "approvedAt": "2026-05-24T11:00:00Z",
      "approvedBy": "user_789",
      "approvalComment": "Reviewed and approved",
      "rejectedAt": null,
      "rejectedBy": null,
      "rejectionReason": null
    }
  }
}
```

---

### Error model

Use a consistent JSON error envelope.

```json
{
  "error": {
    "code": "invoice_state_conflict",
    "message": "Invoice cannot be approved because it has already been rejected.",
    "details": {
      "invoiceId": "inv_123",
      "currentStatus": "rejected"
    },
    "requestId": "req_abc123"
  }
}
```

Recommended error codes:

| HTTP status | Error code | Meaning |
|---:|---|---|
| `400` | `missing_idempotency_key` | Required idempotency key was not provided. |
| `401` | `unauthenticated` | Caller is not authenticated. |
| `403` | `forbidden` | Caller cannot view or approve/reject this invoice. |
| `404` | `invoice_not_found` | Invoice does not exist or is not visible to caller. |
| `409` | `invoice_state_conflict` | Invoice is not in a state that allows the requested transition. |
| `409` | `idempotency_key_conflict` | Same idempotency key was reused with a different payload. |
| `422` | `validation_failed` | Request body is syntactically valid but semantically invalid. |
| `429` | `rate_limited` | Caller exceeded rate limits, if applicable. |
| `500` | `internal_error` | Unexpected server error. |

---

## 3. Key tradeoffs

### Action subresources vs direct status update

Recommended:

```http
POST /invoices/{invoiceId}/approval
POST /invoices/{invoiceId}/rejection
```

Instead of:

```http
PATCH /invoices/{invoiceId}
```

with:

```json
{
  "status": "approved"
}
```

Why:

- Approval and rejection are domain actions, not simple field edits.
- Easier to apply distinct validation rules.
- Easier to capture audit events.
- Easier to enforce idempotency on each transition.
- Prevents clients from attempting unsupported status changes.

Tradeoff:

- Adds more endpoints.
- Less generic than a single `PATCH`.

---

### `200 OK` vs `201 Created` for approval

Recommended: `200 OK`.

Reason:

- The invoice already exists.
- Approval changes invoice state.
- Idempotent retries are easier for clients when the response status remains stable.

Alternative:

- `201 Created` if the platform models approval as a separate persistent approval resource.

---

### Cursor pagination vs offset pagination

Recommended: cursor pagination using `pageToken`.

Reason:

- More stable for lists that can change while clients paginate.
- Better for large datasets.

Tradeoff:

- Slightly less transparent for client debugging than `offset` and `limit`.

---

### Audit metadata exposure

Expose only necessary actor and timestamp information.

Recommended fields:

- `createdAt`
- `createdBy`
- `updatedAt`
- `updatedBy`
- `approvedAt`
- `approvedBy`
- `rejectedAt`
- `rejectedBy`
- `rejectionReason`

Avoid exposing:

- Internal authorization decisions.
- Sensitive employee details.
- Internal database IDs if they are not part of the public contract.
- Full audit logs unless explicitly required and reviewed.

---

## 4. Risks and human gates

### Risks

1. **Authorization ambiguity**
   - The API must define who can view, approve, and reject invoices.
   - Approval permissions may depend on amount, vendor, department, or role, but those rules were not supplied.

2. **Sensitive audit data exposure**
   - Audit metadata can reveal user identities and business processes.
   - Security/privacy review is needed before exposing actor fields.

3. **State transition conflicts**
   - Concurrent approval and rejection attempts may race.
   - The implementation must guarantee only one terminal state wins.

4. **Idempotency storage**
   - The platform must define how long idempotency keys are retained.
   - The API contract should document the retention window, for example 24 hours, but no requirement was supplied.

5. **Backward compatibility**
   - Status values become part of the public contract.
   - Adding new statuses later should be non-breaking only if clients are prepared for unknown values.

6. **Audit completeness**
   - The response exposes audit metadata, but a full immutable audit log is not specified.
   - If regulatory auditability is required, this contract may be insufficient.

### Human gates

Require approval from:

- **Product** for invoice lifecycle states and rejection reason requirements.
- **Security** for authentication, authorization, and audit metadata exposure.
- **API platform** for idempotency-key standards, pagination conventions, and error envelope consistency.
- **Legal/compliance**, if invoice approvals have regulatory retention or audit requirements.
- **Consumer teams** before committing this as a public or partner API contract.

---

## 5. Verification checklist

Before implementation or publication, verify:

### Contract consistency

- [ ] Endpoint names follow platform naming conventions.
- [ ] Status values are explicitly documented.
- [ ] Request and response schemas are versioned or otherwise compatibility-managed.
- [ ] Unknown future fields are safely ignored by clients.

### Listing behavior

- [ ] `GET /invoices?status=pending_approval` returns only invoices visible to caller.
- [ ] Empty results return `200 OK` with an empty array.
- [ ] Pagination works consistently using `limit` and `pageToken`.
- [ ] Sorting behavior is defined, for example by `submittedAt` ascending or descending.

### Approval behavior

- [ ] Approval requires valid authorization.
- [ ] Approval requires `Idempotency-Key`.
- [ ] Same idempotency key and same payload returns the same effective result.
- [ ] Same idempotency key with different payload fails predictably.
- [ ] Already rejected invoices cannot be approved.
- [ ] Concurrent approval/rejection attempts produce one final state.

### Rejection behavior

- [ ] Rejection requires valid authorization.
- [ ] Rejection requires a non-empty `reason`.
- [ ] Rejection reason length and allowed content are validated.
- [ ] Already approved invoices cannot be rejected.
- [ ] Rejection is idempotent or explicitly documented if not.

### Error handling

- [ ] All errors use the standard error envelope.
- [ ] `requestId` or equivalent correlation ID is included.
- [ ] Validation failures identify the invalid fields.
- [ ] State conflicts return `409 Conflict`.

### Audit and observability

- [ ] Approval and rejection events are recorded with actor and timestamp.
- [ ] Response audit metadata does not expose sensitive fields.
- [ ] Logs and metrics include request ID, invoice ID, operation type, result, and latency.
- [ ] Audit retention requirements are confirmed.

### Security

- [ ] Authentication scheme is defined.
- [ ] Authorization rules are reviewed.
- [ ] Invoice visibility is enforced on list and item endpoints.
- [ ] Rejection reasons are handled as potentially sensitive user-provided content.
