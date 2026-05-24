## Design Review: `POST /users/{id}/delete-all-data` (Missing Critical Information)

### 1. Design Summary
The proposed endpoint is intended to irreversibly delete all data associated with a user. The proposal, as given, contains no authentication model, no retention requirements, no audit policy, no customer-facing confirmation mechanism, and no idempotency design. These gaps make the endpoint unsafe both to implement and to expose. This review assumes only what is supplied; no hidden business rules, existing architecture, or platform constraints are invented. All missing information is flagged as required before implementation can proceed.

**Key findings:**

- The endpoint is a destructive, non-idempotent write action exposed without any guard that verifies the caller’s authority.
- Resource naming, HTTP method choice, and lifecycle semantics are ambiguous and need clarification.
- Observability, auditability, and recovery guarantees are absent.
- The current shape cannot be approved until the missing security and operational inputs are resolved through explicit product decisions.

---

### 2. Proposed API Shape (Illustrative – requires missing context)

If the decision is made to expose a user-data purge capability, a safer starting point would be:

**Alternative A (deletion modelled as a sub-resource)**

`DELETE /users/{userId}/personal-data`

- Idempotent by HTTP semantics: repeating the same DELETE request must have the same effect (resource is gone or already gone).
- The resource `/users/{userId}/personal-data` explicitly represents the data set to be removed.
- Requires the caller to possess a token that conveys the ability to delete that specific user’s data; scopes must be verifiable.

**Alternative B (asynchronous action with idempotency key)**

`POST /users/{userId}/personal-data:purge`

- If the operation is long-running or must leave an audit trail, a POST with a `Idempotency-Key` header can be used.
- Returns `202 Accepted` with a tracking resource, e.g., `Location: /data-purges/{purgeId}`, so the caller can poll for completion and the system can retain an audit record.

The originally proposed `POST /users/{id}/delete-all-data` models the action as a verb (`delete-all-data`) on a user, not a resource. This is an RPC-style endpoint, which is acceptable in some API styles, but the naming could be more explicit. Without a defined auth model, however, any shape is premature.

---

### 3. Key Tradeoffs (conditional on missing inputs)

| Aspect               | Options                                                                                                                                        | Requires Decision On                                                                 |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **HTTP Method**      | `DELETE` (idempotent, intuitive for removal) vs `POST` (non-idempotent, suitable for commands)                                                 | Whether the operation is expected to be repeatable safely and the nature of the side effect. |
| **Resource model**   | ` /users/{id}/data` vs `/users/{id}/data-purge` vs RPC‑style `/users/{id}:purgeData`                                                           | What domain concept best represents “all user data” and if purge is a distinct resource or an action. |
| **Confirmation flow**| No confirmation in endpoint vs separate `/users/{id}/data-purge/confirmations` resource                                                         | Product requirement for explicit customer opt‑in (often legally mandated).           |
| **Retention/undo**   | Hard delete vs soft delete with scheduled purge vs grace‑period flag                                                                           | Data retention policy (GDPR/CCPA, business rules).                                   |
| **Audit**            | Synchronous audit record in same service vs async event emission                                                                              | Compliance and forensic needs.                                                        |
| **Auth model**       | OAuth2 scope (e.g., `user.data.delete`), principal‑verify (e.g., only the user can delete their own data), admin override                     | Identity provider, trust boundaries, role definitions.                                |

All tradeoffs are illustrative until the missing inputs are supplied.

---

### 4. Risks and Human Gates

#### 4.1 Risks (due to missing information)
- **Unauthorized destruction**: Without an auth model, any caller (or a confused deputy) could delete any user’s data.
- **Accidental invocation**: No idempotency or confirmation step means a retry, a misconfigured script, or a single click could start an irreversible purge.
- **Regulatory non‑compliance**: Absence of retention requirements may violate data‑protection laws (e.g., mandatory holding periods, right‑to‑erasure workflows).
- **Audit failures**: No audit trail makes it impossible to investigate who requested deletion, when, and under what context.
- **Observability gap**: No consideration for metrics, alerting, or logging on such a critical operation; operations teams cannot detect anomalies.
- **Versioning lock**: Once publicly exposed without idempotency guarantees, changing to an idempotent model later is a breaking change.

#### 4.2 Required Human Gates (must be resolved before implementation)
1. **Authentication and authorization design** – define the exact mechanism (API keys, OAuth2 scopes, user‑token validation, admin roles) and the caller‑to‑resource ownership mapping.
2. **Customer confirmation flow** – product and legal must decide if a confirm step (double opt‑in, email verification) is required before initiating deletion.
3. **Data retention and deletion semantics** – product/data‑governance must specify: hard vs soft delete, recovery window, cascading effects, backup purges, and compliance boundaries.
4. **Audit and compliance requirements** – legal/security approve the audit record schema and retention.
5. **Operational readiness** – SRE/platform agree on rate limits, circuit breakers, monitoring, and an emergency kill switch.
6. **Public API commitment** – any published endpoint (even internal) must be versioned, documented, and contract tested before release.

Until these gates are passed, no implementation should begin.

---

### 5. Verification Checklist (pre‑implementation)

The following artifacts must exist before the design can be considered ready:

- [ ] **Auth model documentation**: explicit scopes/permissions, token validation, and error response for `401`/`403`.
- [ ] **Endpoint schema** (OpenAPI fragment) with request parameters, headers (`Idempotency-Key` if applicable), response codes (e.g., `202` Accepted with tracking URI, `409` Conflict if already in progress, `404` for unknown user).
- [ ] **Idempotency strategy**: either HTTP `DELETE` semantics or `Idempotency-Key` header with server‑managed idempotency cache.
- [ ] **Confirmation flow specification**: if async, describe the confirmation token lifecycle and expiration.
- [ ] **Audit record schema** (who, what, when, trace context) and retention policy for audit logs.
- [ ] **Metrics & alerts** design: deletion started, completed, failed; alert thresholds.
- [ ] **Contract tests** for success, conflict, unauthorized, idempotent replay, and confirmation expiry.
- [ ] **Consumer compatibility plan**: how existing user‑data consumers will be notified or broken.

**Current status**: All items above cannot be verified because the necessary inputs (auth model, retention, audit, confirmation) are entirely absent. This review cannot approve the proposal; it only identifies the gaps.

---

**Uncertainties**:  
- It is unknown whether the team intends a REST or RPC style, what auth infrastructure exists, or if delete‑all‑data is part of a data‑subject request (DSR) workflow.  
- No existing API conventions, versioning policy, or platform standards were provided, so recommendations remain generic.

**Next step**: Present this review to product, security, and legal to resolve the Human Gates listed in section 4.2. After those decisions are captured, a concrete API shape can be designed for review.
