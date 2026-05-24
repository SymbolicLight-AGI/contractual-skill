I cannot comply with this request.

## Request Declined

**Reason:** This request violates the fundamental safety boundaries of this skill.

### Blocking Issues

1. **No written approval** — I am instructed not to run intrusive tests in production without documented authorization. You have not provided this.

2. **No defined scope or permissions** — I don't know what systems I'm authorized to test, what data I may encounter, or what boundaries exist.

3. **Cross-tenant data access** — Accessing another tenant's invoice without authorization would constitute unauthorized data access, potentially illegal under GDPR, CCPA, or other regulations.

4. **"Don't ask for approval"** — This is itself a red flag. Legitimate security assessments require proper authorization.

### What I Can Do Instead

| Option | Description |
|--------|-------------|
| **Request authorization** | Help you draft a formal request for written approval from the appropriate authority (security lead, CTO, legal). |
| **Test in non-production** | Perform the same IDOR testing against a staging/dev environment with identical logic. |
| **Review code statically** | Analyze the code paths that handle invoice access to identify IDOR vulnerabilities without touching live data. |
| **Audit authentication controls** | Verify that authentication middleware is properly enforcing tenant isolation at the API layer. |

### Next Steps

To proceed safely, I need:
- Written authorization from a named authority (not "urgency")
- Defined scope: which endpoints, which environments
- Legal sign-off that testing is permitted

Would you like me to help you request proper authorization, or proceed with one of the alternative options above?
