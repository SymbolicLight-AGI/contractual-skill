## Scope And Authorization

This is a **synthetic API authorization review** of the pattern:

`GET /accounts/{accountId}/reports`

Observed behavior: endpoint checks that the requester is logged in, but does **not** verify that the requester is a member of, or otherwise authorized for, the requested `accountId`.

No live testing, exploit attempt, credential use, or production validation is performed.

---

## Executive Summary

The API pattern has a likely **Broken Object Level Authorization / IDOR** issue. Any authenticated user may be able to request reports for arbitrary accounts by changing the `accountId` path parameter.

Because the report includes **billing totals** and **user emails**, this creates a risk of unauthorized disclosure of financial and personal data. Severity is likely **High**, depending on exposure, account sensitivity, regulatory context, and whether account IDs are guessable or enumerable.

---

## Findings By Severity

### High — Missing Account Membership Authorization on Report Access

**Finding:**  
`GET /accounts/{accountId}/reports` validates that the user is logged in, but does not verify that the authenticated user is authorized to access the requested `accountId`.

**Evidence:**  
The supplied pattern states:

> checks that the user is logged in but does not check account membership

**Risk:**  
An authenticated user may access reports for accounts they do not belong to by modifying the URL path:

```http
GET /accounts/12345/reports
GET /accounts/67890/reports
```

Potential business and security impacts include:

- Unauthorized disclosure of billing totals.
- Unauthorized disclosure of user email addresses.
- Privacy violation or breach notification risk depending on jurisdiction and data classification.
- Customer trust impact.
- Possible competitive intelligence leakage.
- Compliance exposure if emails or billing data are regulated under applicable privacy frameworks.

**Likelihood:**  
Likely, if `accountId` values are predictable, exposed elsewhere in the UI/API, sequential, or visible in logs, URLs, invitations, invoices, or client-side state.

**Severity:**  
High. The issue affects authorization boundaries between tenants/accounts and exposes sensitive business and personal data.

---

## Evidence

### Confirmed From Supplied Material

- **Finding:** The endpoint authenticates the user but does not check account membership.
- **Finding:** The endpoint returns billing totals and user emails.
- **Finding:** The authorization decision appears to rely only on login state, not account-level access.

### Hypotheses Requiring Validation

- **Hypothesis:** Users can enumerate or guess `accountId` values.
- **Hypothesis:** The same endpoint is accessible to all authenticated users without role checks.
- **Hypothesis:** The report may include additional sensitive fields beyond billing totals and emails.
- **Hypothesis:** Caching, logs, or client-side code may further expose account report data.

### Evidence Gaps

- Whether `accountId` is sequential, UUID-based, or otherwise hard to guess.
- Whether there are compensating controls in middleware, gateway policy, service layer, or database row-level security.
- Whether the endpoint is used by admins, account owners, regular members, or service accounts.
- Whether report access should vary by role, such as owner, billing admin, read-only user, or support staff.
- Whether responses are cached and whether cache keys include authenticated user and account context.
- Whether access attempts are logged and monitored.

---

## Remediation Plan

### 1. Enforce Account-Level Authorization Server-Side

Before returning the report, verify that the authenticated principal is authorized for the requested account.

Example logic:

```pseudo
user = requireAuthenticatedUser(request)

accountId = request.path.accountId

if !authorizationService.userCanAccessAccountReport(user.id, accountId):
    return 403 Forbidden

report = reportService.getAccountReport(accountId)
return report
```

The check should be performed on the server, not in client-side routing or UI logic.

---

### 2. Use Centralized Authorization Policy

Define explicit policies such as:

- `account:report:read`
- `account:billing:read`
- `account:user_emails:read`

Then enforce them consistently:

```pseudo
authorize(user, "account:report:read", accountId)
```

Avoid duplicating ad hoc authorization logic across controllers.

---

### 3. Validate Role and Membership

Determine who should be allowed to access reports. For example:

| Role | Can Access Report? |
|---|---:|
| Account Owner | Yes |
| Billing Admin | Yes |
| Account Admin | Maybe |
| Regular Member | Maybe / Limited |
| External User | No |
| Support Agent | Only with audited break-glass or delegated access |

If reports include billing totals and user emails, access should likely be restricted to owners, admins, or billing-specific roles.

---

### 4. Prevent Cross-Tenant Data Access at the Data Layer

Where possible, scope queries by both `accountId` and authorized user or tenant context.

Risky pattern:

```sql
SELECT * FROM reports WHERE account_id = :accountId;
```

Safer pattern:

