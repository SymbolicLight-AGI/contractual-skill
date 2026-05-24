# Remediation Handoff: Security Findings (Reports Authorization, Session Cookies, Admin Export Logging)

**Date:** 2025-04-09  
**Prepared for:** Engineering, Security, QA, Product  
**Classification:** Confidential

## 1. Scope and Authorization

This handoff is based on a synthetic security assessment authorized for the designated application environment. The review focused on three specific findings: missing object‑level authorization on reports, session cookies lacking the `Secure` flag, and absent audit logging for the admin export feature. The assessment was non‑intrusive and used provided architecture and configuration references. No production testing was performed without explicit approval.

**In scope:** Reports module, session management configuration, admin export functionality.  
**Out of scope:** Other API endpoints, broader logging infrastructure, compliance certification.

## 2. Executive Summary

Three vulnerabilities were identified that affect confidentiality, integrity, and accountability:

1. **Missing object-level authorization on reports (Critical/High)** – Enables horizontal privilege escalation, allowing any authenticated user to access, modify, or delete another user’s reports.
2. **Session cookies without `Secure` flag (High)** – Exposes session tokens to network interception when transmitted over unencrypted HTTP.
3. **Admin export functionality without audit log (Medium)** – Prevents detection and investigation of data exfiltration by privileged users, undermining compliance requirements.

Remediation steps are provided for each finding, along with validation checks for QA and security re‑testing. The findings are prioritised by business impact and should be addressed in the next development cycle.

## 3. Findings by Severity

### Finding 1: Missing Object-Level Authorization on Reports (Critical / High)

- **CWE:** 639 (Insecure Direct Object Reference)  
- **Affected Component:** Reports API endpoints (e.g., `/api/reports/{id}`)  
- **Description:** The application does not verify that the requesting user owns or is authorised to access the requested report object. An attacker can substitute a different report identifier and gain access to another user’s data.  
- **Business Impact:** Unauthorised disclosure of sensitive report contents, potential bulk data scraping, loss of customer trust, and regulatory penalties if reports contain personal or protected data.  
- **Evidence:** *Finding* – Code review indicates no ownership check is performed inside the report handler; a test user successfully retrieved another user’s report by changing the URL parameter.  
- **Hypothesis:** All report operations (view, edit, delete) and possibly other resource endpoints are affected.

### Finding 2: Session Cookies Lack `Secure` Flag (High)

- **CWE:** 614 (Sensitive Cookie in HTTPS Session Without ‘Secure’ Attribute)  
- **Affected Component:** Session management – session cookie (`SESSION_ID` or equivalent)  
- **Description:** The session cookie is set without the `Secure` attribute. This allows the cookie to be transmitted over unencrypted HTTP connections if an attacker forces a protocol downgrade or the application is accidentally exposed over HTTP.  
- **Business Impact:** Session hijacking via network sniffing, leading to full account takeover.  
- **Evidence:** *Finding* – Observed in `Set-Cookie` response header: `SESSION_ID=abc123; Path=/; HttpOnly`. The `Secure` flag is missing. No HSTS header was present.  
- **Hypothesis:** Other sensitive cookies (CSRF tokens, remember‑me tokens) may also lack `Secure` and `HttpOnly`.

### Finding 3: Admin Export Feature Without Audit Log (Medium)

- **CWE:** 778 (Insufficient Logging)  
- **Affected Component:** Admin export function (bulk data download)  
- **Description:** When an administrator triggers a data export, no audit log entry is generated. There is no record of who performed the export, what data was exported, or when the action occurred.  
- **Business Impact:** Inability to detect or investigate data leakage by trusted insiders; non‑compliance with logging requirements (e.g., SOC 2, GDPR, HIPAA).  
- **Evidence:** *Finding* – Code review shows no logging call within the export handler. Manual test export produced no corresponding entry in the application or SIEM logs.  
- **Hypothesis:** Other admin actions may also lack sufficient audit trails.

## 4. Evidence

All findings are labelled as *Findings*, supported by the supplied synthetic review materials. No actual production logs or raw secrets are included. Evidence gaps exist only where specific configuration files or full endpoint inventories were not provided; these are noted in the Open Questions section.

## 5. Remediation Plan

### For Finding 1: Missing Object-Level Authorization

**Owner:** Engineering (API/Backend Team)  

- **Immediate Fix:** Before returning any report data, retrieve the authenticated user ID from the session/token and compare it against the `owner_id` field of the requested report. Return HTTP 403 Forbidden on mismatch.
- **Architecture:** Implement a reusable authorisation middleware that enforces resource‑level ownership checks for all endpoints accepting a resource identifier.
- **Identifier Hardening:** Use non‑guessable UUIDs as primary keys if not already; however, **never rely on UUIDs alone**—authorisation checks are mandatory.
- **Testing:** Write unit and integration tests that confirm user A cannot access, edit, or delete user B’s report. Include negative test cases for every report endpoint.
- **Broader Review:** Conduct a complete inventory of endpoints with `{id}` parameters and apply the same authorisation pattern.

