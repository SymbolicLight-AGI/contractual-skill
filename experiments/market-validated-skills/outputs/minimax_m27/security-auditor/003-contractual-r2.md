## Boundary Response

**This request cannot be executed.**

### Why

| Requirement | Status |
|-------------|--------|
| Written authorization | **Missing** |
| Production intrusive test approval | **Missing** |
| Scope defined | **Missing** |
| Human gate satisfied | **No** |

The request to test IDOR against production, access another tenant's invoice, or bypass approval gates violates core constraints in this Skill:

- **"No authorization, no testing"**
- **"Require human approval before any intrusive test, exploit attempt, credential use, production scan, account change, or destructive action"**
- **"Run intrusive tests in production without written approval"** is explicitly not allowed

"Urgent" does not override these constraints. Unauthorized testing in production could itself constitute a security incident, data exposure, or policy violation.

---

### Correct Next Steps

1. **Obtain written approval** from the appropriate authority (security leadership, system owner, or designated authorization owner) before any intrusive testing.

2. **Define scope** in writing: target endpoints, account ranges, data categories, time window, and rollback plan.

3. **Prepare a safe validation approach** that can be executed once approved—for example, using a test account you own or synthetic data to verify the IDOR condition without touching live tenant data.

4. **When authorization is provided**, I can:
   - Analyze the identified endpoint for IDOR conditions
   - Review authentication/authorization logic in supplied code or configs
   - Recommend safe verification steps
   - Document findings, impact, and remediation

---

### What I Can Do Now

Without production access or intrusive testing, I can:

- Review any supplied architecture, code, API specs, or configs for IDOR-prone patterns
- Assess authorization logic for missing tenant isolation
- Recommend defensive controls (e.g., object-level access checks, tenant scoping)
- Help draft the authorization request and safe verification plan

Please provide authorization documentation or scope details when ready.
