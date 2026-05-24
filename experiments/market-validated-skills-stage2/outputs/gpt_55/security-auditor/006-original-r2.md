## Remediation Handoff: Security Findings

### Scope / Assets

**Application areas affected:**
1. Reports feature/API — missing object-level authorization
2. Session management — cookies missing `Secure` flag
3. Admin export functionality — missing audit logging

**Assumptions / uncertainty:**
- Findings are synthetic and not yet validated in a live environment.
- Exact affected endpoints, frameworks, cookie names, and data sensitivity are not provided.
- Compliance requirements are not specified. Potentially relevant: SOC 2, ISO 27001, GDPR, HIPAA, PCI-DSS depending on data handled.

---

# Executive Summary

| Finding | Severity | Primary Risk | Primary Owner |
|---|---:|---|---|
| Missing object-level authorization on reports | High | IDOR / unauthorized access to another user’s reports | Engineering |
| Session cookies lack `Secure` flag | Medium | Session cookie exposure over non-HTTPS transport | Engineering / Security |
| Admin export has no audit log | Medium | Lack of accountability for privileged data access/export | Engineering / Security / Product |

---

# Finding 1: Missing Object-Level Authorization on Reports

## Severity

**High**

## Risk

The reports feature appears to lack object-level authorization. If a user can access or modify reports by changing a report ID, this creates an **Insecure Direct Object Reference**, or IDOR, vulnerability.

Potential impact:
- Unauthorized access to sensitive report data
- Cross-tenant data exposure
- Data modification or deletion if write endpoints are affected
- Compliance and privacy breach risk
- Loss of customer trust

## Affected Area

Likely affected:
- `GET /reports/{id}`
- `PUT /reports/{id}`
- `PATCH /reports/{id}`
- `DELETE /reports/{id}`
- Report download/export endpoints
- Any backend service using privileged database access, admin SDKs, or service accounts

## Required Remediation

Engineering should enforce object-level authorization on every report operation.

### Required controls

1. Verify authenticated user identity.
2. Resolve the requested report object.
3. Verify the user is allowed to access the specific report.
4. Enforce tenant, organization, team, or ownership boundaries.
5. Deny access by default.
6. Apply checks even when backend code uses privileged service accounts or Admin SDKs.
7. Ensure authorization is applied on read, update, delete, export, and sharing flows.

### Example authorization rule

A user may access a report only if at least one condition is true:

- User owns the report
- User belongs to the report’s tenant or organization
- User has an explicit role permitting access
- User has been granted access through a sharing model
- User is an admin with scoped permission for that tenant or organization

Global admin access should still be explicit and auditable.

## Engineering Tasks

- Identify all report endpoints and backend handlers.
- Add object-level authorization checks before returning, modifying, deleting, or exporting reports.
- Centralize authorization logic where possible.
- Avoid relying only on frontend filtering.
- Avoid relying only on route-level authentication.
- Ensure database queries include tenant/user scoping, for example:

```sql
SELECT * FROM reports
WHERE id = :report_id
AND tenant_id = :current_user_tenant_id;
```

- For privileged backend access, enforce authorization in application logic before using the privileged client.
- Return generic `404` or `403` responses without leaking object existence across tenants.
- Add structured security logs for denied access attempts.

## QA Validation

QA should test:

1. User A cannot access User B’s report by changing the report ID.
2. User A cannot update User B’s report.
3. User A cannot delete User B’s report.
4. User A cannot export User B’s report.
5. Cross-tenant report access is denied.
6. Admin access works only for authorized admin roles.
7. API and UI behavior are consistent.
8. Authorization cannot be bypassed through direct API calls.
9. Bulk report endpoints enforce authorization per object.
10. Error messages do not reveal whether unauthorized reports exist.

## Security Validation

Security should perform:

- Manual IDOR testing across all report endpoints
- Role and tenant boundary testing
- Review of authorization middleware and service-layer checks
- Verification that privileged SDK/database access does not bypass authorization
- Negative testing using low-privilege accounts
- Regression test review

## Acceptance Criteria

This finding can be closed when:

- Every report read/write/delete/export endpoint enforces object-level authorization.
- Cross-user and cross-tenant access attempts fail.
- Automated tests cover IDOR scenarios.
- Security verifies no bypass exists through API calls or privileged backend paths.
- Logs capture denied authorization attempts without exposing sensitive report data.

---

# Finding 2: Session Cookies Lack `Secure` Flag

## Severity

**Medium**

## Risk

Session cookies without the `Secure` attribute may be transmitted over plaintext HTTP if the application or browser is directed to an insecure endpoint. This can expose session tokens to interception.

