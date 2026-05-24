# Remediation Handoff: Security Findings

## Scope & Assumptions

**Assets in scope:**  
- Reports feature/API  
- Session management/authentication cookies  
- Admin export functionality  
- Related backend services, frontend flows, logs, and QA test coverage  

**Findings provided:**  
1. Missing object-level authorization on reports  
2. Session cookies lack `Secure` flag  
3. Admin export has no audit log  

**Compliance requirements:** Not specified. Potential relevance to SOC 2, ISO 27001, GDPR, HIPAA, PCI-DSS depending on exported/report data sensitivity.

**Testing boundary:** This handoff is based on synthetic findings only. Engineering and security should validate in the target environment before closure.

---

# Executive Summary

| ID | Finding | Severity | Primary Risk | Owner |
|---|---|---:|---|---|
| SEC-001 | Missing object-level authorization on reports | High | IDOR / unauthorized report access | Engineering |
| SEC-002 | Session cookies lack `Secure` flag | Medium | Session token exposure over non-TLS channels | Engineering |
| SEC-003 | Admin export has no audit log | Medium | Inability to detect or investigate sensitive data exports | Engineering / Security |

---

# Finding SEC-001: Missing Object-Level Authorization on Reports

## Severity

**High**

## Risk

The reports feature appears to lack object-level authorization checks. This may allow an authenticated user to access, modify, download, or delete reports belonging to another user, organization, tenant, or business unit by changing a report ID or request parameter.

This is a classic **IDOR / broken access control** issue.

## Likely Attack Scenario

An attacker with a valid account intercepts a request such as:

```http
GET /api/reports/report_123
```

They change the identifier:

```http
GET /api/reports/report_456
```

If the backend only checks that the user is authenticated, but not whether the user is authorized for `report_456`, the attacker may access unauthorized data.

## Data Flow Risk

Expected secure flow:

```text
Client/UI
  -> API route/controller
  -> Authentication middleware
  -> Object-level authorization check
  -> Report service
  -> Database query scoped by user/org/tenant
  -> Response
```

Risky flow:

```text
Client/UI
  -> API route/controller
  -> Authentication check only
  -> Report service
  -> Database query by report_id only
  -> Response
```

Special attention should be given to backend paths that use privileged service accounts, Admin SDKs, ORM bypasses, or direct database access, because these can bypass database-level security rules.

## Engineering Remediation

Engineering should implement object-level authorization checks for every report operation, including:

- View report
- Download/export report
- Edit report
- Delete report
- Share report
- List reports
- Bulk report actions
- Background jobs or async report retrieval
- Admin/service-account paths, if applicable

### Required Fix

Every report lookup must be scoped to the authenticated user’s authorization boundary.

Examples:

```sql
SELECT *
FROM reports
WHERE id = :report_id
AND tenant_id = :current_tenant_id;
```

Or, if ownership-based:

```sql
SELECT *
FROM reports
WHERE id = :report_id
AND owner_user_id = :current_user_id;
```

For role-based access:

```text
Allow access only if:
- user belongs to the same tenant/org as the report
- user has required report permission
- report is not archived/deleted/restricted
- sharing rules allow access, if applicable
```

### Engineering Acceptance Criteria

- All report endpoints enforce object-level authorization server-side.
- Authorization is not enforced only in the frontend.
- Report IDs cannot be used to access reports across users, tenants, or organizations.
- Admin/service-account code paths still verify requester authorization before accessing reports.
- Unauthorized access returns a generic `404` or `403` without leaking report existence unnecessarily.
- Authorization checks are covered by unit and integration tests.
- Bulk operations validate each object independently.
- Logs capture denied access attempts without exposing sensitive report contents.

## Security Validation

Security should verify:

- Horizontal access control: user A cannot access user B’s report.
- Cross-tenant access control: tenant A cannot access tenant B’s report.
- Role downgrade scenarios: viewer cannot perform editor/admin actions.
- Direct API requests bypassing UI controls.
- Bulk endpoint abuse.
- Predictable or enumerable report IDs.
- Admin SDK or privileged backend paths that bypass database security rules.

## QA Test Cases

QA should add regression tests for:

| Test Case | Expected Result |
|---|---|
| User accesses own report | Allowed |
| User accesses another user’s report | Denied |
| User accesses another tenant’s report | Denied |
| Viewer edits report | Denied |
| Editor views allowed shared report | Allowed |
| User modifies `report_id` in API request | Denied |
| Bulk export with mixed authorized and unauthorized reports | Unauthorized objects blocked |
| Deleted or archived report access | Denied or handled according to business rules |

## Product Considerations

Product should confirm:

- Report sharing model
- Tenant/org boundaries
- Expected roles and permissions
- Whether users should receive `403`, `404`, or product-specific messaging
- Whether access-denied events should be visible to admins
- Whether existing reports require permission backfill or migration

---

# Finding SEC-002: Session Cookies Lack `Secure` Flag

## Severity

**Medium**

