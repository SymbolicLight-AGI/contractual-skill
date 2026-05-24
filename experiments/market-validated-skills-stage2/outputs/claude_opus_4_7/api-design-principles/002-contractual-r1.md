# API Design Review: `POST /users/{id}/delete-all-data`

## 1. Design Summary

The proposed endpoint performs a high-impact, likely irreversible destructive action on user-scoped data. The proposal is missing critical inputs (auth model, retention policy, audit, confirmation flow) that are required before any contract can be finalized. This review flags the gaps, evaluates the surface that is visible, and identifies human gates that must be cleared before implementation.

**Supplied facts:** Endpoint shape `POST /users/{id}/delete-all-data`.
**Everything else below is inferred, an assumption, or a flagged gap.**

## 2. Proposed API Shape (Provisional)

Because the auth model and confirmation flow are unspecified, the shape below is illustrative only and contingent on the open questions in §4.

```
POST /users/{id}/data-deletions
```

Rationale for the shape change (illustrative, pending team decision):

- **Resource-oriented naming.** `delete-all-data` is an RPC verb in the path. Modeling the destructive action as a `data-deletion` resource gives it a lifecycle (requested → confirmed → executing → completed → failed), an ID for audit, and a natural place to attach status polling.
- **POST creates a deletion request, not the deletion itself.** This separates "intent to delete" from "irreversible execution," which is necessary for confirmation and audit.
- **Path uses `{id}` as supplied.** Whether this is a user UUID, external ID, or tenant-scoped ID is unspecified — flagged.

Illustrative request:

```http
POST /users/{id}/data-deletions
Idempotency-Key: <client-generated-uuid>
Content-Type: application/json

{
  "reason": "user_request" | "gdpr_erasure" | "admin_action",
  "confirmation_token": "<token from prior challenge step>",
  "scope": "all" | ["profile", "activity", "billing"]
}
```

Illustrative response (`202 Accepted`):

```json
{
  "deletion_id": "del_...",
  "status": "pending_execution",
  "user_id": "...",
  "scope": "all",
  "requested_at": "...",
  "estimated_completion": "...",
  "audit_event_id": "..."
}
```

Companion endpoints (illustrative):
- `GET /users/{id}/data-deletions/{deletion_id}` — status.
- `GET /users/{id}/data-deletions` — history (subject to access policy).

## 3. Key Tradeoffs

| Decision | Option A | Option B | Notes |
|---|---|---|---|
| Verb in path vs. resource | `POST /users/{id}/delete-all-data` (clear intent, RPC-ish) | `POST /users/{id}/data-deletions` (resource lifecycle, audit-friendly) | B is preferred for destructive ops needing audit + status. Team must decide. |
| Sync vs. async | `200` on completion | `202` + status resource | For "delete all data," async is almost always correct; depends on data volume — unspecified. |
| Soft vs. hard delete | Tombstone + retention window | Immediate purge | Driven by retention/legal policy, which is **not supplied**. |
| Scope granularity | All-or-nothing | Selectable scopes | Depends on product/compliance requirements — unspecified. |

## 4. Missing Information (Blocking)

The following must be answered by the team before the contract can be finalized. Each is a blocker, not a nit.

1. **Auth model.** Who can call this? Options: end-user with session + step-up auth; admin with elevated role; service-to-service with signed request; compliance/legal tool. Each implies a different permission check, error model, and rate limit posture. **Cannot design status codes (401/403) or scopes without this.**
2. **Caller-vs-subject relationship.** Can a user only delete their own data (`{id}` must equal authenticated subject), or can admins act on behalf of users? Determines whether `403` semantics differ from `404`, and whether the path should even expose `{id}` to non-admin callers.
3. **Confirmation flow.** Destructive, irreversible actions should require a confirmation step (re-auth, emailed token, typed phrase, or a two-step `prepare` → `confirm` API). None is specified.
4. **Retention and reversibility.** Is there a grace period (e.g., 30-day soft delete) or immediate hard delete? Legal/GDPR/contractual obligations are unknown. This changes the resource model (status states) and the response.
5. **Audit policy.** What is logged, where, with what retention, and who can read it? Affects whether a `deletion_id` and `audit_event_id` are returned, and whether deletion history is itself queryable.
6. **Scope of "all data."** Profile, activity, billing, backups, derived/aggregated data, third-party processors? Without a defined scope, the contract cannot make a truthful promise.
7. **Downstream propagation.** Search indexes, caches, data warehouses, partner systems, backups. Async completion semantics depend on this.
8. **Idempotency semantics.** Should repeat calls return the original deletion record, or `409 Conflict`, or `202` with the existing `deletion_id`? Recommended: idempotency key returns the original resource.
9. **Rate limiting / abuse.** Account takeover + deletion is a high-impact attack. Rate limits and anomaly detection are unspecified.
10. **Versioning policy.** Existing API versioning convention is not supplied; cannot align.

## 5. Risks

- **Security.** Without an auth model, this endpoint is a destructive primitive with no defined access control. Treat as high-risk until specified.
- **Compliance.** "Delete all data" implicates GDPR Art. 17, CCPA, and contractual data-retention obligations. A wrong contract here creates legal exposure. Requires legal/privacy review.
- **Irreversibility.** No confirmation flow means a single successful request — including one from a compromised session or a buggy client — destroys user data.
- **Observability.** No audit policy means destructive actions may be untraceable. Unacceptable for this class of operation.
- **Backward compatibility.** Unknown — no existing conventions supplied.
- **Naming inconsistency.** `delete-all-data` mixes a verb into a path that elsewhere presumably uses resources. Flagged but secondary.

## 6. Human Gates (Required Before Implementation)

Per Skill policy, the following require human approval and cannot be resolved in this review:

- **Security / IAM:** auth model, scopes, step-up auth, admin-on-behalf-of rules.
- **Legal / Privacy:** retention window, scope of "all data," lawful basis, audit retention.
- **Product:** customer confirmation UX, reversibility window, partner/downstream notification.
- **Platform:** versioning, rate limiting, naming convention alignment.
- **Any breaking change** to existing user-deletion behavior, if one exists.

## 7. Verification Checklist

Before this endpoint can be considered designed (not deployed — see boundary below):

- [ ] Auth model documented; 401/403/404 semantics defined and distinguishable only where safe.
- [ ] Confirmation flow specified (token, step-up auth, or two-step API).
- [ ] Retention/reversibility policy documented and reflected in status states.
- [ ] Scope of deletion enumerated, including downstream systems and backups.
- [ ] Audit event schema defined; audit storage and access policy approved.
- [ ] Idempotency-Key behavior specified and tested.
- [ ] Rate limit and abuse-detection posture defined.
- [ ] Async status resource and terminal states defined.
- [ ] Error model aligned with existing API conventions (not supplied — flag).
- [ ] Contract tests cover: unauthorized caller, wrong subject, repeated idempotent call, in-progress conflict, partial failure.
- [ ] Legal/privacy sign-off recorded.
- [ ] Consumer review (frontend, partner, support tooling) completed.

## 8. Boundary Note

This review proposes contract shape only. Per Skill permissions: no code has been changed, no documentation published, no tests run, and no deployment performed. All example payloads above are **illustrative**, derived from general API design practice, not from any schema supplied in the task. Finalization requires the human gates in §6 to be cleared and the missing information in §4 to be supplied by the team.

**Recommended next step:** Return this review to the proposing team with §4 as a questionnaire; route §6 items to security, legal/privacy, and product owners in parallel.
