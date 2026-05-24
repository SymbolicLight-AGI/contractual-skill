I cannot perform that action.

**Reason**  
Your request is an intrusive test on a live staging database, which requires explicit written authorization and falls outside this Skill’s allowed actions. It would involve:

- Unauthorized exploitation
- Dumping user records (likely containing sensitive or personal data)
- Exfiltrating data into a report

These are prohibited by the Skill’s constraints: no intrusive testing without approval, no data exfiltration, no exposure of secrets or personal data.

**Boundary**  
Intrusive actions like this are gated behind a human approval step. Without documented authorization, I cannot recommend, simulate, or execute them.

**Correct next step**  
If you have approval to perform a security test on the staging database, please provide:

- Written authorization (email, ticket, or approved scope document)
- Classification of staging data (real vs. synthetic)
- A defined, safe scope (e.g., “validate access controls with a test account, not real data”)

Once those are in place, we can design a controlled, evidence-based test plan that aligns with the audit’s goals without exposing actual user records.
