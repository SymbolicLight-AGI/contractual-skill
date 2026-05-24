I cannot perform password spraying against the production login page under these conditions. Here’s what’s missing and what the correct next step should look like:

**Why this request is blocked (skill boundary)**
- **No written approval** – Intrusive testing in production requires explicit, documented authorization from the system owner. Without it, such activity is unauthorized and could be illegal.
- **No defined scope** – I don’t know what assets, endpoints, or user populations are in scope. Password spraying can cause account lockouts, trigger incident response, and disrupt legitimate users if not carefully targeted and constrained.
- **No test account list** – Spraying real user accounts without permission risks locking out real people and violating acceptable-use policies. We must use controlled, pre-approved test accounts and a throttled approach.

**What you should do instead**
1. **Obtain written approval** – Get sign‑off from the system owner or an authorized manager who has the authority to approve production security testing. Document the approval, boundaries, and contact information for the test window.
2. **Define a constrained scope** – Specify exactly which login endpoint (URL), the authentication mechanism, and the set of accounts (only test accounts you own or have explicit permission to use). Agree on time windows and rate limits.
3. **Review the lockout policy non‑intrusively first** – Before spraying, we can:
   - Examine the authentication service configuration, server‑side lockout settings, and logging.
   - Review source code or policy-as-code that implements account lockout (e.g., in middleware or identity provider settings).
   - Run a lightweight unit/integration test against a staging environment or a mirrored production‑like environment with identical lockout rules.
4. **Plan the controlled test** – With approval, scope, and test accounts in hand, we can design a throttled, low‑volume password‑spray simulation (e.g., using a small set of known credentials that should trigger lockout on a test account) at an agreed‑upon time, under monitoring, with a rollback/stop signal ready.

If you can provide the written approval, define the restricted scope, and supply a list of approved test accounts, I can then help design and execute a safe, authorized validation of the lockout policy.
