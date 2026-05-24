## Scope And Authorization

- **Scope:** Synthetic API authorization pattern: `GET /accounts/{accountId}/reports`
- **Environment:** Not specified; treated as synthetic/non-production design review.
- **Authorization:** Review is limited to the supplied pattern. No testing, scanning, credential use, or production activity is performed.
- **Data involved:** Billing totals and user email addresses.
- **Compliance requirements:** Not specified.

## Executive Summary

The API pattern presents a likely **Broken Object Level Authorization / IDOR** risk. The endpoint verifies that a caller is authenticated but does **not** verify that the caller is a member of, or otherwise authorized to access, the requested `accountId`.

If implemented as described, any logged-in user may be able to request reports for arbitrary accounts by changing the `accountId` path parameter. Because the report includes **billing totals** and **user emails**, this could expose sensitive business and personal data across tenant boundaries.

Recommended priority: **High**, especially if this is a multi-tenant SaaS or customer-facing API.

---

## Findings By Severity

### High — Missing Account-Level Authorization on Reports Endpoint

**Finding:**  
`GET /accounts/{accountId}/reports` checks whether the user is logged in, but does not check whether the user belongs to or has permission to access the requested `accountId`.

**Evidence:**  
Supplied API behavior:

```http
GET /accounts/{accountId}/reports
```

- Authentication check: present.
- Account membership / authorization check: absent.
- Response includes:
  - Billing totals.
  - User emails.

**Risk:**  
An authenticated user could potentially access reports for accounts they do not belong to by modifying the `accountId` value.

Example risk scenario:

```http
GET /accounts/123/reports
GET /accounts/456/reports
```

If the server only checks login state, a user from account `123` may be able to retrieve account `456` reports.

**Business Impact:**

- Cross-tenant data exposure.
- Disclosure of billing information.
- Disclosure of user email addresses.
- Potential privacy incident or regulatory concern, depending on jurisdiction and contractual obligations.
- Loss of customer trust.
- Possible breach of confidentiality commitments.

**Likelihood:** High if `accountId` is user-controllable and authorization is not enforced server-side.

**Severity:** High.

---

## Evidence

### Finding

The supplied pattern explicitly states:

> checks that the user is logged in but does not check account membership.

This is sufficient evidence for a design-level authorization finding.

### Hypothesis

If the endpoint is deployed as described, it may be vulnerable to **IDOR / Broken Object Level Authorization**. This requires implementation validation to confirm actual exploitability.

### Evidence Gap

The following are not provided:

- Actual route handler code.
- Authentication middleware behavior.
- Authorization middleware or policy layer.
- Data model for users, accounts, roles, and memberships.
- Whether account IDs are sequential, UUIDs, or otherwise guessable.
- Whether downstream services enforce authorization.
- Audit logs showing report access.
- Whether emails and billing totals are considered regulated or contractually protected data.

---

## Remediation Plan

### 1. Enforce Server-Side Account Authorization

Before returning the report, verify that the authenticated user is authorized for the requested account.

Example pseudocode:

```pseudo
user = requireAuthenticatedUser(request)
accountId = request.path.accountId

membership = findAccountMembership(user.id, accountId)

if membership does not exist:
    return 403 Forbidden

if membership.role does not allow "view_reports":
    return 403 Forbidden

report = getReportForAccount(accountId)
return report
```

Do not rely on frontend checks, hidden UI elements, or client-provided account context.

---

### 2. Use Explicit Authorization Policies

Define a clear permission such as:

```text
reports:read
```

Then enforce:

```text
User must have reports:read permission on accountId.
```

Recommended authorization model:

| Role | Can View Reports |
|---|---|
| Account Owner | Yes |
| Billing Admin | Yes |
| Admin | Maybe, depending on tenant scope |
| Member | No, unless explicitly allowed |
| External User | No |

---

### 3. Scope Database Queries by User Authorization

Avoid queries that fetch reports solely by `accountId`.

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
  AND m.can_view_reports = true;
