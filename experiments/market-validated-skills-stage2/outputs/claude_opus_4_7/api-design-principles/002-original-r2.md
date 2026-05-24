# API Design Review: `POST /users/{id}/delete-all-data`

## Summary

The proposed endpoint touches a high-risk destructive operation (full user data deletion). Several critical inputs are missing, so I cannot approve the design as-is. Below is a review against the API design principles, with explicit uncertainty markers where information was not provided.

---

## 1. Consumers, Use Cases, Constraints — **Insufficient information**

The proposal does not specify:

- **Consumer**: Is this called by the end user (self-service), a support/admin operator, an automated retention job, or a downstream regulator-driven workflow (GDPR/CCPA "right to erasure")? Each implies a different auth model and confirmation flow.
- **Trigger context**: User-initiated account closure vs. admin-forced deletion vs. scheduled purge.
- **Regulatory constraints**: GDPR Art. 17, CCPA, HIPAA, or sector-specific retention floors may *forbid* immediate deletion of certain records (financial, audit logs).

**Required before proceeding** — please provide answers.

---

## 2. Resource Modeling — **Needs revision**

`POST /users/{id}/delete-all-data` is an RPC-style verb in the path, which deviates from REST resource conventions. Recommended alternatives:

- **Option A (preferred — async, auditable):** Model deletion as a resource.
  ```
  POST /users/{id}/deletion-requests
  GET  /users/{id}/deletion-requests/{requestId}
  ```
  Returns `202 Accepted` with a request resource that can be tracked, cancelled during a grace period, and audited.

- **Option B (REST-idiomatic, synchronous):**
  ```
  DELETE /users/{id}
  ```
  with query/body parameters distinguishing soft vs. hard delete. Less flexible for multi-step confirmation flows.

The current verb-in-path form is the weakest option and should be rejected.

---

## 3. Auth Model — **Missing; blocking**

No authentication or authorization scheme was provided. At minimum, specify:

- **Authentication**: OAuth 2.0 bearer token, session, mTLS for service-to-service?
- **Authorization**:
  - Self-deletion: caller's token subject must equal `{id}`, plus a recent step-up (re-authentication or MFA challenge within N minutes).
  - Admin deletion: a distinct scope/role (e.g., `users:delete`) with separation-of-duties (two-person rule for irreversible actions is recommended).
- **Scope granularity**: `users:delete-self` vs. `users:delete-any`.
- **Rate limiting / abuse controls**: destructive endpoints should be rate-limited per principal.

**Cannot approve without an explicit auth model.**

---

## 4. Confirmation Flow — **Missing; blocking**

A single POST that immediately erases all data is dangerous. Recommended pattern:

1. `POST /users/{id}/deletion-requests` → creates request in `pending_confirmation` state; server emits an out-of-band confirmation (email/SMS link with signed token, or requires a re-authenticated `confirmation_token` in the body).
2. `POST /users/{id}/deletion-requests/{requestId}/confirm` with the token → moves to `scheduled`, with a grace window (commonly 14–30 days) during which the user can cancel.
3. `DELETE /users/{id}/deletion-requests/{requestId}` → cancels during grace window.
4. After grace window, background worker executes irreversible erasure.

Also include an **idempotency key** header (`Idempotency-Key`) so retries do not create duplicate requests.

---

## 5. Retention & Erasure Semantics — **Missing; blocking**

Clarify what "all data" means. Typical categories:

| Category | Typical treatment |
|---|---|
| Profile, preferences, user-generated content | Hard delete |
| Financial/transaction records | Retain per legal floor (often 7 yrs), then purge |
| Security/audit logs | Retain, but pseudonymize PII references |
| Backups | Document the rotation window before backup expiry |
| Derived analytics | Anonymize or delete |

The API response should be explicit about what is deleted immediately, what is retained under legal obligation, and the expected timeline. Without a documented retention policy, this endpoint cannot be specified.

---

## 6. Audit Policy — **Missing; blocking**

Every invocation must produce an immutable audit record containing: actor (principal id + auth method), target user, request id, timestamp, source IP / user agent, justification (for admin calls), and outcome. The audit store itself must be exempt from the deletion (per §5). Specify:

- Audit log location and retention.
- Whether audit entries are surfaced via a `GET /users/{id}/deletion-requests` history endpoint to the user.

---

## 7. Errors — **Not specified**

Define at minimum:

- `400` — malformed request / missing idempotency key.
- `401` — unauthenticated.
- `403` — authenticated but lacks scope, or step-up required (include `WWW-Authenticate` challenge).
- `404` — user not found (or `403` if existence should not be disclosed).
- `409` — deletion already in progress / user has unresolvable holds (e.g., open dispute).
- `423` — locked due to legal hold.
- `429` — rate limited.

Use a structured error body (RFC 7807 `application/problem+json` recommended).

---

## 8. Versioning — **Not specified**

Destructive endpoints in particular need a stable contract. Recommend URI versioning (`/v1/users/...`) or header-based (`Accept: application/vnd.api.v1+json`). Pick one and apply consistently.

---

## 9. Pagination — Not applicable to this endpoint, but the deletion-request listing (`GET /users/{id}/deletion-requests`) should follow the team's standard cursor pagination.

---

## Blocking Questions (please answer before re-review)

1. Who is the intended caller (end user, admin, automated job)?
2. What is the auth scheme and which scopes/roles gate this action?
3. What regulatory regime applies, and what is the retention floor per data category?
4. Is a grace/cancellation window acceptable, and if so, how long?
5. What is the audit log destination and retention?
6. Is "all data" defined anywhere, or does it need to be defined as part of this work?

## Recommended Next Step

Reject the current proposal. Replace with a `deletion-requests` sub-resource design (§2 Option A), and return when items 1–6 above are answered. I can produce a full OpenAPI sketch once the auth model and retention policy are provided.

---

*Uncertainty note: This review is based solely on principle-level reasoning; no organization-specific policies, legal counsel input, or existing API conventions were supplied. Environment-specific validation and legal/security review are required before implementation.*
