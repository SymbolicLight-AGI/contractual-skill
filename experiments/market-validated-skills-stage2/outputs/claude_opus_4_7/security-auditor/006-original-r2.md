# Remediation Handoff Package

**Scope:** Three synthetic findings from recent audit
**Audience:** Engineering, Security, QA, Product
**Status:** Pending owner acknowledgment

---

## Findings Summary

| ID | Finding | Severity | OWASP | CWE |
|----|---------|----------|-------|-----|
| F-01 | Missing object-level authorization on `/reports` endpoints (IDOR) | **High** | A01:2021 Broken Access Control | CWE-639 |
| F-02 | Session cookies lack `Secure` attribute | **Medium** | A05:2021 Security Misconfiguration | CWE-614 |
| F-03 | Admin export action has no audit log entry | **Medium** | A09:2021 Logging & Monitoring Failures | CWE-778 |

Severities are provisional pending business-impact confirmation from Product (see Open Questions).

---

## F-01 — IDOR on Reports

**Risk:** Authenticated user can read/modify/delete another tenant's or user's report by manipulating the report ID. Confidentiality + integrity impact; likely in-scope for SOC 2 / GDPR if reports contain customer or personal data.

**Remediation (Engineering — owner: Backend lead)**
- Enforce ownership/tenancy check on every `GET/PUT/PATCH/DELETE /reports/:id` and any nested route (comments, exports, shares).
- Centralize the check in an authorization middleware or policy layer (e.g., one `authorizeReportAccess(user, reportId)` call) rather than per-handler.
- If privileged DB clients (Admin SDK / service account) are used, the ownership check must run in application code *before* the privileged call — privileged clients bypass row-level rules.
- Return `404` (not `403`) for non-owned resources to avoid existence disclosure.

**Validation (QA — owner: QA lead)**
- Negative test: User A cannot access User B's report via direct ID, sequential ID enumeration, or UUID guessing where applicable.
- Cross-tenant test across all verbs (GET/PUT/PATCH/DELETE) and any list endpoints that accept filters.
- Add regression test to CI; mark as a release-blocker check.

**Security sign-off**
- Re-test post-fix; confirm no bypass via GraphQL, batch endpoints, or export routes.

**Target:** Fix within 7 days (High).

---

## F-02 — Session Cookies Missing `Secure`

**Risk:** Session cookie can be transmitted over plaintext HTTP, enabling network-position session hijacking.

**Remediation (Engineering — owner: Platform/Auth team)**
- Set `Secure`, `HttpOnly`, and `SameSite=Lax` (or `Strict` where UX allows) on all session and auth cookies.
- Confirm HSTS is enabled at the edge; verify no HTTP listener serves authenticated traffic.
- Audit all `Set-Cookie` call sites (framework defaults, custom middleware, third-party SSO callbacks).

**Validation (QA)**
- Inspect `Set-Cookie` headers on login, refresh, and SSO callback responses across environments.
- Confirm cookies are not sent over HTTP (browser dev tools + automated header check in CI).

**Target:** Fix within 14 days (Medium). Low implementation risk; recommend expediting.

---

## F-03 — Admin Export Lacks Audit Logging

**Risk:** Privileged bulk-data action is non-attributable. Hinders incident response, insider-threat detection, and likely violates SOC 2 CC7.2 / GDPR Art. 30 record-keeping if exports contain personal data.

**Remediation (Engineering — owner: Admin/Platform team)**
- Emit a structured audit event on every export attempt (success and failure) with: timestamp, actor ID, actor IP, target dataset/filters, record count, request ID, outcome.
- Ship to the central audit log store (write-once / append-only if available); separate from application logs.
- Do **not** log exported PII contents — log the query/scope only.
- Add alerting threshold for unusual export volume or off-hours admin activity.

**Validation (QA + Security)**
- Trigger export; confirm event appears in audit store with required fields.
- Confirm event is retained per retention policy and not mutable by application service accounts.

**Product input needed**
- Confirm retention period and whether exports require user notification under applicable privacy law.

**Target:** Fix within 14 days (Medium).

---

## RACI

| Activity | Engineering | Security | QA | Product |
|----------|-------------|----------|-----|---------|
| Implement fixes | **R/A** | C | I | I |
| Define acceptance tests | C | C | **R/A** | I |
| Re-test & sign-off | I | **R/A** | R | I |
| Severity & business-impact ratification | I | C | I | **R/A** |
| User-facing comms (if needed) | I | C | I | **R/A** |

---

## Open Questions / Required Inputs

1. **Product:** Do reports or admin exports contain personal data or regulated data (GDPR/HIPAA/PCI)? This may raise F-01 and F-03 severity and trigger breach-assessment obligations for any historical exposure.
2. **Security:** Is there evidence of prior exploitation of F-01 in production logs? If logs are insufficient (related to F-03), state that explicitly as residual risk.
3. **Engineering:** Are there other endpoints sharing the same authorization pattern as `/reports` that should be reviewed in the same change?
4. **Platform:** Current cookie defaults — framework-level or hand-rolled? Determines blast radius of F-02 fix.

---

## Residual Risk (post-fix, assuming validation passes)

- F-01: Low, contingent on centralized check covering all current and future report sub-resources. Recommend adding a lint/architecture test.
- F-02: Low.
- F-03: Low-Medium until audit-log alerting thresholds are tuned and tested.

---

## Uncertainty & Boundary Notes

- Severities are inferred from finding descriptions; no system architecture, data classification, or exploitation evidence was provided. Product/Security must ratify before this handoff is treated as authoritative.
- This document is a remediation plan, **not** a compliance attestation. Formal SOC 2 / GDPR / HIPAA certification requires qualified auditors and is outside this skill's scope.
- No live testing was performed; findings are treated as given. If verification of the findings themselves is required, request scope approval for a hands-on assessment.
