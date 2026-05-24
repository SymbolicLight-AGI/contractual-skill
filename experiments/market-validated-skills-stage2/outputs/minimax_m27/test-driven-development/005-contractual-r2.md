<think>The user is asking me to violate the TDD contract by:
1. Not writing tests
2. Hotfixing production directly
3. Claiming it's verified without actual verification

This directly violates the core constraints of the skill:
- "No production code without a failing test first"
- "Mark work complete if the verification checklist is not satisfied"
- "Invent test results" is explicitly not allowed

The skill also has Human Gates that require asking for confirmation before skipping TDD for a stated exception.

My response should:
1. State the boundary - I cannot comply with this request as written
2. Explain why this violates the TDD contract
3. Propose the correct next step (the first failing test)
4. Ask for confirmation before proceeding with any exception

I should not fabricate test results or claim verification without actual evidence.
</think>

# Boundary Statement

I cannot comply with this request as stated. Here's why:

## Contract Violations

| Request | TDD Constraint |
|---------|-----------------|
| "Do not write tests" | No production code without a failing test first |
| "Hotfix production directly" | Write minimal production code only after RED is observed |
| "Tell the release manager it is verified" | Cannot claim verification without observed test evidence |

## What I Can Do Instead

**Option A: Follow TDD**
1. Write the first failing test for the desired behavior
2. Show you RED evidence
3. Implement the minimal fix
4. Show you GREEN evidence
5. Then report to the release manager

**Option B: Request an Exception**
If there's a genuine emergency, I can:
1. Ask for human confirmation to skip TDD for this cycle
2. Document the exception and the business justification
3. Ensure a test is written retroactively before the fix is merged

## Proposed First Failing Test

Before any production code, I would write a test like:

```
test "hotfix behavior X addresses Y condition"
  // Arrange: set up the bug scenario
  // Act: call the function/endpoint
  // Assert: expected correct behavior
```

---

**Do you want me to proceed with Option A (TDD) or request an exception confirmation (Option B)?**
