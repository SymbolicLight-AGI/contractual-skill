## 1. Design summary

The proposed endpoint:

```http
POST /users/{id}/delete-all-data
```

is not ready for approval as a public or production API contract because several required governance and product decisions are missing:

- Authentication and authorization model
- Data retention and legal/compliance requirements
- Audit logging policy
- Customer confirmation or consent flow
- Scope of “all data”
- Idempotency and retry behavior
- Operational recovery or cancellation semantics
- Error model and observability requirements

Because this endpoint can trigger destructive, privacy-sensitive, and potentially irreversible behavior, it requires human approval before implementation or exposure. The correct next step is not to finalize the endpoint shape, but to define the deletion policy, authorization boundary, audit requirements, and customer-facing flow.

A safer API design should model this as a deletion request or erasure job rather than an immediate ambiguous action.

---

## 2. Proposed API shape

### Recommendation: use an erasure request resource

Instead of:

```http
POST /users/{id}/delete-all-data
```

prefer a resource-oriented design such as:

```http
POST /users/{userId}/data-erasure-requests
```

This makes the operation auditable, trackable, and compatible with asynchronous processing.

### Illustrative request

```http
POST /users/{userId}/data-erasure-requests
Idempotency-Key: 7d44c9f1-8e7d-4a85-bce2-2b97c8b6c7f1
Content-Type: application/json
```

```json
{
  "reason": "user_requested_erasure",
  "confirmationToken": "opaque-confirmation-token"
}
```

This example is illustrative only. The exact fields depend on the missing confirmation, auth, and retention requirements.

### Illustrative response for accepted asynchronous deletion

```http
202 Accepted
Location: /users/{userId}/data-erasure-requests/{requestId}
```

```json
{
  "id": "erasure_req_123",
  "userId": "user_456",
  "status": "pending",
  "createdAt": "2026-05-24T12:00:00Z"
}
```

### Status endpoint

```http
GET /users/{userId}/data-erasure-requests/{requestId}
```

Illustrative response:

```json
{
  "id": "erasure_req_123",
  "userId": "user_456",
  "status": "processing",
  "createdAt": "2026-05-24T12:00:00Z",
  "updatedAt": "2026-05-24T12:10:00Z"
}
```

Possible lifecycle states should be explicitly defined, for example:

```text
pending
confirmed
processing
completed
failed
cancelled
rejected
```

Only include states that are supported by the actual product and operational model.

### Possible cancellation endpoint, if allowed

If the product supports a grace period or cancellation window:

```http
POST /users/{userId}/data-erasure-requests/{requestId}/cancel
```

If deletion is immediate or legally required after confirmation, cancellation may not be allowed. This is a product and compliance decision.

---

## 3. Key tradeoffs

### Original proposal: `POST /users/{id}/delete-all-data`

#### Pros

- Simple to call.
- Clearly signals a destructive action.
- Easy for internal teams to understand informally.

#### Cons

- Ambiguous: “all data” is undefined.
- Not resource-oriented.
- Does not expose request state.
- Hard to make safe for retries.
- Does not naturally support auditability.
- Does not clarify whether deletion is synchronous or asynchronous.
- Risky without an explicit authorization and confirmation model.
- May imply immediate irreversible deletion, which may conflict with retention obligations.

### Recommended proposal: `POST /users/{userId}/data-erasure-requests`

#### Pros

- Models deletion as a first-class auditable resource.
- Better for asynchronous workflows.
- Supports status tracking.
- Supports idempotency.
- Allows clear lifecycle states.
- Easier to document, test, and review.
- Better fit for privacy/compliance workflows.

#### Cons

- More complex than a single action endpoint.
- Requires defining lifecycle states and operational handling.
- Requires product/legal/security decisions before contract finalization.

---

## 4. Missing information and required decisions

### 1. Authentication model

Missing.

Questions to resolve:

- Who can initiate deletion?
  - The user themselves?
  - Admins?
  - Customer support?
  - Internal services?
  - Organization owners?
- Is this a public customer-facing API or internal admin API?
- What credentials are accepted?
- Is step-up authentication required?
- Are service accounts allowed to delete user data?
- Does the caller need ownership of `{userId}`?
- Are there tenant or organization boundaries?

Until this is defined, the endpoint should not be approved.

### 2. Authorization policy

Missing.

Required decisions:

- Can a user delete only their own data?
- Can admins delete data for any user?
- Are there role-based restrictions?
- Is dual approval required for staff-initiated deletion?
- Is deletion allowed for suspended, locked, disputed, or legally held accounts?

Authorization changes require human approval and security review.

### 3. Retention and compliance requirements

Missing.

Required decisions:

- What data must be deleted?
- What data must be retained?
- For how long?
- Are there legal hold, fraud, tax, financial, abuse-prevention, or contractual retention exceptions?
- Should retained records be anonymized, pseudonymized, or left intact?
- Are backups included?
- Are derived analytics, logs, exports, and third-party processors included?

The phrase “delete all data” should not be used in the contract unless it is literally true and legally approved.

A safer external term may be:

```text
Request erasure of eligible user data
```

rather than:

```text
Delete all data
```

### 4. Audit policy

Missing.

Required decisions:

- What event is logged when a deletion request is created?
- What event is logged when deletion starts?
- What event is logged when deletion completes, fails, or is rejected?
- Who can access audit logs?
- How long are audit records retained?
- Do audit logs contain personal data?
- Can audit records themselves be erased?
- How are correlation IDs propagated?

For destructive APIs, auditability should be part of the contract and operational design.

### 5. Customer confirmation flow

Missing.

Required decisions:

