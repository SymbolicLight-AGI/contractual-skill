## Security Audit Response: `GET /accounts/{accountId}/reports`

### Scope Reviewed

Synthetic API pattern:

```http
GET /accounts/{accountId}/reports
```

Current behavior:

- Verifies that the caller is authenticated.
- Does **not** verify that the authenticated user is a member of, owner of, or otherwise authorized for the requested `accountId`.
- Returns report data containing:
  - Billing totals
  - User email addresses

### Summary Finding

This endpoint has a **Broken Access Control / IDOR vulnerability**.

An authenticated user can potentially access reports for accounts they do not belong to by changing the `accountId` path parameter.

Example:

```http
GET /accounts/acct_123/reports
GET /accounts/acct_999/reports
```

If the API only checks login state, a user from `acct_123` may be able to retrieve sensitive billing and user information for `acct_999`.

---

## Finding 1: Missing Account-Level Authorization

### Severity: High

### Category

- OWASP A01: Broken Access Control
- Insecure Direct Object Reference, IDOR
- Multi-tenant data exposure

### Affected Endpoint

```http
GET /accounts/{accountId}/reports
```

### Risk

The endpoint trusts a user-controlled identifier, `accountId`, without verifying whether the authenticated principal is allowed to access that account’s reports.

Authentication answers:

> “Who is this user?”

But this endpoint also needs authorization:

> “Is this user allowed to access reports for this specific account?”

### Potential Impact

An attacker with any valid account could enumerate or guess account IDs and retrieve another account’s report data.

Exposed data includes:

- Billing totals
- User email addresses
- Potential business-sensitive account activity
- Personally identifiable information, depending on jurisdiction and context

Business impact may include:

- Customer data breach
- Privacy violations
- Regulatory exposure under frameworks such as GDPR, SOC 2, ISO 27001, or similar obligations depending on business context
- Loss of customer trust
- Cross-tenant data leakage in a multi-tenant system

---

## Data Flow Risk Trace

Current likely flow:

```text
Client
  -> GET /accounts/{accountId}/reports
  -> Authentication middleware checks session/JWT
  -> API handler reads accountId from URL
  -> Report service queries billing/user/report data for accountId
  -> Database returns report
  -> API returns report to caller
```

Security bypass:

```text
Authenticated user + arbitrary accountId
  -> API does not verify membership
  -> Backend returns sensitive data for requested account
```

The main trust boundary failure occurs between:

```text
Authenticated request -> account-scoped data access
```

The endpoint treats authentication as sufficient, but the resource is tenant-scoped and requires account-specific authorization.

---

## Adversarial Analysis

An attacker may attempt to:

1. Log in with a normal low-privilege account.
2. Modify the path parameter:

   ```http
   GET /accounts/{victimAccountId}/reports
   ```

3. Enumerate account IDs if they are sequential, guessable, exposed in URLs, logs, invites, billing pages, or client-side state.
4. Harvest:
   - Billing totals
   - Email addresses
   - Account-level report metadata
5. Use exposed emails for phishing, account targeting, or social engineering.
6. Use billing totals for competitive intelligence or fraud.

If account IDs are UUIDs, the issue still exists. Unguessable IDs reduce exploitability but do not replace authorization.

---

## Required Remediation

### 1. Enforce Account Membership Authorization

Before returning report data, verify that the authenticated user has access to the requested `accountId`.

Example logic:

```pseudo
user = requireAuthenticatedUser(request)

accountId = request.path.accountId

membership = findAccountMembership(user.id, accountId)

if membership does not exist:
    return 404 or 403

if membership.role does not allow report access:
    return 403

return reports for accountId
```

Recommended authorization rule:

```text
User may access /accounts/{accountId}/reports only if:
- user is authenticated, and
- user is an active member of accountId, and
- user has a role/permission that allows report viewing.
```

For example:

```text
account:reports:read
```

---

### 2. Prefer Permission-Based Authorization

Do not rely only on broad roles like `admin` or `member`.

Use explicit permissions:

```text
account:reports:read
account:billing:read
account:users:read
```

Because this report contains both billing information and user emails, access should be limited to roles that legitimately need both.

Possible role mapping:

| Role | Can Access Reports? |
|---|---:|
| Account Owner | Yes |
| Billing Admin | Maybe, if reports are billing-specific |
| Workspace Admin | Depends on business rules |
| Standard Member | Usually no |
| External Contractor | No by default |

---

### 3. Scope Database Queries by Authorized Accounts

Avoid querying directly by user-supplied `accountId` alone.

Risky pattern:

```sql
SELECT * FROM reports WHERE account_id = :accountId;
```

Safer pattern:

