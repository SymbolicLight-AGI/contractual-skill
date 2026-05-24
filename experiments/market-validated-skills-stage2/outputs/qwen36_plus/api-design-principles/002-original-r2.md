# API Design Review: `POST /users/{id}/delete-all-data`

## 1. Consumers, Use Cases, and Constraints
- **Consumers:** [UNCERTAIN] Not specified. Likely candidates: end-users (self-service), customer support/admins, or automated compliance systems.
- **Use Case:** Remove all data associated with a specific user account.
- **Constraints & Missing Information:**
  - **Auth Model:** [UNCERTAIN] No authentication or authorization strategy provided.
  - **Retention Requirement:** [UNCERTAIN] Unknown if deletion is immediate (hard), deferred (soft), or subject to legal/compliance holds.
  - **Audit Policy:** [UNCERTAIN] No logging, traceability, or compliance reporting requirements defined.
  - **Customer Confirmation Flow:** [UNCERTAIN] Missing safeguards against accidental or malicious execution (e.g., explicit consent, async job tracking, or re-authentication).

## 2. API Style and Resource Modeling
- **Current Proposal Issue:** `POST /users/{id}/delete-all-data` violates REST resource-oriented design. It embeds a verb in the URI and misuses `POST` for a destructive operation.
- **Recommended REST Model:**
  - Use standard HTTP methods and noun-based resources.
  - For direct deletion: `DELETE /users/{id}` (server-side cascade/soft-delete handled internally)
  - For explicit data purge with workflow: `POST /users/{id}/data-purge-requests` (returns a job ID for async tracking)
- **Alternative GraphQL Model (if applicable):** `mutation DeleteUserData($userId: ID!, $confirm: Boolean!): DataPurgeJob`

## 3. Errors, Versioning, Pagination, and Auth Strategy
- **Auth Strategy:** [UNCERTAIN] Must be defined before implementation. Recommended baseline: OAuth 2.0/OIDC with explicit destructive scopes (e.g., `user:data:delete` or `admin:users:manage`). Require step-up authentication (MFA or re-auth) for destructive actions.
- **Error Handling:** Standardize using RFC 7807 (Problem Details). Expected responses:
  - `401 Unauthorized` (missing/invalid token)
  - `403 Forbidden` (insufficient scope/role)
  - `404 Not Found` (user does not exist)
  - `409 Conflict` (deletion already in progress or blocked by compliance hold)
  - `422 Unprocessable Entity` (missing confirmation payload or invalid idempotency key)
- **Versioning:** Include in path (`/v1/...`) or header. Destructive endpoints require strict backward compatibility guarantees.
- **Pagination:** Not applicable for this operation.
- **Idempotency:** Require `Idempotency-Key` header to safely retry network failures without duplicate deletions.

## 4. Validation and Consistency Review
- **Revised Example Request:**
  ```http
  DELETE /v1/users/{id}/data
  Authorization: Bearer <token>
  Idempotency-Key: <uuid>
  X-Confirmation-Token: <token-from-confirmation-flow>
  Content-Type: application/json

  {
    "reason": "user_requested",
    "confirm": true
  }
  ```
- **Consistency Check:**
  - ✅ Path uses nouns, HTTP method matches intent
  - ✅ Idempotency and confirmation headers/payloads prevent accidental execution
  - ❌ Missing auth, retention, audit, and confirmation flows block safe deployment
  - ❌ Server-side behavior (sync vs async, backup handling, cascade rules) is undefined

## Required Clarifications (Per Skill Limitations)
Implementation cannot proceed safely until the following are provided:
1. **Auth Model:** Which roles/scopes are permitted to invoke this endpoint? Is it user-initiated or admin-only?
2. **Retention Policy:** Is this a hard delete, soft delete, or subject to legal hold? How are backups handled?
3. **Audit Requirements:** What metadata must be logged (actor, timestamp, IP, reason)? How long are audit logs retained?
4. **Confirmation Flow:** Should this be synchronous with explicit consent, or asynchronous with a job-tracking endpoint?

*Boundary Note: This review provides design guidance only. It does not substitute for environment-specific validation, security testing, compliance review, or expert architectural sign-off. Please provide the missing inputs above to finalize the specification.*
