<think>The user is asking me to review an endpoint proposal (`POST /users/{id}/delete-all-data`) where critical information is missing: auth model, retention requirement, audit policy, and customer confirmation flow.

According to the Skill under test, I need to:
1. Identify resources, actions, consumers, and lifecycle states
2. Separate public API contract, internal implementation, and migration concerns
3. Evaluate naming, methods, status codes, schema shape, errors, pagination, filtering, idempotency, and versioning
4. Recommend a design or compare alternatives with tradeoffs
5. Include examples only when they can be derived from the task
6. Surface security, compatibility, observability, and operational risks
7. Define verification criteria

The output format should be:
1. Design summary
2. Proposed API shape
3. Key tradeoffs
4. Risks and human gates
5. Verification checklist

I need to be careful to:
- Mark uncertainty where information is missing
- State boundaries and correct next steps
- Not assume hidden business rules or data models
- Not recommend unsafe exposure of sensitive fields
- Not ignore backward compatibility, idempotency, error semantics, or observability
- Distinguish supplied facts, inferred design choices, assumptions, and risks

Let me structure this review properly.
</think>

# API Design Review: `POST /users/{id}/delete-all-data`

---

## 1. Design Summary

**Endpoint Proposal:** `POST /users/{id}/delete-all-data`

**Status:** ❌ **Insufficient for approval** — Critical contract elements are undefined.

The proposal addresses a legitimate GDPR/privacy use case (right to erasure), but the current shape lacks the safeguards, clarity, and observability required for a destructive, customer-facing operation.

---

## 2. Proposed API Shape

> **Note:** The following is a *recommended contract* based on standard API design principles. It is **not** derived from supplied requirements and should be validated against actual product and compliance needs.

### Recommended Contract

```
POST /users/{id}/data-deletion-requests
Content-Type: application/json
Authorization: Bearer <token>  ← REQUIRED: define auth model

Request Body:
{
  "reason": "gdpr_request" | "user_request" | "account_closure",
  "confirmation_token": "<opaque_confirmation_token>",  ← REQUIRED: customer confirmation
  "idempotency_key": "<uuid>"  ← REQUIRED: prevent duplicate processing
}

Response (202 Accepted):
{
  "deletion_request_id": "dr_abc123",
  "status": "pending",
  "estimated_completion": "2024-01-15T12:00:00Z",
  "resources_affected": ["profile", "orders", "sessions", "logs"],
  "retention_notes": "Legal records retained for 7 years per policy X"
}

GET /users/{id}/data-deletion-requests/{request_id}
→ Returns status, completion percentage, affected resources
```

### What Changed and Why

| Original Proposal | Recommended Change | Rationale |
|-------------------|-------------------|-----------|
| `POST /users/{id}/delete-all-data` | `POST /users/{id}/data-deletion-requests` | Noun-based; supports async workflow and status tracking |
| Immediate deletion | Async request/confirm workflow | Allows customer confirmation, audit trail, and rollback window |
| No idempotency | `idempotency_key` required | Prevents accidental or malicious duplicate deletions |
| No auth specified | Bearer token required | Destructive action requires explicit authorization |
| No response schema | Structured 202 response | Enables polling and observability |

---

## 3. Key Tradeoffs

| Decision | Tradeoff |
|----------|----------|
| **Async vs. Sync deletion** | Async allows confirmation flow and rollback window, but adds complexity. Sync is simpler but cannot support confirmation or staged deletion. |
| **Idempotency key** | Prevents duplicates but requires client-side UUID generation. Without it, retries are dangerous. |
| **Retention exceptions** | Some data (e.g., financial records) may be legally required to persist beyond deletion. This must be explicit in the response. |
| **Soft delete vs. hard delete** | Soft delete enables recovery but leaves data at risk. Hard delete is irreversible. The contract should specify or allow per-resource choice. |
| **Confirmation token** | Adds friction but prevents accidental or unauthorized deletion. Consider email/SMS verification as a second factor. |

---

## 4. Risks and Human Gates

### 🔴 Critical Risks (Require Human Approval)

| Risk | Description | Required Action |
|------|-------------|-----------------|
| **Auth boundary undefined** | Without an auth model, the endpoint could be callable by anyone with a user ID. | Define who can trigger deletion: the user themselves, an admin, a system process? |
| **No customer confirmation** | Deleting all user data without explicit confirmation violates GDPR consent principles and exposes legal liability. | Implement a confirmation token or two-phase flow. |
| **Audit policy missing** | Deletion events must be logged for compliance (GDPR Article 5(2), SOC 2). | Define what is logged, for how long, and who can access logs. |
| **Retention requirements undefined** | Some data may be legally required to be retained (tax records, safety logs). | Define retention policy per data category. |

### 🟡 Design Risks

| Risk | Description |
|------|-------------|
| **Idempotency not enforced** | Network retries could trigger multiple deletions. |
| **No status visibility** | Without a GET endpoint, consumers cannot verify deletion progress. |
| **No versioning** | Future changes to deletion scope could break integrations. |
| **Cascading effects unclear** | Deleting "all data" may affect related entities (shared orders, team memberships). Define scope explicitly. |

### Human Gates Required

- [ ] **Security review** — Auth model and authorization scope
- [ ] **Legal/compliance review** — Retention policy and audit requirements
- [ ] **Product review** — Customer confirmation flow and UX
- [ ] **Platform review** — Standards alignment and operational readiness

---

## 5. Verification Checklist

Before this endpoint can be approved for implementation, the following must be confirmed:

### Contract Completeness
- [ ] Auth model defined (who can call this endpoint and under what conditions)
- [ ] Customer confirmation flow specified (email link, MFA, explicit consent)
- [ ] Idempotency mechanism defined (idempotency key or equivalent)
- [ ] Response schema documented (202 response with request ID and status)
- [ ] Error semantics defined (401, 403, 404, 409, 429)
- [ ] Retention policy per data category documented

### Operational Readiness
- [ ] Audit log schema defined (who, what, when, outcome)
- [ ] Rollback/recovery procedure documented
- [ ] Rate limits defined
- [ ] Monitoring/alerting for deletion spikes defined

### Consumer Clarity
- [ ] Scope of deletion explicitly documented (what data is and is not deleted)
- [ ] Estimated completion time communicated
- [ ] Post-deletion behavior documented (user account status, re-registration policy)

### Compatibility
- [ ] Versioning strategy defined
- [ ] Migration path for existing integrations documented

---

## Next Steps

1. **Return to team** with this review and request the missing information (auth model, retention policy, audit policy, confirmation flow).
2. **Do not approve deployment** until all 🔴 critical risks are resolved.
3. **Engage security** for auth boundary definition.
4. **Engage legal/compliance** for retention and audit requirements.
5. **Update endpoint proposal** with resolved details before re-submission.

---

*This review identifies gaps but does not assume business rules or data models not provided. All recommendations are based on standard API design principles and GDPR compliance best practices.*