## Risk

Session cookies without the `Secure` attribute may be transmitted over unencrypted HTTP connections. If a user accesses the application through HTTP, a network attacker may capture the session cookie and hijack the session.

This risk is higher if:

- HTTP is still reachable.
- TLS redirects are not enforced.
- The application is used on public or untrusted networks.
- Cookies contain session identifiers or authentication tokens.

## Engineering Remediation

Set the `Secure` flag on all session/authentication cookies.

Recommended cookie attributes:

```http
Set-Cookie: session=<value>; HttpOnly; Secure; SameSite=Lax; Path=/;
```

For highly sensitive flows or cross-site risk reduction:

```http
Set-Cookie: session=<value>; HttpOnly; Secure; SameSite=Strict; Path=/;
```

If cross-site authentication flows require it:

```http
Set-Cookie: session=<value>; HttpOnly; Secure; SameSite=None; Path=/;
```

Note: `SameSite=None` requires `Secure`.

### Additional Controls

Engineering should also confirm:

- HTTPS is enforced for all application routes.
- HTTP requests are redirected to HTTPS.
- HSTS is enabled where appropriate:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

- Cookies containing authentication/session data also use `HttpOnly`.
- Session cookie scope is limited with appropriate `Domain` and `Path`.
- Non-production environments do not weaken production cookie settings accidentally.

## Engineering Acceptance Criteria

- All authentication/session cookies include `Secure`.
- All authentication/session cookies include `HttpOnly`, unless there is a documented exception.
- `SameSite` is explicitly configured.
- HTTPS is enforced in production.
- HTTP access does not expose session cookies.
- Automated tests verify cookie attributes.
- Configuration is environment-safe and cannot silently disable `Secure` in production.

## Security Validation

Security should verify:

- Login response sets cookies with `Secure`.
- Session refresh response sets cookies with `Secure`.
- Logout flow clears cookies safely.
- OAuth/OIDC callback cookies, CSRF cookies, and remember-me cookies are reviewed.
- HTTP requests do not receive or transmit session cookies.
- TLS and HSTS configuration are appropriate.

## QA Test Cases

| Test Case | Expected Result |
|---|---|
| Login over HTTPS | Session cookie has `Secure` |
| Refresh session | Refreshed cookie has `Secure` |
| Logout | Cookie is invalidated/cleared correctly |
| HTTP request to app | Redirects to HTTPS |
| Inspect auth cookies | `Secure`, `HttpOnly`, and `SameSite` are present |
| Cross-browser session test | Auth still works as expected |

## Product Considerations

Product should confirm:

- Any embedded, iframe, or cross-domain login use cases.
- Whether `SameSite=Strict` would break expected workflows.
- Whether mobile apps, SSO, or third-party integrations rely on cookie behavior.
- User impact of enforcing HTTPS-only sessions.

---

# Finding SEC-003: Admin Export Has No Audit Log

## Severity

**Medium**

## Risk

The admin export function appears to allow sensitive data export without audit logging. This weakens detection, investigation, compliance evidence, and accountability.

If an administrator exports customer, financial, operational, or regulated data, the organization may be unable to answer:

- Who exported the data?
- What was exported?
- When did it happen?
- From where was it requested?
- Was the export successful?
- Was the export authorized?
- Was the exported data downloaded?

## Engineering Remediation

Add audit logging for all admin export activity.

### Events to Log

At minimum:

- Export requested
- Export approved, if approval workflow exists
- Export started
- Export completed
- Export failed
- Export downloaded
- Export cancelled or expired

### Required Audit Fields

Each audit event should include:

```json
{
  "event_type": "admin_export_requested",
  "actor_user_id": "user_123",
  "actor_role": "admin",
  "tenant_id": "tenant_456",
  "export_id": "export_789",
  "export_type": "reports",
  "data_scope": "date_range=2026-01-01..2026-01-31",
  "record_count": 2500,
  "request_ip": "203.0.113.10",
  "user_agent": "browser-or-client",
  "timestamp": "2026-05-24T12:00:00Z",
  "status": "success"
}
```

Avoid logging sensitive exported contents directly.

### Security Requirements

- Logs must be tamper-resistant or write-once where possible.
- Logs must be retained according to compliance and business requirements.
- Logs should be searchable by actor, tenant, export ID, and time range.
- Failed and denied export attempts must also be logged.
- Export logs should integrate with SIEM/security monitoring if available.
- Alerting should be configured for suspicious export behavior.

### Suggested Alerts

Security should configure alerts for:

- Large exports
- Repeated exports by the same admin
- Exports outside business hours
- Exports from unusual IPs or geographies
- Export attempts by newly created admins
- Failed export attempts
- Export of high-sensitivity datasets
- Export after permission changes

## Engineering Acceptance Criteria

- All admin export actions emit audit events.
- Audit events include actor, target/scope, timestamp, status, and source metadata.
- Audit logs do not expose sensitive exported data.
- Audit logs are immutable or protected against normal admin modification.
- Export failures and denied attempts are logged.
- Audit events are available to security/compliance reviewers.
- Retention period is documented and enforced.

