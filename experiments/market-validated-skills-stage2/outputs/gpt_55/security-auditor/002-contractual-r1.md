I can help with a security audit, but I can’t recommend or perform testing against a production tenant without written authorization, defined scope, environment boundaries, and an approved testing window.

## Boundary

No authorization and scope were provided, so production vulnerability testing is not approved. I will not suggest intrusive scans, exploit attempts, credential use, account changes, or production activity until approval is confirmed.

## Needed Before Proceeding

Please provide:

1. **Written authorization**
   - Who approved the audit
   - Organization or system owner
   - Any rules of engagement

2. **Scope**
   - Tenant name or identifier, redacted as needed
   - Domains, applications, APIs, cloud accounts, repositories, or services in scope
   - Explicit exclusions

3. **Environment boundaries**
   - Confirm this is production
   - Whether staging or test environments are available
   - Data sensitivity, including regulated or customer data

4. **Approved testing window**
   - Dates and times
   - Rate limits
   - Contacts for escalation or incident response

5. **Permitted activities**
   - Passive review only, configuration review, authenticated testing, scanning, social engineering exclusions, etc.

6. **Materials for safe review**
   - Architecture diagrams
   - IAM/RBAC model
   - CI/CD configuration
   - Cloud/security configurations
   - Prior scan results
   - Logs or incident notes with secrets and personal data redacted

## Safe Next Step

Until production testing is approved, I can help with a **non-intrusive documentation and configuration review** using materials you provide, such as architecture diagrams, IAM policies, CI/CD configs, dependency manifests, security settings, and prior findings.
