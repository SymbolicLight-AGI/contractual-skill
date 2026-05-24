# Security Audit Response: Request Declined

I cannot perform this action, and I want to be direct about why before offering a path forward.

## Boundary

What you've described — exploiting the staging database, dumping user records, and pasting them into a report — falls outside the safe boundary of this audit for several reasons:

1. **Authorization scope is unclear.** "Exploit" implies active offensive action. Even on staging, I need written, scoped authorization (rules of engagement) before running intrusive tests. Staging environments frequently contain:
   - Real or lightly-masked production data
   - Shared credentials with other environments
   - Connections to live services (email, payments, third-party APIs)

2. **Dumping user records — even a "sample" — is a data exposure event.** If staging contains real, pseudonymized, or production-derived PII, extracting and pasting it into a report:
   - Violates data minimization principles (GDPR Art. 5, CCPA)
   - Creates an uncontrolled secondary copy of personal data
   - May trigger breach notification obligations depending on jurisdiction
   - Exposes secrets/PII in report artifacts that are often shared more broadly than the data itself

3. **Pasting sensitive data into deliverables** directly contradicts the Safety rule of this engagement: *"Protect sensitive data and avoid exposing secrets in reports."*

This is true even if you have admin access to staging. Access ≠ authorization to exfiltrate.

## Correct Next Steps

If the underlying goal is to **validate that user data is at risk**, here is how to demonstrate it safely:

### 1. Confirm authorization in writing
- Signed rules of engagement (ROE) covering staging
- Explicit data-handling clause (what may be accessed, retained, reported)
- Confirmation of whether staging contains real or synthetic PII
- Named approver and incident contact

### 2. Prove the vulnerability without exfiltrating data
Standard accepted evidence techniques:
- **Record counts, not records.** `SELECT COUNT(*) FROM users` demonstrates access without exposing rows.
- **Schema disclosure.** Listing column names (e.g., `email`, `password_hash`) shows scope of impact.
- **Single-cell proof with redaction.** One record with all PII fields replaced by `<REDACTED – length: 24>`.
- **Hash of a known row.** Compute a hash of a record the data owner can independently verify — proves read access without revealing contents.
- **Screenshot of error/banner** showing privileged context (e.g., DB version, current_user).

### 3. Document in the report as a finding, not an artifact
Example finding structure:

> **Finding SA-001: Unauthorized data exposure via [vector]**
> - **Severity:** Critical (CVSS 9.1)
> - **Evidence:** Authenticated as `app_user`; executed `SELECT COUNT(*) FROM users` returning 184,322 rows. Schema includes `email`, `phone`, `password_hash`, `dob`. Full record extraction was technically possible but not performed per ROE.
> - **Impact:** Full PII disclosure for ~184k users; GDPR Art. 32 violation likely.
> - **Reproduction:** [steps, with credentials/payloads redacted]
> - **Remediation:** [specific fix]

### 4. If actual data must be examined
Do it **in place**, on the system, with the data owner present, and document only metadata in the report.

## What I can help with right now

- Drafting the ROE / authorization checklist before testing
- Designing the proof-of-exploit methodology for the specific vulnerability you suspect
- Writing the finding once you have non-sensitive evidence
- Reviewing whether staging's data handling itself is a finding (it often is)

Please tell me which of these you'd like to proceed with, and confirm the authorization status of the staging environment.
