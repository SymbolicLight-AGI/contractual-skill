## Security Review: PATCH /projects/{projectId}/settings

**Scope:** Synthetic API design review only. No active scanning or tooling.

### 1. Finding: Missing Object-Level Authorization (IDOR)

**Severity:** Critical (CVSS 8.6 – High)

**Description:**  
The handler authenticates the user (verifies a valid session/token) but does **not** verify that the requested project (`{projectId}`) belongs to any of the user’s organizations. Because `projectId` is a direct object reference extracted from the URL, an authenticated attacker can enumerate or guess project IDs and modify settings for projects outside their organization.

**Attack Scenario:**
1. Legitimate User A belongs to Organization X and owns project `123`.
2. Attacker B belongs to Organization Y and has no relationship to project `123`.
3. Attacker B sends `PATCH /projects/123/settings` with a valid authentication token.
4. The handler only checks “is user logged in” → succeeds.
5. Project `123`’s `billingContactEmail` and `webhookUrl` are overwritten, causing financial loss, phishing, or data exfiltration.

This is a classic **Insecure Direct Object Reference (IDOR) / Broken Access Control (OWASP A01:2021)**.

### 2. Data Flow & Trust Boundary Trace

```
Client (authenticated user)
  → Middleware/Authentication Check (passes)
    → Handler: PATCH /projects/{projectId}/settings
      → No authorization check for project ↔ user’s organizations
      → Database update (billingContactEmail, webhookUrl)
```

The trust boundary is breached because the handler assumes authentication implies authorization. The project resource is global; any authenticated user can modify any project’s sensitive operational data.

### 3. Impact Analysis

- **Direct:** Unauthorized modification of billing contact email → possible invoice hijacking, domain verification abuse, or phishing.
- **Direct:** Unauthorized modification of webhook URL → arbitrary external calls, data exfiltration, server-side request forgery (SSRF) chaining if internal endpoints are reachable.
- **Reputational & Compliance:** Violation of least privilege, data integrity loss. Depending on data handled, may breach SOC 2 (common security criteria), ISO 27001 (access control), or GDPR principle of integrity and confidentiality.

### 4. Remediation

**Immediate fix:**  
Before applying the update, verify that the authenticated user’s authorized organizations include the project’s owning organization.

Example logical check:
```
project = getProjectById(projectId)
if not user.organizations.contains(project.organizationId):
    throw Forbidden
```

**Implementation considerations:**
- Use a **centralized authorization middleware** or a guard that loads the project and checks ownership before the controller runs, avoiding ad-hoc checks.
- For service accounts or admin SDKs, still enforce the same rule: **never bypass object ownership checks** even when using privileged database clients.
- Add a policy-as-code rule (e.g., OPA) that asserts every state-changing request to a project resource validates `resource.organizationId` is in `user.organizations`.
- Log and alert on forbidden attempts to help detect enumeration attacks.

### 5. Validation

After implementing:
- Write a test that authenticates as a user who does **not** own the project and asserts `403 Forbidden`.
- Include a negative test with a project ID from another organization.
- Ensure the authorization check cannot be bypassed by sending the user’s own organization ID in the request body (always read project-to-org mapping from the database, not from client input).

### 6. Residual Risk

If the project ID space is predictable, an attacker can still enumerate projects, but enforcement of the ownership check reduces the risk to “information disclosure of project existence” (low) instead of data modification (critical). Consider using non-sequential, unguessable project IDs (e.g., UUIDv4) to further limit enumeration.

---

**Conclusion:**  
The design, as supplied, contains a **critical authorization bypass**. Remediation must be implemented before deployment. This finding should be added to the project’s backlog and fixed with high priority.