## Security Validation

Security should verify:

- Export events appear in audit logs.
- Logs contain sufficient detail for investigation.
- Logs do not contain raw sensitive data or secrets.
- Admins cannot delete or alter audit logs through normal application access.
- Events reach SIEM or monitoring platform, if applicable.
- Alerting works for high-risk export patterns.

## QA Test Cases

| Test Case | Expected Result |
|---|---|
| Admin requests export | Audit event created |
| Admin export completes | Completion event created |
| Admin export fails | Failure event created |
| Admin downloads export | Download event created |
| Non-admin attempts export | Denied event logged |
| Export with filters/date range | Scope captured in audit log |
| Large export | Alert or high-risk event generated if configured |
| Audit log access | Only authorized reviewers can view logs |

## Product Considerations

Product should define:

- Which export types require logging.
- Whether admin exports require justification.
- Whether high-risk exports require approval.
- Who can view export audit history.
- Retention period for export audit events.
- Whether customers should see export history for their tenant.
- UX impact of adding justification, approval, or notifications.

---

# Cross-Team Remediation Plan

## Engineering Responsibilities

Engineering owns implementation of the technical fixes.

### Engineering Action Items

1. Add object-level authorization to report access paths.
2. Add or standardize centralized authorization helpers/policies.
3. Ensure privileged backend paths do not bypass authorization.
4. Set `Secure` on session cookies.
5. Confirm `HttpOnly` and `SameSite` settings.
6. Enforce HTTPS and consider HSTS.
7. Add audit logging for admin exports.
8. Protect audit logs from tampering.
9. Add automated unit and integration tests.
10. Provide evidence of fixes to Security and QA.

## Security Responsibilities

Security owns risk validation and control requirements.

### Security Action Items

1. Confirm severity and business impact.
2. Define minimum authorization requirements for reports.
3. Review report data sensitivity.
4. Validate IDOR fixes manually.
5. Review cookie configuration.
6. Define audit log schema and retention requirements.
7. Configure SIEM ingestion and alerts, if applicable.
8. Review residual risk after remediation.
9. Approve closure once evidence is sufficient.

## QA Responsibilities

QA owns regression and acceptance testing.

### QA Action Items

1. Add access-control regression tests for reports.
2. Test cross-user, cross-role, and cross-tenant report access.
3. Verify all session cookies have required attributes.
4. Test HTTPS redirect behavior.
5. Test admin export audit events for success, failure, denied, and download cases.
6. Validate no major product workflow regressions.
7. Document test evidence for release approval.

## Product Responsibilities

Product owns expected behavior and user/business impact.

### Product Action Items

1. Confirm report permission model.
2. Confirm tenant/org/user access boundaries.
3. Define expected UX for unauthorized report access.
4. Confirm cookie/security changes do not break required auth flows.
5. Define admin export audit requirements.
6. Decide whether exports need justification, approval, or customer-visible history.
7. Prioritize remediation in sprint/release planning.
8. Communicate user-facing changes if needed.

---

# Recommended Priority

## Immediate / Hotfix Candidate

### SEC-001: Missing Object-Level Authorization on Reports

This should be addressed first due to the potential for unauthorized data access.

Target remediation: **as soon as possible**, ideally in the next patch release.

## Near-Term

### SEC-002: Session Cookies Lack `Secure`

This is usually a low-effort, high-value fix and should be included in the next deployment after compatibility testing.

## Near-Term

### SEC-003: Admin Export Has No Audit Log

Implement in the next planned release unless the export includes regulated or highly sensitive data. If regulated data is involved, escalate priority.

---

# Definition of Done

A finding can be closed when:

1. Engineering has implemented the remediation.
2. Unit/integration tests are present.
3. QA has completed regression testing.
4. Security has manually validated the fix.
5. Evidence is attached to the ticket.
6. Residual risk is documented.
7. Product has confirmed expected behavior.

---

# Evidence Required for Closure

## SEC-001

- Code references showing authorization enforcement.
- Test results for cross-user and cross-tenant access denial.
- Security validation notes.
- Confirmation that admin/service-account paths are covered.

## SEC-002

- Screenshot or test output showing cookie attributes.
- Configuration showing HTTPS enforcement.
- Test results for login, refresh, and logout flows.

## SEC-003

- Audit log examples for export requested/completed/failed/downloaded.
- Confirmation of log access controls.
- SIEM/monitoring integration evidence, if applicable.
- Retention configuration or documented retention policy.

---

# Residual Risk Notes

Residual risk remains if:

- Report authorization rules are implemented inconsistently across endpoints.
- Bulk operations are not fully covered.
- Privileged service-account paths bypass application authorization.
- Non-production cookie settings leak into production.
- Audit logs exist but are mutable by administrators.
- Export logging does not include enough detail for incident investigation.

Security should validate these areas before closure.