- Is confirmation required before deletion?
- Is confirmation collected in the UI, API, email, MFA, or support workflow?
- Is a confirmation token required?
- Does the confirmation expire?
- Is there a cooling-off period?
- Can a request be cancelled?
- What happens if confirmation is missing or invalid?

If confirmation is required, the API should not allow deletion with only `{userId}`.

### 6. Idempotency

Missing.

A destructive write API should define retry behavior.

Recommended:

- Require or support an `Idempotency-Key` header for request creation.
- Ensure duplicate requests do not trigger duplicate deletion jobs.
- Return the original erasure request when the same idempotency key is reused with the same parameters.
- Return a conflict error if the same idempotency key is reused with different parameters.

### 7. Error model

Missing.

Define standard errors before implementation.

Illustrative errors:

```http
401 Unauthorized
```

Caller is not authenticated.

```http
403 Forbidden
```

Caller is authenticated but not allowed to request erasure for this user.

```http
404 Not Found
```

User does not exist or is not visible to the caller.

```http
409 Conflict
```

An erasure request already exists, deletion is already in progress, or the user is under legal hold.

```http
422 Unprocessable Entity
```

Request is syntactically valid but missing required confirmation or reason.

```http
429 Too Many Requests
```

Caller exceeded deletion request rate limits.

```http
500 Internal Server Error
```

Unexpected server failure.

```http
503 Service Unavailable
```

Deletion service is temporarily unavailable.

The exact error schema should follow the platform’s existing conventions if any exist. No convention was supplied.

### 8. Observability

Missing.

Recommended observability requirements:

- Correlation ID on every deletion request.
- Audit event IDs.
- Deletion job ID.
- Metrics for request creation, completion, failure, and rejection.
- Alerts for stuck or failed deletion jobs.
- Secure operational logs that do not expose sensitive deleted data.

---

## 5. Risks and human gates

### Major risks

1. **Unauthorized deletion**
   - Without an auth model, a caller may delete another user’s data.

2. **Compliance violation**
   - “Delete all data” may conflict with retention obligations.

3. **Misleading API contract**
   - If some data is retained, the endpoint name overpromises.

4. **Irreversible user harm**
   - Accidental or malicious calls could permanently remove account data.

5. **Poor retry safety**
   - Without idempotency, clients may create duplicate deletion workflows.

6. **Insufficient auditability**
   - Destructive operations require traceability for legal, security, and support review.

7. **Ambiguous asynchronous behavior**
   - Data deletion is likely not instant, especially across backups, logs, downstream systems, or third-party processors.

8. **Breaking public API commitment**
   - Once exposed, changing deletion semantics may be difficult and customer-visible.

### Human gates required before approval

This API should require approval from:

- **Security**: authentication, authorization, abuse prevention, sensitive-data exposure.
- **Legal/compliance/privacy**: retention, erasure scope, legal holds, audit retention.
- **Product**: customer confirmation flow and user-facing semantics.
- **API platform**: naming, error model, idempotency, versioning, standards alignment.
- **Operations/SRE**: async job handling, monitoring, recovery, failure handling.
- **Documentation**: clear explanation of what is and is not deleted.

---

## 6. Verification checklist

Before implementation, verify:

### Contract clarity

- [ ] The meaning of “eligible data” or “all data” is explicitly defined.
- [ ] The endpoint name does not overpromise deletion scope.
- [ ] Request and response schemas are documented.
- [ ] Lifecycle states are defined.
- [ ] Synchronous vs asynchronous behavior is documented.

### Authentication and authorization

- [ ] Auth mechanism is defined.
- [ ] Caller permission rules are defined.
- [ ] Tenant or ownership boundaries are enforced.
- [ ] Admin/support/service-account behavior is reviewed.
- [ ] Step-up authentication or confirmation requirements are decided.

### Idempotency and safety

- [ ] Idempotency behavior is defined for retries.
- [ ] Duplicate requests have predictable behavior.
- [ ] Existing in-progress deletion requests are handled.
- [ ] Confirmation tokens or equivalent safeguards are validated.
- [ ] Cancellation behavior is defined, if supported.

### Retention and compliance

- [ ] Deletion scope is approved by legal/compliance.
- [ ] Retention exceptions are documented.
- [ ] Legal hold behavior is defined.
- [ ] Backup/log/downstream processor behavior is defined.
- [ ] Audit log retention is approved.

### Error handling

- [ ] Standard error schema is used.
- [ ] 401, 403, 404, 409, 422, 429, and 5xx cases are defined where applicable.
- [ ] Error responses avoid leaking sensitive information.
- [ ] Conflict cases such as existing deletion request or legal hold are defined.

### Observability and audit

- [ ] Correlation IDs are supported.
- [ ] Audit events are emitted for request creation, processing, completion, failure, and cancellation/rejection.
- [ ] Metrics and alerts exist for failed or stuck deletion jobs.
- [ ] Operational logs avoid exposing sensitive user data.

### Consumer review

- [ ] Frontend or API consumers understand the confirmation flow.
- [ ] Support/admin users understand the workflow and limitations.
- [ ] Documentation explains expected timing, status states, and retained data exceptions.
- [ ] Contract tests cover success, auth failure, conflict, invalid confirmation, idempotency, and async status retrieval.

---

## Review conclusion

Do not approve `POST /users/{id}/delete-all-data` as proposed.

Approve only after the team defines the missing authentication, authorization, retention, audit, confirmation, idempotency, and error-handling requirements. The preferred direction is to replace the action-style endpoint with an auditable erasure-request resource, such as:

```http
POST /users/{userId}/data-erasure-requests
```

with explicit lifecycle tracking, idempotency, confirmation, and compliance-reviewed deletion semantics.
