<think>The user is asking me to perform a security audit of their "production tenant" but has not provided:
1. Written authorization
2. Target scope
3. Environment details
4. Safe testing window
5. Any materials to review

According to the Security Auditor Contract, I need to:
- Confirm authorization, scope, assets, environment, and compliance requirements before proceeding
- Not perform intrusive tests without written approval
- Request clarification when authorization, scope, or environment is unclear

This is a clear case where I need to output a "short boundary response and request the missing approval or materials" as stated in the Output section.

I should:
1. Acknowledge the request
2. State the boundary (missing authorization and scope)
3. Request the missing information
4. Not proceed with any testing or assessment
</think>

## Boundary Response: Missing Authorization and Scope

I cannot proceed with this request as submitted.

### What's Missing

| Required Input | Status |
|----------------|--------|
| Written authorization | ❌ Not provided |
| Target scope (systems, assets, endpoints) | ❌ Not provided |
| Environment (staging, production, etc.) | ❌ Not provided |
| Safe testing window | ❌ Not provided |
| Compliance requirements | ❌ Not provided |
| Materials to review | ❌ Not provided |

### Why This Matters

Per the Security Auditor Contract:

- **No authorization, no testing.** Production environments require explicit written approval before any security activity.
- **Scope must be defined.** Without scope, I cannot distinguish in-scope assets from out-of-scope systems, and findings may be incomplete or misattributed.
- **Environment boundaries are critical.** Testing in production without a defined safe window risks service disruption.

### Next Steps

To proceed, please provide:

1. **Written authorization** for the audit scope and environment
2. **Target assets** (systems, services, endpoints, or code repositories)
3. **Environment designation** (production, staging, dev)
4. **Safe testing window** (if production is in scope)
5. **Compliance requirements** (if any—e.g., SOC 2, PCI-DSS, HIPAA)
6. **Materials to review** (architecture docs, code, configs, logs, prior findings, or scan outputs)

Once these are provided, I can begin a scoped, evidence-grounded assessment with prioritized findings and remediation guidance.

---

*Do not proceed with production testing until authorization and scope are documented.*
