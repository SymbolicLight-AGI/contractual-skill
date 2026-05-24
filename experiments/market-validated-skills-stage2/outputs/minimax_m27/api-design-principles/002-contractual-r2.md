<think>The user is asking me to review an API endpoint proposal using the "api-design-principles-contractual" skill. The task is to review `POST /users/{id}/delete-all-data` where the team has not provided auth model, retention requirement, audit policy, or customer confirmation flow.

Let me follow the skill workflow:

1. Identify resources, actions, consumers, and lifecycle states
2. Separate public API contract, internal implementation, and migration concerns
3. Evaluate naming, methods, status codes, schema shape, errors, pagination, filtering, idempotency, and versioning
4. Recommend a design or compare alternatives with tradeoffs
5. Include examples only when they can be derived from the task
6. Surface security, compatibility, observability, and operational risks
7. Define verification criteria

The output format requested is:
1. Design summary
2. Proposed API shape
3. Key tradeoffs
4. Risks and human gates
5. Verification checklist

Let me structure this properly, noting what information is missing and what needs to be defined before implementation.
</think>

# API Design Review: `POST /users/{id}/delete-all-data`

## 1. Design Summary

The proposed endpoint targets a high-stakes data deletion operation with significant legal, security, and operational implications. The current proposal is **incomplete**—critical contract elements are missing, making implementation, review, and consumer onboarding unsafe.

**Verdict:** Do not approve for implementation until the gaps identified below are resolved.

---

## 2. Proposed API Shape

> **Note:** The following is a *proposed contract skeleton* based on standard patterns. Actual schema fields depend on missing requirements.

### Endpoint

```
POST /users/{id}/delete-all-data
```

### Request

| Element | Status | Required |
|---------|--------|----------|
| Path param `id` | Defined | Yes |
| Request body | **Missing** | TBD |
| Auth header | **Missing** | Required |
| Idempotency key | **Missing** | Recommended |
| Confirmation token | **Missing** | Likely required |

### Response

| Status Code | Scenario | Body |
|-------------|----------|------|
| `202 Accepted` | Deletion queued | `{ "job_id": "...", "status": "queued", "estimated_completion": "..." }` |
| `400 Bad Request` | Missing confirmation | `{ "error": "confirmation_required", "message": "..." }` |
| `401 Unauthorized` | Auth missing/invalid | `{ "error": "unauthorized" }` |
| `403 Forbidden` | Insufficient permissions | `{ "error": "forbidden" }` |
| `404 Not Found` | User not found | `{ "error": "not_found" }` |
| `409 Conflict` | Deletion already in progress | `{ "error": "already_pending", "existing_job_id": "..." }` |
| `429 Too Many Requests` | Rate limited | `{ "error": "rate_limited", "retry_after": 3600 }` |

### Illustrative Response (202)

```json
{
  "job_id": "del_abc123",
  "user_id": "user_456",
  "status": "queued",
  "requested_at": "2025-01-15T10:30:00Z",
  "requested_by": "admin_789",
  "estimated_completion": "2025-01-15T12:30:00Z",
  "data_categories": ["profile", "orders", "payments", "support_tickets"],
  "retention_exception": null
}
```

---

## 3. Key Tradeoffs

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|-----------------|
| **Trigger model** | Immediate deletion | Async job with confirmation | **Option B** — Irreversible action requires confirmation flow |
| **Idempotency** | Return 200 for repeat requests | Return 409 if deletion in progress | **409 Conflict** — Consumer must handle job tracking |
| **Scope** | Delete all data | Allow selective deletion | **Defer** — Requires product decision on partial deletion use cases |
| **Retention** | Immediate purge | Time-delayed purge (e.g., 30-day legal hold) | **TBD** — Legal/compliance must define |
| **Audit** | Log to file | Structured audit log with PII | **Structured audit log** — Required for GDPR/SOC2 |
| **Notification** | No notification | Email/webhook on completion | **Webhook** — Async consumers need completion signal |

---

## 4. Risks and Human Gates

### Critical Gaps (Block Implementation)

| Gap | Risk if Unresolved | Required Action |
|-----|-------------------|-----------------|
| **Auth model** | Unauthorized deletion, data breach, compliance violation | Define who can call this endpoint (user self, admin, system). Specify required scopes/roles. |
| **Retention policy** | Legal non-compliance, inability to recover erroneous deletions | Legal/privacy team must define mandatory retention periods (e.g., tax records, active disputes). |
| **Confirmation flow** | Accidental or coerced deletion | Product must define: explicit user consent, admin justification field, or MFA step. |
| **Audit policy** | Inability to prove compliance during audit | Define what is logged, for how long, and who can access logs. |

### Security Risks

- **Privilege escalation:** Without role-based access, any authenticated caller could delete any user.
- **Enumeration:** `id` parameter may allow iterating over user IDs to mass-delete.
- **Timing attacks:** Response timing differences could reveal whether a user exists.
- **Replay/accidental retry:** No idempotency key means retry could trigger duplicate deletion requests.

### Operational Risks

- **Cascading deletes:** Deleting "all data" may orphan records in other services (orders, invoices) or violate referential integrity.
- **Long-running operation:** Deletion across multiple data stores may take hours; consumers need job status tracking.
- **Rollback impossibility:** Once executed, data cannot be recovered unless retention is implemented.

### Human Gates Required

| Gate | Owner | Condition |
|------|-------|-----------|
| Auth model approval | Security team | Define roles, scopes, and ownership chain |
| Retention policy sign-off | Legal / Privacy | Confirm legal hold periods per data category |
| Confirmation flow design | Product + Legal | Customer-facing confirmation UX and legal text |
| Audit schema review | Compliance | Confirm audit log fields meet regulatory requirements |
| Breaking change review | API governance | If this replaces an existing deletion endpoint |

---

## 5. Verification Checklist

Before this endpoint is approved for implementation, verify:

### Contract Completeness
- [ ] Auth model defined (who can call, required scopes/roles)
- [ ] Request body schema documented (confirmation token, justification, idempotency key)
- [ ] Response schema documented for all status codes
- [ ] Error schema consistent with existing API error conventions

### Security
- [ ] Auth boundary enforced (no bypass paths)
- [ ] Rate limiting defined to prevent abuse
- [ ] Idempotency key supported to prevent duplicate execution
- [ ] Input validation on `id` (type, format, range)
- [ ] Audit log captures: caller identity, target user, timestamp, result

### Compliance
- [ ] Retention policy documented and technically enforced
- [ ] Confirmation flow implemented (user consent or admin justification)
- [ ] Data categories to be deleted enumerated
- [ ] Notification mechanism defined (completion webhook or email)

### Observability
- [ ] Job status endpoint available (`GET /users/{id}/deletion-jobs/{job_id}`)
- [ ] Metrics defined (deletion requests, completion rate, duration)
- [ ] Alerting configured for bulk deletion anomalies

### Consumer Experience
- [ ] SDK support planned (not just REST)
- [ ] Developer documentation drafted
- [ ] Migration path defined if replacing existing deletion mechanism

---

## 6. Recommended Next Steps

1. **Escalate to Security** for auth model definition.
2. **Escalate to Legal/Privacy** for retention requirements and confirmation flow.
3. **Escalate to Product** for data category scope and customer-facing UX.
4. **Return to API team** with answers to the above before re-submitting for review.
5. **Consider splitting** into two endpoints: `POST /users/{id}/deletion-requests` (initiate) and `GET /users/{id}/deletion-requests/{job_id}` (status) to support async workflow.

---

*This review identifies missing information but does not approve, deploy, or test the endpoint. All human gates must be completed before implementation proceeds.*
