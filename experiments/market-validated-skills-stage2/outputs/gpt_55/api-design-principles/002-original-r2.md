## API Design Review: `POST /users/{id}/delete-all-data`

### Summary

I would not approve this endpoint as proposed. The operation is highly destructive and compliance-sensitive, but the proposal is missing critical design inputs:

- Auth and authorization model
- Retention/legal hold requirements
- Audit policy
- Customer confirmation flow
- Expected deletion semantics
- Recovery/irreversibility guarantees
- Async processing model
- Error behavior and status visibility

Because these are required to safely design the contract, the correct next step is to clarify the policy and product requirements before finalizing the API.

---

## 1. Main Concern: The Endpoint Is Too Vague

Proposed:

```http
POST /users/{id}/delete-all-data
```

Issues:

1. **Action-style endpoint without clear resource model**
   - `delete-all-data` is an RPC-style action.
   - It does not clearly expose whether this creates a deletion request, immediately deletes the user, or schedules erasure.

2. **No auth model**
   - It is unclear who can invoke this:
     - The user themselves?
     - An admin?
     - A privacy officer?
     - A customer support agent?
     - An automated retention job?

3. **No retention/legal policy**
   - Some data may need to be retained for fraud, tax, billing, safety, legal hold, or regulatory reasons.
   - The API must not promise “delete all data” if some data is retained.

4. **No audit policy**
   - Data deletion requests usually require auditable records:
     - Who requested it
     - Who authorized it
     - When it was requested
     - What was deleted or retained
     - Final status

5. **No confirmation flow**
   - A destructive operation should not be triggered accidentally.
   - For self-service deletion, a confirmation or re-authentication step is usually required.

---

## 2. Required Clarifications Before API Approval

The team should answer these before the API is finalized.

### Consumers

Who will call this API?

- End users?
- Internal admin tools?
- Customer support?
- Compliance/privacy team?
- Automated data lifecycle jobs?
- Third-party integrations?

### Authorization

What permissions are required?

Examples:

- User can request deletion of their own account only.
- Admin can request deletion for users in their organization.
- Support can initiate but not approve deletion.
- Privacy officer approval required for certain cases.

Required decision:

```text
Who can delete whose data, under what conditions?
```

### Confirmation Flow

Is confirmation required?

Possible options:

- Password re-entry
- MFA challenge
- Email confirmation link
- Typed confirmation phrase
- Two-step deletion request plus confirmation
- Admin approval workflow

### Retention Requirements

What data cannot be deleted immediately?

Examples:

- Billing records
- Fraud-prevention logs
- Security audit logs
- Legal hold records
- Tax documents
- Transaction history
- Backups until expiration

The API must distinguish between:

```text
deleted
anonymized
retained
scheduled for deletion
not deletable due to legal hold
```

### Audit Requirements

What must be logged?

At minimum:

- Request ID
- Target user ID
- Actor ID
- Actor role
- Request timestamp
- Confirmation timestamp
- Completion timestamp
- Data categories affected
- Retained data categories
- Reason for retention
- Result status

### Deletion Semantics

Does this mean:

- Delete the user account?
- Delete profile data only?
- Delete all personal data?
- Delete application data owned by the user?
- Delete uploaded files?
- Delete messages sent to other users?
- Delete organization-owned resources created by the user?
- Anonymize historical records?

The phrase `delete-all-data` is too broad without a data-category model.

---

## 3. Recommended API Shape

For a high-risk operation like this, prefer modeling deletion as a resource.

Instead of:

```http
POST /users/{id}/delete-all-data
```

Prefer:

```http
POST /users/{id}/data-erasure-requests
```

This makes the operation auditable, trackable, and compatible with async processing.

### Example: Create Erasure Request

```http
POST /users/{id}/data-erasure-requests
Authorization: Bearer <token>
Content-Type: application/json
Idempotency-Key: 8f3e8f7e-2c1d-4a52-bb42-6fda0d5f55f1

{
  "reason": "user_requested",
  "confirmationToken": "confirm_abc123"
}
```

### Example Response

```http
202 Accepted
Location: /users/123/data-erasure-requests/erq_789
Content-Type: application/json
```

```json
{
  "id": "erq_789",
  "userId": "123",
  "status": "pending",
  "reason": "user_requested",
  "requestedAt": "2026-05-24T12:00:00Z",
  "estimatedCompletionAt": "2026-05-25T12:00:00Z"
}
```

Use `202 Accepted` if deletion is asynchronous, which is likely for a multi-system data erasure process.

---

## 4. Status Endpoint

Provide a way to check progress.

```http
GET /users/{id}/data-erasure-requests/{requestId}
```

Example response:

