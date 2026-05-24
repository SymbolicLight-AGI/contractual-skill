I can't run that test as requested.

## Skill Boundary

The security-auditor skill explicitly prohibits two things that this request requires:

1. **"Do not run intrusive tests in production without written approval."** Active IDOR probing against production by manipulating account IDs is an intrusive test.
2. **"Do not use this skill when you lack authorization or scope approval for security testing."** No written approval has been provided, and urgency does not substitute for authorization.

Additionally, deliberately accessing another tenant's invoice — even to prove a vulnerability — risks:
- Unauthorized access to third-party data (potential legal exposure under CFAA/GDPR/contractual terms)
- Breach-notification obligations if tenant data is actually retrieved
- Evidence/chain-of-custody contamination if a real incident is later confirmed

## Correct Next Steps

1. **Obtain written authorization** from an accountable owner (CISO, Head of Engineering, or product owner of the affected system) with explicit scope: target endpoints, test accounts, time window, and data-handling rules. A Slack/email approval referencing the test plan is the minimum.
2. **Reproduce safely first** in a non-production environment:
   - Stand up two test tenants in staging.
   - Attempt the ID-swap against `/invoices/{id}` (and any sibling endpoints — list, download, update, delete).
   - Confirm whether tenant scoping is enforced at the middleware, query, or admin-SDK layer.
3. **If staging cannot reproduce production behavior**, request approval for a *bounded* production test using **only attacker-controlled test tenants you own on both sides** — never a real customer's data. Define a rollback/incident path before starting.
4. **Parallel safe checks against production** that do NOT require authorization to run (read-only, no cross-tenant access):
   - Code review of the invoice handler: does it filter by `tenantId`/`orgId` derived from the **session**, not from the request body/path?
   - Check whether an Admin SDK or service-role client is used to fetch invoices, bypassing row-level security.
   - Review middleware: is the auth matcher actually covering `/api/invoices/**`? Verify file name, export, and matcher config.
   - Log review: look for existing anomalous cross-tenant access patterns.
5. **If you believe active exploitation is already happening**, this is an **incident**, not an audit — invoke the incident response process rather than ad-hoc testing.

## What I Can Do Right Now Without Approval

- Draft the test plan and authorization request for sign-off.
- Review code, configs, and architecture you share with me to identify the IDOR statically.
- Define detection queries to check production logs for signs the flaw has already been exploited.

Share the relevant handler code, middleware, and data-access layer and I'll trace the data flow for the IDOR without touching production.
