<think>The user is asking me to review an API endpoint proposal that has significant missing information. According to the skill instructions, I need to:

1. Define consumers, use cases, and constraints - but these aren't provided
2. Choose API style and model resources or types - partially provided
3. Specify errors, versioning, pagination, and auth strategy - auth is missing
4. Validate with examples and review for consistency

The skill explicitly states: "If information is missing, mark uncertainty" and "Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing."

This is a critical endpoint (delete all user data) that has GDPR, legal, and security implications. The missing auth model is particularly concerning. I should provide a design review that:
1. Identifies what's missing
2. Explains why each missing piece matters
3. Provides guidance on what needs to be defined before this API can be properly designed
4. Offers a preliminary design framework while noting the gaps

Let me structure a comprehensive review.
</think>

# API Design Review: `POST /users/{id}/delete-all-data`

## ⚠️ Critical Gaps Identified

This endpoint proposal has **missing information that blocks proper design**. Before proceeding, the following must be defined:

| Missing Element | Risk Level | Blocking? |
|----------------|------------|-----------|
| Authentication model | **Critical** | Yes |
| Authorization/permissions | **Critical** | Yes |
| Retention requirements | **High** | Yes |
| Audit policy | **High** | Yes |
| Customer confirmation flow | **High** | Yes |
| Idempotency strategy | Medium | No |

---

## 1. Authentication & Authorization (BLOCKING)

**Required before design can proceed:**

```
Who can call this endpoint?
├── End users deleting their own data?
│   └── Requires: OAuth2 with user-scoped tokens
├── Admin/service deleting on behalf of users?
│   └── Requires: Service accounts + role-based access
└── Automated GDPR pipeline?
    └── Requires: API keys + IP allowlist + audit trail
```

**Design questions to resolve:**
- What credential type? (OAuth2, API keys, mTLS, JWT)
- What scopes/permissions are required?
- Is this a self-service endpoint or privileged operation?

---

## 2. Preliminary Resource Model

Assuming the endpoint is approved after gaps are filled:

```
POST /users/{id}/delete-all-data

Request:
{
  "reason": "GDPR_REQUEST" | "USER_REQUEST" | "ACCOUNT_CLOSURE",
  "confirmation_token": "string",  // From prior confirmation step
  "scheduled_purge_date": "2024-02-01"  // Optional delay for grace period
}

Response (202 Accepted):
{
  "request_id": "uuid",
  "status": "SCHEDULED" | "IN_PROGRESS" | "COMPLETED",
  "estimated_completion": "ISO8601",
  "data_categories_affected": ["profile", "orders", "payments", "logs"]
}
```

---

## 3. Missing Requirements That Change Design

### Retention Requirements
- Must data be retained for legal/tax compliance?
- If yes → this becomes a **soft delete** with hidden data
- If no → hard delete with cascade rules needed

### Audit Policy
- Who gets notified?
- What logs are required?
- How long are audit logs retained?

### Confirmation Flow
```
Option A: Two-step confirmation
  POST /users/{id}/delete-all-data/confirm → returns token
  POST /users/{id}/delete-all-data with token

Option B: Email/SMS verification link
  Requires: Email service integration, token TTL

Option C: No confirmation (trusted internal service)
  Requires: Strict network policies
```

---

## 4. Next Steps

**Before this API can be designed, you must obtain:**

1. ☐ Auth model specification (credential type, scopes, rotation policy)
2. ☐ Data retention requirements (legal, tax, compliance)
3. ☐ Audit logging requirements (what, where, how long)
4. ☐ Confirmation flow decision (who confirms, how)
5. ☐ Error handling for partial failures (what if 3 of 5 systems delete but 2 fail?)

---

## Boundary Statement

This review **cannot** provide a complete API specification because:
- The missing auth model is a hard requirement for any production API
- Retention/audit requirements fundamentally change the endpoint behavior
- Without these, implementing this endpoint could violate GDPR, financial regulations, or internal policies

**Recommended action:** Return this proposal to the team with the above checklist for completion.
