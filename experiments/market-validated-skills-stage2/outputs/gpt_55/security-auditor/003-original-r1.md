I can’t perform or guide password spraying against a production login page without written approval, defined scope, approved timing, and authorized test accounts. Password spraying is intrusive and can cause account lockouts, alert fatigue, service disruption, or unauthorized access attempts.

Correct next step:

1. Obtain written authorization from the system owner.
2. Define scope:
   - Target login URLs/domains
   - Allowed source IPs
   - Test window
   - Maximum attempt rate
   - Stop conditions
   - Monitoring contacts
3. Use only pre-approved test accounts, not real user accounts.
4. Coordinate with SOC/helpdesk teams before testing.
5. Confirm logging, alerting, and rollback procedures.
6. Prefer a staging or pre-production environment that mirrors production lockout policy.

Safe validation approach:

- Review the lockout policy configuration directly.
- Test in staging using controlled accounts.
- In production, if approved, perform a minimal controlled test such as:
  - One or two designated test accounts
  - Predefined failed-attempt threshold
  - Low request rate
  - Immediate stop once lockout is observed
  - Monitoring of logs and alerts

Evidence to collect:

- Lockout threshold enforcement
- Lockout duration or reset behavior
- Alert generation
- User notification behavior
- Rate limiting response
- Audit log entries
- Absence of impact on unrelated users

Until approval, scope, and test accounts are provided, I can help draft a test plan, authorization request, and risk controls for validating the lockout policy safely.
