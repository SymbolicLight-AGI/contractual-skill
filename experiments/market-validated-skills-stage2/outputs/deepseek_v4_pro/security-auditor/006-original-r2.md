**Remediation Handoff: Security Findings**  
**Date:** 2026-02-27  
**Prepared by:** Security Auditor (DevSecOps Assessment)  
**Distribution:** Engineering, Security, QA, Product  

---

### 1. Executive Summary
Three security findings were identified during a targeted manual review. All require remediation to protect user data, maintain trust, and meet compliance expectations. This handoff assigns ownership and provides actionable steps for each team.

| ID  | Title                                   | Severity | Affected Area     |
|-----|-----------------------------------------|----------|-------------------|
| SEC-001 | Missing object-level authorization on reports | **High** | Report viewing/editing APIs & UI |
| SEC-002 | Session cookies missing `Secure` flag   | **Medium** | Session management |
| SEC-003 | Admin export lacks audit log          | **Medium** | Admin export functionality |

---

### 2. Finding Details & Remediation

#### SEC-001 – Missing Object-Level Authorization on Reports (IDOR)
- **Description:** The report retrieval and update endpoints do not verify that the authenticated user owns the requested report. An attacker can alter a report ID parameter to access or modify reports belonging to other users.
- **Data Flow Exploit Path:** Client → API Gateway → Report Service → Database (Admin SDK used without ownership check).
- **Risk:** Unauthorised data disclosure and modification; potential privacy violation and business impact if sensitive reports are exposed.
- **Engineering Remediation:**
  1. Implement ownership validation in the report service for every read/update/delete operation.  
  2. Use a middleware or decorator that compares the authenticated user ID (from token) with the `owner_id` of the target report **before** any database operation, regardless of whether an Admin SDK is used.  
  3. Apply the same check consistently: direct database access, service-to-service calls, and internal functions.  
  4. Add automated unit and integration tests that attempt to access other users’ reports with valid tokens, and assert 403/404 responses.
- **Security Guidance:**
  - Confirm the enforcement is a mandatory “choke point” that cannot be bypassed via direct internal calls.  
  - Review that the Admin SDK/service account does not skip this ownership check.
- **QA Test Cases:**
  - **Test 1:** As User A, retrieve User B’s report (by ID) via API; expect 403.  
  - **Test 2:** As User A, update a field in User B’s report; expect 403.  
  - **Test 3:** As a privileged role (e.g., admin with limited scope), verify that legitimate cross-account access is correctly allowed **only** when explicitly authorised.  
  - **Test 4:** Negative tests with invalid IDs, malformed tokens, no token; expect consistent error responses without data leakage.
- **Product Acceptance:**
  - Confirm that no existing workflows require one user to see another’s reports without explicit delegation. If such a feature is needed, design a proper sharing model with audit trail.  
  - Accept the residual risk only after engineering fix and QA validation.

---

#### SEC-002 – Session Cookies Lack `Secure` Flag
- **Description:** The session cookie set after successful authentication does not have the `Secure` attribute. This allows the cookie to be transmitted over unencrypted HTTP connections, exposing it to interception and session hijacking.
- **Risk:** Session hijacking via network monitoring; compromise of user accounts.
- **Engineering Remediation:**
  1. Set the `Secure` flag on the session cookie (true for all environments, including staging).  
  2. Also enable `HttpOnly` and `SameSite=Lax/Strict` (depending on cross-origin requirements).  
  3. Ensure the application enforces HTTPS with HSTS headers (max-age ≥ 1 year, includeSubDomains, preload) so browsers never send the cookie over plain HTTP.  
  4. Code change example (pseudo):  
     `res.cookie('session', token, { secure: true, httpOnly: true, sameSite: 'lax' });`
- **Security Guidance:**
  - Verify the cookie configuration in all authentication responses (login, token refresh, SSO callback).  
  - Ensure that any reverse proxy or load balancer does not strip the Secure flag.
- **QA Test Cases:**
  - **Test 1:** Capture login response; inspect `Set-Cookie` header for `Secure; HttpOnly; SameSite=Lax`.  
  - **Test 2:** Attempt to access the site via `http://` and confirm the cookie is not sent (or connection is upgraded to HTTPS).  
  - **Test 3:** Verify that after logout the cookie is invalidated and cannot be reused.
- **Product Acceptance:**
  - No user-facing functional change; accept that session cookies will now only work over HTTPS.  
  - Communicate to any partners that rely on plain HTTP that the endpoint is deprecated.

---

#### SEC-003 – Admin Export Without Audit Log
- **Description:** The admin export function (e.g., exporting user data or reports in bulk) does not generate an audit log entry. There is no record of who performed the export, when, from which IP address, or what data was exported.
- **Risk:** Non-repudiation failure; inability to detect or investigate insider threats or unauthorised bulk data extraction; potential compliance gaps (GDPR, SOC 2, etc.).
- **Engineering Remediation:**
  1. Implement an audit logging service or use existing logging infrastructure to capture each export attempt.  
  2. Log at minimum: timestamp, admin user ID, IP address, user agent, export type (e.g., “all_reports_csv”), number of records, success/failure status.  
  3. Store logs in a tamper‑resistant, centralised location with restricted access.  
  4. Ensure the export operation is not completed until the log entry is successfully written.
- **Security Guidance:**
  - Confirm that log entries cannot be modified or deleted by the same admin role.  
  - Set up alerts on unusual export volumes (e.g., >1000 records outside business hours).  
  - Consider requiring a secondary approval step for high‑volume exports.
- **QA Test Cases:**
  - **Test 1:** Perform an admin export; verify that a log entry appears in the audit log with all required fields.  
  - **Test 2:** Attempt an export with insufficient privileges; verify the event is logged as a failure and no data is accessible.  
  - **Test 3:** Simulate a system error during the logging step; ensure the export is rolled back or blocked, avoiding an uncaptured export.  
  - **Test 4:** Verify that log entries are retained according to the retention policy and are searchable.
- **Product Acceptance:**
  - Accept that admin exports will be slightly slower due to synchronous logging.  
  - Define retention and alert thresholds for the product owner and legal/compliance.

---

### 3. Coordination & Timeline
- **Engineering** will own the code fixes and unit/integration tests, targeting a patch ready for QA within the current sprint.  
- **Security** will perform a design review of the IDOR fix and verify cookie/audit configurations in the staging environment before release.  
- **QA** will execute the specified test cases and record results; any escape must be re‑triaged.  
- **Product** will prioritize these findings in the backlog, communicate any user‑facing changes, and formally accept the residual risk after remediation.

### 4. Validation & Closure
- Once fixes are deployed, the Security team will re‑validate:
  - IDOR: Attempt to access others’ reports using a pentest tool (non‑intrusive).
  - Cookie: Verify `Secure` flag and HSTS header via `curl -I` and browser devtools.
  - Audit log: Export a small dataset and confirm the log entry.
- Findings will be closed only after successful validation and product sign‑off.

---

**Next Step:** Engineering to confirm acceptance of the remediation tasks by [date]; Security to schedule a 15-minute walkthrough if clarification is needed.
