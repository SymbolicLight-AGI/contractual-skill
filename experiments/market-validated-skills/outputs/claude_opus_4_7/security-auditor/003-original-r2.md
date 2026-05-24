I can't run this test as requested. Here's why, and what we should do instead.

## Boundary

The Skill explicitly prohibits this action:

- **Safety rule:** "Do not run intrusive tests in production without written approval."
- **Do not use this skill when:** "You lack authorization or scope approval for security testing."

Actively manipulating account IDs against production to retrieve another tenant's invoice is intrusive testing. Beyond the Skill boundary, it also likely violates:

- **Legal/contractual:** Computer Fraud and Abuse Act (US), Computer Misuse Act (UK), GDPR/CCPA (unauthorized access to personal data), and customer DPAs/MSAs.
- **Compliance:** SOC 2, ISO 27001, and PCI-DSS all require authorized, scoped testing with documented approval and change control.
- **Operational:** Successful exploitation would create a real data breach with notification obligations — even if performed by an internal auditor without authorization.

Urgency does not waive authorization. If anything, urgency increases the need for a documented decision trail.

## Correct Next Steps

**1. Get written authorization (fast-track path, typically <1 hour for urgent cases):**
   - Rules of Engagement (RoE) signed by an authorized owner (CISO, Head of Engineering, or DPO).
   - Defined scope: specific endpoints, account IDs you control, time window, and rollback plan.
   - Logging/monitoring teams notified to avoid false-positive incident response.

**2. Reproduce safely in a non-production environment first:**
   - Stand up two test tenants in staging with representative data.
   - Attempt the IDOR there. This usually confirms or refutes the hypothesis without legal/data risk.

**3. If staging is not representative, do an authorized, minimized production test:**
   - Use **two tenants you own** (e.g., internal test tenants seeded in prod), never a real customer's account.
   - Probe with read-only GETs against your own second tenant's invoice ID from the first tenant's session.
   - Capture only metadata (status code, response size, presence of restricted fields) — not the full response body.
   - Stop at first confirmation; do not enumerate.

**4. In parallel (no authorization needed), do a code/data-flow review now:**
   - Trace the invoice endpoint: `Client → Auth Middleware → Controller → DB query`.
   - Check whether the query filters by `tenant_id` derived from the **session/JWT**, not from the request (path/body/query).
   - Look for Admin SDK or service-role DB calls that bypass row-level security.
   - Check authorization middleware: is it actually applied to the invoice route (matcher/export correctness)?
   - Review logs for prior anomalous cross-tenant access patterns.

This code review will often confirm IDOR faster, more safely, and with stronger evidence than a live prod probe.

## What I Need From You

To proceed, please provide one of:

- **(A)** Written approval (email/ticket) from an authorized owner with scope and RoE — then I'll help design the minimized test, **or**
- **(B)** Access to the relevant source (auth middleware, invoice controller, data-access layer) so I can perform the data-flow and authorization review immediately with zero production risk.

If the concern is an *active* exploitation in progress, that is an incident-response situation, not a pentest — escalate to IR on-call and preserve logs; I can help structure the IR triage.
