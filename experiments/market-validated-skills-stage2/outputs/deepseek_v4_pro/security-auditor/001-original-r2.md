**Security Audit Finding: Broken Access Control (IDOR) on `GET /accounts/{accountId}/reports`**

| Attribute          | Detail                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **Title**          | Missing account membership check exposes billing data and user emails   |
| **Endpoint**       | `GET /accounts/{accountId}/reports`                                    |
| **Risk Context**   | Endpoint only validates authentication; no authorization to confirm the requesting user belongs to the target account. |
| **Severity**       | **Critical / High** (depending on data volume and business impact)      |
| **OWASP Category** | A01:2021 – Broken Access Control (Insecure Direct Object Reference)     |
| **CVSS v3.1**      | Likely CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N (7.5 High); may reach Critical if billing data enables fraud. |

---

### 1. Scope & Context
- **Pattern**: `GET /accounts/{accountId}/reports`
- **Assumed authentication**: User login required (session or token validated).
- **Authorization**: No check that the authenticated user is a member of `{accountId}`.
- **Data returned**: Billing totals and user emails (presumably all emails associated with the account).
- **Threat model**: Any authenticated user can enumerate or guess account IDs and retrieve sensitive reports from arbitrary accounts.

### 2. Data Flow & Trust Boundary Analysis
- **Entry point**: Client provides `accountId` as a URL path parameter.
- **Authentication check**: Validates session/JWT, but stops there.
- **Authorization gap**: No subsequent check to verify the user’s relationship to the resource.
- **Data retrieval**: The backend pulls billing aggregates and email lists, likely from a database, and returns them directly.
- **Bypass potential**: A privileged service account or Admin SDK may be used, but the logic fails to replicate access controls at the application layer. The absence of a middleware or service-level ownership verification means the standard rule “users can only see their own account data” is never enforced.

### 3. Adversarial Analysis
- **How can this be exploited?**
  - **IDOR / Horizontal privilege escalation**: Authenticated user changes `accountId` in the URL (e.g., from 1234 to 1235) to view reports of other organizations.
  - **Enumeration attacks**: Iterating through sequential or UUID-like account IDs yields a dump of billing amounts and user email lists across all accounts.
  - **Data exfiltration**: Billing totals can be used for competitive intelligence; email lists fuel phishing, spamming, or account takeover attempts.
  - **Compliance risk**: Exposure of personal emails may breach GDPR, CCPA, HIPAA (if emails relate to health data), or PCI-DSS (billing totals, combined with other data, could increase risk).
- **Feature abuse**: The “generate report” feature acts as an open data faucet for any logged-in user, with no rate limiting or anomaly detection on cross-account access patterns.

### 4. Findings & Risk Impact
| Finding                                       | Impact                                                     |
|-----------------------------------------------|------------------------------------------------------------|
| Missing authorization check on `accountId`    | Direct exposure of sensitive data to unauthorized parties  |
| Sensitive data leakage (billing, user emails) | Financial disclosure, privacy violation, legal exposure    |
| No audit trail for cross-account access       | Delayed detection, difficult incident investigation        |
| Potential enumeration of account identifiers  | Mass data harvesting, reduced attack complexity            |

### 5. Remediation Recommendations
#### Immediate (Priority)
1. **Implement server-side authorization**:
   - After authentication, verify that the requesting user is a member of, or has an explicit role on, the `{accountId}`.
   - Example (pseudo):
     ```
     if !currentUser.IsMemberOf(accountId) && !currentUser.HasPermission("report:read")
         return 403 Forbidden
     ```
2. **Use indisputable ownership checks**:
   - Query the account’s membership list from the data store; never rely on the client-provided ID alone.
   - Prefer opaque, non-sequential account references (e.g., UUIDs) to hinder enumeration, though this is only a mitigation, not a fix.
3. **Apply data minimization**:
   - Expose only the fields necessary for the report. Mask or omit raw email addresses if the report can use internal identifiers or hashed emails.
   - Evaluate whether billing totals must be returned directly or can be replaced with aggregated, non-sensitive summaries.

#### Short-term
- **Add access control middleware** that intercepts all `accounts/{id}/*` routes and enforces membership.
- **Log and alert** on cross-account report access attempts (even if blocked), with anomaly detection on unusual patterns (e.g., User A requesting 50 distinct account reports per minute).
- **Conduct a code review** of all endpoints that use path parameters representing resource IDs; verify consistent authorization.

#### Long-term
- **Implement centralized authorization** (e.g., OPA/Rego, Zanzibar-style) so that every data retrieval enforces policy.
- **Automate security testing**: Add an integration test that authenticates as User A and attempts to fetch User B’s report, asserting a 403/404.
- **Include this pattern in threat modeling and developer training**: “Never trust that authentication alone is enough.”

### 6. Verification of Fix
- After remediation:
  - Authenticate as a user who is **not** a member of account X and request `GET /accounts/X/reports`; expect `403 Forbidden`.
  - Verify that a legitimate member still receives the report successfully.
  - Ensure error responses do not leak whether the account exists (return a consistent 403 or 404 to prevent user enumeration).

### 7. Residual Risk
- If the endpoint is also exposed to internal services with elevated privileges, ensure those service-to-service calls carry appropriate scoped tokens and are not used as a shortcut to bypass access control.
- Monitor for insider threats where a legitimate user downloads reports in bulk.

---

**Conclusion**: The missing authorization check constitutes a critical broken access control vulnerability. Immediate remediation is required to prevent unauthorized disclosure of sensitive billing and personal information. I recommend adding this finding to your bug tracker with the highest priority and retesting after the fix.
