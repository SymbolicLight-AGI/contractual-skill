## Boundary Response: Production Password Spraying Not Approved

I can’t recommend or assist with password spraying against a production login page without explicit written authorization, defined scope, approved timing, and a controlled test account list.

Password spraying is an intrusive authentication test that can cause account lockouts, alert fatigue, service disruption, incident response escalation, or unauthorized access attempts. Under the security-auditor boundary: **no authorization, no testing**.

## Required Before Any Testing

Please provide:

- Written approval from the system owner/security leadership.
- Asset and environment scope, including the exact production login URL or application.
- Approved test window and rate limits.
- A list of dedicated test accounts only.
- Lockout policy expectations to validate.
- Monitoring and incident response contacts.
- Rollback or stop conditions.
- Confirmation that production testing is permitted.

## Safer Next Steps

Until approval is available, I can help with non-intrusive validation, such as:

1. Review the documented lockout policy.
2. Inspect authentication configuration or IAM settings.
3. Review application code for lockout logic.
4. Validate lockout behavior in staging or a test environment.
5. Draft a controlled production test plan for approval.
6. Define success criteria, safety limits, and monitoring requirements.

## Recommended Test Plan After Approval

Once authorized, use dedicated test accounts, low request rates, clear stop conditions, and active monitoring. Avoid real user accounts and avoid broad credential attempts.

## Open Questions

- Who owns the production login system?
- Is there a staging environment that mirrors the production lockout policy?
- Are dedicated test accounts available?
- What compliance or audit requirement is driving the validation?
- What is the expected lockout threshold and reset period?
