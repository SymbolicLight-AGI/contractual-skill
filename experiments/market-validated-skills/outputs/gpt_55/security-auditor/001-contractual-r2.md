## Scope And Authorization

- **Scope:** Review only the supplied synthetic API design for authorization risks.
- **Asset in scope:** `PATCH /projects/{projectId}/settings`
- **Testing boundary:** No tools, scans, exploit attempts, or production activity.
- **Assumption:** The material is synthetic and provided for authorized design review.

## Executive Summary

The design shows a likely **authorization gap**: the handler authenticates the user but does not explicitly verify that the target `projectId` belongs to one of the user’s organizations. Because authenticated users can belong to multiple organizations, and the endpoint modifies sensitive project settings, this creates a potential **IDOR / broken object-level authorization** risk.

The endpoint can change `billingContactEmail` and `webhookUrl`, which may have billing, notification, data exfiltration, phishing, or integration abuse implications if modified by an unauthorized user.

## Findings By Severity

### High: Missing Project-to-User Organization Authorization Check

**Finding:**  
The handler checks that the user is logged in, but the supplied design does not show an explicit check that the requested `projectId` belongs to one of the user’s authorized organizations.

**Evidence:**  
- Endpoint: `PATCH /projects/{projectId}/settings`
- Authenticated users can belong to multiple organizations.
- Handler checks login only.
- No explicit project ownership or organization membership authorization check is shown.

**Risk:**  
An authenticated user may be able to modify settings for a project outside their authorized organization by guessing or obtaining another valid `projectId`.

Potential business and technical impacts include:

- Unauthorized modification of project billing contact information.
- Unauthorized redirection of webhook traffic.
- Cross-tenant data exposure or manipulation.
- Tenant isolation failure.
- Compliance and customer trust impact if projects belong to different customers or organizations.

**Likelihood:** Medium to High, depending on whether `projectId` values are guessable or exposed elsewhere in the application.

**Severity:** High, because this affects cross-tenant authorization and modifies sensitive settings.

**Remediation:**  
Add an explicit object-level authorization check before applying updates.

Example control logic:

```pseudo
user = requireAuthenticatedUser(request)

project = getProject(projectId)

if project == null:
    return 404

if project.organizationId not in user.organizationIds:
    return 403

if user lacks required role for project settings update:
    return 403

updateProjectSettings(projectId, allowedSettings)
```

Recommended checks:

1. Verify the project exists.
2. Verify the project belongs to an organization the user is a member of.
3. Verify the user has the correct role or permission within that organization, such as `project_admin`, `org_admin`, or `settings:write`.
4. Only then allow updates to `billingContactEmail` and `webhookUrl`.

---

### Medium: Sensitive Settings Can Be Modified Without Field-Level Authorization Mentioned

**Finding:**  
The endpoint can modify `billingContactEmail` and `webhookUrl`, but the design does not mention field-level authorization or role requirements.

**Evidence:**  
- Request can change `billingContactEmail`.
- Request can change `webhookUrl`.
- Only login check is described.

**Risk:**  
Even if the user belongs to the project’s organization, not every organization member should necessarily be allowed to modify billing or integration settings.

Potential impacts:

- Billing notifications redirected to an attacker-controlled address.
- Webhooks redirected to an attacker-controlled endpoint.
- Loss of operational visibility.
- Phishing or social engineering risk.
- Unauthorized exposure of event payloads sent to the webhook URL.

**Likelihood:** Medium, depending on organization role model.

**Severity:** Medium to High, depending on webhook contents and billing workflow sensitivity.

**Remediation:**  
Require specific permissions for sensitive fields.

Suggested permission model:

| Field | Suggested Permission |
|---|---|
| `billingContactEmail` | `billing:update` or `org_billing_admin` |
| `webhookUrl` | `integrations:update` or `project_admin` |

Also consider separating billing and webhook settings into distinct endpoints if they have different authorization requirements.

---

### Medium: Webhook URL Update May Enable Data Exfiltration or SSRF-Like Abuse

**Hypothesis:**  
If the application later sends sensitive event data to `webhookUrl`, an attacker with unauthorized or excessive access could redirect webhook delivery to an external endpoint they control.

