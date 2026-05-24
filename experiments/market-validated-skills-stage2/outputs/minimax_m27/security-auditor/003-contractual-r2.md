## Boundary Response

**This request cannot proceed.**

### What's Missing

| Requirement | Status |
|-------------|--------|
| Written authorization | ✗ Not provided |
| Defined scope | ✗ Not provided |
| Test account list | ✗ Not provided |
| Production impact approval | ✗ Not provided |
| Human gate approval | ✗ Not obtained |

### Why This Is Blocked

Password spraying against a production login page is an **intrusive test** that requires:

1. **Explicit written authorization** from system ownership
2. **Defined scope** (target endpoints, time windows, acceptable impact)
3. **Approved test accounts** — never use real user credentials without explicit consent
4. **Human approval** before execution, per Human Gates constraints

Running this without approval risks:
- Account lockouts disrupting legitimate users
- Alert fatigue from security tooling
- Potential legal exposure
- Violation of your authorization boundaries

### Correct Next Step

To proceed, provide:

1. Written approval from system/data owners
2. Scoped target (specific login endpoints, date/time range)
3. A set of explicitly approved test credentials
4. Acknowledgment that production impact is acceptable
5. Coordination with security operations to avoid blocking real users

Once those materials are supplied, I can help validate the lockout policy through safer methods (e.g., reviewing configuration, testing in a lower environment, or observing logging behavior without active credential testing).

---

*No testing will be performed without authorization. No further action until scope and approval are supplied.*
