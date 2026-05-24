I can’t perform or facilitate password spraying against a production login page without written approval, defined scope, and controlled test accounts. Password spraying is intrusive and can cause account lockouts, alert fatigue, service disruption, or unauthorized access attempts.

Correct next steps:

1. Obtain written authorization
   - Approved test window
   - Target login URLs / systems in scope
   - Explicit permission for authentication testing
   - Emergency contacts and stop conditions

2. Define safe test parameters
   - Dedicated test accounts only
   - Agreed attempt volume and rate limits
   - Known passwords for test validation
   - Monitoring and rollback plan
   - Coordination with SOC / support teams

3. Validate the lockout policy safely
   - Use non-production first if available
   - Use controlled production test accounts if approved
   - Confirm:
     - Failed-attempt threshold
     - Lockout duration
     - MFA behavior
     - Alerting and logging
     - User notification behavior
     - Rate limiting and IP/device protections

4. Review configuration and logs
   - Identity provider lockout settings
   - WAF / bot protection rules
   - SIEM alerts
   - Authentication audit logs
   - Helpdesk/account recovery workflows

5. Document residual risk
   - Whether spraying is mitigated by lockout, MFA, rate limiting, detection, and response
   - Any gaps in monitoring or enforcement

If you can provide written approval, scope, test accounts, and success criteria, I can help design a safe validation plan.
