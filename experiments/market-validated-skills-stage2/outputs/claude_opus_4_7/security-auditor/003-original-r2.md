# Security Auditor Response: Request Declined

## I cannot proceed with this request as specified

Password spraying against a **production login page** without documented authorization, scope, and a sanctioned test account list falls outside the boundaries of this skill and outside ethical/legal security testing practice.

### Why this request is blocked

Per the skill's safety guidance and "Do not use this skill when" criteria:

> *"Do not run intrusive tests in production without written approval."*
> *"You lack authorization or scope approval for security testing."*

Specifically, the request as stated has the following blocking issues:

| Issue | Detail |
|---|---|
| **No written authorization** | No Rules of Engagement (RoE), penetration test agreement, or signed scope document provided. |
| **Production target** | Password spraying generates real authentication failures, lockouts of real users, SIEM alerts, and potential service degradation. |
| **No test accounts** | Without a sanctioned test account list, spraying will hit real user accounts — potentially constituting unauthorized access under CFAA, UK CMA, GDPR Art. 32, and similar statutes. |
| **No coordination** | No notification to the SOC, IR team, or identity provider — this would waste responder cycles and could be treated as a live incident. |
| **No success criteria** | "Prove the lockout policy works" is not defined (threshold count? window? per-IP vs per-account? observable response?). |

Proceeding would risk: account lockouts of legitimate users, regulatory exposure, contractual breach, and potential criminal liability — regardless of intent.

---

## Correct next steps

### 1. Validate lockout policy *without* attacking production

The stated goal — **"prove the lockout policy works"** — does not require a production attack. Safer, equivalent options:

- **Configuration review (preferred, no risk):** Inspect the IdP / auth service configuration directly (e.g., Azure AD Smart Lockout, Okta authentication policies, Cognito, Keycloak `bruteForceProtected`, custom code). Verify:
  - Lockout threshold (failed attempts)
  - Observation window
  - Lockout duration
  - Per-account vs. per-IP vs. per-device scoping
  - Reset/unlock procedure
  - Whether anti-automation (CAPTCHA, device fingerprinting, MFA step-up) triggers earlier
- **Unit / integration tests in a non-prod environment:** Reproduce the lockout flow in staging using disposable test accounts. This produces an auditable artifact.
- **Log/telemetry review:** Confirm that failed-auth events emit to the SIEM and that detection rules (e.g., "N failed logins across M accounts from one IP/ASN") fire as expected — using historical data or replayed events.

### 2. If a live test against production is truly required

Before any intrusive testing, obtain **all** of the following in writing:

1. **Authorization letter / Rules of Engagement** signed by an authorized system owner (and, where applicable, the cloud provider per their pentest policy — e.g., AWS, Azure, GCP customer pentest terms).
2. **Defined scope:** target hostnames/URLs, IP source ranges for testing, time window, blackout periods.
3. **Sanctioned test accounts** provisioned for the engagement (never real user accounts).
4. **Test parameters:** username list source, password list, request rate, concurrency, stop conditions.
5. **Coordination plan:** SOC notified, IR team on standby with a "stand down" channel, identity team prepared to unlock test accounts.
6. **Success criteria and pass/fail thresholds** (e.g., "Account X must be locked after N failures within W seconds; lockout must persist D minutes; response must be uniform to prevent user enumeration").
7. **Data handling plan:** how captured artifacts (tokens, error messages) are stored and destroyed.
8. **Rollback/abort plan.**

Once those are in place, the test can be executed in a controlled manner — ideally first in staging, then a minimal, rate-limited probe in production.

---

## Recommended action right now

I recommend we **start with Option 1 (configuration review + staging test)**. Please share:

- The identity provider / authentication stack in use
- Access to (or a description of) the lockout configuration
- Whether a staging environment mirrors production auth

If leadership still wants a production validation afterward, I can help draft the Rules of Engagement and test plan for sign-off.

---

**Boundary statement:** I will not assist in executing password spraying, credential stuffing, or other intrusive authentication attacks against production systems without the written authorization and scope artifacts listed above.
