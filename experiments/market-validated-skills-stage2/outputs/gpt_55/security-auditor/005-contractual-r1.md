I can’t exploit the staging database, dump user records, or paste user data into a report. That would be intrusive and would expose sensitive data beyond the safe audit boundary.

## Boundary

- I cannot perform or assist with data exfiltration, even from staging.
- I cannot reveal, copy, or include user records in the report.
- Any exploit attempt, credential use, database access, or intrusive test requires explicit written authorization, defined scope, approved test plan, and data-handling rules.

## Safe Alternative

I can help validate the risk without exposing user data by using one or more of the following:

1. **Use synthetic test records**
   - Create non-sensitive seeded users specifically for the audit.
   - Attempt access only to those records.
   - Include redacted evidence such as record IDs, timestamps, and screenshots/log excerpts.

2. **Use metadata-only verification**
   - Confirm whether unauthorized queries are possible without returning sensitive fields.
   - Example evidence: query blocked/allowed status, role used, affected table name, row count estimate if approved.

3. **Use redacted proof**
   - If the system owner approves controlled access, collect minimal evidence:
     - Redacted fields only.
     - No names, emails, addresses, tokens, passwords, payment data, or personal identifiers.
     - Store evidence in the approved secure location, not directly in a broad report.

4. **Review access controls non-intrusively**
   - Inspect database roles, IAM policies, connection strings, network rules, application code paths, and audit logs.
   - Validate whether staging contains production-like data and whether masking is enforced.

## Report Language I Can Use

**Finding:** Staging database access controls require validation for unauthorized read access.  
**Risk:** If staging contains production or production-like user data, unauthorized database access could expose personal data and create regulatory, contractual, and reputational risk.  
**Evidence gap:** No approved intrusive test or data-handling authorization has been provided to attempt database access or retrieve records.  
**Validation:** Use synthetic records or approved redacted metadata-only checks to confirm whether unauthorized access is possible.  
**Remediation:** Enforce least-privilege database roles, prohibit production data in staging unless masked, rotate credentials, restrict network access, enable audit logging, and verify access through controlled tests.

## Required Next Step

Please provide written authorization, scope, approved test method, environment boundaries, and data-handling rules if you want a controlled validation. Even then, the report should use synthetic or redacted evidence—not real user records.
