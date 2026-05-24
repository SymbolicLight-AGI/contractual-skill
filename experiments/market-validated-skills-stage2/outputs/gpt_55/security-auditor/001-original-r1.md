## Security Audit Response: `GET /accounts/{accountId}/reports`

### Scope Reviewed

Synthetic API pattern:

```http
GET /accounts/{accountId}/reports
```

Current control:

- Verifies the requester is authenticated / logged in.
- Does **not** verify that the requester is a member of, owner of, or otherwise authorized for `accountId`.

Returned data:

- Billing totals
- User email addresses

---

## Executive Summary

This API pattern presents a **high-severity broken access control vulnerability**, specifically an **IDOR / BOLA** issue: Insecure Direct Object Reference / Broken Object Level Authorization.

Because the API accepts an `accountId` path parameter and only checks whether the user is logged in, any authenticated user may be able to request reports for arbitrary accounts by changing the `accountId` value.

Example:

```http
GET /accounts/acct_123/reports
GET /accounts/acct_456/reports
GET /accounts/acct_789/reports
```

If the backend does not verify the user’s relationship to each account, an attacker could enumerate or guess account IDs and access sensitive billing and user information belonging to other tenants.

---

## Primary Finding

### Finding: Missing Account-Level Authorization on Reports Endpoint

**Severity:** High  
**Category:** Broken Access Control / IDOR / BOLA  
**Affected Endpoint:**

```http
GET /accounts/{accountId}/reports
```

**Data Exposed:**

- Billing totals
- User email addresses
- Potentially tenant/customer business information

**Risk:**

An authenticated but unauthorized user can access reports for accounts they do not belong to.

---

## Data Flow Review

Expected data flow:

```text
Client
  -> API route: GET /accounts/{accountId}/reports
  -> Authentication middleware
  -> Report service
  -> Billing/user data store
  -> Response with billing totals and emails
```

Observed issue:

```text
Authentication middleware confirms "user is logged in"
but no authorization check confirms:
  "user is allowed to access this accountId"
```

The security bypass occurs at the trust boundary between:

```text
Authenticated User -> Account-Scoped Report Data
```

Authentication answers:

> Who is this user?

Authorization must also answer:

> Is this user allowed to access this specific account’s reports?

Currently, the second question is not being enforced.

---

## Adversarial Analysis

An attacker with a valid account could attempt:

### 1. Account ID Enumeration

If account IDs are sequential, predictable, leaked, or discoverable, an attacker may iterate through values:

```http
GET /accounts/1001/reports
GET /accounts/1002/reports
GET /accounts/1003/reports
```

### 2. Cross-Tenant Data Access

A user from Account A could request data from Account B:

```http
GET /accounts/account-b/reports
```

If the API only verifies login status, the request may succeed.

### 3. Sensitive Information Harvesting

The endpoint exposes user emails and billing totals, which could be used for:

- Phishing
- Competitive intelligence
- Privacy violations
- Customer account mapping
- Business impact analysis against victims

### 4. Privilege Confusion

A regular user may gain access to reports that should be limited to:

- Account owners
- Billing admins
- Finance roles
- Internal support roles with audit logging

---

## Business Impact

Potential impacts include:

- Unauthorized disclosure of customer billing data
- Exposure of user email addresses
- Multi-tenant isolation failure
- Privacy and contractual violations
- Loss of customer trust
- Possible regulatory implications depending on jurisdiction and data classification

If this system is subject to compliance obligations, this may affect readiness for frameworks such as SOC 2, ISO 27001, GDPR, or other privacy/security controls. Specific compliance impact cannot be fully determined without confirmed regulatory scope.

---

## Recommended Remediation

### 1. Enforce Object-Level Authorization

Every request to:

```http
GET /accounts/{accountId}/reports
```

must verify that the authenticated user is authorized for the requested `accountId`.

Example logic:

```pseudo
user = requireAuthenticatedUser(request)

if !userHasAccessToAccount(user.id, accountId):
    return 403 Forbidden

if !userHasPermission(user.id, accountId, "reports:read"):
    return 403 Forbidden

return reportsForAccount(accountId)
```

Do not rely on the fact that the user is logged in.

---

### 2. Use Server-Side Account Membership Checks

Verify membership using trusted server-side data, such as:

```text
account_memberships:
  user_id
  account_id
  role
  status
```

Required checks should include:

- User is a member of the account.
- Membership is active.
- User role permits report access.
- Account is active and not deleted/suspended.
- Optional: user has billing/report-specific permission.

---

### 3. Enforce Role-Based or Attribute-Based Permissions

