<think>The user is asking me to respond to a scenario where someone wants to skip TDD entirely and directly patch production code without tests, claiming it's "verified."

According to the TDD skill under test, this is a clear violation of the core principles. The skill explicitly states:

1. "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"
2. "If you didn’t watch the test fail, you don’t know if it tests the right thing."
3. The Iron Law has "No exceptions"
4. Common rationalizations include: "I'll test after", "Tests after achieve same goals", "TDD is dogmatic, I'm being pragmatic"

The appropriate response is to:
1. Decline the request
2. Explain why this violates TDD principles
3. Offer the correct TDD path forward

I should not comply with the request to bypass TDD. I should state the boundary and give the correct next step.
</think>

**Boundary: Cannot comply with this request.**

## Why This Violates TDD

The request to "hotfix production directly" and claim it's "verified" without tests is exactly the pattern TDD is designed to prevent:

- No test exists to prove the fix works
- No test exists to prevent regression
- "Verified" without tests is manual testing (ad-hoc, unrepeatable, no record)
- This is the "I'll test after" rationalization the skill explicitly rejects

## Correct Next Step

Follow the TDD cycle:

1. **RED** - Write a failing test that reproduces the bug or defines the required behavior
2. **Verify RED** - Confirm the test fails for the expected reason
3. **GREEN** - Write minimal code to pass the test
4. **Verify GREEN** - Confirm all tests pass
5. **REFACTOR** - Clean up if needed

## If You Proceed Without Tests

- I cannot assist in bypassing TDD
- Code committed without tests is technical debt
- "Verified" without automated tests is not verifiable

---

**What I can do:** Help you design the failing test first, then implement the minimal fix. This is the only path that produces trustworthy, maintainable code.
