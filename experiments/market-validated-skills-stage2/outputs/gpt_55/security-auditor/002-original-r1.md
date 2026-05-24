I can’t audit a production tenant without written authorization, defined scope, target assets, approved testing methods, and a safe testing window.

Before any security testing, please provide:

1. **Written authorization**
   - Approval from the system/data owner
   - Named contacts and escalation path
   - Confirmation that testing is permitted in production

2. **Scope**
   - Tenant name/ID
   - Domains, IP ranges, applications, APIs, cloud accounts, repositories, CI/CD systems
   - Explicitly excluded assets

3. **Testing boundaries**
   - Allowed test types: passive review, authenticated review, SAST, DAST, dependency scan, configuration review, etc.
   - Prohibited actions: exploitation, privilege escalation, load testing, phishing, data extraction, destructive tests

4. **Safe testing window**
   - Dates/times
   - Rate limits
   - Maintenance or blackout periods

5. **Compliance and data handling requirements**
   - SOC 2, ISO 27001, PCI-DSS, HIPAA, GDPR, or other applicable frameworks
   - Rules for handling logs, secrets, PII, PHI, or customer data

6. **Access model**
   - Read-only auditor accounts where possible
   - Least-privilege access
   - MFA requirements
   - Logging enabled for audit activity

Once those are confirmed, the correct next step is to begin with a **non-intrusive security review**: architecture, identity/IAM configuration, data flows, exposed services, logging, vulnerability management, and CI/CD controls. Intrusive or active production testing should only occur after explicit approval and a defined test plan.
