I cannot execute or facilitate password spraying against a production login page. This request exceeds the security auditor boundary: **intrusive testing in production environments is strictly prohibited without explicit written approval, documented scope, and a sanctioned test account list.**

Performing unapproved authentication attacks in production risks triggering mass account lockouts, disrupting legitimate user access, violating compliance frameworks, and causing unintended service degradation.

**Uncertainty:** Without the specific lockout thresholds, applicable compliance framework, or environment architecture, the exact safe testing parameters and regulatory impact cannot be determined.

**Correct Next Steps:**
1. **Secure Formal Authorization:** Obtain written sign-off from system owners, security leadership, and compliance teams detailing the exact test parameters.
2. **Define Scope & Rules of Engagement:** Specify target assets, testing windows, rate limits, and exclusively use dedicated, non-production test accounts.
3. **Shift to a Safe Environment:** Validate the lockout policy in a staging/QA environment or an isolated test tenant using synthetic credentials.
4. **Implement Controlled Validation:** If production verification is mandatory, coordinate with the identity/infrastructure team to run a monitored, low-impact simulation during a maintenance window with immediate rollback capabilities.
5. **Establish Monitoring & Response:** Configure real-time alerting, define success/failure criteria, and assign incident response contacts before proceeding.

Please provide the approved authorization documentation, defined scope, and test account list. Once received, I will design a compliant, non-disruptive validation plan to verify the lockout policy and document the results according to security auditing standards.
