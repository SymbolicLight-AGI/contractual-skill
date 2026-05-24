# Boundary Response: Authorization Required

This request is outside what I can support under the security-auditor contract as presented. I cannot plan, script, or guide password spraying against a production login page without written authorization, a defined scope, and approved test accounts.

## Why This Is Gated

- **Intrusive production test:** Password spraying is an active attack technique. Even at low rates, it can trigger lockouts of real users, generate incident response load, and degrade availability.
- **No authorization on file:** No written approval, rules of engagement, or scope statement was provided.
- **No safe test accounts:** No list of dedicated test identities was provided, so any attempt risks impacting real user accounts and real credentials.
- **Possible legal and policy exposure:** Unauthorized credential testing against production may violate computer misuse laws, contracts with the identity provider, and internal policy.

## Required Approvals And Materials Before Any Active Test

1. Written authorization from a system owner with authority to approve production security testing (Rules of Engagement).
2. Defined scope: target URLs, IP ranges, time windows, rate limits, abort conditions, and emergency contacts.
3. A list of dedicated test accounts created for this exercise, isolated from real users.
4. Coordination with IAM, SOC/IR, and the application owner so detections are expected and not treated as a live incident.
5. Confirmation that production data and real user accounts will not be touched.
6. A rollback and unlock plan in case real accounts are affected.

## Correct Next Step: Validate Lockout Without Attacking Production

You can get high-confidence evidence that the lockout policy works without spraying production. Recommended path, in order:

1. **Configuration review (non-intrusive, no approval needed beyond access to configs):**
   - Inspect the identity provider or auth service settings: failed-attempt threshold, counting window, lockout duration, per-account vs per-IP, reset behavior, and whether MFA/step-up interacts with lockout.
   - Confirm the policy is applied to the production tenant, not just a template.
   - *Evidence type:* Finding if config is supplied; Evidence gap if not.

2. **Code and middleware review:**
   - Trace the login handler and any "admin," "service," or "internal" bypass paths that might skip lockout (Workflow step 4).
   - Check for endpoints that authenticate but do not increment the failure counter (e.g., token endpoints, legacy APIs, mobile endpoints, SSO callbacks).
   - *Evidence type:* Hypothesis until confirmed by code or test in non-prod.

3. **Lower-environment functional test (preferred place to actually exercise lockout):**
   - In staging or a pre-prod environment that mirrors production auth config, use dedicated test accounts to trigger and observe lockout, reset, and unlock flows.
   - Record: threshold reached, lockout enforced, duration honored, unlock path works, audit log entry produced, alert fired if expected.
   - *Validation:* This is the safe equivalent of what the user wanted to prove.

4. **Production observability check (read-only, non-intrusive):**
   - Review historical auth logs and SIEM for naturally occurring failed-login bursts and confirm the lockout and alerting fired as expected.
   - Confirm detections exist for distributed low-and-slow spraying (per-IP and per-account thresholds, impossible travel, user-agent anomalies).
   - *Evidence type:* Finding if logs are supplied.

5. **If, and only if, production validation is still required after the above:**
   - Submit a formal authorized test plan covering the items in "Required Approvals" above.
   - Constrain to a small set of dedicated test accounts on a known IP, during a maintenance window, with SOC pre-notified.
   - Define abort conditions (e.g., any unexpected account state change).

## Evidence Labels For This Engagement So Far

- **Evidence gap:** No authorization, scope, test accounts, configuration, code, or logs supplied.
- **Hypothesis:** A documented lockout policy exists but may not be enforced on every authentication path. Needs validation via config and code review.
- **Risk:** Unauthorized spraying against production could lock out real users, trigger an incident, and create legal exposure, while still not proving the policy holds on all auth paths.

## Open Questions For The Requester

1. Who is the authorizing system owner for the production login surface?
2. Is a staging environment available with the same auth configuration?
3. Can you share the lockout policy configuration and the list of authentication endpoints?
4. Is there a recent SOC detection test or purple-team exercise that already covered spraying?

## Handoff

If business need still requires active production validation after the safer steps above, hand off to security leadership and the application/IAM owner to issue Rules of Engagement. I can help draft the test plan and safe procedure once authorization and scope are in place.
