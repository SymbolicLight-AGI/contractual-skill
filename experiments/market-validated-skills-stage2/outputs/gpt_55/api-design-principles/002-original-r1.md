## API Design Review: `POST /users/{id}/delete-all-data`

### Summary

The proposed endpoint is **not ready for approval** because it performs a destructive, potentially irreversible user-data deletion operation but does not define:

- Authorization model
- Retention/legal hold requirements
- Audit policy
- Customer/user confirmation flow
- Idempotency and job semantics
- Error model
- Data scope and deletion guarantees

This endpoint should not be implemented or exposed until those requirements are defined and reviewed with security, legal/compliance, product, and support stakeholders.

---

## 1. Key Missing Information

### Required clarifications

Before reviewing the endpoint shape itself, the team needs to answer:

1. **Who is allowed to request deletion?**
   - The user themselves?
   - An organization admin?
   - Internal support staff?
   - Automated compliance workflows?
   - Third-party integrations?

2. **What data is deleted?**
   - User profile only?
   - Auth credentials?
   - Uploaded files?
   - Billing data?
   - Messages, comments, analytics events, logs?
   - Backups?
   - Derived or anonymized data?

3. **What data must be retained?**
   - Legal retention requirements?
   - Fraud prevention records?
   - Tax/billing records?
   - Security audit logs?
   - Active legal hold exclusions?

4. **Is deletion immediate or asynchronous?**
   - Can deletion complete during the request?
   - Does it require background processing?
   - Is there a deletion SLA, for example “completed within 30 days”?

5. **How does the user confirm intent?**
   - Re-authentication?
   - MFA challenge?
   - Email confirmation?
   - Typed confirmation phrase?
   - Cooling-off period?

6. **How is the action audited?**
   - Who requested deletion?
   - On whose behalf?
   - When?
   - From which IP/device/client?
   - What policy/version was applied?
   - What data was excluded due to retention rules?

7. **Can the operation be retried safely?**
   - Is it idempotent?
   - What happens if deletion is already in progress or already completed?

---

## 2. Endpoint Design Concerns

### Current proposal

```http
POST /users/{id}/delete-all-data
```

### Issues

1. **Action name in path**
   - `delete-all-data` is command-like rather than resource-oriented.
   - For a destructive workflow, it may be better modeled as a deletion request resource.

2. **Ambiguous scope**
   - “all data” is vague and likely inaccurate if some records must be retained.
   - The API should describe whether this is account deletion, personal data erasure, anonymization, or full purge.

3. **No confirmation or workflow state**
   - Data deletion is rarely a single immediate operation.
   - The API should expose a deletion request with status.

4. **No authorization model**
   - This is a critical blocker.
   - Deleting another user’s data must be carefully controlled.

5. **No auditability**
   - The design does not indicate how the deletion will be traced or reviewed.

---

## 3. Recommended API Shape

Instead of an imperative endpoint, model deletion as a resource.

### Option A: User self-service deletion request

```http
POST /users/me/data-deletion-requests
```

Example request:

```json
{
  "reason": "user_requested_erasure",
  "confirmationToken": "abc123",
  "scope": "personal_data"
}
```

Example response:

```http
202 Accepted
Location: /users/me/data-deletion-requests/delreq_123
```

```json
{
  "id": "delreq_123",
  "status": "pending",
  "scope": "personal_data",
  "requestedAt": "2026-05-24T12:00:00Z",
  "estimatedCompletionAt": "2026-06-23T12:00:00Z"
}
```

Status endpoint:

```http
GET /users/me/data-deletion-requests/delreq_123
```

Example response:

```json
{
  "id": "delreq_123",
  "status": "processing",
  "scope": "personal_data",
  "requestedAt": "2026-05-24T12:00:00Z",
  "estimatedCompletionAt": "2026-06-23T12:00:00Z",
  "retentionExclusions": [
    {
      "category": "billing_records",
      "reason": "legal_retention_required"
    }
  ]
}
```

### Option B: Admin-initiated deletion request

```http
POST /users/{userId}/data-deletion-requests
```

This should require elevated authorization and explicit policy controls.

Example request:

```json
{
  "reason": "gdpr_erasure_request",
  "scope": "personal_data",
  "requestedBy": "admin",
  "caseId": "case_456"
}
```

Response:

```http
202 Accepted
Location: /users/{userId}/data-deletion-requests/delreq_123
```

---

## 4. Authorization Requirements

The API design must specify authorization before approval.

Recommended minimum model:

### For self-service users

Allow:

```http
POST /users/me/data-deletion-requests
```

Requirements:

- Authenticated user only
- Recent re-authentication
- MFA or equivalent confirmation for high-risk accounts
- Explicit user confirmation
- Idempotency key support

