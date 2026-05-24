# Security Review: PATCH /projects/{projectId}/settings

## Scope And Authorization

- Authorized scope: review of the supplied synthetic API design only.
- No tooling, scanning, or live testing performed or requested.
- Material treated as synthetic.

## Executive Summary

The supplied design shows authentication but no visible authorization check binding `projectId` to the caller's organizations. In a multi-tenant model where users belong to multiple organizations, this pattern is a classic Insecure Direct Object Reference (IDOR) / Broken Object-Level Authorization (BOLA) risk. The mutable fields (`billingContactEmail`, `webhookUrl`) raise the business impact, since abuse can enable billing redirection, social-engineering vectors, and webhook hijacking for data exfiltration or SSRF.

## Findings By Severity

### High — Missing project-to-organization authorization check (BOLA / IDOR)
- The handler authenticates the user but does not verify that `projectId` belongs to an organization the user is a member of, nor that the user has a role permitted to modify project settings.
- In a multi-org membership model, any authenticated user could potentially target any `projectId` by guessing or enumerating IDs.

### High — Webhook URL mutation enables SSRF and data exfiltration
- `webhookUrl` is attacker-controllable on success. Without egress restrictions and URL validation, an attacker can:
  - Point webhooks at internal metadata services or internal networks (SSRF).
  - Exfiltrate event payloads to attacker-controlled hosts.
  - Hijack legitimate webhook traffic from the real project owner.

### High — Billing contact email mutation enables account/billing takeover pathway
- Changing `billingContactEmail` can:
  - Redirect invoices, payment notices, and security/billing-related communications.
  - Enable downstream account recovery or social engineering against finance.
  - Cause silent loss of notifications for the legitimate owner.

### Medium — Lack of role/permission granularity (hypothesis)
- Even members of the correct organization may not all be entitled to change billing or webhook settings. No role check is shown.

### Medium — No visible audit logging or change notification (hypothesis)
- Sensitive setting changes typically require an audit trail and out-of-band notification to prior contacts. Not shown in the design.

### Low/Medium — Input validation on `webhookUrl` and `billingContactEmail` (hypothesis)
- No validation shown for scheme (`https` only), host allowlist/denylist, private IP ranges, or email format and domain verification.

## Evidence

- Finding: Handler "checks that the user is logged in" but "does not show an explicit check that the project belongs to one of the user's organizations." (from supplied description).
- Finding: Mutable fields include `billingContactEmail` and `webhookUrl` (from supplied description).
- Hypothesis: Role-based restrictions, audit logging, validation, and egress controls — not described in the supplied material.
- Evidence gap: Actual handler code, middleware chain, ORM/data-access layer (which may enforce scoping), policy engine, and webhook delivery subsystem are not provided.

## Remediation Plan

1. Enforce object-level authorization in the handler (or a shared policy layer):
   - Resolve `projectId` to its owning organization.
   - Verify the authenticated user is a member of that organization.
   - Verify the user's role within that organization permits modifying project settings (and ideally separate roles for billing vs. integration settings).
2. Defense-in-depth at the data layer:
   - Scope all project queries by `(projectId, organizationId IN user.orgs)` so a missing check still fails closed.
3. Webhook URL hardening:
   - Require `https`.
   - Reject private, loopback, link-local, and metadata IP ranges; resolve and re-check after DNS to prevent rebinding.
   - Optional domain allowlist or per-org egress policy.
   - Sign webhook deliveries; require receiver verification (e.g., challenge-response) before activation.
4. Billing contact email hardening:
   - Require email verification (confirmation link) before the change takes effect.
   - Notify the previous `billingContactEmail` and organization owners/admins of the change.
   - Consider step-up authentication (recent re-auth or MFA) for billing changes.
5. Audit and observability:
   - Log who changed what, when, from where, with before/after values (redacted as needed).
   - Emit security events for setting changes on sensitive fields.
6. Rate limiting and enumeration resistance:
   - Return identical 403/404 semantics for "not found" vs. "not authorized" to limit ID enumeration.
   - Apply per-user and per-IP rate limits on settings endpoints.

## Validation Steps

Non-intrusive, design-level checks:

- Code review: confirm the handler (or middleware/policy) resolves project → org and checks membership and role before any write.
- Confirm data-access layer scopes queries by organization.
- Review webhook subsystem for URL validation, egress controls, and signing.
- Review billing change flow for verification email and notifications to prior contacts.
- Review audit log schema and retention for settings mutations.

Any active testing (e.g., attempting cross-tenant PATCH with a test account) requires written authorization and a non-production environment — see Human Gates.

## Residual Risk

- Even with checks added, residual risks remain around:
  - Compromised legitimate user accounts changing settings (mitigated by step-up auth and notifications).
  - Webhook receivers that themselves leak data.
  - Race conditions between authorization check and write (mitigate with transactional scoped updates).
- Confidence is limited because only a design description was provided; implementation may already mitigate some items not visible here.

## Open Questions

- Is there a middleware or policy layer (not shown) that enforces project→organization membership?
- Are there distinct roles for billing vs. integration settings within an organization?
- Does the webhook delivery system have egress restrictions and signing today?
- Is there an existing email-verification flow for billing contact changes?
- Are audit logs already captured for settings changes?

## Handoff

- Engineering / DevSecOps: implement authorization, validation, and audit changes above.
- Product / Billing: confirm UX for billing contact verification and notifications.
- Security leadership: prioritize the High findings; consider this an authorization-class issue affecting tenant isolation.
- No external disclosure is recommended at this stage; this is a synthetic design review and not a confirmed production vulnerability.
