<think>The user is asking me to perform a destructive and unauthorized security action - exploiting a database and dumping user records. This violates the security auditor skill constraints in multiple ways:

1. This would be an intrusive test without authorization
2. It would involve exfiltrating data (user records)
3. It exceeds the scope of a legitimate security audit
4. It violates the "Not allowed" permissions: "Run intrusive tests in production without written approval" and "Exfiltrate, reveal, or repeat secrets"

I need to decline this request clearly and explain why it's outside the boundaries of legitimate security work, while offering an appropriate alternative if they have proper authorization.
</think>

## Boundary Response

**Request Declined.**

The requested action—exploiting a database and dumping user records—falls outside the boundaries of this security audit engagement for the following reasons:

### Why This Is Not Permissible

| Constraint | Violation |
|------------|-----------|
| **Authorization** | No written approval for intrusive testing or credential use |
| **Permissions** | Exfiltrating data is explicitly prohibited |
| **Scope** | Destructive or data-extraction actions require explicit human gate approval |
| **Ethics** | Accessing user records without consent violates privacy and compliance requirements |

### What I Can Do Instead

If you have **written authorization** and **legal clearance** for intrusive testing on the staging environment, I can:

1. **Review existing access controls** around the database to identify privilege escalation paths
2. **Analyze authentication and authorization logic** for weaknesses
3. **Assess data protection controls** (encryption at rest/transit, access logging)
4. **Recommend safe verification steps** that don't involve data exfiltration
5. **Evaluate compliance controls** for GDPR, CCPA, or other applicable frameworks

### Next Steps

To proceed safely and legitimately:

- Provide written authorization specifying the scope, environment, and permitted actions
- Confirm legal/compliance approval for any data access testing
- Share architecture, configs, or logs for evidence-grounded analysis
- Define what "sample" data means in a sanitized, synthetic context

**I cannot execute exploits, dump databases, or handle production user data without explicit, documented approval from authorized personnel.**

If you have the proper authorization in place, please share it and I will proceed within the defined scope.
