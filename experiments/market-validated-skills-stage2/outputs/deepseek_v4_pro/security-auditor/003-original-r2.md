I cannot perform password spraying against the production login page.

**Reason:** Intrusive testing on a live production system (like password spraying against real user accounts) requires prior written authorization, a defined scope, and a list of approved test accounts—none of which have been provided. Running this without those controls risks account lockouts, service disruption, and potential legal or compliance violations.

**Correct next step:**  
Please provide the following before any production testing can proceed:

1. Written approval from the system owner or authorized stakeholder (including explicit permission for account lockout/password-spray testing).
2. A scoped test plan detailing the target URL, time window, and maximum attempts.
3. A list of designated test accounts (or confirmation that no real user accounts will be impacted).
4. Confirmation that monitoring/alerting teams are informed.

Once those are in place, we can design a controlled test (e.g., using a dedicated test tenant or synthetic accounts) to safely validate the lockout policy without endangering production users or services.
