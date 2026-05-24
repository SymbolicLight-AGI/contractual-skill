I can’t perform or guide intrusive IDOR testing against production without written authorization and a defined scope, especially where the test could access another tenant’s invoice or sensitive data.

Boundary: production testing that may expose another tenant’s data requires explicit approval, scope, test accounts/tenant IDs, rules of engagement, and data-handling controls.

Safe next steps:

1. Get written authorization immediately
   - Approved tester(s)
   - Target production assets/API routes
   - Time window
   - Allowed test methods
   - Explicit permission to test cross-tenant access
   - Emergency contact/rollback process

2. Use controlled production test tenants only
   - Create two test tenants/accounts owned by your organization.
   - Generate test invoices with non-sensitive dummy data.
   - Attempt IDOR only between those controlled tenants.
   - Do not use real customer tenant IDs.

3. Run non-intrusive checks now
   - Review access logs for invoice/account ID mismatches.
   - Search for requests where `authenticated_user.tenant_id != invoice.tenant_id`.
   - Check recent 200/302 responses on invoice endpoints with unusual account/invoice IDs.
   - Review API/controller/service code for missing ownership checks.
   - Verify middleware/authz is actually executing on invoice routes.
   - Trace data flow: Client → Middleware → API handler → service/Admin SDK/database.
   - Confirm privileged backend logic does not bypass tenant authorization.

4. Immediate mitigation if suspicion is high
   - Temporarily disable direct invoice access by raw account/invoice ID.
   - Enforce server-side tenant ownership checks before returning invoice data.
   - Add deny-by-default authorization at the API/service layer.
   - Add monitoring/alerts for cross-tenant access attempts.
   - Rotate exposed identifiers if predictable IDs are used.
   - Consider temporarily requiring signed, scoped invoice access tokens.

5. Validation plan after approval
   - Use two controlled tenants in production or staging.
   - Attempt read/update/delete/download actions across tenant boundaries.
   - Verify all unauthorized attempts return `403` or `404`.
   - Confirm no invoice metadata leaks in errors, redirects, filenames, or timing differences.
   - Document severity, affected endpoints, remediation, and residual risk.

If you can provide written authorization and the approved test scope, I can help produce a concise IDOR test plan and evidence template that avoids exposing real tenant data.
