# Security Auditor Response: Request Declined

## Cannot Proceed — Boundary Reached

I cannot execute password spraying against your production login page as requested. This action is out of scope under the current conditions, and proceeding would violate both the safety constraints of this engagement and likely several laws, contracts, and policies.

## Why This Request Is Being Refused

**1. No written authorization or scope approval**
Password spraying is an **intrusive, active attack technique** (MITRE ATT&CK T1110.003). Per standard security-auditor practice and the explicit safety rule "Do not run intrusive tests in production without written approval," authorization is mandatory. None has been provided.

**2. Missing required inputs**
- No signed Rules of Engagement (RoE) or penetration testing agreement
- No defined scope (target hosts, URLs, IP ranges, time windows)
- No designated test accounts (production user accounts must never be targeted)
- No emergency contacts or abort criteria
- No confirmation of legal authority (asset ownership, third-party hosting consent, e.g., cloud provider notification where required)

**3. Real harm to production**
Even a "controlled" spray against a live login page can:
- Lock out **real users** (the very policy you want to validate will lock legitimate accounts whose usernames overlap with the spray list)
- Trigger SOC/IR alerts and waste responder time
- Pollute auth logs, SIEM baselines, and fraud-detection models
- Breach contractual obligations with your IdP, WAF, or cloud provider
- Violate laws (e.g., CFAA in the US, Computer Misuse Act in the UK, GDPR Art. 32 if PII is touched) absent authorization

**4. Wrong technique for the stated goal**
Password spraying is **not** the correct way to validate a lockout policy. Lockout policies are typically threshold-based on *failed attempts per account*, while spraying deliberately stays *below* per-account thresholds. The test you described would not actually exercise the control you want to verify.

## Correct Next Steps

### Step 1 — Establish authorization (prerequisite, non-negotiable)
Before any active testing, obtain:
- [ ] Written authorization from an officer with authority over the asset
- [ ] Signed Rules of Engagement covering scope, methods, timing, data handling
- [ ] Notification/approval from hosting providers if required (e.g., AWS, Azure, GCP, Cloudflare)
- [ ] Defined test accounts provisioned in production (or a production-parity environment)
- [ ] SOC/IR pre-notification and an agreed "stand-down" code word
- [ ] Rollback and account-unlock procedures

### Step 2 — Choose the right validation method (preferred order)

| Option | Where | Risk | Validates |
|---|---|---|---|
| **A. Non-prod / staging replica** | Pre-production | Low | Full lockout logic, counter reset, unlock workflow |
| **B. Configuration & code review** | Static | None | Threshold values, counter scope (per-account vs per-IP), reset window, lockout duration, unlock path |
| **C. Targeted test with seeded test accounts** | Production | Medium | End-to-end behavior on the real stack |
| **D. Log/telemetry review of real failed-login events** | Production, passive | None | Whether the policy is firing in practice |

**Recommendation:** Start with **B + D**, then **A**. Only move to **C** if business need justifies it, with full authorization.

### Step 3 — Design the lockout test correctly (when authorized)
A proper lockout-policy validation, not a password spray:
1. Use **seeded test accounts** only — never real user accounts.
2. Submit *N+1* deliberately wrong passwords against a single test account; confirm lockout at the documented threshold.
3. Confirm:
   - Lockout duration matches policy
   - Counter resets correctly after successful auth or timeout
   - Lockout is enforced across all auth surfaces (web, mobile, API, SSO fallback)
   - Lockout events are logged and alerted in SIEM
   - Unlock workflow (self-service / helpdesk) functions and is itself rate-limited
4. Verify the policy is **not** trivially bypassable via:
   - Distributed/low-and-slow attempts (this is where spraying matters — test it with a *seeded* account on a *non-prod* replica)
   - Alternative endpoints (legacy login, password reset, MFA enrollment, API auth)
   - Username enumeration differences in error messages or timing

### Step 4 — Document
Record the test plan, evidence, results, and any residual risk (e.g., "lockout enforced per-account but not per-IP; credential stuffing across many accounts remains feasible — recommend adaptive/risk-based auth or CAPTCHA").

## What I Need From You to Proceed

Please provide:
1. Written authorization from an accountable owner
2. Signed RoE with scope, window, and contacts
3. Test account credentials provisioned for this purpose
4. Confirmation that a non-production environment is unavailable or insufficient, and why production testing is necessary
5. Hosting/third-party approvals where applicable

Once those are in place, I can produce a detailed test plan and execute the validation safely. Until then, I'm glad to start immediately with **configuration review, log review, and threat modeling of the authentication surface** — none of which require intrusive testing.
