## Boundary: Production IDOR Testing Requires Approval

I can’t try changing account IDs against production or attempt to access another tenant’s invoice without explicit written authorization and a defined scope. That would be an intrusive production test and could expose tenant data.

## What I Need Before Any Production Testing

Please provide:

- Written approval from the system/data owner for production testing.
- Exact assets, endpoints, tenants, and account IDs in scope.
- Approved test accounts only, ideally two controlled tenants created for this test.
- Time window and rate limits.
- Confirmation that accessing real customer data is prohibited unless separately authorized.
- Incident/contact escalation path if unintended access occurs.

## Safe Next Steps I Can Help With Now

### 1. Non-Intrusive Review

I can review:

- Route handlers and authorization checks.
- Invoice access control logic.
- API gateway or middleware policies.
- Tenant isolation design.
- Logs or prior suspected access patterns, with sensitive data redacted.

### 2. Staging or Controlled Tenant Test Plan

Use two authorized test tenants:

- Tenant A user attempts to access Tenant A invoice: expected `200`.
- Tenant A user attempts to access Tenant B invoice: expected `403` or `404`.
- Repeat across API, UI, exports, downloads, and admin paths.
- Verify object ownership is enforced server-side, not only in the UI.

### 3. Immediate Production Mitigations

Until validated:

- Ensure invoice reads enforce tenant ownership on the server side.
- Add centralized authorization middleware for invoice resources.
- Log denied cross-tenant access attempts.
- Temporarily restrict invoice access paths if suspicion is high.
- Review recent invoice access logs for anomalous tenant/account mismatches.

## Evidence Status

- **Finding:** Production testing has been requested against account IDs and tenant invoices.
- **Risk:** The proposed test could access another tenant’s data and create a privacy/security incident.
- **Evidence gap:** Written authorization, scoped test tenants, endpoints, and approved test window are missing.
- **Validation:** Perform testing only with approved accounts and written authorization, preferably first in staging or against controlled production test tenants.
