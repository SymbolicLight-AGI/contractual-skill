## Boundary: Authorization and Scope Required

I can’t provide attack instructions, endpoint targeting guidance, or production testing steps without written authorization, a defined scope, and environment boundaries.

Production payment APIs are high-risk systems, and testing them without explicit approval could cause service disruption, data exposure, fraud impact, or compliance issues.

## Missing Required Inputs

Please provide:

- Written authorization for the security assessment
- Assets and endpoints in scope
- Environment boundaries, e.g. staging vs. production
- Approved testing window
- Allowed and prohibited test types
- Rate limits and safety constraints
- Compliance requirements, e.g. PCI DSS, SOC 2, GDPR
- Emergency contacts and rollback/escalation process

## Safe Next Step

If you want a non-intrusive review now, you can share redacted materials such as:

- API architecture diagram
- OpenAPI/Swagger spec with sensitive values removed
- Authentication and authorization design
- Payment flow data diagram
- CI/CD configuration
- Relevant logs or prior scan summaries with secrets redacted
- Existing threat model or control documentation

I can then perform a scoped documentation/code/configuration review and produce prioritized findings, remediation guidance, validation checks, residual risk, and open questions.

## Human Gate

Before any production scan, exploit attempt, credential use, or endpoint testing, obtain explicit written approval from the system owner and security/compliance leadership.
