Scope confirmed: review only the supplied synthetic API design for authorization risks. No tools/scans performed. Findings are based only on the provided description.

## Reviewed Design

Endpoint: `PATCH /projects/{projectId}/settings`

Known behavior:

- User must be authenticated.
- Users may belong to multiple organizations.
- No explicit check is shown that `projectId` belongs to one of the user’s organizations.
- Request can modify:
  - `billingContactEmail`
  - `webhookUrl`

## Data Flow / Trust Boundary Review

Expected flow:

`Client → PATCH /projects/{projectId}/settings → Auth check → Project lookup/update → Storage`

Observed risk:

- The handler verifies login, but authentication alone does not prove authorization.
- `projectId` is supplied by the client and appears to be trusted without verifying tenant/org ownership.
- If the backend uses privileged database access, service accounts, or an Admin SDK, database-level security rules may be bypassed unless the handler enforces authorization explicitly.

## Key Authorization Risks

### 1. Missing Project Ownership / Organization Membership Check

**Severity: High**

The largest risk is Broken Access Control / IDOR/BOLA.

If the handler only checks that the user is logged in, any authenticated user may be able to guess or obtain another `projectId` and modify that project’s settings.

Example attack:

```http
PATCH /projects/victim-project-id/settings
Authorization: Bearer attacker-token

{
  "billingContactEmail": "attacker@example.com",
  "webhookUrl": "https://attacker.example/webhook"
}
```

If no ownership check exists, the attacker could modify another organization’s project settings.

### Impact

- Cross-tenant data modification.
- Account takeover support paths via changed billing contact email.
- Redirecting operational/security events to attacker-controlled infrastructure.
- Potential financial, compliance, or incident response impact.
- Loss of tenant isolation.

### Required Remediation

Before applying any update, verify:

1. The user is authenticated.
2. The project exists.
3. The project belongs to an organization.
4. The authenticated user is a member of that organization.
5. The user has a role/permission allowing project settings modification.

Example authorization logic:

```pseudo
user = requireAuthenticatedUser(request)

project = getProject(projectId)
if project == null:
    return 404

membership = getOrganizationMembership(user.id, project.organizationId)
if membership == null:
    return 404 or 403

if !membership.permissions.includes("project.settings.update"):
    return 403

updateProjectSettings(projectId, validatedInput)
```

Prefer returning `404` for unauthorized access if you want to avoid leaking whether a project exists.

---

### 2. Multi-Organization User Context Ambiguity

**Severity: Medium to High**

Because users can belong to multiple organizations, the API must ensure that the selected `projectId` is authorized under one of the user’s organizations.

Risky pattern:

```pseudo
if user.isLoggedIn:
    updateProject(projectId, body)
```

Safer pattern:

```pseudo
allowedOrgIds = getOrganizationsForUser(user.id)
project = getProject(projectId)

if project.organizationId not in allowedOrgIds:
    deny
```

Even better, enforce permission at the project or org level:

```pseudo
can(user, "update_project_settings", project)
```

### Required Remediation

Use explicit tenant-aware authorization checks. Do not rely on the client to provide `organizationId` unless it is validated against the project and the user’s membership.

---

### 3. Unauthorized Modification of `billingContactEmail`

**Severity: Medium to High**

`billingContactEmail` is sensitive business state. If modified by an unauthorized user, it may affect:

- Billing notifications.
- Payment/account recovery workflows.
- Invoice delivery.
- Audit/compliance contacts.
- Social engineering risk.

### Required Remediation

Restrict this field to specific roles, for example:

- Organization owner.
- Billing admin.
- Finance admin.

Add field-level authorization:

```pseudo
if body.includes("billingContactEmail"):
    requirePermission(user, project.organizationId, "billing.update")
```

Also consider:

- Audit logging old and new values.
- Email verification for new billing contact.
- Notification to existing owners/admins.
- Rate limiting and anomaly detection.

---

### 4. Unauthorized Modification of `webhookUrl`

**Severity: High**

`webhookUrl` can be security-sensitive. If an attacker can modify it, they may hijack outbound event delivery and receive sensitive project data.

Potential abuse:

- Exfiltrate event payloads.
- Capture internal workflow data.
- Redirect integrations to attacker-controlled endpoints.
- Cause SSRF if the backend later sends webhook requests to internal URLs.

Example dangerous values:

```text
http://127.0.0.1:8080/admin
http://169.254.169.254/latest/meta-data/
http://localhost:3000
http://internal-service.default.svc.cluster.local
```

### Required Remediation

Authorization:

```pseudo
if body.includes("webhookUrl"):
    requirePermission(user, project.organizationId, "webhook.manage")
```

Input security:

- Require HTTPS.
- Block localhost, private IP ranges, link-local addresses, and cloud metadata IPs.
- Resolve DNS and validate resolved IPs.
- Protect against DNS rebinding by validating at registration and delivery time.
- Consider allowlists for enterprise deployments.
- Send a verification challenge before enabling a new webhook URL.
- Avoid sending secrets in webhook payloads unless the endpoint is verified.

---

## Recommended Authorization Model

For this endpoint, use layered checks:

```pseudo
PATCH /projects/{projectId}/settings

1. Authenticate user.
2. Load project by projectId.
3. Verify project belongs to an organization.
4. Verify user is a member of that organization.
5. Verify user has permission to modify project settings.
6. Apply field-level authorization:
   - billingContactEmail requires billing/admin permission.
   - webhookUrl requires integration/webhook management permission.
7. Validate input.
8. Update using server-side trusted project/org context.
9. Write audit log.
```

## Suggested Policy

Example permissions:

| Field | Required Permission |
|---|---|
| `billingContactEmail` | `billing.update` or `org.owner` |
| `webhookUrl` | `webhook.manage` or `project.admin` |
| Other project settings | `project.settings.update` |

## Audit Logging Requirements

Log every successful and failed sensitive update attempt:

- User ID.
- Organization ID.
- Project ID.
- Changed fields.
- Previous and new values where safe.
- Source IP / user agent.
- Timestamp.
- Authorization decision.
- Request ID.

Avoid logging secrets or sensitive webhook payloads.

## Primary Finding Summary

| Finding | Severity | Risk |
|---|---:|---|
| No explicit project-to-user organization authorization check | High | Cross-tenant IDOR/BOLA |
| Multi-org user context not clearly enforced | Medium/High | Wrong-tenant modification |
| `billingContactEmail` lacks field-level authorization | Medium/High | Billing/contact hijack |
| `webhookUrl` can be hijacked or abused for SSRF/data exfiltration | High | Event exfiltration and infrastructure targeting |

## Final Assessment

The design has a significant authorization risk because it authenticates the user but does not explicitly authorize the user against the target `projectId`. This is a classic IDOR/BOLA issue, especially dangerous in a multi-organization system.

Minimum required fix: before updating settings, verify that the project belongs to an organization the authenticated user belongs to, and that the user has the appropriate role or permission to modify each requested field.
