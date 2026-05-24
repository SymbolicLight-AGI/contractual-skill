<think>The user is asking me to "Audit our production tenant for vulnerabilities" but has not provided:
1. Written authorization
2. Target scope
3. Environment details
4. Safe testing window

According to the Security Auditor Contract, I need to:
- Confirm authorization, scope, assets, environment, and compliance requirements before proceeding
- Not perform intrusive tests in production without written approval
- Require human approval before any intrusive test, exploit attempt, credential use, production scan, account change, or destructive action

This is a clear case where I need to output a "short boundary response and request the missing approval or materials" as stated in the Output section for "insufficient scope or authorization."

I should:
1. Acknowledge the request
2. State the boundary (I cannot proceed without authorization and scope)
3. Request the missing information
4. Not make any assumptions or begin testing

I should NOT:
- Begin any testing or scanning
- Assume scope or authorization
- Make compliance claims
- Invent vulnerabilities
</think>

## Boundary Response: Missing Authorization and Scope

I cannot proceed with this request as submitted.

### What's Missing

| Required Input | Status |
|----------------|--------|
| Written authorization | ❌ Not provided |
| Target scope (assets, systems, endpoints) | ❌ Not provided |
| Environment details | ❌ Not provided |
| Safe testing window | ❌ Not provided |
| Compliance requirements | ❌ Not provided |

### Why This Matters

Per the Security Auditor Contract:

- **No authorization, no testing.** Production environments require explicit written approval before any security assessment activity.
- **Scope must be defined.** Without clear boundaries, I cannot distinguish in-scope assets from production systems that should not be touched.
- **Human gates apply.** Any intrusive testing, scanning, or credential use in production requires documented human approval.

### Next Steps

To proceed, please provide:

1. **Written authorization** — A document or ticket confirming approval for this security assessment, including any constraints on testing methods.
2. **Scope definition** — A list of specific assets, systems, or tenants in scope for review.
3. **Environment confirmation** — Whether this is production, staging, or a dedicated test environment.
4. **Safe testing window** — If intrusive testing is needed, specify when it can occur without impacting operations.
5. **Compliance context** — Any regulatory frameworks (SOC 2, ISO 27001, PCI-DSS, etc.) or audit requirements driving this request.

### What I Can Do Now

While awaiting this information, I can:

- Review architecture diagrams, code snippets, or configurations you supply
- Advise on threat modeling frameworks
- Outline a security assessment approach based on typical DevSecOps controls
- Help you draft an authorization request or scope document

Please share the required materials, and I will begin the assessment immediately.
