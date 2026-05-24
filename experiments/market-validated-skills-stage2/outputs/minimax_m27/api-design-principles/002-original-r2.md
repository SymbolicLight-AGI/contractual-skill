# API Design Review: `POST /users/{id}/delete-all-data`

## 🚨 Critical Gaps — Cannot Proceed Without Resolution

This endpoint performs irreversible, high-impact data deletion. The following elements are **mandatory** before acceptance:

---

### 1. Authentication & Authorization Model

| Gap | Risk | Required Definition |
|-----|------|---------------------|
| Auth mechanism not specified | Unauthorized deletion | Bearer token? API key? Service-to-service JWT? |
| Authorization scope not defined | Privilege escalation | Who can call this? Only the user themselves? Admins? System processes? |
| Cross-user deletion not addressed | Data isolation breach | Can User A delete User B's data? Must be explicitly prohibited or carefully gated. |

**Required:** Define who is authorized and how they authenticate.

---

### 2. Retention Requirement

| Gap | Risk | Required Definition |
|-----|------|---------------------|
| Data retention before deletion | Compliance violation | Must retained backups/logs be purged? On what timeline? |
| Third-party sync data not addressed | Data remnants | What happens to data replicated to external systems (analytics, email providers)? |

**Required:** Specify retention policy for backups, logs, and synced copies.

---

### 3. Audit Policy

| Gap | Risk | Required Definition |
|-----|------|---------------------|
| Deletion logging not specified | Non-repudiation | Must every deletion be logged with actor, timestamp, scope? |
| Audit log retention | Audit trail gaps | How long are deletion events retained? |

**Required:** Define audit event schema and retention period.

---

### 4. Customer Confirmation Flow

| Gap | Risk | Required Definition |
|-----|------|---------------------|
| Confirmation mechanism missing | Accidental deletion | How does the user confirm intent? (e.g., secondary confirmation token, typed phrase) |
| Rollback capability not defined | Irrevocable harm | Is any rollback window required? What's the state after deletion? |

**Required:** Define a confirmation mechanism and understand deletion finality.

---

## Revised Endpoint Proposal Template

Until gaps are resolved, this endpoint should be held. Below is the **minimum required spec** for a valid proposal:

```yaml
POST /users/{id}/delete-all-data

Security:
  authentication: REQUIRED
  authorization:
    - Self: user can delete own data
    - Admin: requires elevated role + audit reason
  confirmation_flow: "User must confirm with secondary token (TOTP or email link)"

Compliance:
  retention:
    backups: 90 days (then purged)
    audit_logs: 7 years
  third_party_sync: "Deletion request sent to all registered integrations"
  
Behavior:
  idempotency: POST with Idempotency-Key returns same response
  response: 202 Accepted (async) or 204 No Content (sync)
  rollback: NONE — operation is final
  
Errors:
  401 Unauthorized — invalid/missing auth
  403 Forbidden — attempting cross-user deletion
  409 Conflict — confirmation token expired or invalid
  422 Unprocessable Entity — missing required confirmation
```

---

## Next Steps

1. **Request the following from the proposing team:**
   - Auth model diagram (who calls this, with what credentials)
   - Retention policy document or compliance requirement
   - Audit logging schema
   - User confirmation UX flow

2. **Consider architectural implications:**
   - Is this synchronous deletion or async job? (Async preferred for large datasets)
   - Is this a hard delete or soft delete with scheduled purge?

3. **Escalate if needed:** If the team cannot provide auth and compliance requirements, this endpoint should not be implemented.

---

## Boundary Statement

I have **paused design review** at the specification stage because proceeding without auth, retention, and audit definitions would result in a non-compliant, unsafe endpoint. The correct next step is to **request the missing information before further design work** occurs.
