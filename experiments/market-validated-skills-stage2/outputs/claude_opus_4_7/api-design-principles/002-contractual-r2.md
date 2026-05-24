# API Design Review: `POST /users/{id}/delete-all-data`

## 1. Design Summary

The proposal is a destructive, customer-impacting operation. The supplied information is insufficient to approve a contract. This review flags the endpoint shape concerns, names the missing inputs required before design can proceed, and proposes a conditional design that can be finalized once those inputs are provided.

**Status:** Cannot finalize. Requires human gates (auth model, data retention policy, audit policy, customer confirmation flow) and product decisions on breaking-change and compatibility implications.

## 2. Proposed API Shape (Conditional / Illustrative)

The current verb-in-path style (`/delete-all-data`) is RPC-flavored. Two REST-aligned alternatives, pending clarification:

**Option A — Resource sub-collection deletion (preferred if "delete all data" maps to a known resource set):**
```
DELETE /users/{id}/data
Headers:
  Authorization: <scheme TBD>
  Idempotency-Key: <client-generated UUID>
  X-Confirmation-Token: <token from prior confirmation step>
Response: 202 Accepted
{
  "deletion_request_id": "<uuid>",
  "status": "pending",
  "estimated_completion": "<ISO-8601, if known>"
}
```

**Option B — Async job resource (preferred if deletion is long-running, auditable, and reversible within a grace period):**
```
POST /users/{id}/data-deletion-requests
Body:
{
  "confirmation_token": "<token>",
  "reason": "<optional enum: user_request | gdpr_erasure | account_closure>"
}
Response: 201 Created
{
  "id": "<uuid>",
  "user_id": "<id>",
  "status": "pending_confirmation | scheduled | in_progress | completed | cancelled",
  "scheduled_for": "<ISO-8601>",
  "cancellable_until": "<ISO-8601>"
}

GET /users/{id}/data-deletion-requests/{request_id}
DELETE /users/{id}/data-deletion-requests/{request_id}   # cancel during grace period
```

Both options are **illustrative** — they are not derived from supplied schemas.

### Issues with the original `POST /users/{id}/delete-all-data`
- Uses a verb in the path instead of an HTTP method semantic.
- `POST` is acceptable for non-idempotent actions but no idempotency key is specified for a destructive write.
- "all data" is undefined — scope must be enumerated (profile, content, billing, logs, backups, derived analytics, third-party shares).
- `{id}` placement implies an admin acting on a user; unclear if the user is the actor.
- No status code, response body, or async contract is defined.

## 3. Key Tradeoffs

| Concern | Option A (DELETE sub-resource) | Option B (deletion-request resource) |
|---|---|---|
| REST clarity | High | High |
| Async / long-running support | Weak | Strong |
| Cancellable grace period | No native model | Native |
| Auditability | Requires side-channel | Built into resource |
| Client complexity | Lower | Higher (polling or webhooks) |

If deletion must be irreversible and immediate, Option A is simpler. If regulatory erasure (e.g., GDPR Article 17) with grace period and audit trail is required, Option B is stronger. **The task does not specify which applies.**

## 4. Risks and Human Gates

### Missing information (must be supplied before approval)
1. **Auth model** — Who can call this? Self-service by user, admin only, support agent with elevated scope, or system-to-system? What scheme (OAuth scopes, session + step-up auth, mTLS)?
2. **Retention requirement** — Hard delete vs. soft delete vs. anonymization. Legal holds. Backup propagation timeline. Cross-region replicas.
3. **Audit policy** — What is logged, who can read audit records, retention of the audit trail itself, immutability requirements.
4. **Customer confirmation flow** — Step-up auth, email/SMS confirmation token, cooling-off window, cancellation window, notification on completion.
5. **Scope of "all data"** — Enumerated list of data domains affected and any excluded categories (e.g., financial records under legal retention).
6. **Idempotency contract** — Required for any destructive write; behavior on retry must be specified.
7. **Rate limiting and abuse prevention** — Especially if user-initiated.
8. **Cascading effects** — Shared resources, team-owned data, content others depend on.

### Required human gates (per Skill)
- **Security review** — auth scheme, sensitive-data exposure, step-up auth, token handling.
- **Legal / compliance review** — retention, GDPR/CCPA erasure semantics, legal hold exceptions.
- **Product approval** — customer-visible behavior, confirmation UX, grace period.
- **Platform standards** — naming convention (`delete-all-data` likely violates REST conventions in most style guides).
- **Breaking-change review** — if this replaces or alters an existing deletion endpoint.

### Risks if shipped as proposed
- Accidental or malicious mass deletion without confirmation.
- Non-compliance with regulatory erasure obligations (under- or over-deletion).
- No rollback path if deletion is synchronous and irreversible.
- Inconsistent semantics with rest of API (verb-in-path).
- Silent partial failure across data domains with no per-domain status.

## 5. Verification Checklist

Before this endpoint can be approved:

- [ ] Auth model documented and reviewed by security.
- [ ] Retention and legal-hold rules documented and reviewed by legal/compliance.
- [ ] Audit log schema and retention defined.
- [ ] Customer confirmation flow (step-up auth + token + grace period) specified end-to-end.
- [ ] Enumerated scope of data domains affected, with explicit exclusions.
- [ ] Idempotency contract specified (`Idempotency-Key` header, replay window, response semantics).
- [ ] Async vs. sync decision made; if async, status resource and terminal states defined.
- [ ] Error model defined for partial failure, unauthorized, already-deleted, in-progress.
- [ ] Rate limits and abuse controls defined.
- [ ] Contract tests cover: unauthorized caller, missing confirmation token, replay with same idempotency key, cancellation within grace window, completion notification.
- [ ] Consumer review with frontend/partner teams.
- [ ] Documentation drafted (not claimed as published).

## Evidence Notes

- **Supplied facts:** endpoint string `POST /users/{id}/delete-all-data`; absence of auth, retention, audit, and confirmation specifications.
- **Inferred:** that this is a destructive, customer-impacting operation likely tied to account deletion or regulatory erasure.
- **Assumptions (flagged):** that REST conventions apply; that the platform supports async job resources and idempotency keys — not confirmed by the task.
- **Examples above are illustrative**, not copied from any provided schema.

## Handoff

- Security: auth scheme and step-up confirmation.
- Legal/compliance: retention and erasure semantics.
- Platform: naming and async-job conventions.
- QA: contract tests for destructive-write semantics.
- Product: confirmation UX and grace period.
- Documentation: developer-facing examples once contract is finalized.
