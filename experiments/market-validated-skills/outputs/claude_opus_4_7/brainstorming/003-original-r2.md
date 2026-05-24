I can't implement yet — we're still in brainstorming mode, and the Exit Criteria haven't been met. Specifically:

- No Understanding Lock has been confirmed
- No design approach has been proposed or accepted
- Assumptions and risks haven't been documented
- The Decision Log is empty

This workflow moves money and grants approval authority, so jumping to implementation without design would risk exactly what this skill is meant to prevent: hidden assumptions, missing controls, and fragile systems around refunds, audit, and fraud.

**Boundary:** I won't write or modify code for this workflow until we complete the design process.

**Correct next step:** Start with Step 1 — understanding context — followed by one-question-at-a-time discovery.

To begin, one question:

**Who is the intended approver population for refunds up to $5,000?**

A. Any user with the "Manager" role, globally
B. Only managers within the customer's assigned region/team
C. Only managers in a designated Finance or Support-Ops group
D. Tiered — e.g., line managers up to a lower cap, senior managers up to $5,000
E. Other / not sure yet

Once we settle approver scope, we'll move on to triggers, audit/logging requirements, fraud checks, finance rules, and non-functional requirements (security, reliability, scale) before any design is proposed.