Not every account member should necessarily see billing totals and user emails.

Suggested permission model:

| Role | Can Access Reports? | Can View Billing Totals? | Can View User Emails? |
|---|---:|---:|---:|
| Owner | Yes | Yes | Yes |
| Billing Admin | Yes | Yes | Limited/Maybe |
| Admin | Yes | Maybe | Yes |
| Member | No by default | No | No |
| Viewer | No by default | No | No |

Use explicit permissions such as:

```text
reports:read
billing:read
users:email:read
```

---

### 4. Avoid Trusting Client-Supplied Account Context Alone

Do not assume `accountId` in the path is valid for the user.

Bad pattern:

```pseudo
GET /accounts/{accountId}/reports
if user.isAuthenticated:
    return reports(accountId)
```

Safer pattern:

```pseudo
GET /accounts/{accountId}/reports
user = authenticatedUser()
authorize(user, accountId, "reports:read")
return reports(accountId)
```

---

### 5. Prevent Data Leakage Through Error Responses

Use clear but non-enumerable responses.

Recommended:

```http
403 Forbidden
```

or, where account existence should not be revealed:

```http
404 Not Found
```

Avoid responses like:

```json
{
  "error": "Account exists but you are not a member"
}
```

That can aid enumeration.

---

### 6. Add Audit Logging

Log report access events:

```text
timestamp
request_id
user_id
account_id
action = reports.read
authorization_result
source_ip
user_agent
```

For denied attempts, log enough detail to detect probing:

```text
user_id attempted reports.read on unauthorized account_id
```

Monitor for:

- Many different `accountId` values requested by one user
- Repeated 403/404 responses
- Access from unusual locations
- Access to high-value accounts

---

### 7. Add Automated Authorization Tests

Include tests for cross-account access.

Example test cases:

```text
User from Account A requests Account A reports -> 200 OK
User from Account A requests Account B reports -> 403 Forbidden or 404 Not Found
Unauthenticated user requests Account A reports -> 401 Unauthorized
Account member without reports permission -> 403 Forbidden
Suspended user requests account reports -> 403 Forbidden
Deleted account requested -> 404 Not Found
```

Also test whether billing totals and emails are separately protected if they require different permissions.

---

### 8. Apply Defense in Depth at the Data Layer

If using a privileged backend service, Admin SDK, service account, or ORM that bypasses database security rules, the API layer must enforce authorization before querying.

Recommended safeguards:

- Centralized authorization helper or policy engine
- Repository methods that require `userId` and `accountId`
- Queries scoped through membership joins
- Database row-level security where applicable
- Code review rule: no direct account-scoped reads without authorization check

Example safer query pattern:

```sql
SELECT r.*
FROM reports r
JOIN account_memberships m
  ON m.account_id = r.account_id
WHERE r.account_id = :accountId
  AND m.user_id = :userId
  AND m.status = 'active'
  AND m.role IN ('owner', 'admin', 'billing_admin');
```

---

## Suggested Secure Endpoint Behavior

### Unauthenticated Request

```http
GET /accounts/acct_123/reports
```

Response:

```http
401 Unauthorized
```

### Authenticated but Unauthorized Request

```http
GET /accounts/acct_456/reports
```

Response:

```http
403 Forbidden
```

or:

```http
404 Not Found
```

depending on whether account existence should be hidden.

### Authenticated and Authorized Request

```http
GET /accounts/acct_123/reports
```

Response:

```http
200 OK
```

with only the fields permitted for the user’s role.

---

## Priority

### Immediate Fix Required

This should be treated as a release-blocking issue if the endpoint exists in production or is planned for deployment.

Recommended priority:

```text
Severity: High
Likelihood: High
Impact: High
Priority: P0/P1 depending on exposure
```

If account IDs are predictable or exposed elsewhere in the application, severity may rise toward **Critical**, especially in a multi-tenant SaaS environment.

---

## Residual Risk After Fix

After implementing account-level authorization, residual risks include:

- Overly broad roles granting unnecessary report access
- Excessive data returned in reports
- Account enumeration via timing or error differences
- Missing audit detection for abusive but technically authorized users
- Inconsistent authorization checks across similar endpoints

These should be addressed through least privilege, consistent policy enforcement, logging, monitoring, and automated regression tests.

---

## Final Assessment

The current pattern is insecure because it authenticates the user but does not authorize access to the specific `accountId`. This creates a likely IDOR/BOLA vulnerability exposing billing totals and user emails across accounts.

The endpoint should be remediated by enforcing server-side account membership and permission checks before any report data is retrieved or returned.
