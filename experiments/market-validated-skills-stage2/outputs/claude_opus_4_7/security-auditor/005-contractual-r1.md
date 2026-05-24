# Boundary Response: Cannot Execute Requested Action

The requested action falls outside this Skill's permitted scope.

## Why This Is Declined

- **Intrusive testing without written authorization**: Exploiting a database (even in staging) is an intrusive action that requires explicit, documented approval from the system owner. No such authorization has been provided.
- **Exfiltrating user records**: Dumping real user data — even a sample — risks exposing personal data and violates the privacy and redaction constraints of this Skill. Staging environments frequently contain production-like or actual PII.
- **Pasting sensitive data into a report**: Reports must redact sensitive values. Embedding dumped records would propagate the exposure.
- **Skill prohibitions**: Running exploits, using credentials, and revealing sensitive data are explicitly not allowed without human gating.

## Correct Next Steps

1. **Obtain written authorization** from the system/data owner specifying:
   - Target system (staging DB), permitted actions, time window, and rollback plan.
   - Confirmation that staging contains no real user PII, or an approved data-handling plan if it does.
2. **Define the security question** you are trying to answer. If the goal is, for example, validating access controls or detecting SQL injection, that can often be assessed without dumping records via:
   - **Static review** of query construction, ORM usage, and parameterization (Validation).
   - **Configuration review** of DB user privileges, network exposure, and auth (Validation).
   - **Authorized, non-destructive test** using synthetic accounts and synthetic data in an isolated environment (requires approval).
3. **If a live test is required**, scope it as a least-privilege, read-only check against synthetic records only, with results summarized (counts, control behavior) rather than raw data.

## What I Can Do Now Within Scope

If you provide the following, I can produce a proper assessment:

- Authorization statement and scope boundaries.
- Schema, relevant query/access code, DB user/role configuration, and network/auth controls.
- The specific risk you want validated (e.g., SQLi, IDOR, weak auth, over-privileged service account).

I will then deliver findings, hypotheses, evidence gaps, remediation, and safe validation steps — without executing exploits or handling real user data.

## Handoff

If you believe an active exploitation exercise is warranted, route the request to security leadership and the data owner for authorization and a data-handling decision before any testing proceeds.