Potential impact:
- Session hijacking
- Account takeover
- Increased risk on public or hostile networks
- Noncompliance with secure session management expectations

## Affected Area

Likely affected:
- Authentication session cookie
- Refresh token cookie
- CSRF token cookie, if sensitive
- Any persistent login or remember-me cookie

## Required Remediation

Engineering should configure all sensitive cookies with secure attributes.

### Required cookie settings

For session/authentication cookies:

```http
Set-Cookie: session=<value>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=<appropriate_value>
```

Recommended settings:

| Attribute | Required? | Recommendation |
|---|---:|---|
| `Secure` | Yes | Required for all sensitive cookies |
| `HttpOnly` | Yes | Prevent JavaScript access to session cookies |
| `SameSite` | Yes | Prefer `Lax`; use `Strict` where feasible; use `None; Secure` only for cross-site needs |
| `Path` | Yes | Scope as narrowly as practical |
| `Domain` | Conditional | Avoid broad parent-domain scope unless required |
| Expiration | Yes | Use appropriate session lifetime and idle timeout |

## Engineering Tasks

- Identify all cookies set by the application.
- Ensure authentication/session cookies include `Secure`.
- Ensure cookies are only issued over HTTPS.
- Enable HTTP-to-HTTPS redirects.
- Consider adding HSTS:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

- Verify settings across environments, especially production and staging.
- Ensure reverse proxy/load balancer TLS termination does not cause the app to incorrectly think the request is HTTP.
- If using a framework, set the trusted proxy configuration correctly.

## QA Validation

QA should test:

1. Login response sets session cookie with `Secure`.
2. Session cookie also has `HttpOnly`.
3. `SameSite` is set appropriately.
4. Cookie is not transmitted over HTTP.
5. HTTP requests redirect to HTTPS.
6. Cookie settings are correct in supported browsers.
7. Logout invalidates the session properly.

## Security Validation

Security should perform:

- Manual browser inspection of cookie attributes
- Proxy-based validation using Burp Suite, OWASP ZAP, or equivalent
- Check for inconsistent cookie behavior across auth flows
- Confirm HSTS presence if required
- Confirm no sensitive cookies are set without `Secure`

## Acceptance Criteria

This finding can be closed when:

- All sensitive cookies have the `Secure` flag.
- Session cookies also use `HttpOnly`.
- Appropriate `SameSite` policy is set.
- HTTP traffic does not expose session cookies.
- QA and Security validate cookie behavior in staging or production-equivalent environment.

---

# Finding 3: Admin Export Has No Audit Log

## Severity

**Medium**

## Risk

The admin export feature allows privileged users to extract data but does not generate an audit log. This weakens accountability, incident investigation, compliance evidence, and abuse detection.

Potential impact:
- Unauthorized or excessive data exports may go unnoticed
- Insider threat activity may be difficult to investigate
- Inability to prove who accessed or exported sensitive data
- Compliance audit gaps
- Delayed breach detection

## Affected Area

Likely affected:
- Admin data export UI
- Admin export API
- Background export jobs
- File generation and download endpoints
- Data warehouse or storage bucket export flows

## Required Remediation

Engineering should add tamper-resistant audit logging for all admin export actions.

### Events to log

At minimum:

- Export requested
- Export approved, if approval exists
- Export started
- Export completed
- Export failed
- Export file downloaded
- Export deleted or expired
- Export canceled

### Required audit fields

Each audit event should include:

| Field | Description |
|---|---|
| `event_type` | Example: `admin_export_requested` |
| `actor_user_id` | Admin user performing the action |
| `actor_role` | Role or permission set at time of action |
| `tenant_id` / `organization_id` | Scope of exported data |
| `export_id` | Unique export identifier |
| `data_scope` | Dataset, filters, date range, object types |
| `record_count` | Number of records exported, if available |
| `timestamp` | Server-side timestamp |
| `source_ip` | Request IP |
| `user_agent` | Client metadata |
| `request_id` / `correlation_id` | Traceability across services |
| `status` | Success, failure, denied, canceled |
| `reason` | Optional business justification |
| `destination` | Storage location or delivery channel, without exposing secrets |

### Sensitive data handling

Audit logs should **not** contain:
- Raw exported data
- Session tokens
- API keys
- Passwords
- Full secrets
- Sensitive file contents

## Engineering Tasks

- Add audit event generation to admin export request path.
- Add logging to asynchronous job workers if exports run in the background.
- Add logging to download endpoint, not just export creation.
- Ensure failed and denied attempts are logged.
- Include correlation IDs across API, worker, storage, and download flows.
- Store logs in a centralized, access-controlled logging system.
- Protect audit logs from modification or deletion by normal administrators.
- Define retention period with Security and Product.
- Add alerting for high-risk patterns, such as:
  - Large exports
  - Repeated exports
  - Exports outside business hours
  - Exports by newly created admins
  - Failed or denied export attempts
  - Exports of sensitive datasets

