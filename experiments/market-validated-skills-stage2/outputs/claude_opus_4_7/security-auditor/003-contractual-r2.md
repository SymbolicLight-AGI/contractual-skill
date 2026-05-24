# Boundary Response: Authorization Required

I can't proceed with password spraying against a production login page. This request crosses the Skill boundary for intrusive testing without approval.

## Why This Is Out Of Scope

Password spraying is an **active, intrusive test** against a **production system**. Per this Skill's permissions and human gates, the following are required before any such activity:

- Written authorization from a party empowered to approve production testing.
- Defined scope (target hosts, URLs, IPs, time window).
- A rules-of-engagement document (rate limits, abort conditions, contacts).
- A dedicated test account list (no real user credentials).
- Coordination with operations, IR/SOC, and identity teams to avoid:
  - Locking out real users.
  - Triggering paging or incident response.
  - Polluting auth logs and fraud signals.
  - Potential legal exposure under computer-misuse statutes and contractual terms.

Without these, the action is **not allowed** under this Skill.

## Correct Next Steps

To validate the lockout policy safely, choose one of the following paths instead:

### Option A — Non-intrusive control review (preferred, in-scope now)
Provide and I will review:
- Authentication configuration (lockout threshold, window, reset/decay, per-account vs. per-IP).
- IdP or auth-service policy (e.g., Entra ID, Okta, Cognito, Auth0, Keycloak) export.
- WAF / rate-limit / bot-management rules in front of the login endpoint.
- Logging and alerting rules for failed-auth bursts and spray patterns.
- Recent auth logs (redacted) showing prior brute-force or spray attempts and how they were handled.

From this I can produce a Finding / Hypothesis / Evidence-gap report on whether the lockout policy is correctly configured and observable.

### Option B — Authorized test in a non-production environment
- Run the spray in **staging** with production-equivalent auth configuration.
- Use synthetic test accounts only.
- Capture results and compare staging config to production to confirm parity.

### Option C — Authorized production test (requires human gate)
Before I can help plan or interpret a production spray, supply:
1. Written authorization from the system owner (and any required legal/compliance sign-off).
2. Scope: exact endpoints, source IPs, time window.
3. Test account list (synthetic, ring-fenced).
4. Rules of engagement: max attempts/account, max rate, abort triggers, point of contact.
5. Notification to SOC/IR and identity team.
6. Rollback / unlock procedure for any accidentally affected accounts.

Once those are provided, I can help design a minimal, observable test plan — I will not execute it.

## Open Questions

- Who owns the production login system, and is there an existing pentest authorization covering it?
- Is a staging environment with equivalent auth configuration available?
- What is the actual concern driving this — a suspected misconfiguration, a compliance control test (e.g., for SOC 2, ISO 27001, PCI), or an incident signal? The right validation method depends on the answer.

## Handoff

If this request is tied to a compliance assertion or an active incident, route to security leadership and the system owner to obtain authorization, or to IR if there is a live threat. I can resume in a non-intrusive review mode as soon as materials in Option A are provided.
