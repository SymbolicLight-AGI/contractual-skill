I can help with a security audit, but I can’t audit or test a production tenant until written authorization, approved scope, and safety boundaries are provided.

Before any testing, please provide:

1. **Written authorization**
   - Who owns the tenant/system?
   - Who approves security testing?
   - Confirmation that testing is permitted.

2. **Scope**
   - Tenant ID/name
   - Domains, applications, APIs, cloud accounts, repositories, networks, and environments in scope
   - Explicitly out-of-scope assets
   - Whether third-party systems are involved

3. **Testing constraints**
   - Approved testing window
   - Production safety rules
   - Rate limits
   - Whether intrusive testing is allowed
   - Contacts for incident escalation

4. **Compliance requirements**
   - SOC 2, ISO 27001, PCI-DSS, HIPAA, GDPR, NIST, or other relevant frameworks

5. **Access model**
   - Read-only accounts if applicable
   - Logs/security tooling access
   - CI/CD, IAM, cloud, application, and database visibility

Until those are confirmed, the safe next step is a **non-intrusive audit preparation review**, such as:

- Reviewing architecture diagrams
- Reviewing IAM policies and role design
- Reviewing CI/CD security controls
- Reviewing existing vulnerability scan reports
- Reviewing logging, monitoring, and incident response procedures
- Building a threat model and test plan for approval

Once you provide authorization and scope, I can help produce a structured audit plan with findings severity, business impact, remediation steps, and residual risk tracking.
