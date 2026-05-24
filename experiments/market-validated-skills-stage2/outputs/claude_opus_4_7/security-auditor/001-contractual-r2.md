# Security Audit: API Authorization Review

## Scope And Authorization

- Authorization: Implicit — synthetic pattern provided by user for review.
- Scope: Single API endpoint pattern `GET /accounts/{accountId}/reports`.
- Environment: Synthetic / illustrative. No live testing performed or requested.
- Compliance: None specified. Note: billing and email data may trigger PCI-adjacent, GDPR, or CCPA considerations depending on real deployment.

## Executive Summary

The endpoint pattern exhibits a classic **Insecure Direct Object Reference (IDOR) / Broken Object Level Authorization (BOLA)** flaw — OWASP API Security Top 10 #1. Authentication alone is enforced; authorization to the specific `accountId` resource is not. Any authenticated user can likely enumerate `accountId` values and retrieve billing totals and user emails belonging to other tenants.

Severity: **High** (Critical in a multi-tenant production setting).

## Findings By Severity

### High — Missing Object-Level Authorization (BOLA / IDOR)

- **Type:** Finding (based on the supplied description).
- **Impact:** Cross-tenant disclosure of billing totals (financial data) and user emails (PII). Enables targeted phishing, competitive intelligence harvesting, and potential regulatory exposure (GDPR Art. 32, CCPA, contractual confidentiality).
- **Likelihood:** High. `accountId` values are typically sequential or guessable; even when opaque (UUIDs), they often leak via referrers, logs, support tickets, or prior compromises.
- **Attack path:** Authenticated attacker iterates or substitutes `accountId` → server returns reports for accounts they do not belong to.

### Medium — Sensitive Data in Report Payload

- **Type:** Finding.
- **Impact:** Reports combine financial (billing totals) and identity (emails) data in a single response. This amplifies the blast radius of any authorization bug and increases logging-leak and cache-leak risk.
- **Likelihood:** Conditional on the above finding or other disclosure paths.

### Hypothesis — Missing Audit Logging and Anomaly Detection

- **Type:** Hypothesis (no logging evidence provided).
- **Impact:** Without per-access audit trails, enumeration attacks may go undetected and post-incident forensics will be incomplete.

### Hypothesis — Enumerable Identifiers

- **Type:** Hypothesis.
- If `accountId` is an integer or short sequential value, enumeration is trivial. UUIDv4 or other opaque, non-sequential identifiers reduce (but do not eliminate) this risk.

## Evidence

- Supplied: "checks that the user is logged in but does not check account membership."
- Supplied: response contains "billing totals and user emails."
- Not supplied: source code, framework, middleware chain, identifier format, logging configuration, rate limiting, WAF rules, or tenancy model.

## Remediation Plan

1. **Enforce object-level authorization.** Before returning reports, verify the authenticated principal has an active membership/role on `accountId`. Implement as a centralized authorization check (policy middleware, decorator, or guard) — not ad-hoc per route.
   - Example (pseudocode):
     ```
     require_membership(user=current_user, account_id=accountId, role_in={"viewer","admin","owner"})
     ```
2. **Apply deny-by-default.** Route handlers should fail closed if no explicit policy decision is made.
3. **Use opaque, non-sequential identifiers** (UUIDv4/ULID) for `accountId` to reduce trivial enumeration. This is defense-in-depth, not a substitute for authorization.
4. **Return `404 Not Found` rather than `403 Forbidden`** for unauthorized access to avoid confirming existence of accounts (or use a uniform error policy).
5. **Minimize data in reports.** Consider separating billing data from emails; gate email exposure behind a higher-privilege role; mask emails where full disclosure is not needed.
6. **Add audit logging** for each report access: principal, target `accountId`, timestamp, source IP, decision. Forward to SIEM.
7. **Rate-limit per principal** on `/accounts/{accountId}/reports` to slow enumeration.
8. **Add automated authorization tests** to CI: a non-member user must receive 404/403 for another account's reports. Cover this with at least one negative test per privileged endpoint.
9. **Sweep for similar patterns.** This is likely systemic — audit every route with a path-parameter resource ID for the same defect.

## Validation Steps

All steps assume **authorized, non-production** testing.

1. Static review: confirm presence of a membership check in the handler chain for `GET /accounts/{accountId}/reports`.
2. Unit/integration tests:
   - User A (member of account 1) requests `/accounts/2/reports` → expect 404/403.
   - User A (member of account 1) requests `/accounts/1/reports` → expect 200 with correct scope.
   - Unauthenticated request → expect 401.
3. Verify audit log entries are produced for both allowed and denied requests.
4. Confirm error responses do not leak account existence or internal IDs.
5. Re-run the authorization test suite in CI as a regression gate.

## Residual Risk

- Even after fix, risks remain from: compromised member accounts, over-privileged roles, identifier leakage via logs or referrers, and report caching at CDN or browser layers. Recommend reviewing `Cache-Control` headers on this endpoint (`private, no-store`).
- Confidence in this assessment is bounded by the synthetic scope; real implementation may have additional controls (e.g., gateway-level policy) not visible here.

## Open Questions

1. Is the system multi-tenant, and what is the membership/role model?
2. What identifier scheme is used for `accountId`?
3. Are there gateway-, mesh-, or middleware-level authorization controls that were not described?
4. What logging and monitoring exist for this endpoint today?
5. What is the regulatory context (GDPR, CCPA, PCI scope) for the billing and email data?
6. Are similar `/{resourceId}` patterns used elsewhere in the API?

## Handoff

- **Engineering / DevSecOps:** Implement centralized authorization middleware and CI authorization tests.
- **Security leadership:** Sponsor a broader BOLA sweep across the API surface.
- **Compliance / Privacy:** Assess notification or DPIA obligations if this pattern reflects production behavior with real user data.
- **Incident response:** If this pattern is live in production, evaluate whether log review for prior exploitation is warranted before this report is treated as purely preventive.
