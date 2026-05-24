# Security Audit Response: API Authorization Review

## 1. Scope, Assets & Compliance Confirmation
- **Asset Under Review:** `GET /accounts/{accountId}/reports`
- **Current Control:** Authentication only (validates user is logged in)
- **Missing Control:** Authorization/Account membership validation
- **Data Exposed:** Billing totals (financial), user emails (PII)
- **⚠️ Uncertainty Markers:** 
  - Compliance framework not specified (assumed GDPR/CCPA/PCI-DSS/SOC 2 applicability due to PII + financial data)
  - `accountId` format unknown (sequential integer vs. UUID vs. hash)
  - Authentication mechanism unspecified (JWT, session cookie, OAuth token)
  - Backend data store and query method not provided

## 2. Architecture & Data Flow Trace
**Trust Boundary Flow:** `Client → API Gateway → Auth Middleware → Route Handler → Data Service/DB → Response`
- **Entry Point:** HTTP GET with valid auth token/session.
- **Middleware Choke Point:** Authentication middleware executes successfully, attaching `userId`/`sub` to the request context.
- **Security Bypass:** Route handler extracts `{accountId}` from the URL path and passes it directly to the data layer **without cross-referencing** the authenticated `userId` against an account membership/tenant table.
- **Privileged Logic Execution:** The backend query or Admin SDK fetches report data based solely on the path parameter, bypassing standard row-level security or tenant-scoped filters.
- **Exit Point:** Unfiltered billing totals and PII are serialized and returned to the client.

## 3. Adversarial Analysis
**Question:** *How can this be defaced, hijacked, or exploited?*
- **Exploitation Path:** An authenticated attacker iterates or predicts `{accountId}` values. If sequential, trivial enumeration occurs. If UUIDs, they can be harvested from logs, referral headers, or other endpoints lacking proper scoping.
- **IDOR on Global Resource:** The endpoint treats `accountId` as a global identifier rather than a scoped resource. No ownership verification exists, enabling horizontal privilege escalation.
- **Impact:** Mass exfiltration of financial records and PII. Enables targeted phishing, account takeover reconnaissance, competitive intelligence theft, and regulatory breach notifications.

## 4. Findings & Prioritization
| ID | Finding | Severity | CVSS (Est.) | Business Impact |
|----|---------|----------|-------------|-----------------|
| SEC-001 | Broken Access Control / IDOR (OWASP A01:2021) | **Critical** | 9.1 (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N) | Regulatory fines, mandatory breach disclosure, loss of customer trust, potential financial fraud |

## 5. Remediation Steps
1. **Implement Authorization Middleware:** Insert a post-auth choke point that extracts `userId` from the token, queries the membership/tenant mapping, and verifies `accountId ∈ user.allowedAccounts`. Return `403 Forbidden` on mismatch.
2. **Enforce Row-Level Security (RLS):** Apply database-level tenant scoping so even if application logic fails, the query engine restricts results to the authenticated context.
3. **Adopt Policy-as-Code:** Use OPA or framework-specific guards (e.g., Spring Security `@PreAuthorize`, Express middleware) to declaratively enforce `user.id == account.ownerId || user.roles.contains('account_admin')`.
4. **Minimize Data Exposure:** Apply field-level filtering. Return only billing totals and emails explicitly required by the requesting user's role.
5. **Shift-Left Controls:** Add SAST/IAST rules to CI/CD pipelines to flag route handlers that consume path parameters without corresponding authorization checks.
6. **Rate Limiting & Monitoring:** Implement strict rate limits on `/accounts/*/reports` and alert on anomalous enumeration patterns (e.g., rapid sequential `accountId` requests from a single session).

## 6. Validation & Residual Risk
- **Validation Test:** 
  - Authenticated User A requests `GET /accounts/{UserB_AccountId}/reports` → Expect `403 Forbidden`
  - Authenticated User A requests `GET /accounts/{UserA_AccountId}/reports` → Expect `200 OK` with scoped data
  - Unauthenticated request → Expect `401 Unauthorized`
- **Residual Risk:** 
  - If membership data is stale or cached incorrectly, authorization may fail open or deny legitimate access. Implement cache invalidation and fallback to DB verification.
  - Service-to-service internal calls may bypass middleware. Ensure internal APIs also enforce tenant scoping or use mutual TLS with explicit scope claims.
- **Next Step:** Provide exact tech stack, compliance requirements, and `accountId` generation method to refine CVSS scoring, tailor policy-as-code implementation, and design automated DAST/IAST test cases.
