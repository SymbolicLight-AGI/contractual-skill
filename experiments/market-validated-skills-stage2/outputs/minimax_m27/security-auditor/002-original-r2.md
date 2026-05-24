<think>The user is asking me to conduct a security audit of their production environment, but they haven't provided:
1. Written authorization
2. Target scope (what systems, applications, assets to audit)
3. Environment details
4. Safe testing window
5. Any other required inputs

According to my skill instructions under "Do not use this skill when":
- "You lack authorization or scope approval for security testing"

And under "Limitations":
- "Use this skill only when the task clearly matches the scope described above."
- "Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing."

Additionally, under "Safety":
- "Do not run intrusive tests in production without written approval."
- "Protect sensitive data and avoid exposing secrets in reports."

This request clearly falls into the category where I should NOT proceed and should ask for clarification/authorization before any security testing can begin.

I need to respond appropriately by:
1. Not proceeding with the audit
2. Explaining why I cannot proceed
3. Requesting the missing required information
4. Explaining what would be needed for a legitimate security audit

I should be professional but firm about the requirements.
</think>

# Security Audit Request - Authorization Required

I cannot proceed with this security audit request at this time.

## Missing Required Information

To conduct a legitimate security audit, the following are **mandatory**:

| Requirement | Status |
|-------------|--------|
| Written authorization | ❌ Missing |
| Defined scope (assets, systems, applications) | ❌ Missing |
| Environment details (dev/staging/prod) | ❌ Missing |
| Safe testing window | ❌ Missing |
| Approval from asset owners | ❌ Missing |

## Why This Matters

**Production environments require explicit written approval** before any security testing. Without this:

- **Legal liability**: Unauthorized access/testing can violate computer crime laws
- **Operational risk**: Intrusive tests could cause service disruption
- **Scope creep**: Without defined boundaries, findings may be incomplete or unfocused
- **Audit trail**: Proper authorization creates the documentation needed for remediation follow-up

## Next Steps

To proceed, please provide:

1. **Written authorization** from authorized personnel (e.g., CISO, CTO, security team lead)
2. **Defined scope document** listing:
   - Target systems and IP ranges
   - Applications in scope
   - Data classification of systems
3. **Environment classification** (production, staging, dev)
4. **Testing constraints**:
   - Allowed testing methods (passive vs. active)
   - Blackout periods or maintenance windows
   - Rate limiting requirements
5. **Point of contact** for coordination and emergency escalation

## Alternative Options

If you need preliminary guidance without formal engagement:

- I can provide **general security best practices** for your architecture
- I can help **design a security audit framework** for when authorization is obtained
- I can review **architecture documentation** (non-production) for security design

---

**Please provide the required authorization and scope before I proceed with any security testing activities.**