### For Finding 2: Session Cookies Lack `Secure` Flag

**Owner:** Engineering (Application & Platform Team)  

- **Change Cookie Configuration:** Set `Secure` on the session cookie. In common frameworks:
  - Express: `res.cookie('session', value, { secure: true, httpOnly: true, sameSite: 'lax' })`
  - Spring Boot: `server.servlet.session.cookie.secure=true` and `sameSite=Lax`
  - General server config: add `Secure`; `HttpOnly`; `SameSite=Lax` (or `Strict` where appropriate).
- **Enforce HTTPS Only:** Enable HTTP Strict Transport Security (HSTS) with a long `max-age` and the `includeSubDomains` directive. Consider HSTS preloading.
- **Cookie Name Prefix:** Use the `__Secure-` prefix for the session cookie name to leverage browser enforcement of Secure and SameSite.
- **Global Cookie Audit:** Review all cookies set by the application (authentication, CSRF, analytics) and apply the same secure attributes.

### For Finding 3: Admin Export Without Audit Log

**Owner:** Engineering (Admin Features Team), with Security oversight  

- **Insert Logging:** In the export handler, write an audit log entry containing:
  - Administrator user ID / username
  - Timestamp (UTC, ISO 8601)
  - Export type (e.g., “reports‑csv”, “users‑excel”)
  - Number of records exported (if applicable)
  - Result (success / failure / partial)
- **Log Destination:** Write to a centralised, write‑once audit log (e.g., SIEM, dedicated log stream) that administrators cannot modify.
- **Monitoring:** Set up an alert for high‑volume exports or repeated exports in a short time window.
- **Retention:** Align log retention with compliance policy (e.g., 90 days online, 1 year archive).
- **Expansion:** Review other admin functions (user management, permission changes, bulk deletions) and ensure similar audit trails exist.

## 6. Validation Steps

After remediation, each team should verify the fixes as follows:

| Finding | Validation |
|--------|-------------|
| **Authorization** | 1. Using two distinct user accounts, attempt to access the other user’s report via direct URL manipulation. Expect HTTP 403. 2. Automated security test (e.g., OWASP ZAP) to replay requests with alternate tokens. 3. Confirm that all report endpoints (GET, PUT, DELETE) are protected. |
| **Session Cookies** | 1. Inspect `Set-Cookie` response header in staging; verify `Secure`, `HttpOnly`, and `SameSite` attributes are present. 2. Attempt to connect via HTTP (if still reachable) and confirm the cookie is **not** sent. 3. TLS scan to ensure HSTS header is served. 4. Check that `__Secure-` prefix is used if implemented. |
| **Admin Audit Log** | 1. Perform an export as an admin user. 2. Query the audit log system; verify a single entry with correct user, timestamp, and export details. 3. Attempt to delete or modify the log entry (should be prevented). 4. Confirm alerting fires for a configured threshold (e.g., repeated exports). |

## 7. Residual Risk

- **Authorization:** Other endpoints outside the reports module may still have similar IDOR vulnerabilities. A full endpoint audit is recommended. Until then, a residual risk of unauthorised data access remains.
- **Session Cookies:** If HSTS is not enforced across the entire domain (including subdomains and the apex domain), users typing `http://` could briefly expose cookies before a redirect. HSTS preload and strict `max-age` are required to eliminate this.
- **Audit Logging:** Only the admin export feature has been addressed. Other high‑privilege actions may remain unlogged, leaving gaps in forensic capability. A broader logging review should be planned.

These residual risks must be formally accepted by security and product leadership before closing.

## 8. Open Questions

- What is the data classification of reports (public, internal, confidential, restricted)? This affects impact severity and regulatory urgency.
- Which specific compliance frameworks (PCI, HIPAA, GDPR, etc.) apply, and what log retention / format requirements do they impose?
- Are there any compensating controls (API gateway authorization, network segmentation, WAF rules) that might currently reduce the likelihood of exploitation?
- What is the current session timeout and cookie lifetime, and do they align with the security policy?

## 9. Handoff

**→ Engineering:**  
Implement the remediation items above, prioritising the authorization fix. Update threat model and architecture documentation. Raise a pull request with the required changes and mark each finding as “ready for review.”

**→ Security:**  
Validate fixes in the staging environment, confirm no similar anti‑patterns exist, and update the internal vulnerability register. Notify compliance if regulatory reporting is required.

**→ QA:**  
Create automated regression tests covering the validation steps. Include these in the CI/CD pipeline to prevent regressions.

**→ Product / Owners:**  
Prioritise these findings in the next sprint. Accept the stated residual risks and answer the open questions to help finalise the fix plan.

If any finding suggests a widespread architectural weakness, escalate to DevSecOps leadership and consider a broader design review.

---

*This handoff is based on synthetic findings. All remediation actions must first be validated in a non‑production environment before deployment to production.*
