# API Design Review: `POST /users/{id}/delete-all-data`

## 1. Design Summary

The proposal requests an endpoint to permanently delete all data associated with a user. The team has **not supplied** any authentication model, data retention requirements, audit policy, or customer confirmation flow. In its current form, the endpoint is unsafe and incomplete; it cannot proceed to implementation. This review enumerates the missing information, proposes safer alternatives, and defines the required human gates before any commitment.

## 2. Proposed API Shape (with Missing Information)

Because the action is destructive and touches personally identifiable or business‑critical data, a full contract cannot be drafted. The following **illustrative** shape demonstrates what a **properly governed** design might require once the missing inputs are decided. **Everything in this shape is contingent on clarifying the unknowns listed below.**

```
# Resource: User Data Deletion Request
# Requires: Strong authentication, customer confirmation token, audit log.

POST /users/{id}/data-deletion-requests
Description: Initiate a deletion request. Returns a confirmation token that must be presented to finalize.

DELETE /users/{id}/data
Description: Execute deletion after token validation and customer consent.
Header: X-Idempotency-Key: <client-generated UUID>
Body: { "confirmation_token": "...", "reason": "..." }
```

**Why not `POST …/delete-all-data`?**
- The action is a deletion, so `DELETE` on the user’s data resource is semantically clearer.
- Using `POST` for a destructive, non-idempotent operation without a confirmation flow risks accidental replay and lacks built‑in idempotency. A `DELETE` with an idempotency key is standard; a two‑step flow with a request token is even safer.

**What is missing before any shape can be fixed:**
- **Authentication & Authorization:** Who can call this? (only the user themselves, admins, a system account?) What token format and scopes? Is MFA required for such a high‑risk action?
- **Data retention:** Must data be hard‑deleted, soft‑deleted, or retained for a legal hold? For how long? Does this include backups?
- **Audit policy:** What fields must be logged (who, when, source IP, user‑agent, reason)? Where is the audit trail stored? Is it tamper‑proof?
- **Customer confirmation flow:** How does the application confirm the user’s intent? A confirmation token sent out‑of‑band (email/SMS)? A second factor? A grace period before the deletion executes?
- **Idempotency & safety:** What mechanism prevents accidental duplicate execution? What happens if called while a deletion is in progress?
- **Error semantics:** What status codes for “not authorized”, “token expired”, “deletion already requested”, “data already deleted”?

Until these are decided, I cannot recommend any concrete endpoint contract.

## 3. Key Tradeoffs

| Decision | Option A (simple DELETE) | Option B (asynchronous request + token) | Comments |
|----------|--------------------------|----------------------------------------|----------|
| **User experience** | Immediate deletion, lower friction | Multi‑step, higher friction but explicit confirmation | Option B preferred for irreversible data loss; missing requirements prevent choice. |
| **Safety** | Relies solely on front‑end confirmation; prone to accidental or CSRF‑like triggers | Server‑side token verifies intent; can enforce timeouts and revocation | Without a confirmation flow, the risk of accidental deletion is high. |
| **Idempotency** | DELETE with idempotency key works if state is stable | POST/DELETE combination requires careful state machine | Both require definition of “already deleted” response. |
| **Auditability** | Must be built separately; logging the DELETE call itself may be enough if auth is logged | The request object provides a natural audit event | Audit trail must include both request and execution events. |
| **Retention** | Hard‑delete immediately violates many regulatory requirements | Can add a soft‑delete or hold period before final purge | The requirements must state the legal and business retention policy. |

These tradeoffs cannot be resolved without the missing inputs.

## 4. Risks and Human Gates

### Risks
- **Unrestricted access:** Without an auth model, the endpoint could allow anonymous, unauthorized, or privilege‑escalated deletion of user data.
- **Irreversible data loss:** No retention or backup policy means that once called, data might be unrecoverable, violating GDPR, CCPA, or internal data governance.
- **No audit trail:** Lack of audit makes it impossible to verify who deleted data, when, and why. This is a compliance liability.
- **Accidental execution:** Without a server‑side confirmation token or idempotency key, a network retry, browser refresh, or bug could trigger repeated deletions.
- **Missing observability:** No defined metrics, logging, or status codes make it impossible to monitor the health and usage of this destructive operation.

### Human Gates (Required Before Approval)
This endpoint **cannot be deployed, tested, or committed to a public API** until all of the following are reviewed and signed off by the appropriate humans:

1. **Authentication & Authorization architecture** – review by security team.
2. **Data retention and purge policy** – legal and compliance sign‑off.
3. **Customer confirmation flow** – product and UX approval.
4. **Audit trail design** – security and platform alignment.
5. **Breaking change / versioning decision** – if this replaces an existing process, product must approve the migration and customer communication plan.
6. **Production migration plan** – if data already exists, how is the deletion job executed safely?

Without these, I cannot claim the design is ready.

## 5. Verification Checklist

Once the missing information is supplied and a concrete contract is drafted, the following must be verified:

- [ ] **Auth tests:** Only permitted principals can call the endpoint; unauthorized requests receive `403` or `401`.
- [ ] **Confirmation flow:** End‑to‑end test of request‑token‑confirm lifecycle, including token expiry and reuse attempts.
- [ ] **Idempotency:** Sending the same idempotency key twice (or the same confirmation token) yields the same response and no side‑effect on the second call.
- [ ] **Schema validation:** Request and response payloads are validated against a published OpenAPI schema.
- [ ] **Error handling:** Defined error responses for missing token, expired token, already deleted, rate limit, and server failure.
- [ ] **Audit logging:** Every deletion event (request received, confirmation, execution) is recorded with all required fields and is immutable.
- [ ] **Observability:** Metrics for request rate, success/failure, latency, and alerts on abnormal patterns.
- [ ] **Consumer documentation:** Developer portal includes clear examples of the flow, error scenarios, and rate limits.

**Note:** This checklist is preparatory. No claim is made that the endpoint has been tested or deployed; those activities are impossible without the missing requirements.

---

**Conclusion:** The proposal `POST /users/{id}/delete-all-data` is not approvable as provided. The gaps in authentication, retention, audit, and confirmation are blocking. Resolve those with the relevant human stakeholders, then return with concrete requirements for a full design review.
