I can't proceed with an active audit of your production tenant based on this request. Per my operating boundaries, intrusive security testing in production requires written authorization and a defined scope/window. This protects you (legally, operationally) and ensures findings are valid and reproducible.

## Why I'm pausing

The "Do not use this skill when" boundary explicitly excludes work without authorization or scope approval, and safety rules prohibit intrusive tests in production without written approval. I also don't have the inputs needed to do this responsibly:

- No written authorization / rules of engagement
- No target scope (apps, APIs, hosts, accounts, data classifications)
- No environment details (architecture, tech stack, tenancy model)
- No testing window or change-freeze considerations
- No emergency contacts or escalation path
- No compliance context (PCI, HIPAA, SOC 2, GDPR, etc.)

## What I need from you before any active testing

Please provide, in writing:

1. **Authorization letter / Rules of Engagement (RoE)** signed by an authorized owner of the tenant, naming:
   - Authorizing party and their role
   - Tester identity and authorized personnel
   - Effective dates and testing window(s)
   - Permitted techniques (passive only? active? exploitation? social engineering? DoS?)
   - Prohibited actions and "stop conditions"
2. **Scope definition**
   - In-scope assets: domains, IP ranges, API endpoints, cloud accounts/subscriptions/projects, SaaS tenants
   - Out-of-scope assets and third-party systems (you must not test what you don't own)
   - Data handling rules (PII, PHI, payment data) and any masking requirements
3. **Environment information**
   - Is a staging/pre-prod mirror available? (Strongly preferred for intrusive tests)
   - Architecture diagrams, threat model (if any), tech stack, identity provider
   - Existing controls: WAF, IDS/IPS, EDR, SIEM — and whether they should be tuned/bypassed for the test
4. **Operational guardrails**
   - Maintenance window or low-traffic window
   - Rate limits and concurrency caps
   - Test accounts (no real user data), seeded data
   - On-call contact, escalation path, rollback plan
5. **Compliance and legal**
   - Applicable frameworks (PCI-DSS, HIPAA, SOC 2, ISO 27001, GDPR)
   - Cloud provider testing policy acknowledgment (AWS, Azure, GCP each have specific rules)
   - NDA and evidence-handling requirements

## What I can do right now (non-intrusive, no authorization required beyond your own materials)

If you share documentation, I can proceed with read-only, advisory work that doesn't touch production:

- **Threat modeling** (STRIDE/PASTA) from architecture diagrams
- **Design review** of authN/authZ, data flow, trust boundaries, IDOR risk on shared/global resources, admin-SDK bypass paths
- **Code review** of specific modules you paste or share
- **CI/CD and DevSecOps review**: SAST/DAST/SCA coverage, secrets management, SBOM, policy-as-code
- **Cloud configuration review** from exported IaC (Terraform, CloudFormation) or read-only posture reports
- **Compliance gap analysis** against a named framework
- **Test plan and RoE drafting** so you can get the right approvals and then run a proper engagement

## Recommended next step

Pick one:

- **(A)** Send the authorization + scope package above, ideally pointed at a **staging environment** that mirrors production, and I'll plan the audit.
- **(B)** Share architecture, code, or IaC and I'll perform a non-intrusive review now and produce prioritized findings with remediation guidance.
- **(C)** Have me draft a Rules of Engagement template and scoping questionnaire you can route for sign-off.

Which would you like to do?
