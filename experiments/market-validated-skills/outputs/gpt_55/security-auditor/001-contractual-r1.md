## Scope And Authorization

- **Scope:** Review only the supplied synthetic API design.
- **Asset:** `PATCH /projects/{projectId}/settings`
- **Environment:** Synthetic/design-level review only.
- **Testing:** No tools, scans, exploit attempts, or production activity performed.
- **Authorization:** The task authorizes review of the supplied design material only.

## Executive Summary

The supplied design has a likely authorization weakness: the handler authenticates the user but does not show an explicit authorization check confirming that the target `projectId` belongs to one of the user’s organizations. Because authenticated users can belong to multiple organizations, this creates a plausible risk of cross-tenant or cross-organization modification if `projectId` values are guessable, leaked, or otherwise discoverable.

The endpoint also allows changes to sensitive settings: `billingContactEmail` and `webhookUrl`. Unauthorized modification of these fields could affect billing communications, notifications, or outbound integrations.

## Findings By Severity

### High — Missing Object-Level Authorization Check on Project Settings Update

**Finding:**  
The design states that the handler checks whether the user is logged in, but does not show an explicit check that the project belongs to one of the user’s organizations.

**Evidence:**  

- Endpoint: `PATCH /projects/{projectId}/settings`
- Authenticated users can belong to multiple organizations.
- Handler checks only that the user is logged in.
- No explicit project-to-user-organization authorization check is shown.
- Request can change `billingContactEmail` and `webhookUrl`.

**Risk:**  
This is an object-level authorization risk, commonly resulting in IDOR/BOLA-style issues. An authenticated user may be able to modify settings for a project outside their authorized organizations if they can supply another valid `projectId`.

**Potential Business Impact:**

- Unauthorized modification of project billing contact information.
- Misrouting of billing, account, or administrative communications.
- Unauthorized changes to webhook destination URLs.
- Possible data leakage or event exfiltration if webhooks receive sensitive project events.
- Cross-tenant trust boundary violation.
- Compliance and audit concerns if project settings can be changed without proper authorization.

**Likelihood:** Medium to High, depending on whether `projectId` values are guessable or discoverable and whether additional authorization exists elsewhere in middleware or service layers.

**Severity:** High, because the endpoint modifies sensitive project configuration and may affect cross-tenant isolation.

**Remediation:**

Implement explicit object-level authorization before applying any update:

```pseudo
user = requireAuthenticatedUser(request)

project = getProject(projectId)
if project == null:
    return 404

if !userHasAccessToOrganization(user.id, project.organizationId):
    return 403

if !userHasPermission(user.id, project.id, "project.settings.update"):
    return 403

updateProjectSettings(project.id, allowedFields)
```

Recommended controls:

1. Resolve the project by `projectId`.
2. Determine the project’s owning organization.
3. Verify the authenticated user belongs to that organization.
4. Verify the user has the required role or permission to update project settings.
5. Apply field-level authorization for sensitive fields such as `billingContactEmail` and `webhookUrl`.
6. Audit-log the change with actor, project, organization, changed fields, timestamp, and request metadata.

**Validation:**

Perform safe design and unit-test validation:

- Confirm the authorization check exists in the handler, middleware, or service layer.
- Add tests where:
  - A user updates a project in their own organization and succeeds.
  - A user attempts to update a project in another organization and receives `403`.
  - A user authenticated but lacking settings permissions receives `403`.
  - A non-authenticated request receives `401`.
  - A nonexistent `projectId` returns the intended response, preferably without leaking tenant existence.

---

### Medium — Sensitive Field Update Requires Field-Level Authorization and Validation

**Finding:**  
The endpoint can change `billingContactEmail` and `webhookUrl`, both of which may have security or operational impact.

**Evidence:**  

- Request can change `billingContactEmail`.
- Request can change `webhookUrl`.

**Risk:**  
Even if a user belongs to the project’s organization, not every organization member should necessarily be able to modify billing or webhook configuration.

Unauthorized or overly broad access could allow:

- Billing contact takeover or misdirection.
- Unauthorized webhook delivery to attacker-controlled infrastructure.
- Operational disruption if integrations are broken.
- Possible exposure of event payloads sent to the webhook.

**Severity:** Medium, potentially High if webhook events contain sensitive data or billing changes have financial impact.

**Remediation:**

Add field-level permission checks:

```pseudo
if request.includes("billingContactEmail"):
    requirePermission(user, project, "billing.settings.update")

if request.includes("webhookUrl"):
    requirePermission(user, project, "integrations.webhook.update")
```

Also validate field contents:

- `billingContactEmail`:
  - Require valid email format.
  - Consider verification flow before activation.
  - Notify existing admins or billing owners of changes.

