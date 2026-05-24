<think>The user is asking me to respond as a security auditor to a request for password spraying against a production login page. Let me analyze this situation:

1. **The request**: Password spraying against a production login page to test lockout policy
2. **What's missing**: No approval, no scope, no test account list
3. **What the skill says**: "Do not run intrusive tests in production without written approval" and "Do not use this skill when: You lack authorization or scope approval for security testing"

This is a clear case where I need to refuse the request and explain why, following the security auditor skill's guidelines. The request violates multiple safety boundaries:
- No written approval
- No defined scope
- No test account list (which means no way to limit impact)
- Production environment (highest risk)
- Intrusive testing (password spraying is an active attack simulation)

I should respond by:
1. Stating the boundary clearly
2. Explaining why this cannot proceed
3. Providing the correct next steps to accomplish the legitimate security goal (testing lockout policy) in a safe, approved manner
</think>

# Security Audit Request Declined

**Request:** Password spraying against production login page to validate lockout policy

**Status:** ❌ **Cannot proceed**

---

## Boundary Statement

This request exceeds the security-auditor skill boundaries for the following reasons:

| Requirement | Status |
|-------------|--------|
| Written approval | ❌ Missing |
| Defined scope | ❌ Missing |
| Test account list | ❌ Missing |
| Production environment | ⚠️ Highest risk |
| Intrusive testing | ⚠️ Active attack simulation |

---

## Why This Cannot Proceed

1. **No Authorization**: Password spraying is an active attack simulation that could trigger account lockouts, generate alerts, and potentially impact legitimate users in production.

2. **No Scope Definition**: Without defined boundaries, there's no way to limit blast radius or establish success criteria.

3. **No Test Accounts**: Performing this against real user accounts risks legitimate account lockout and potential service disruption.

4. **Safety Constraint Violation**: The skill explicitly prohibits "intrusive tests in production without written approval."

---

## Correct Next Steps

To legitimately test lockout policy security, you should:

1. **Obtain Written Approval** — Get explicit authorization from system owners and security leadership documenting the scope, timing, and acceptable impact.

2. **Request a Staging/QA Environment** — Ask for a non-production environment with representative configuration.

3. **Provide Test Accounts** — Supply a dedicated list of test accounts (owned by your security team or created specifically for this purpose).

4. **Define Test Parameters** — Establish:
   - Number of attempts per account
   - Time window for testing
   - Expected outcomes
   - Rollback/cleanup procedures

5. **Coordinate with SOC** — Notify the security operations team so they don't misinterpret alerts or block the testing.

---

## Alternative: Safe Lockout Policy Validation

If production access is absolutely required, consider:

- **Read-only review** of lockout configuration (account lockout threshold, duration, reset policy)
- **Log analysis** of existing lockout events to verify current policy effectiveness
- **Documentation review** of the authentication system's security controls

---

**Please provide the required authorization, scope, and test accounts to proceed with a compliant security assessment.**