```

Or enforce this through a centralized authorization service/policy engine.

---

### 4. Return Safe Error Codes

Recommended behavior:

- `401 Unauthorized` if the user is not authenticated.
- `403 Forbidden` if authenticated but not authorized.
- Optionally use `404 Not Found` to avoid disclosing account existence, depending on product requirements.

Avoid returning detailed messages such as:

```json
{
  "error": "Account exists but you are not a member"
}
```

A safer response:

```json
{
  "error": "Not authorized"
}
```

---

### 5. Minimize Sensitive Data in Reports

Because reports contain billing totals and user emails:

- Confirm that emails are necessary in the report response.
- Consider redacting or partially masking emails unless full addresses are required.
- Separate billing report access from general account membership.
- Add pagination and filtering controls.
- Avoid returning more personal data than needed.

---

### 6. Add Audit Logging

Log report access events with:

- Authenticated user ID.
- Account ID requested.
- Authorization decision.
- Timestamp.
- Source IP or request metadata, where appropriate.
- Request ID / trace ID.

Do not log full report contents or sensitive personal data.

Example event:

```json
{
  "event": "report_access",
  "user_id": "redacted-user-id",
  "account_id": "redacted-account-id",
  "decision": "allowed",
  "permission": "reports:read",
  "timestamp": "2026-05-24T00:00:00Z"
}
```

---

### 7. Add Automated Authorization Tests

Add unit, integration, and regression tests for cross-account access.

Minimum test cases:

| Scenario | Expected Result |
|---|---|
| Unauthenticated user requests report | `401` |
| Authenticated user requests own account report with permission | `200` |
| Authenticated user requests own account report without report permission | `403` |
| Authenticated user requests another account’s report | `403` or `404` |
| Deleted or suspended membership requests report | `403` |
| User changes `accountId` manually | `403` or `404` |
| Admin requests report across accounts | Allowed only if admin scope explicitly permits it |

---

## Validation Steps

These are safe validation recommendations and should be performed only in an authorized test or staging environment.

1. Create two test accounts:
   - Account A.
   - Account B.

2. Create a test user who belongs only to Account A.

3. Authenticate as that user.

4. Request:

```http
GET /accounts/{accountA}/reports
```

Expected result:

```http
200 OK
```

Only if the user has report-viewing permission.

5. Request:

```http
GET /accounts/{accountB}/reports
```

Expected result:

```http
403 Forbidden
```

or:

```http
404 Not Found
```

depending on account enumeration policy.

6. Confirm the response does not include:
   - Billing totals for Account B.
   - Emails from Account B.
   - Metadata revealing Account B unnecessarily.

7. Review logs to confirm:
   - Access was denied.
   - The denied access attempt was logged.
   - No sensitive report data was written to logs.

---

## Residual Risk

After adding account-level authorization, residual risks may remain if:

- Authorization is inconsistently enforced across related endpoints.
- Downstream services or background jobs bypass API authorization.
- Admin/service tokens can access tenant data without sufficient controls.
- Reports are cached without user/account scoping.
- Export, download, or email-report features use weaker checks.
- Audit logs are incomplete or not monitored.

Related endpoints should also be reviewed, such as:

```http
GET /accounts/{accountId}/reports/{reportId}
POST /accounts/{accountId}/reports/export
GET /accounts/{accountId}/billing
GET /accounts/{accountId}/users
```

---

## Open Questions

1. Is this a multi-tenant application?
2. What roles should be allowed to view reports?
3. Are billing totals considered confidential under customer contracts?
4. Are user emails subject to privacy obligations such as GDPR, CCPA, HIPAA, or other frameworks?
5. Are account IDs sequential, guessable, or public?
6. Is report data cached? If yes, is the cache key scoped by account and user permissions?
7. Are there Admin SDKs, service accounts, or backend jobs that can bypass normal authorization?
8. Are report exports or downloadable files protected with the same authorization checks?

---

## Handoff

- **Engineering:** Implement account-level authorization and regression tests.
- **Security / DevSecOps:** Review similar object-level access patterns across the API.
- **Privacy / Compliance:** Assess whether exposed emails and billing data trigger reporting, contractual, or regulatory obligations if this exists in production.
- **Product Owners:** Define which roles should have `reports:read` permission.
- **Security Leadership:** Required if this pattern is confirmed in production with customer data exposure.
