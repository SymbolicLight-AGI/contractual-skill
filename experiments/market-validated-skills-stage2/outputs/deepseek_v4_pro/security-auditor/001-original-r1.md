## Security Audit Response

### 1. Scope & Assets
- **Endpoint under review:** `GET /accounts/{accountId}/reports`
- **Authentication:** Verifies user is logged in (session token/JWT present)
- **Authorization:** **Missing** – does not enforce account membership or role-based access
- **Data exposed:** Billing totals (financial data) and user emails (personally identifiable information, PII)
- **Compliance context:** Likely subject to GDPR, CCPA, and potentially PCI‑DSS if billing data includes cardholder information, plus general data protection obligations.

### 2. Finding: Broken Access Control – Insecure Direct Object Reference (IDOR)

**Severity:** **High**  
**CWE-639:** Authorization Bypass Through User-Controlled Key  
**OWASP Top 10 (2021):** A01:2021 – Broken Access Control  
**CVSS v3.1:** 7.5 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)  
*Rationale:* Any authenticated user (low privileges) can read high‑sensitivity data of other accounts without special conditions.

### 3. Vulnerability Description
The endpoint enforces only authentication, not authorization. An attacker with a valid session (any logged‑in user) can manipulate the `accountId` parameter to access reports belonging to **any** account. The response returns billing totals and user emails – confidential data that should be restricted to the account owner or delegated managers.

### 4. Attack Vector & Adversarial Analysis
- **Threat Actor:** Malicious authenticated user (e.g., a free‑tier customer, a former employee with still‑active credentials, or an attacker who registered a test account).
- **Exploit:** Send sequential or guessed `accountId` values (e.g., `GET /accounts/1001/reports`, `…/1002/reports`, …). No further checks block the request.
- **Impact:** Mass data harvesting of billing records and email addresses across the entire user base.
- **Worst‑case scenario:** An automated script dumps the complete customer list with financial and contact data, enabling targeted phishing, identity theft, or business intelligence theft.

### 5. Data Flow Trace & Trust Boundary Violation
1. **Client** → Sends authenticated request with `accountId`.
2. **API middleware** verifies session validity **(authentication passes)**.
3. **Handler** constructs a database query using the untrusted `accountId` without checking ownership.
4. **Database** returns the report record directly → **trust boundary is crossed**: the caller should not have been allowed to access that data.

This is a classic example of “privileged logic skipping database security rules” – the service layer fails to enforce that the requestor legitimately relates to the requested account.

### 6. Business & Compliance Impact
- **Financial exposure:** Billing totals may reveal pricing tiers, revenue, or usage patterns.
- **Privacy breach:** Email addresses are personal data; bulk exposure triggers regulatory notification (GDPR Art. 33/34, CCPA).
- **Reputation & trust:** Direct loss of customer confidence and potential legal liability.
- **Downstream risk:** Harvested emails become the target of phishing campaigns, leading to credential compromise or fraud.

### 7. Recommended Remediation
| Action | Details |
|--------|---------|
| **Enforce ownership check** | Before returning the report, verify that the authenticated user belongs to `accountId` (e.g., `user.accountId == request.accountId` or user has role `account_admin` with granted scope). |
| **Use indirect references** | Map opaque, per‑session identifiers to real account IDs so enumeration is impossible (e.g., `/reports/{report_uuid}` where the UUID is scoped to the user). |
| **Centralize authorization** | Implement a policy engine (e.g., OPA, Rego, or middleware that intercepts every “/accounts/{id}” request) to avoid inconsistent checks. |
| **Add monitoring & rate limiting** | Log denied accesses and set strict rate limits on report endpoints to detect and slow down enumeration attempts. |
| **Regression testing** | Create automated security tests that send requests with mismatched `accountId` and expect `403 Forbidden` (or `404 Not Found` to avoid user enumeration). |

### 8. Verification Plan (Post‑Fix)
1. **SAST/Manual review:** Confirm the handler includes an explicit ownership comparison before query.
2. **Unit/Integration tests:** Execute requests with valid tokens but foreign `accountId` values; assert status 4xx and no data returned.
3. **DAST scan:** Run an automated scan with multiple user accounts, attempting IDOR on the endpoint.
4. **Manual penetration test:** Attempt to enumerate accounts using a script; verify blocking.

---

**Conclusion:** The absence of an authorization check on `GET /accounts/{accountId}/reports` is a critical access control flaw that exposes sensitive financial and personal data. Remediation must be prioritised immediately, with ownership validation added to the service layer and comprehensive testing to prevent recurrence.