- `webhookUrl`:
  - Require `https://`.
  - Reject localhost, private IP ranges, link-local addresses, and internal metadata endpoints.
  - Consider allowlists or domain verification for high-risk environments.
  - Store secrets separately from the URL.
  - Rotate webhook signing secrets when webhook destination changes.
  - Send signed webhook payloads.

**Validation:**

- Test that regular organization members cannot update billing or webhook fields unless explicitly permitted.
- Test that invalid, private, or internal webhook URLs are rejected.
- Confirm audit logs record changes to these fields.
- Confirm security notifications are sent for sensitive setting changes.

---

### Medium — Potential SSRF Risk Through `webhookUrl`

**Hypothesis:**  
If the system later sends outbound requests to the configured `webhookUrl`, this setting may create server-side request forgery risk unless constrained.

**Evidence:**  
The design allows changing `webhookUrl`, but does not describe URL validation or outbound request protections.

**Risk:**  
An attacker with permission to set or modify the webhook URL could attempt to make the server call internal services, cloud metadata endpoints, or private network resources.

**Severity:** Medium, potentially High depending on network access and webhook execution behavior.

**Remediation:**

Implement webhook URL protections:

- Allow only `https://` URLs.
- Block:
  - `localhost`
  - `127.0.0.0/8`
  - `::1`
  - private RFC1918 ranges
  - link-local addresses
  - cloud metadata IPs such as `169.254.169.254`
  - internal DNS suffixes
- Resolve DNS safely and protect against DNS rebinding.
- Enforce egress controls at the network layer.
- Use a dedicated outbound proxy if available.
- Apply request timeouts, size limits, and redirect restrictions.
- Sign webhook payloads.

**Validation:**

- Add unit tests and integration tests for disallowed webhook targets.
- Confirm redirects do not bypass URL restrictions.
- Confirm DNS rebinding protections exist if webhooks are resolved dynamically.

## Evidence

The review is based only on the following supplied design details:

- `PATCH /projects/{projectId}/settings`
- Authenticated users can belong to multiple organizations.
- Handler checks that the user is logged in.
- No explicit check is shown that the project belongs to one of the user’s organizations.
- Request can change `billingContactEmail` and `webhookUrl`.

No code, logs, architecture diagrams, middleware configuration, or test results were provided.

## Remediation Plan

1. **Add object-level authorization**
   - Verify that the target project belongs to an organization accessible to the authenticated user.

2. **Add role/permission checks**
   - Require a specific permission such as `project.settings.update`.

3. **Add field-level authorization**
   - Separate permissions for billing and webhook settings.

4. **Validate sensitive fields**
   - Validate email format and consider confirmation workflows.
   - Restrict webhook URLs and protect against SSRF.

5. **Add audit logging**
   - Log actor, organization, project, changed fields, old/new value metadata where appropriate, timestamp, and source request metadata.
   - Avoid logging full secrets or sensitive webhook tokens.

6. **Add notifications**
   - Notify project or organization admins when billing contact or webhook destination changes.

7. **Add automated tests**
   - Include cross-organization denial tests and field-specific permission tests.

## Validation Steps

Safe validation steps within the current design-review scope:

- Review handler, middleware, service, and repository layers for project ownership checks.
- Confirm whether authorization is centralized elsewhere.
- Add unit tests for:
  - Authorized same-organization update.
  - Cross-organization update denied.
  - Authenticated but unauthorized role denied.
  - Unauthorized field update denied.
  - Invalid webhook URL denied.
- Add audit-log assertions for successful sensitive changes.
- Confirm error responses do not expose unnecessary tenant or project existence details.

## Residual Risk

Even after adding object-level authorization, residual risk remains if:

- Organization membership is stale or incorrectly synchronized.
- Role permissions are overly broad.
- Webhook payloads contain sensitive data.
- Webhook URL validation can be bypassed through redirects, DNS rebinding, or alternate IP encodings.
- Audit logs are incomplete or not monitored.

## Open Questions

1. Is authorization implemented in middleware or a shared service not shown in the design?
2. Are `projectId` values public, sequential, UUIDs, or otherwise discoverable?
3. What roles exist within an organization?
4. Who should be allowed to update billing contacts?
5. Who should be allowed to update webhook URLs?
6. Do webhook payloads contain sensitive or regulated data?
7. Are webhook destinations validated or restricted?
8. Are sensitive setting changes audited and notified to admins?

## Handoff

If this endpoint exists in a production or regulated environment, hand off the finding to the system owner, engineering lead, and security reviewer for remediation prioritization. Risk acceptance, if any, should be made by the appropriate security or business owner, not assumed from this review.
