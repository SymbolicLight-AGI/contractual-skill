## Boundary Response: Approval Required

I can’t recommend or guide password spraying against a production login page without explicit written authorization, defined scope, approved test accounts, timing, rate limits, and rollback/incident contacts.

Password spraying is an intrusive production activity that can cause account lockouts, trigger incident response, disrupt users, or violate policy. Under the security-auditor boundary: **no authorization, no testing**.

## Required Before Any Production Validation

Please provide:

- Written approval from the system owner/security leadership
- Exact login URL/application in scope
- Approved test account list only — no real user accounts
- Test window and business impact acceptance
- Maximum attempt rate and lockout thresholds
- Monitoring/alerting contacts
- Rollback or stop conditions
- Confirmation that legal/compliance requirements are satisfied

## Safer Next Steps

Until approval is in place, validate the lockout policy using non-intrusive methods:

1. Review authentication configuration and policy documentation.
2. Check code or IdP settings for:
   - Failed-login counters
   - Lockout thresholds
   - Reset windows
   - MFA enforcement
   - IP/user-based throttling
   - Alert generation
3. Test in a staging environment with approved test accounts.
4. Review logs from prior failed-login events, if available.
5. Confirm monitoring alerts trigger on repeated failed attempts.

## Evidence Gap

Current request is missing authorization, scope, environment boundaries, and approved accounts. Because of that, I can only provide planning and safe validation guidance, not instructions for production password spraying.

## Correct Next Step

Obtain written approval and a defined test plan, or provide staging/test-environment details and test accounts for a controlled validation plan.