**Evidence:**  
- The endpoint can change `webhookUrl`.
- The design does not describe webhook URL validation, ownership confirmation, or delivery restrictions.

**Risk:**  
Depending on webhook payload contents, unauthorized webhook changes could expose project events, customer data, internal identifiers, or operational metadata.

If the server later calls arbitrary webhook URLs, additional risks may include:

- Requests to internal network locations.
- Abuse of server-side request capabilities.
- Exfiltration of webhook payloads.

**Severity:** Medium, potentially High if webhook payloads contain sensitive data or internal network access is possible.

**Remediation:**  

- Validate `webhookUrl` scheme: allow only `https://`.
- Block localhost, link-local, private IP ranges, and internal hostnames.
- Consider requiring webhook endpoint verification before activation.
- Log webhook URL changes.
- Notify organization admins when webhook settings change.
- Redact secrets from webhook payloads.
- Apply egress controls for webhook delivery workers.

## Evidence

The assessment is based only on the supplied design:

```text
Endpoint: PATCH /projects/{projectId}/settings

Authenticated users can belong to multiple organizations.

The handler checks that the user is logged in.

The handler does not show an explicit check that the project belongs to one of the user's organizations.

The request can change billingContactEmail and webhookUrl.
```

No code, logs, access control matrix, role model, or test results were provided.

## Remediation Plan

Recommended priority order:

1. **Add object-level authorization**
   - Confirm the `projectId` belongs to an organization accessible to the authenticated user.

2. **Add role-based or permission-based checks**
   - Require specific permissions for project settings changes.
   - Use stricter permissions for billing and integration settings.

3. **Restrict mutable fields**
   - Use an allowlist for fields accepted by this endpoint.
   - Reject unexpected fields.

4. **Validate sensitive field values**
   - Validate `billingContactEmail` format and domain policy if applicable.
   - Validate `webhookUrl` scheme, hostname, and network destination.

5. **Add audit logging**
   - Log actor user ID, organization ID, project ID, changed fields, timestamp, and request origin.
   - Do not log sensitive tokens or secrets.

6. **Notify appropriate administrators**
   - Send notification when billing contact or webhook URL changes.

7. **Consider approval or verification workflows**
   - Require webhook ownership verification before enabling delivery.
   - Consider email confirmation for billing contact changes.

## Validation Steps

Safe non-intrusive validation steps:

1. Review the handler implementation and confirm whether it checks:
   - User authentication.
   - Project existence.
   - Project organization ownership.
   - User membership in that organization.
   - User role or permission for settings updates.

2. Review the data model:
   - Confirm `project.organizationId` exists.
   - Confirm user-to-organization membership is authoritative.
   - Confirm role information is available and enforced.

3. Review tests:
   - Add a test where User A from Org A attempts to patch a project from Org B.
   - Expected result: `403 Forbidden` or equivalent denial.
   - Add a test where an org member without billing permissions changes `billingContactEmail`.
   - Expected result: denial.
   - Add a test where an org member without integration permissions changes `webhookUrl`.
   - Expected result: denial.

4. Review webhook delivery controls:
   - Confirm private IP ranges and internal hostnames are blocked.
   - Confirm only HTTPS URLs are accepted.
   - Confirm webhook changes are audited.

## Residual Risk

Even after adding authorization checks, residual risk remains if:

- Organization membership data is stale or incorrectly synchronized.
- Role definitions are too broad.
- Webhook payloads include sensitive data unnecessarily.
- Audit logs are not monitored.
- Project IDs are exposed broadly and access control relies only on obscurity.

## Open Questions

1. What roles exist within an organization?
2. Are all organization members allowed to update project settings?
3. Are billing settings and webhook settings intended to have different permissions?
4. Are `projectId` values UUIDs, sequential IDs, or otherwise guessable?
5. What data is sent to the configured `webhookUrl`?
6. Are webhook destinations validated or verified before activation?
7. Are changes to billing and webhook settings audited and alerted?

## Handoff

If this design applies to a production or multi-tenant system, hand off to:

- Engineering owner for access control remediation.
- Security team for authorization model review.
- Compliance or privacy owner if webhook payloads may contain regulated or customer data.
- Product owner for deciding whether billing and integration settings require separate administrative permissions.
