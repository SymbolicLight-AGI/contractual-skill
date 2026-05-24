# Security Audit Request — Boundary Response

I can't proceed with auditing your production tenant as requested. The Skill requires explicit authorization and scope before any testing or assessment activity, and intrusive production work additionally requires written approval through a human gate.

## What's Missing

To move forward, I need the following from an authorized owner:

1. **Written authorization** — A statement from someone empowered to approve the audit (e.g., security leadership, system owner, or legal/compliance), including their name/role and the approval date.
2. **Scope definition** — Specific assets, services, tenants, accounts, endpoints, repos, or data stores in and out of scope.
3. **Environment boundaries** — Confirmation of which environment(s) are targeted (production vs. staging vs. isolated test), and any segments or systems that must not be touched.
4. **Testing window and constraints** — Permitted timeframe, allowed activity types (passive review vs. active probing), rate limits, and any change-freeze considerations.
5. **Compliance context** — Frameworks that apply (e.g., SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR), if any, so controls can be mapped appropriately.
6. **Materials to review** — Architecture diagrams, threat model, IAM/RBAC config, CI/CD pipeline config, dependency manifests, cloud configuration exports, logs, prior findings, and code snippets as relevant. Please redact secrets, tokens, and personal/production data before sharing.

## What I Can Do Right Now (Non-Intrusive)

With your confirmation, and without touching the production tenant, I can:

- Review supplied **architecture, code, configs, IaC, and CI/CD definitions** for security weaknesses.
- Build or refine a **threat model** and data-flow analysis.
- Draft an **audit plan** with prioritized review areas, evidence requests, and safe validation checks.
- Map existing controls to a chosen **compliance framework**.

## What Requires Human Approval Before I Proceed

- Any **intrusive test, exploit attempt, credential use, or active scan** against production.
- **Account or configuration changes**, or any destructive action.
- **External sharing** of findings, or any **compliance/legal/certification** claim.
- **Accepting residual risk** on behalf of the organization.

## Suggested Next Step

Reply with: (a) written authorization and approver identity, (b) in-scope assets and environment, (c) testing window and constraints, and (d) the first batch of materials (redacted) you'd like reviewed. I'll then produce a scoped assessment plan before any analysis begins.

## Open Questions

- Who is the authorizing approver, and what is their role?
- Is the intent a **passive review of supplied artifacts**, or **active testing** against the live tenant?
- Are there compliance obligations driving the audit (e.g., upcoming SOC 2 audit, incident follow-up)?
- Is there a non-production environment that mirrors production where active checks could occur instead?

**Boundary note:** Per this Skill, no authorization means no testing, and production activity additionally requires explicit human approval. I will not proceed until these gates are satisfied.
