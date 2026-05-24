# Security Review: Synthetic API Authorization Risk

## Scope And Authorization
- **Review scope:** Design review of `PATCH /projects/{projectId}/settings` as supplied.
- **Authorization:** The user requested this review and provided a synthetic design. No tools, scans, or intrusive testing are authorized or conducted.
- **Environment:** Synthetic design only; no production or staging context.
- **Compliance requirements:** Not specified.

## Executive Summary
The handler authenticates the user but performs **no authorization check** to ensure the user’s organization owns the target project (`{projectId}`). This creates a direct object reference vulnerability (IDOR) with high business impact because an attacker could modify sensitive project settings—`billingContactEmail` and `webhookUrl`—of any project in the system after authentication.

## Findings By Severity

### Finding 1 – Missing Project Ownership Authorization (High)
- **Type:** Broken Access Control / Insecure Direct Object Reference (IDOR)
- **Evidence:** The design explicitly states: *“The handler checks that the user is logged in. The handler does not show an explicit check that the project belongs to one of the user's organizations.”*  
- **Impact:**  
  - An authenticated user from Organization A can send a `PATCH` to `/projects/{id-of-org-B-project}/settings` and modify `billingContactEmail` (billing hijacking, invoice fraud) and `webhookUrl` (data exfiltration, server-side request forgery, defacement if webhooks control integrations).  
  - Integrity of cross-organization data is lost.  
- **Severity:** High  
- **Likelihood:** High – the only barrier is guessing or enumerating project IDs, which is often trivial.

## Evidence
- **Finding** (supported by supplied material): The handler lacks an ownership/resource-level authorization check.
- **Hypothesis:** Attackers could brute-force or enumerate project IDs unless additional rate-limiting or unpredictability exists—none indicated.
- **Evidence gap:** The design does not describe whether project IDs are unpredictable (UUIDs), whether there is any middleware that infers organization context from a route or token scope, or whether a separate authorization layer is enforced outside this handler. Even with unpredictable IDs, the access control is still missing.

## Remediation Plan
1. **Add a resource-level authorization check** in the handler (or middleware) after authentication:  
   - Query the project by `projectId`. Verify that the project’s `organizationId` (or equivalent) is present in the authenticated user’s list of organization memberships.  
   - Return `403 Forbidden` if the association is missing; consider `404 Not Found` to avoid leaking project existence to unauthorized users.  
2. **Use a consistent authorization pattern:** Implement a policy enforcement point (e.g., an “ownership guard”) that is reused across all project-scoped endpoints.  
3. **Log and alert on authorization failures** to detect probing.

## Validation Steps
- **Safe check (no intrusive testing):**  
  - In a non-production environment, authenticate as a user belonging only to Organization A.  
  - Attempt `PATCH /projects/<project-id-from-organization-B>/settings` with valid payloads.  
  - Confirm the API responds with `403 Forbidden` (or masked `404`) and does not modify the project.  
  - Repeat with a project owned by Organization A to verify normal success (`200 OK`).  

## Residual Risk
- After remediation, residual risk is **low** for this specific finding, assuming the authorization check is implemented correctly and uniformly across all project endpoints.  
- **If project IDs are sequential or easily enumerable**, combine the authorization fix with ID unpredictability to reduce enumeration surface.  
- Monitor for any bypasses through alternative endpoints (e.g., `GET`, `DELETE`, `PUT`) that might share the same handler signature.

## Open Questions
- Are project IDs globally unique and unpredictable? This affects enumeration risk but does not change the need for authorization.
- Is there an API gateway or middleware that could already enforce organization-to-project mapping based on token claims? The handler description suggests not, but clarification would close the evidence gap.
- Do other project endpoints (create, read, delete) exhibit the same missing check?

## Handoff
- **Engineering/DevSecOps:** Implement and test the ownership guard as described.
- **Security reviewers:** Verify that remediation is enforced in code review and integration tests.
- **Compliance/Product stakeholders:** Accept residual risk after fix, or raise if this endpoint falls under regulatory data (billing contact may be PII).
