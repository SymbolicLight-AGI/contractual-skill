# Security Audit Report: API Authorization Vulnerability

## Finding Overview
**Vulnerability:** Broken Object Level Authorization (BOLA) / Insecure Direct Object Reference (IDOR)
**Endpoint:** `GET /accounts/{accountId}/reports`
**Severity:** **CRITICAL**
**OWASP Category:** API1:2023 - Broken Object Level Authorization / OWASP Top 10 A01:2021 - Broken Access Control

## 1. Threat Model & Adversarial Analysis
**Attack Vector:** 
The endpoint currently implements authentication (verifying the user is logged in) but lacks authorization (verifying the user has the right to access the requested resource). 

**Exploitation Scenario:**
An attacker registers for a legitimate account on the platform to obtain a valid session token. They then intercept their own request to `GET /accounts/1042/reports` and modify the `{accountId}` parameter to `1043`, `1044`, etc. Because the backend does not validate if the authenticated user's identity is mapped to the requested `accountId`, the server will return the reports for other tenants.

## 2. Business & Compliance Impact
- **Data Breach (Confidentiality Loss):** Exposure of sensitive financial data (billing totals) and Personally Identifiable Information (PII - user emails).
- **Regulatory Violations:** Unauthorized disclosure of PII directly violates frameworks such as **GDPR**, **CCPA**, and potentially **SOC 2** privacy/confidentiality trust principles.
- **Reputational Damage:** Cross-tenant data exposure is a critical breach of trust in multi-tenant architectures.

## 3. Data Flow & Root Cause Analysis
Tracing the data flow from the API entry point to the database reveals a "security bypass" flaw:
1. **Middleware:** Validates the JWT/Session (Authentication passes).
2. **Controller:** Extracts `{accountId}` from the URL path.
3. **Data Access Layer:** Executes a query similar to `SELECT * FROM reports WHERE account_id = {accountId}`.
**Root Cause:** The query or business logic fails to include the authenticated user's context (e.g., `userId` or `tenantId` extracted from the validated token) in the authorization check or database query.

## 4. Remediation Plan

### Immediate Fixes (Code Level)
1. **Implement Ownership/Membership Validation:** 
   Modify the backend logic to verify that the authenticated user has an explicit relationship with the requested `accountId` before fetching the data.
   *Example (SQL context):* 
   `SELECT r.* FROM reports r JOIN account_users au ON r.account_id = au.account_id WHERE r.account_id = ? AND au.user_id = ?`
2. **Enforce Authorization Middleware:** 
   Implement an authorization choke point (e.g., ABAC or RBAC policy engine) that explicitly evaluates `can_read_report(currentUser, requestedAccountId)` before the controller executes.

### Defense-in-Depth (Architecture Level)
1. **Obfuscate Identifiers:** 
   If `{accountId}` is a predictable sequential integer, migrate to **UUIDv4** or high-entropy ULIDs. While this does not fix the underlying BOLA vulnerability, it prevents trivial enumeration attacks.
2. **Implement Zero-Trust Principles:** 
   Never trust client-provided input for access control decisions. Always derive the user's identity and permissions strictly from the validated server-side session or JWT claims.

## 5. DevSecOps & Automation Recommendations (Shift-Left)
To prevent regressions and detect similar vulnerabilities across the API surface, implement the following pipeline controls:
- **Dynamic Application Security Testing (DAST):** Integrate tools like OWASP ZAP or Burp Suite Enterprise into the CI/CD pipeline. Configure authenticated scans with multiple test users to specifically test for cross-account access (BOLA/IDOR).
- **Static Application Security Testing (SAST):** Deploy custom Semgrep or CodeQL rules to flag database queries or ORM calls that filter by an object ID without simultaneously filtering by a user ID or tenant context.
- **Integration Testing:** Mandate that every API endpoint unit/integration test includes a negative test case asserting that `User A` receives an `HTTP 403 Forbidden` or `404 Not Found` when attempting to access `User B`'s resources.