```sql
SELECT r.*
FROM reports r
JOIN account_memberships m
  ON m.account_id = r.account_id
WHERE r.account_id = :accountId
  AND m.user_id = :currentUserId
  AND m.status = 'active'
  AND m.can_view_reports = true;
```

Or enforce authorization in service logic before the report query.

---

### 4. Centralize Authorization Checks

Do not duplicate ad hoc checks inconsistently across endpoints.

Create a reusable authorization function, policy, or middleware:

```pseudo
authorize(user, "account:reports:read", accountId)
```

Then require it in the route handler:

```pseudo
GET /accounts/:accountId/reports:
    user = requireAuth()
    authorize(user, "account:reports:read", accountId)
    return getReports(accountId)
```

This reduces the chance that another account-scoped endpoint has the same flaw.

---

### 5. Return Safe Error Responses

Use either `403 Forbidden` or `404 Not Found`.

Recommended:

- `403` if it is acceptable to reveal that the account exists but access is denied.
- `404` if account existence should not be disclosed.

Avoid verbose errors such as:

```json
{
  "error": "Account exists but user is not a member"
}
```

Prefer:

```json
{
  "error": "Not found"
}
```

or:

```json
{
  "error": "Forbidden"
}
```

depending on your security posture.

---

## Additional Controls

### Logging and Monitoring

Log denied access attempts with:

- Authenticated user ID
- Requested `accountId`
- Endpoint
- Timestamp
- Source IP / device/session identifier
- Authorization decision

Alert on suspicious behavior such as:

- One user requesting many different account IDs
- Repeated 403/404 responses on account-scoped resources
- Access attempts against accounts the user has never belonged to

Do not log sensitive report contents.

---

### Rate Limiting

Apply rate limits to reduce account ID enumeration.

Recommended:

- Per-user rate limits
- Per-IP rate limits
- Higher scrutiny for repeated cross-account access failures

Rate limiting is not a substitute for authorization.

---

### Minimize Data Exposure

Because the report contains billing totals and user emails, verify whether all fields are necessary.

Consider:

- Redacting or aggregating email addresses where possible
- Returning billing-only reports to billing roles
- Returning user-email reports only to user-management roles
- Separating report types by sensitivity

Example:

```text
/accounts/{accountId}/reports/billing
/accounts/{accountId}/reports/users
```

Each should have its own permission requirement.

---

## Test Cases to Validate the Fix

### Positive Test

User is an active member with report permission:

```text
Given user U is a member of account A
And U has account:reports:read
When U requests GET /accounts/A/reports
Then response is 200
```

### Negative Test: Non-Member

```text
Given user U is not a member of account B
When U requests GET /accounts/B/reports
Then response is 403 or 404
And no report data is returned
```

### Negative Test: Member Without Permission

```text
Given user U is a member of account A
But U does not have account:reports:read
When U requests GET /accounts/A/reports
Then response is 403
And no report data is returned
```

### Negative Test: Suspended Membership

```text
Given user U was formerly a member of account A
But membership status is suspended or removed
When U requests GET /accounts/A/reports
Then response is 403 or 404
```

### Enumeration Test

```text
Given user U is authenticated
When U requests reports for many accountIds
Then only authorized account reports are returned
And unauthorized attempts are denied and logged
```

---

## Recommended Priority

### Priority: Immediate Fix

This should be treated as a high-priority remediation because:

- The endpoint exposes sensitive cross-account data.
- The exploit is simple if account IDs are known or discoverable.
- Authentication-only protection is insufficient for tenant-scoped resources.
- The issue can result in broad customer data exposure.

---

## Residual Risk After Fix

After implementing account-level authorization, residual risk remains if:

- Account membership data is stale or incorrectly synchronized.
- Authorization is only implemented on this endpoint but not other account-scoped APIs.
- Privileged backend services bypass checks.
- Report exports, background jobs, or cached report URLs expose data without the same authorization checks.
- Logs or analytics pipelines store report data insecurely.

Recommended follow-up:

- Audit all endpoints using `accountId`, `organizationId`, `tenantId`, `workspaceId`, or similar path/query parameters.
- Add automated authorization tests for cross-tenant access.
- Review backend jobs and admin/service-account access paths.
- Validate cache keys include tenant/account scoping.
- Include IDOR checks in CI/CD security testing.

---

## Final Assessment

The current design is vulnerable to **high-severity IDOR due to missing account membership authorization**. The API must enforce resource-level access control for `accountId` before returning billing totals or user emails. Authentication alone is not sufficient. Implement centralized permission checks, scope data access by authorized membership, add negative authorization tests, and monitor denied cross-account access attempts.