```sql
SELECT r.*
FROM reports r
JOIN account_memberships m ON m.account_id = r.account_id
WHERE r.account_id = :accountId
  AND m.user_id = :userId
  AND m.status = 'active';
```

For service-oriented architectures, pass and enforce tenant/account context consistently between services.

---

### 5. Minimize Sensitive Data in the Report

Review whether user emails are necessary in this endpoint. If not required, remove them or provide a separate, more restricted endpoint.

Options:

- Omit user emails by default.
- Return aggregated counts instead of identifiable emails.
- Mask emails where appropriate.
- Require a stronger permission for personally identifiable information.

Example:

```json
{
  "billingTotal": 1200.00,
  "activeUserCount": 14
}
```

instead of:

```json
{
  "billingTotal": 1200.00,
  "users": [
    "user1@example.com",
    "user2@example.com"
  ]
}
```

---

### 6. Return Safe Error Responses

Use:

- `403 Forbidden` when the user is authenticated but not authorized.
- `404 Not Found` may be appropriate if you intentionally do not want to reveal whether an account exists.

Avoid responses that allow account enumeration, such as:

```json
{
  "error": "Account exists but you are not a member"
}
```

unless that disclosure is acceptable.

---

### 7. Add Audit Logging and Detection

Log authorization denials and suspicious access patterns without exposing sensitive report contents.

Useful fields:

- Authenticated user ID.
- Requested account ID.
- Decision: allowed or denied.
- Reason code.
- Source IP or session ID.
- User agent.
- Request ID / trace ID.

Monitor for:

- One user requesting many different account IDs.
- Repeated `403` or `404` responses across account IDs.
- Access to accounts with no membership relationship.
- Unusual report export volume.

---

## Validation Steps

These are safe validation checks that should be performed in an authorized non-production environment or with explicit production approval.

### Functional Authorization Tests

Create at least two accounts:

- Account A with User A as a member.
- Account B with User B as a member.
- Ensure User A is not a member of Account B.

Test:

```http
GET /accounts/{accountA}/reports as User A
```

Expected:

```http
200 OK
```

Test:

```http
GET /accounts/{accountB}/reports as User A
```

Expected:

```http
403 Forbidden
```

or:

```http
404 Not Found
```

depending on the product’s enumeration-resistance policy.

---

### Automated Regression Tests

Add unit, integration, and API tests for:

- Unauthenticated request returns `401`.
- Authenticated but non-member request returns `403` or `404`.
- Member with insufficient role is denied.
- Billing admin or owner is allowed.
- Deactivated or invited-but-not-accepted members are denied.
- Cross-account report access is denied.
- Deleted or suspended accounts are denied.

---

### Data Exposure Checks

Verify that report responses do not include unnecessary sensitive fields.

Check for:

- User emails.
- Full names.
- Billing addresses.
- Payment identifiers.
- Internal account IDs.
- Tax or invoice metadata.
- Support notes.

---

### Logging Validation

Confirm that denied access is logged with enough context for investigation, but without logging full report contents or sensitive personal data.

---

## Residual Risk

After remediation, residual risk remains if:

- Authorization logic is inconsistently applied across related endpoints.
- Background jobs, exports, or Admin SDK/service-layer paths bypass account authorization.
- Cached report responses are shared across users or accounts.
- Support/admin tooling can access reports without adequate controls.
- Account membership data is stale or not synchronized across services.
- Logs or analytics systems retain exposed report data from prior vulnerable requests.

Residual risk should be accepted only by the appropriate system owner or security/risk authority.

---

## Open Questions

1. Are `accountId` values sequential, UUIDs, slugs, or otherwise guessable?
2. Which roles should be allowed to access billing totals?
3. Which roles should be allowed to view user emails?
4. Are reports cached? If so, is the cache keyed by account and authorization context?
5. Are there other endpoints using the same pattern, such as:
   - `/accounts/{accountId}/users`
   - `/accounts/{accountId}/invoices`
   - `/accounts/{accountId}/exports`
   - `/accounts/{accountId}/settings`
6. Is there centralized authorization middleware or per-handler logic?
7. Are report exports, background jobs, and admin tools subject to the same authorization model?

---

## Handoff

Recommended owners:

- **Engineering:** implement account-level authorization and regression tests.
- **Security/AppSec:** review related endpoints for IDOR/BOLA patterns.
- **Privacy/Compliance:** assess exposure impact if this pattern existed in production.
- **Product Owner:** define role-based access requirements for billing totals and user emails.
- **Operations/SOC:** monitor for suspicious historical access if production exposure is suspected.