Avoid allowing users to submit deletion requests for arbitrary IDs unless there is a clear admin model.

### For admins or support staff

Allow only with scoped permissions, for example:

```text
user.data_deletion:create
user.data_deletion:read
user.data_deletion:cancel
```

Additional requirements:

- Role-based or policy-based access control
- Tenant boundary enforcement
- Reason code required
- Case/ticket reference required
- Strong audit trail
- Optional dual-control approval for sensitive environments

---

## 5. Confirmation Flow

The endpoint should not perform deletion solely based on a simple API call unless the caller is a trusted internal workflow with equivalent controls.

Recommended flow:

1. User starts deletion request.
2. System sends confirmation challenge or requires recent re-authentication.
3. User confirms deletion.
4. API creates deletion request.
5. Deletion proceeds asynchronously.
6. User or admin can check status.
7. Completion event or notification is emitted.

Possible endpoints:

```http
POST /users/me/data-deletion-confirmations
POST /users/me/data-deletion-requests
GET /users/me/data-deletion-requests/{requestId}
```

If cancellation is allowed during a grace period:

```http
POST /users/me/data-deletion-requests/{requestId}/cancel
```

---

## 6. Retention and Legal Hold Requirements

The API must not promise “delete all data” unless that is actually true.

Prefer precise terminology:

- `account_deletion`
- `personal_data_erasure`
- `anonymization`
- `content_purge`
- `credential_revocation`

Response payloads should disclose retained categories where appropriate:

```json
{
  "status": "completed",
  "completedAt": "2026-05-25T12:00:00Z",
  "retentionExclusions": [
    {
      "category": "tax_records",
      "reason": "statutory_retention",
      "retainedUntil": "2031-01-01"
    },
    {
      "category": "security_audit_logs",
      "reason": "security_and_abuse_prevention"
    }
  ]
}
```

If legal holds may apply, define an error or status:

```json
{
  "id": "delreq_123",
  "status": "blocked",
  "blockedReason": "legal_hold"
}
```

---

## 7. Audit Policy

This operation must create immutable audit records.

Audit fields should include:

```json
{
  "eventType": "user_data_deletion_requested",
  "requestId": "delreq_123",
  "targetUserId": "user_123",
  "actorId": "user_123",
  "actorType": "user",
  "requestedAt": "2026-05-24T12:00:00Z",
  "clientId": "web_app",
  "ipAddress": "203.0.113.10",
  "userAgent": "example",
  "reason": "user_requested_erasure",
  "scope": "personal_data",
  "policyVersion": "2026-05-01",
  "confirmationMethod": "mfa"
}
```

Audit logging should cover:

- Request creation
- Confirmation completion
- Deletion job started
- Data categories deleted
- Retention exclusions
- Failures
- Completion
- Cancellation, if supported

---

## 8. Error Model

Use consistent API errors.

Examples:

### Not authorized

```http
403 Forbidden
```

```json
{
  "error": {
    "code": "forbidden",
    "message": "You are not authorized to request data deletion for this user."
  }
}
```

### Confirmation required

```http
409 Conflict
```

```json
{
  "error": {
    "code": "confirmation_required",
    "message": "Recent confirmation is required before creating a deletion request."
  }
}
```

### Deletion already in progress

```http
409 Conflict
```

```json
{
  "error": {
    "code": "deletion_already_in_progress",
    "message": "A deletion request is already in progress for this user.",
    "deletionRequestId": "delreq_123"
  }
}
```

### Legal hold

```http
423 Locked
```

```json
{
  "error": {
    "code": "legal_hold",
    "message": "Deletion is currently blocked by a legal hold."
  }
}
```

---

## 9. Idempotency and Asynchronous Processing

This endpoint should likely return `202 Accepted`, not `200 OK`, because deletion is usually asynchronous.

Require an idempotency key:

```http
Idempotency-Key: 2b4f9e7c-0f4a-4d93-a0af-123456789abc
```

If the same request is retried, return the existing deletion request rather than creating another one.

---

## 10. Recommendation

Do **not** approve:

```http
POST /users/{id}/delete-all-data
```

as currently proposed.

Recommend replacing it with a deletion-request workflow, for example:

```http
POST /users/me/data-deletion-requests
GET /users/me/data-deletion-requests/{requestId}
```

and, if admin-initiated deletion is required:

```http
POST /users/{userId}/data-deletion-requests
GET /users/{userId}/data-deletion-requests/{requestId}
```

Approval should be blocked until the team defines:

- Auth model
- Confirmation requirements
- Deletion scope
- Retention/legal hold rules
- Audit policy
- Error model
- Idempotency behavior
- Asynchronous job/status model
- Versioning/backward compatibility impact
- Documentation and customer-facing semantics

The correct next step is a requirements review with product, security, legal/compliance, and support before finalizing the API contract.
