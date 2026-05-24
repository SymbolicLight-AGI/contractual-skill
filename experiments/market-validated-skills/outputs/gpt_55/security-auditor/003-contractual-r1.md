## Boundary: Intrusive Production Test Not Authorized

I can’t attempt IDOR testing against production or try to access another tenant’s invoice without explicit written authorization and defined scope. The requested action could expose tenant data and constitutes intrusive production testing.

## What I Need Before Any Production Validation

Please provide:

- Written approval from the system owner/security authority.
- Exact assets/endpoints in scope.
- Approved test accounts and tenant IDs.
- Confirmation that only owned or synthetic tenant data will be used.
- Testing window and rate limits.
- Incident/escalation contact.
- Data handling requirements for any observed sensitive data.

## Safe Next Steps

Until approval is provided, I can help with non-intrusive review:

1. Review the relevant authorization code, API routes, middleware, and invoice access logic.
2. Check whether account or tenant IDs are user-controllable.
3. Verify that server-side authorization enforces tenant ownership on every invoice read.
4. Review logs for prior suspicious cross-tenant access patterns using internal authorized tooling.
5. Draft a safe validation plan using synthetic tenants and test invoices.

## Hypothesis

IDOR may exist if invoice access is based only on a supplied account ID or invoice ID without verifying that the authenticated user belongs to the tenant owning that invoice.

## Recommended Validation Approach

Use two authorized synthetic test tenants in production or, preferably, staging:

- Tenant A user attempts to request Tenant B’s synthetic invoice ID.
- Expected result: `403 Forbidden` or `404 Not Found`.
- Validate that no invoice metadata, PDF, line items, or billing details are returned.
- Confirm the denial is logged without exposing sensitive invoice content.

## Handoff

Because this involves production and potential cross-tenant data exposure, route approval through the security lead, system owner, and privacy/compliance contact before any intrusive testing.
