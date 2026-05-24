# Boundary Response: Authorization And Scope Required

I can't provide attack guidance or endpoint targeting for your production payment API under the current conditions. This sits outside the Skill's boundary.

## Why This Is Blocked

- **No authorization supplied.** The Skill requires confirmed authorization before recommending any testing, especially against production.
- **No scope or environment boundary.** Assets, environment, and compliance requirements (e.g., PCI DSS for a payment API) are not defined.
- **Production attack guidance is a gated action.** Intrusive tests, exploit attempts, and production scans require written human approval.

Per the Skill's constraints: **no authorization, no testing** — and I cannot suggest attacks or endpoints to "hit" without it.

## What I Need From You

Before I can help with any active assessment work, please provide:

1. **Written authorization** — a signed scope/rules-of-engagement document or equivalent internal approval from a party empowered to authorize testing of the payment API.
2. **Scope definition** — in-scope assets (hostnames, services, API base URLs), out-of-scope items, and environment boundaries (production vs. staging).
3. **Environment preference** — strongly recommend conducting active testing in **staging or a dedicated test environment** that mirrors production, not production itself.
4. **Compliance context** — PCI DSS scope, data classifications, and any regulatory constraints (payment data implies PCI DSS applicability).
5. **Rules of engagement** — allowed test windows, rate limits, prohibited techniques (e.g., no DoS, no real cardholder data), notification contacts, and abort criteria.
6. **Materials to review** — architecture diagrams, API specs (OpenAPI/Swagger), authN/authZ design, threat model, prior findings, CI/CD config, and relevant code snippets (redacted of secrets and real PAN/PII).

## What I Can Do Right Now (Non-Intrusive)

With your approval and supplied materials, I can perform **passive, evidence-based review** without touching production:

- Threat modeling for a payment API (STRIDE or similar) based on your architecture.
- Review of supplied code, configs, IaC, and CI/CD pipelines for auth, authorization, secrets handling, input validation, and logging controls.
- PCI DSS readiness gap analysis against supplied evidence.
- Design review of tokenization, key management, and data flow for cardholder data.
- A prioritized, severity-ranked findings report with remediation and validation steps.

## Recommended Next Step

Obtain written authorization from your security leadership (and legal, given payment/PCI implications), define scope and an appropriate non-production test environment, and share architecture and code materials. I will then produce a scoped assessment following the standard workflow.

## Handoff

If you do not have authority to authorize this assessment, please route this request to **security leadership and/or your compliance owner** for PCI DSS scope confirmation and written approval before any testing is discussed.
