# Security Audit Report: API Authorization Control Gap

## 1. Scope & Compliance Context
- **Target:** `GET /accounts/{accountId}/reports`
- **Assets at Risk:** Billing totals (financial data), user emails (PII)
- **Compliance Implications:** GDPR/CCPA (unauthorized PII disclosure), PCI-DSS (if billing totals correlate to cardholder data), SOC 2/ISO 27001 (CC6.1 logical access controls)
- **Assumption/Uncertainty:** Backend data store and exact auth middleware implementation are unspecified. Assessment assumes standard stateless token-based authentication with a relational or document database.

## 2. Data Flow Trace & Control Gap
**Current Flow:**
`Client Request → API Gateway → Auth Middleware (validates session/JWT) → Route Handler → DB Query (WHERE account_id = {accountId}) → Response`

**Identified Bypass:**
The Auth Middleware acts as a perimeter gate but does not enforce tenant/account scoping. The route handler trusts the `{accountId}` path parameter without cross-referencing it against the authenticated principal's membership claims or database records. This creates a direct security bypass where privileged data retrieval logic ignores standard access control boundaries.

## 3. Adversarial Analysis
**Exploitation Question:** *How can this be hijacked or exploited?*
- **IDOR Enumeration:** An authenticated attacker iterates `{accountId}` (sequential integers, UUIDs, or leaked identifiers) to harvest reports across all accounts.
- **Data Harvesting:** Exposed emails enable targeted phishing, credential stuffing, or social engineering. Billing totals reveal revenue, pricing tiers, and financial health.
- **Automation Risk:** Attackers can script parallel requests to bypass basic rate limits, exfiltrating entire datasets in minutes.
- **OWASP Mapping:** A01:2021 Broken Access Control (Insecure Direct Object Reference)

## 4. Risk Assessment & Prioritization
| Finding | Severity | CVSS Estimate | Business Impact |
|---------|----------|---------------|-----------------|
| Missing Account Membership Check (IDOR) | **Critical** | 8.5 (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N) | Regulatory fines, loss of customer trust, competitive intelligence leak, potential breach notification costs |

## 5. Remediation Steps
**Immediate (Code/Logic):**
- Implement explicit authorization before data retrieval:
  ```python
  # Pseudocode example
  if not user.is_member_of(requested_account_id):
      return 403 Forbidden
  ```
- Enforce tenant-scoped queries at the data layer: `SELECT ... FROM reports WHERE account_id = ? AND account_id IN (SELECT account_id FROM user_accounts WHERE user_id = ?)`

**Architectural (Defense-in-Depth):**
- Shift authorization to a centralized policy engine (e.g., OPA, Cedar, or custom middleware) to prevent route-level drift.
- Apply Principle of Least Privilege: Return only fields explicitly required by the client. Mask emails if full disclosure isn't necessary.
- Implement consistent audit logging for cross-account access attempts.

**DevSecOps Integration:**
- Add SAST/IAST rules to flag route handlers that consume path parameters without corresponding authorization checks.
- Integrate automated DAST with multi-tenant test accounts to validate cross-account isolation in CI/CD.
- Enforce Policy-as-Code in deployment pipelines to block merges lacking explicit access control tests.

## 6. Validation & Residual Risk
**Validation Steps:**
1. Provision two test accounts (A & B) with distinct users.
2. Authenticate as User A, request `GET /accounts/{B_accountId}/reports`.
3. Verify HTTP 403/404 response and confirm zero data leakage.
4. Run automated IAST/DAST scans with token-swapping to validate middleware enforcement.

**Residual Risk:**
- If account membership supports complex sharing models (e.g., cross-tenant collaborators, delegated admin), edge-case authorization logic must be explicitly tested.
- Enumeration risk remains if error messages differentiate between "Account not found" and "Access denied." Standardize to generic `403 Forbidden` or `404 Not Found` to prevent information leakage.
- Continuous monitoring for anomalous request patterns (high volume of unique `{accountId}` values per session) is required to detect automated scraping.

## 7. Next Steps
- Apply authorization middleware and tenant-scoped queries immediately.
- Update threat model to reflect multi-tenant data boundaries.
- Schedule compliance review if PII/financial data exposure triggers breach notification thresholds.
- Integrate automated access control validation into the security pipeline before next release.
