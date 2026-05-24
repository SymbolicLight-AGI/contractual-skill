## Scope Confirmed

Reviewed only the supplied synthetic API design:

- Endpoint: `PATCH /projects/{projectId}/settings`
- Authenticated users may belong to multiple organizations
- Handler verifies only that the user is logged in
- No explicit authorization check that the `projectId` belongs to one of the user’s organizations
- Mutable fields: `billingContactEmail`, `webhookUrl`
- No tools or scans performed

## Data Flow / Trust Boundary Review

Likely flow:

`Client request → Auth check → PATCH handler → Project settings update → Database`

The key authorization risk is at the transition from authenticated request to privileged update logic. If the backend uses a service account, ORM, or Admin SDK to update the database, normal database-level security rules may be bypassed. Therefore, the API handler itself must enforce object-level authorization before updating project settings.

## Primary Finding: Missing Object-Level Authorization / IDOR

**Severity: High**

The handler checks that the user is authenticated but does not explicitly verify that the requested `projectId` belongs to an organization the user is authorized to manage.

This creates an **Insecure Direct Object Reference, or IDOR**, risk.

### Attack Scenario

An authenticated user from Organization A sends:

```http
PATCH /projects/project-from-org-b/settings
```

If the backend only checks login status, the attacker may be able to modify settings for a project in another organization.

### Impact

An attacker could potentially:

- Change another organization’s billing contact email
- Redirect operational or billing notifications
- Modify webhook delivery targets
- Disrupt integrations
- Exfiltrate event data sent to webhooks
- Hijack business workflows
- Cause reputational, financial, or compliance impact

## High-Risk Field: `webhookUrl`

**Severity: High**

Allowing users to update `webhookUrl` has additional security implications.

### Risks

1. **Webhook hijacking**
   - Attacker changes a victim project’s webhook URL to an attacker-controlled endpoint.
   - Future project events may be sent to the attacker.

2. **Data exfiltration**
   - Webhooks often contain sensitive metadata, billing events, user activity, or internal identifiers.

3. **SSRF risk**
   - If the system later sends outbound requests to the configured `webhookUrl`, an attacker may set it to internal infrastructure, for example:
     - `http://localhost`
     - `http://169.254.169.254`
     - Internal service discovery addresses
     - Private RFC1918 IP ranges

4. **DNS rebinding risk**
   - A hostname may initially resolve to a public IP and later resolve to an internal IP unless DNS resolution and IP pinning protections are used.

## Medium-Risk Field: `billingContactEmail`

**Severity: Medium**

Changing `billingContactEmail` may allow an attacker to:

- Redirect invoices or billing notices
- Interfere with account recovery or billing workflows
- Social-engineer support teams
- Hide payment failures or administrative alerts from the legitimate owner

Severity depends on whether this email is used only for notification or also for account verification, billing authorization, or ownership workflows.

## Required Authorization Control

Before applying the patch, the handler should verify:

1. The user is authenticated.
2. The `projectId` exists.
3. The project belongs to an organization the user belongs to.
4. The user has the required role or permission for that organization/project.
5. The user is authorized to update each requested field.

Example authorization requirement:

```text
User must have project.settings.update permission for the organization that owns projectId.
```

A safer logical flow:

```text
Load authenticated user
Load project by projectId
Verify project.organizationId is in user's authorized organizations
Verify user has settings update permission for that project/org
Validate requested fields
Apply update
Audit log the change
```

## Recommended Remediations

### 1. Add explicit project ownership and permission checks

Do not rely on authentication alone.

Example pseudocode:

```ts
const user = requireAuthenticatedUser(request);

const project = await db.projects.findById(projectId);

if (!project) {
  return notFound();
}

const membership = await db.organizationMembers.findOne({
  userId: user.id,
  organizationId: project.organizationId,
});

if (!membership) {
  return forbidden();
}

if (!hasPermission(membership.role, "project.settings.update")) {
  return forbidden();
}

await updateProjectSettings(projectId, validatedInput);
```

### 2. Enforce field-level authorization

Some users may be allowed to update general settings but not billing or webhook settings.

Recommended split:

- `billingContactEmail` requires `billing.settings.update`
- `webhookUrl` requires `integrations.webhook.update`

### 3. Validate and constrain `webhookUrl`

Implement strict URL validation:

- Allow only `https://`
- Reject localhost and loopback addresses
- Reject private IP ranges
- Reject link-local addresses such as cloud metadata endpoints
- Reject non-HTTP schemes such as `file://`, `gopher://`, `ftp://`
- Resolve DNS server-side and block internal/private results
- Use DNS rebinding protections and IP pinning
- Consider requiring webhook ownership verification before activation

### 4. Add audit logging

Log security-relevant setting changes:

- Actor user ID
- Organization ID
- Project ID
- Changed fields
- Old and new values where appropriate, avoiding sensitive data exposure
- Source IP / user agent
- Timestamp

### 5. Use safe error handling

Avoid leaking whether a project exists across tenant boundaries.

For unauthorized access to another organization’s project, consider returning:

```http
404 Not Found
```

instead of:

```http
403 Forbidden
```

This reduces cross-tenant resource enumeration.

### 6. Add automated authorization tests

Include tests for:

- User can update own organization’s project
- User cannot update another organization’s project
- User in Org A cannot modify project in Org B by guessing `projectId`
- User with read-only role cannot patch settings
- User without billing permission cannot update `billingContactEmail`
- User without integration permission cannot update `webhookUrl`
- Invalid or internal webhook URLs are rejected

## Prioritized Findings

| Severity | Finding | Business Impact | Remediation |
|---|---|---|---|
| High | Missing project-to-organization authorization check | Cross-tenant project settings modification | Verify project ownership and user permission before update |
| High | `webhookUrl` can be hijacked or abused for SSRF | Data exfiltration, integration compromise, internal network access | Validate URL, block internal targets, verify webhook ownership |
| Medium | `billingContactEmail` can be redirected | Billing disruption, notification hijacking | Require billing-specific permission and audit logging |
| Medium | Potential tenant enumeration through errors | Information disclosure | Use consistent 404/403 strategy |
| Medium | Lack of audit trail mentioned | Weak incident response and forensics | Log all sensitive setting changes |

## Overall Assessment

The design has a significant authorization gap. Authentication alone is insufficient for a multi-organization system. The endpoint must enforce object-level and field-level authorization before applying updates, especially because `projectId` is user-controlled and the mutable fields affect billing and integrations.

The most important fix is to ensure every `PATCH /projects/{projectId}/settings` request proves that the authenticated user is authorized to administer the organization that owns the project.