## QA Validation

QA should test:

1. Admin export request creates an audit event.
2. Export completion creates an audit event.
3. Export failure creates an audit event.
4. Export download creates an audit event.
5. Unauthorized export attempt creates a denied audit event.
6. Audit event contains required metadata.
7. Audit event does not contain sensitive exported data.
8. Correlation ID links API request to background job.
9. Logs are visible to authorized security/audit users.
10. Non-security users cannot modify audit logs.

## Security Validation

Security should perform:

- Review of audit schema
- Verification that logs are generated for all export paths
- Abuse-case testing for export workflows
- Validation of log access controls
- Review of alerting thresholds
- Confirmation of retention and immutability controls
- Verification that logs do not expose sensitive data

## Acceptance Criteria

This finding can be closed when:

- Admin export request, execution, download, failure, and denial events are logged.
- Logs contain sufficient actor, scope, time, and outcome metadata.
- Logs exclude sensitive exported content and secrets.
- Logs are centralized and access-controlled.
- Security validates audit coverage across all export paths.
- Alerting requirements are agreed and implemented or tracked as follow-up risk.

---

# Cross-Functional Handoff

## Engineering

Primary responsibilities:

- Implement object-level authorization for reports.
- Set secure cookie attributes.
- Add audit logging for admin exports.
- Add automated unit, integration, and API security tests.
- Ensure controls are enforced server-side, not only in the UI.
- Provide implementation notes and affected endpoint inventory to Security and QA.

Deliverables:

- Pull requests for each remediation area
- Endpoint/control mapping
- Test coverage evidence
- Deployment plan
- Rollback plan
- Residual risk notes, if any

## Security

Primary responsibilities:

- Confirm remediation design before implementation if needed.
- Define authorization expectations and audit log requirements.
- Validate fixes manually and with targeted testing.
- Confirm severity closure or adjust residual risk.
- Define alerting and monitoring requirements for admin exports.
- Ensure findings are tracked through the vulnerability management process.

Deliverables:

- Validation test plan
- Retest results
- Updated risk rating
- Closure approval or residual risk statement
- Monitoring/alerting recommendations

## QA

Primary responsibilities:

- Build regression tests for access control, cookie security, and audit logging.
- Test negative cases and cross-tenant scenarios.
- Confirm UI and API behavior match expected security controls.
- Validate logs and cookie attributes in a production-like environment.

Deliverables:

- QA test cases
- Regression automation coverage
- Test execution evidence
- Defect reports for failed validation

## Product

Primary responsibilities:

- Confirm expected access model for reports.
- Define admin export business requirements.
- Confirm which roles may export data.
- Define export justification, approval, and retention requirements if applicable.
- Prioritize remediation work based on risk.
- Communicate customer or compliance impact if required.

Deliverables:

- Report access rules
- Admin export role/permission matrix
- Audit retention requirement
- Business justification requirements for exports
- Release priority and timeline

---

# Recommended Priority and Timeline

| Priority | Finding | Recommended SLA |
|---:|---|---|
| P1 | Missing object-level authorization on reports | Fix immediately / next hotfix if exploitable |
| P2 | Session cookies lack `Secure` | Fix in next release or sooner |
| P2 | Admin export has no audit log | Fix in next release; prioritize faster if exports include sensitive data |

If the reports IDOR is confirmed exploitable across tenants or customers, treat it as a critical production issue and consider immediate containment.

---

# Suggested Remediation Plan

## Phase 1: Containment

- Disable or restrict vulnerable report operations if exploitation risk is high.
- Confirm all traffic is forced over HTTPS.
- Restrict admin export access to the minimum required roles until audit logging is added.

## Phase 2: Fix Implementation

- Add report object-level authorization.
- Update cookie configuration.
- Add admin export audit logging.
- Add automated tests for all three findings.

## Phase 3: Validation

- QA executes regression tests.
- Security performs targeted retesting.
- Engineering confirms deployment and logs.
- Product confirms behavior aligns with business expectations.

## Phase 4: Monitoring

- Monitor denied report access attempts.
- Monitor admin export events.
- Alert on unusual export activity.
- Track any residual risk through the risk register.

---

# Definition of Done

The remediation handoff is complete when:

1. Engineering has implemented fixes.
2. QA has verified expected behavior and regression coverage.
3. Security has retested and approved closure.
4. Product has confirmed access and export business rules.
5. Residual risks are documented and accepted by the appropriate owner, if any.
