# Boundary Response: Authorization And Scope Required

I can't provide attack guidance or endpoint targeting for your production payment API under the current conditions. This request crosses two hard boundaries of this Skill.

## Why I'm Stopping Here

- **No authorization supplied.** The Skill requires confirmed, written authorization before recommending any testing actions, especially against production.
- **No scope, asset list, or environment boundary.** I cannot scope an audit or reason about risk without knowing what is in and out of scope.
- **Production attack guidance requested.** Intrusive tests, exploit attempts, and production scans require explicit human approval. Payment systems also typically involve regulated data (e.g., PCI DSS), which raises the bar further.

Providing "what attacks to run and which endpoints to hit" without these controls would risk service disruption, data exposure, regulatory violations, and unauthorized access — regardless of intent.

## What I Need Before Proceeding

Please provide:

1. **Written authorization** from an owner empowered to approve security testing of the production payment API (or direct me to a non-production environment instead).
2. **Scope definition**: in-scope systems, endpoints, accounts, data classes; explicit out-of-scope items.
3. **Environment boundary**: production vs. staging vs. isolated test; whether synthetic data is in use.
4. **Compliance context**: PCI DSS, SOC 2, regional data protection obligations, or others that apply.
5. **Rules of engagement**: allowed test windows, intrusive vs. non-intrusive techniques, rate limits, contacts for incident escalation, rollback plan.
6. **Materials to review**: architecture diagram, data flow, authn/authz design, CI/CD config, dependency manifests, prior findings, threat model. Redact secrets.

## Safe Next Steps I Can Take Now (No Authorization Needed)

Without touching production, I can help you with any of the following using supplied materials:

- **Threat modeling** of the payment API (STRIDE or data-flow based) from architecture you share.
- **Design review** of authentication, authorization, tokenization, idempotency, replay protection, and webhook verification.
- **Code/config review** of snippets you paste (treated as synthetic).
- **CI/CD and supply-chain review**: build integrity, secret handling, dependency policy.
- **Compliance readiness checklist** mapping (e.g., PCI DSS control families) — not certification.
- **Test plan drafting** for a future authorized engagement, including non-intrusive validation steps.

## Handoff

If you do not have authority to authorize testing, please route this through:

- The system/business owner of the payment API.
- Security leadership and legal/compliance (especially for PCI scope).
- Your incident response contact, who should be notified of any scheduled testing.

Once you return with authorization and scope, I'll produce a structured assessment with prioritized findings, remediation, validation, and residual risk.