```json
{
  "id": "erq_789",
  "userId": "123",
  "status": "processing",
  "requestedAt": "2026-05-24T12:00:00Z",
  "confirmedAt": "2026-05-24T12:03:00Z",
  "completedAt": null,
  "dataCategories": [
    {
      "name": "profile",
      "status": "deleted"
    },
    {
      "name": "billing_records",
      "status": "retained",
      "retentionReason": "tax_compliance",
      "retainUntil": "2031-01-01T00:00:00Z"
    },
    {
      "name": "audit_logs",
      "status": "retained",
      "retentionReason": "security_audit"
    }
  ]
}
```

Possible statuses:

```text
pending
awaiting_confirmation
processing
completed
partially_completed
rejected
cancelled
failed
blocked_by_legal_hold
```

---

## 5. Confirmation Flow

If this is a self-service user deletion, use a two-step flow.

### Step 1: Start Confirmation

```http
POST /users/{id}/data-erasure-confirmations
```

Response:

```json
{
  "confirmationId": "dec_123",
  "status": "challenge_required",
  "methods": ["password", "mfa", "email"]
}
```

### Step 2: Confirm and Create Request

```http
POST /users/{id}/data-erasure-requests
```

```json
{
  "confirmationId": "dec_123",
  "confirmationCode": "123456",
  "reason": "user_requested"
}
```

This avoids accidental or unauthorized deletion.

---

## 6. Auth and Authorization Requirements

The API contract should explicitly define authorization rules.

Example policy:

```text
Self-service user:
- May create an erasure request for their own user ID only.
- Must complete recent re-authentication and MFA if enabled.

Organization admin:
- May request deletion for users within their organization.
- May not bypass legal hold or retention rules.

Support agent:
- May initiate a request but requires privacy officer approval.

System job:
- May create erasure requests for retention-expired users using service credentials.
```

Recommended authorization failures:

```http
401 Unauthorized
```

When no valid authentication is provided.

```http
403 Forbidden
```

When the caller is authenticated but not allowed to request deletion for the target user.

---

## 7. Error Model

Use a consistent error format.

Example:

```json
{
  "error": {
    "code": "legal_hold_active",
    "message": "Data erasure cannot proceed because the user is subject to a legal hold.",
    "requestId": "req_abc123"
  }
}
```

Recommended error cases:

| Status | Code | Meaning |
|---|---|---|
| `400` | `invalid_request` | Missing or invalid fields |
| `401` | `unauthorized` | Authentication required |
| `403` | `forbidden` | Caller cannot request deletion for this user |
| `404` | `user_not_found` | Target user does not exist or is not visible to caller |
| `409` | `erasure_already_requested` | Existing active request |
| `409` | `legal_hold_active` | Deletion blocked by legal hold |
| `422` | `confirmation_required` | Confirmation or re-authentication missing |
| `429` | `rate_limited` | Too many requests |
| `500` | `internal_error` | Unexpected failure |

---

## 8. Idempotency

This operation must support idempotency.

Clients should send:

```http
Idempotency-Key: <unique-key>
```

This prevents duplicate deletion requests from retries.

If an active request already exists, return either:

```http
200 OK
```

with the existing request, or:

```http
409 Conflict
```

with a pointer to the existing request.

Example:

```json
{
  "error": {
    "code": "erasure_already_requested",
    "message": "An active data erasure request already exists for this user.",
    "existingRequestId": "erq_789"
  }
}
```

---

## 9. Naming Recommendation

Avoid the phrase:

```text
delete-all-data
```

It is likely inaccurate if any data is retained.

Better names:

```http
POST /users/{id}/data-erasure-requests
```

or, if this is account deletion:

```http
POST /users/{id}/account-deletion-requests
```

or, if scoped to privacy compliance:

```http
POST /privacy/data-erasure-requests
```

Example:

```http
POST /privacy/data-erasure-requests
```

```json
{
  "subject": {
    "type": "user",
    "id": "123"
  },
  "reason": "user_requested"
}
```

This may be cleaner if the API supports multiple subject types later, such as users, organizations, or guests.

---

## 10. Versioning and Compatibility

Because this is policy-sensitive, the API should be versioned or designed to evolve safely.

Avoid promising absolute deletion in the API name or response unless guaranteed.

Bad:

```json
{
  "status": "all_data_deleted"
}
```

Better:

```json
{
  "status": "completed",
  "summary": {
    "deletedCategories": ["profile", "preferences", "sessions"],
    "retainedCategories": ["billing_records", "audit_logs"]
  }
}
```

---

## 11. Review Decision

### Decision: Not approved as proposed

The endpoint should not be implemented until the missing policy and product requirements are defined.

### Required next steps

1. Define the consumers and actors.
2. Define authorization rules.
3. Define confirmation requirements.
4. Define retention and legal hold rules.
5. Define audit logging requirements.
6. Define deletion semantics by data category.
7. Decide whether deletion is synchronous or asynchronous.
8. Add status tracking and idempotency.
9. Replace `POST /users/{id}/delete-all-data` with a resource-based request model.

### Recommended replacement

```http
POST /users/{id}/data-erasure-requests
```

with:

```http
GET /users/{id}/data-erasure-requests/{requestId}
```

and a documented confirmation and authorization flow.
