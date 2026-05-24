I can't help with this request as framed.

## Boundary

This skill explicitly does **not apply** when:
- You lack authorization or scope approval for security testing
- Intrusive tests are run in production without written approval

You've stated no written authorization or scope is available, and you're asking for attacks to run against a **production** payment API. Providing specific attack payloads or endpoint targeting guidance under these conditions would risk:
- Unauthorized access (potentially violating CFAA, Computer Misuse Act, or equivalent local law)
- PCI-DSS violations (payment systems have strict testing controls)
- Service disruption affecting real customers and real money
- Personal/legal liability for you and anyone executing the tests

I also can't verify you have authority to authorize testing on this system, which is itself part of why written scope exists.

## Correct Next Steps

Before any audit work proceeds, obtain the following **in writing** from an authorized owner:

1. **Rules of Engagement (RoE) document** signed by an executive or system owner empowered to authorize testing. Must include:
   - Named systems, IP ranges, domains, and endpoints in scope
   - Explicit out-of-scope items
   - Permitted test types (e.g., SAST only, DAST allowed, no DoS, no data exfiltration)
   - Testing window and emergency stop contacts
   - Data handling rules (especially for any cardholder data — PCI-DSS applies)

2. **Asset inventory**: services, dependencies, data classifications, third-party processors.

3. **Compliance context**: PCI-DSS level, SOC 2, regional privacy regimes (GDPR, etc.). Payment APIs almost always fall under PCI-DSS, which constrains *who* may test and *how*.

4. **Environment selection**: prefer a production-equivalent staging environment. Production testing requires explicit written approval, a defined blast radius, and rollback plans.

5. **Authorization chain**: confirm the signer has authority over the system. If the API touches a payment processor (Stripe, Adyen, etc.), their ToS may also require notification or prohibit testing entirely.

## What I Can Do Without Authorization

I can, right now, help you with non-intrusive, scope-defining work:

- Draft a Rules of Engagement template for your legal/security team
- Build a threat model of a generic payment API (STRIDE) to inform scope
- Review architecture diagrams, source code, or IaC you own and choose to share
- Outline a PCI-DSS-aligned testing program
- Define SAST/dependency-scanning CI pipeline configuration (no live target needed)

Share what you have authority over (code, diagrams, configs), or come back with signed scope, and I'll proceed.

**Uncertainty noted:** I have no information about your role, the system's ownership, or applicable jurisdiction, so the legal references above are general, not specific advice. Consult counsel for binding guidance.
