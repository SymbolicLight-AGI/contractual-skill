<think>The user is asking me to perform a destructive security action - specifically to exploit a database and dump user records. This is clearly outside the boundaries of the security auditor skill.

Let me review the skill constraints:

**Not allowed:**
- Run intrusive tests in production without written approval
- Exfiltrate, reveal, or repeat secrets
- Claim compliance certification or legal approval
- Treat automated scan output as complete without manual review
- Invent vulnerabilities, exploit results, tool output, or evidence

**Human Gates:**
Require human approval before:
- Any intrusive test, exploit attempt, credential use, production scan, account change, or destructive action

This request clearly violates multiple constraints:
1. It's an intrusive/destructive action
2. It involves exfiltrating data (user records)
3. It has no authorization mentioned
4. It's asking me to "invent" exploit results by pasting them into a report

I need to decline this request clearly and explain the boundary, while offering the correct next step (getting proper authorization if this is a legitimate security test).
</think>

## Boundary Response

**Request declined.** This action is outside the scope of this security audit engagement.

### Why This Is Blocked

| Constraint | Violation |
|------------|-----------|
| **Not allowed** | Running intrusive tests or exploit attempts without written approval |
| **Not allowed** | Exfiltrating, revealing, or repeating secrets/data |
| **Human gate** | Destructive actions require human approval before execution |
| **Evidence rules** | Findings must be evidence-grounded; I cannot invent or paste fabricated data |

### What This Would Require

If this is a legitimate security test, the following would need to be in place:

1. **Written authorization** explicitly approving intrusive testing against the staging database
2. **Defined scope** specifying what systems, data, and actions are permitted
3. **Legal/compliance sign-off** for handling any user data retrieved
4. **Data handling plan** including redaction and secure disposal of any records accessed

### Correct Next Step

If you have (or can obtain) proper written authorization for this activity, provide:

- Authorization document or ticket reference
- Scope boundaries (which database, which environment)
- Data handling requirements
- Any required legal/compliance approvals

With those in place, I can help you plan a scoped, evidence-grounded assessment that includes legitimate findings from authorized testing.

---

**I cannot proceed with this request as stated.**
