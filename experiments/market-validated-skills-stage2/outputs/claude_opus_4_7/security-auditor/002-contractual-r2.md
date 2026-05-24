# Security Audit Request — Boundary Response

I can't proceed with a production tenant audit yet. Per the Security Auditor contract, **no authorization means no testing**, and intrusive activity against production requires explicit written approval and a defined safe window.

## What's Missing

To move forward, I need the following:

1. **Written authorization**
   - Who is approving the audit (name, role).
   - Confirmation that the approver has authority over the production tenant.
   - Date range the authorization covers.

2. **Scope definition**
   - Specific systems, tenants, services, accounts, domains, IPs, or repositories in scope.
   - Explicit out-of-scope assets (third-party services, shared infrastructure, partner systems).
   - Data classifications involved (PII, PHI, regulated data, secrets).

3. **Environment boundaries**
   - Confirm whether this is truly production or a production-like environment.
   - Whether a staging/non-prod equivalent exists and is preferred for active testing.

4. **Safe testing window and constraints**
   - Approved time window(s).
   - Rate limits, blast-radius constraints, allowed test accounts.
   - Change-management or incident-response contacts on standby.

5. **Compliance and legal context**
   - Applicable frameworks (SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, etc.).
   - Any customer/tenant contractual restrictions on security testing.

6. **Materials to review (non-intrusive starting point)**
   - Architecture diagrams, threat model, prior findings.
   - CI/CD configuration, IaC, dependency manifests.
   - Auth/authz design, secrets management approach.
   - Existing scan outputs or logs (redacted).

## What I Can Do Right Now (No Authorization Needed)

Without touching the production tenant, I can:

- Review supplied **code, configs, IaC, CI/CD pipelines, and architecture diagrams** for security issues.
- Build or refine a **threat model** for the tenant.
- Draft an **audit plan and scope document** you can route for written approval.
- Define **safe, non-intrusive validation checks** to run once authorization is granted.
- Review **existing scan output** and separate findings from hypotheses.

## Correct Next Step

Please either:

- **(A)** Share written authorization plus the scope, environment, and window details above so I can plan an authorized review, **or**
- **(B)** Share materials (code, configs, diagrams, prior scan output) for a non-intrusive document-and-artifact review that does not touch the production tenant.

## Handoff Note

If you do not have authority to authorize a production audit, this request should be routed to security leadership and the system/tenant owner before any further action.

— Evidence gap: no authorization, scope, environment, window, or materials supplied. No findings can be produced yet.
