I can't begin an audit of your production tenant yet — this request falls outside the skill's safety boundary until prerequisites are confirmed.

## Why I'm pausing

The skill explicitly excludes use when:
- Authorization or scope approval for security testing is missing
- Intrusive tests would touch production without written approval

Your request targets a **production tenant** but doesn't include any of the inputs required to scope or safely execute an audit.

## What I need before proceeding

Please provide the following in writing (or confirm a designated approver has):

1. **Written authorization**
   - Named approver with authority over the production tenant (e.g., CISO, VP Eng, system owner)
   - Explicit "rules of engagement" document or signed scope letter
   - Confirmation that any third-party providers (cloud, SaaS, payment processors) permit testing per their AUP

2. **Target scope**
   - Tenant ID / account ID / domains / IP ranges / API endpoints in scope
   - Explicit out-of-scope assets (e.g., shared infrastructure, partner systems)
   - Data classes that may be touched (PII, PHI, PCI, secrets)

3. **Environment and testing constraints**
   - Production vs. staging vs. mirror — strong preference for non-production for intrusive checks
   - Allowed test types: passive review only, SAST/config review, authenticated DAST, exploit validation, etc.
   - Safe testing window (date/time, time zone, blackout periods)
   - Rate limits and traffic caps to avoid DoS

4. **Compliance and contact info**
   - Applicable frameworks (SOC 2, PCI-DSS, HIPAA, GDPR, ISO 27001)
   - Incident escalation contact and on-call channel
   - Data handling requirements for any findings/evidence

5. **Success criteria**
   - Depth (high-level posture review vs. full pentest vs. compliance gap analysis)
   - Deliverable format (report, ticketed findings, executive summary)
   - Deadline

## Safe next steps you can take now (no auth required)

While authorization is being arranged, I can help with non-intrusive work:

- Draft the **Rules of Engagement / authorization template** for your approver to sign
- Build a **threat model** from architecture diagrams you share
- Review **source code, IaC, CI/CD configs, or policy documents** you provide directly
- Define an **audit plan and checklist** (OWASP ASVS, CIS Benchmarks, compliance mappings)
- Prepare a **scoping questionnaire** for stakeholders

## Recommended path

Strongly recommend scoping the audit against a **staging or production-mirror** environment for any active testing, with production limited to read-only configuration review under a documented change window.

Reply with the authorization and scope details (or pick one of the safe-now options) and I'll proceed.
