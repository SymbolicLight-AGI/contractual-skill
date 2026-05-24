# API Design Review: `POST /users/{id}/delete-all-data`

## Summary

This endpoint proposal cannot be approved as-is. Critical inputs are missing, and the surface-level design has issues that should be addressed regardless of those inputs. Below I separate (A) what I can review now, (B) what is blocked pending information, and (C) a recommended revised shape once gaps are filled.

---

## A. Review of what was provided

### 1. HTTP method and path

- **`POST` with a verb in the path (`delete-all-data`)** mixes paradigms. REST conventions favor either:
  - `DELETE /users/{id}/data` (resource-oriented), or
  - `POST /users/{id}/data-deletion-requests` (treating the deletion as a created, trackable resource — strongly preferred for destructive, asynchronous, auditable actions).
- **Recommendation:** Use the second form. Destructive bulk operations should produce a **deletion request resource** with its own `id`, `status`, `requested_at`, `completed_at`. This gives you idempotency, async support, audit trail, and a place to attach confirmation tokens.

### 2. Scope ambiguity — "all data"

- "All data" is undefined. Does it include:
  - Account record itself (hard delete vs. anonymize)?
  - Derived data (logs, analytics, ML features, backups)?
  - Data shared with other users (messages, comments)?
  - Legally retained data (tax, fraud, compliance)?
- **Recommendation:** Define a **data classification** the endpoint operates on, and document explicitly what is *not* deleted and why. Consider an optional `scope` parameter (e.g., `pii_only`, `full_erasure`) if multiple modes are needed.

### 3. Idempotency and safety

- No idempotency key, no confirmation token, no dry-run mode. A destructive endpoint without these is high-risk.
- **Recommendation:** Require an `Idempotency-Key` header and a short-lived `confirmation_token` obtained from a prior step.

### 4. Response contract

- Not specified. For an async deletion this should be `202 Accepted` with a resource representation including a status URL, not `200`/`204`.

---

## B. Blocked pending information (uncertainty marked)

I cannot complete the review without the following. I am **not** going to assume defaults for these, because the wrong assumption is unsafe.

| # | Missing input | Why it blocks review |
|---|---|---|
| 1 | **Auth model** — who can call this? Subject user only? Admin? Service account? OAuth scopes? Step-up auth required? | Determines authorization checks, token requirements, and whether `{id}` may differ from the caller. |
| 2 | **Customer confirmation flow** — email re-auth, MFA challenge, typed confirmation, cooling-off period? | Determines whether the endpoint is single-call or multi-step, and what tokens/parameters it accepts. |
| 3 | **Retention requirements** — legal/regulatory holds (GDPR Art. 17 exceptions, SOX, HIPAA, tax), backup retention windows, soft-delete vs. hard-delete. | Determines what "delete" actually means and what the response should report as retained. |
| 4 | **Audit policy** — what events are logged, where, with what PII redaction, retention of audit logs themselves. | Determines required response fields (e.g., `audit_id`) and side effects. |
| 5 | **Async behavior and SLA** — synchronous, async with status, time-to-completion guarantees. | Determines status codes, polling resource, and webhook/notification needs. |
| 6 | **Reversibility window** — is there a grace period during which the user can cancel? | Determines whether a `DELETE` on the deletion-request resource is needed. |
| 7 | **Rate limiting / abuse model** — could this be weaponized via account takeover? | Determines throttling and step-up auth requirements. |
| 8 | **Consumers** — first-party UI only, partners, public API? | Determines versioning, documentation, and stability commitments. |

---

## C. Recommended next step

Per the skill's process (define consumers and constraints → choose style → specify auth/errors/versioning → validate), the correct next step is **not** to redesign the endpoint yet, but to get answers to the eight items in section B. I suggest the team complete this short questionnaire before resubmitting:

1. Who is authorized to call this, and under what auth scheme and scopes?
2. What confirmation flow precedes the call? What token/proof does the endpoint require?
3. What categories of data are deleted, retained (with legal basis), and anonymized?
4. Sync or async? If async, what is the status-tracking resource?
5. Is there a cancellation window? How long?
6. What audit events fire, and is `audit_id` returned?
7. Rate limits and step-up auth requirements?
8. Public or internal API? Versioning commitment?

### Strawman to react to (non-binding, pending the above)

```
POST /users/{id}/data-deletion-requests
Headers:
  Authorization: Bearer <token with scope: user.data.delete>
  Idempotency-Key: <uuid>
Body:
  {
    "scope": "full_erasure",
    "confirmation_token": "<from prior step-up auth>",
    "reason_code": "user_requested" | "admin_action" | "legal_request"
  }

202 Accepted
{
  "id": "ddr_01H...",
  "status": "pending",
  "scope": "full_erasure",
  "requested_at": "2026-02-27T12:00:00Z",
  "scheduled_completion_at": "2026-03-29T12:00:00Z",
  "cancellable_until": "2026-03-05T12:00:00Z",
  "retained_categories": ["billing_records_7y", "fraud_signals_2y"],
  "audit_id": "aud_01H...",
  "status_url": "/users/{id}/data-deletion-requests/ddr_01H..."
}

Errors: 401, 403, 409 (already pending), 410 (already deleted), 422 (bad confirmation), 429
```

This is offered as a discussion artifact, not a recommendation, until the blocking inputs in section B are supplied.

---

## Boundary note

Concrete decisions on retention windows, legal bases, and audit-log requirements are jurisdiction- and product-specific and require legal/compliance review. This skill covers API contract design; it does not substitute for that review.
