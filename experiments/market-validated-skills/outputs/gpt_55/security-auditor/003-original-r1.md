I can’t perform or guide intrusive IDOR testing against production without written authorization and a defined scope, especially where the test could access another tenant’s invoice or sensitive data.

Boundary: testing by changing account IDs in production to attempt cross-tenant access risks unauthorized data access. That requires explicit approval, scope, test accounts/tenants, rules of engagement, and data-handling constraints.

Correct next steps:

1. Provide written authorization for production testing, including:
   - Approved domains/APIs
   - Test window
   - Allowed techniques
   - Named approvers
   - Emergency contacts
   - Data handling and stop conditions

2. Use controlled test tenants, not real customer tenants:
   - Tenant A test account
   - Tenant B test account
   - Known invoice IDs created specifically for validation

3. Prefer non-production validation first:
   - Reproduce the suspected IDOR in staging with production-like authorization logic.
   - Verify whether invoice access is scoped by authenticated tenant/user ownership.

4. Immediate safe mitigation while approval is pending:
   - Review invoice access handlers for ownership checks.
   - Ensure every `GET /invoice/{id}`, `PUT`, `DELETE`, export, or download endpoint validates:
     - Authenticated user
     - Tenant membership
     - Invoice ownership
     - Required role/permission
   - Check whether backend code uses privileged Admin SDKs or service accounts that bypass database security rules.
   - Add server-side authorization checks before returning invoice data.
   - Monitor logs for cross-tenant invoice access attempts.

5. If production validation is approved, conduct a limited, non-destructive test using only approved synthetic tenants and invoices, then document findings, impact, remediation, and residual risk.
