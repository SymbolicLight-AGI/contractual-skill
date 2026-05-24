# Security Review: `PATCH /projects/{projectId}/settings`

## Scope And Authorization

- Authorized scope: review the supplied synthetic API design only.
- No tools, scans, or intrusive tests requested or permitted.
- Material treated as synthetic.

## Executive Summary

The supplied design shows authentication but no explicit project-to-organization authorization check. As described, the endpoint is exposed to **Insecure Direct Object Reference (IDOR)** and **cross-tenant privilege escalation**, with material business impact via `billingContactEmail` (financial/communications redirection) and `webhookUrl` (data exfiltration and SSRF pivot). Severity: **High**.

## Findings By Severity

### F1 — High: Missing project-to-organization authorization (IDOR / broken object-level authorization)
- **Type:** Finding (based on supplied description that no explicit project-ownership check exists).
- **Impact:** Any authenticated user could modify settings of any project by guessing or enumerating `projectId`, even across organizations they do not belong to.
- **Likelihood:** High once an attacker has any valid account; `projectId` values are often enumerable or leaked.

### F2 — High: Sensitive field `billingContactEmail` mutable without scoped authorization
- **Type:** Finding (impact analysis of F1).
- **Impact:** Redirecting billing contact can enable invoice fraud, account takeover via billing-channel password resets, and social engineering of finance staff.

### F3 — High: `webhookUrl` mutable without scoped authorization
- **Type:** Finding (impact analysis of F1).
- **Impact:** Attacker-controlled webhook can:
  - Exfiltrate event payloads (potentially PII, secrets, tokens in event bodies).
  - Be pointed at internal addresses (e.g., `169.254.169.254`, `localhost`, RFC1918) to attempt **SSRF** against cloud metadata or internal services if outbound calls are not restricted.
  - Be set to a malicious endpoint for downstream phishing or payload injection.

### F4 — Hypothesis: Multi-organization context not bound to the request
- **Type:** Hypothesis.
- **Detail:** Because users can belong to multiple organizations, the handler likely needs an explicit `organizationId` context (header, claim, or derived from the project) plus a membership and role check. Not visible in the supplied design.

### F5 — Hypothesis: No role/permission tier within an organization
- **Type:** Hypothesis.
- **Detail:** Even members of the correct organization should likely require an elevated role (e.g., `owner`, `admin`, `billing_admin`) to change billing or webhook settings. Not shown.

### F6 — Hypothesis: Audit logging and change notification
- **Type:** Hypothesis / Evidence gap.
- **Detail:** Changes to billing contact and webhook URL should produce audit log entries and out-of-band notifications to existing admins/billing contacts to detect abuse. Not shown.

### F7 — Hypothesis: Webhook URL validation
- **Type:** Hypothesis.
- **Detail:** No indication of allowlist scheme (`https` only), DNS/IP filtering (block private ranges, metadata IPs), or signature/secret rotation when URL changes.

## Evidence

- Supplied: endpoint path, auth state (logged-in only), absence of explicit project-ownership check, mutable fields `billingContactEmail` and `webhookUrl`, multi-org user model.
- **Evidence gaps:**
  - Handler source code.
  - Middleware or framework-level authorization (e.g., policy decorators, row-level security).
  - Identity claims structure (does the token carry org memberships and roles?).
  - Webhook delivery design and URL validation logic.
  - Audit logging configuration.

## Remediation Plan

1. **Enforce object-level authorization (fixes F1–F3):**
   - In the handler, load the project by `projectId`, read its `organizationId`, and verify the authenticated user has an active membership in that organization.
   - Fail closed with `404` (preferred, to avoid existence disclosure) or `403` on mismatch.
2. **Require elevated role for sensitive fields (F5):**
   - Gate `billingContactEmail` behind a `billing_admin`/`owner` role.
   - Gate `webhookUrl` behind an `admin`/`owner` role.
3. **Centralize authorization:**
   - Use a policy/middleware layer (e.g., per-route policy, ABAC/RBAC helper) so authorization is not left to individual handlers.
   - Consider database-level guards (row-level security or scoped queries that always filter by `organizationId` derived from the session).
4. **Webhook URL hardening (F7):**
   - Enforce `https://` only.
   - Reject private, loopback, link-local, and cloud metadata addresses at validation and at delivery time (re-resolve DNS at send).
   - Require the caller to prove control of the URL (challenge/verification) before activation.
   - Rotate the webhook signing secret on URL change.
5. **Audit and notify (F6):**
   - Append audit log entries with actor, project, org, old/new values (with sensitive values masked).
   - Send confirmation emails to the prior `billingContactEmail` and existing org admins on change.
6. **Defense in depth:**
   - Rate-limit settings changes per user/org.
   - Add anomaly detection on rapid webhook or billing changes.

## Validation Steps

All steps assume a **non-production, authorized test environment** with synthetic data.

1. As user A in org X, create project P in org X.
2. As user B in org Y (no membership in X), call `PATCH /projects/{P}/settings` with a new `webhookUrl`. Expected: `403` or `404`, no state change, audit entry for denied attempt.
3. As user B (org X member, non-admin role), attempt the same call. Expected: denial based on role policy.
4. As user A (org X admin), perform the change. Expected: success, audit log entry, notification to prior billing contact and admins.
5. Submit `webhookUrl` values pointing at `http://`, `http://127.0.0.1`, `http://169.254.169.254`, and a private IP. Expected: rejected at validation; if accepted in validation, rejected at delivery.
6. Confirm responses do not disclose project existence to unauthorized users (consistent `404`).

## Residual Risk

- Even with object-level checks, **organization membership churn** (a user removed from an org with cached tokens) can leave a short window of access. Mitigate with short token TTLs or session invalidation on membership change.
- Webhook delivery to attacker-influenced but technically-public hosts remains a data-handling concern; payload minimization and per-event consent reduce blast radius.
- Audit logging is detective, not preventive; assume some abuse may occur before alerts fire.

## Open Questions

1. Where is authorization expected to live: handler, middleware, or database layer?
2. Do auth claims include org memberships and roles, or must the handler look them up?
3. Is there a defined role model for project settings (who may edit billing vs. webhook)?
4. Are there existing webhook URL validation and SSRF protections?
5. Is audit logging in place for settings changes?
6. Is `projectId` a guessable integer or an unguessable identifier (e.g., UUID)? (Reduces enumeration risk but does not substitute for authorization.)

## Handoff

- **Engineering / DevSecOps:** Implement object-level authorization, role gating, and webhook hardening.
- **Security leadership:** Review the broader pattern across other `/{resourceId}/...` endpoints for similar IDOR exposure.
- **Compliance owner:** If billing data or PII is in scope, evaluate audit logging and notification requirements against applicable frameworks. No certification claim is made here.

---

**Notes on boundaries:** This review is limited to the supplied synthetic design. No testing was performed. Any intrusive verification (including the validation steps above) requires written authorization and a non-production environment.
