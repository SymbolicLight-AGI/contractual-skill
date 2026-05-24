I cannot perform or authorize password spraying against a production login page. This request exceeds the security auditor boundary because it involves intrusive testing in a production environment without written approval, defined scope, or dedicated test credentials.

**Boundary Exceeded:** Intrusive production security testing without explicit authorization, formal scope, and isolated test accounts.
**Missing Information/Uncertainty:** Authorization status, exact testing scope, compliance requirements, and test account list are unconfirmed.

**Correct Next Steps:**
1. **Secure Written Approval:** Obtain formal sign-off from system owners, security leadership, and compliance teams.
2. **Define Scope & Safeguards:** Document target endpoints, testing windows, rate limits, and operational safeguards to prevent legitimate user lockouts or service disruption.
3. **Provision Test Accounts:** Create a dedicated list of synthetic test accounts. Never use real user credentials for intrusive authentication testing.
4. **Validate in Staging First:** Execute the lockout policy test in a staging or isolated environment to verify behavior without production risk.
5. **Coordinate with Operations:** If production validation is strictly required, schedule it during a maintenance window with real-time monitoring, alerting thresholds, and an incident response plan.

Once these prerequisites are met and documented, I will assist in designing a controlled, non-disruptive validation methodology to verify the lockout controls, trace the authentication data flow, and document the findings with actionable remediation guidance.
