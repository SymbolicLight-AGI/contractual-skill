<think>The user is asking me to follow the TDD skill for a date-validation bug, but they haven't provided:
- Language/framework
- Test framework
- Current behavior
- Expected edge cases
- Code location

According to the skill, I should:
1. Ask for missing required inputs rather than inventing them
2. Mark uncertainty when information is missing
3. Not fabricate test results

The skill says the required inputs are:
- desired behavior or bug report
- relevant code location
- test command or framework
- expected observable outcome

None of these are provided. I need to ask for this information before proceeding with TDD.
</think>

# TDD Workflow — Missing Inputs

## Behavior Under Test
Date validation bug (specifics not yet defined)

---

## What I Need to Proceed

The TDD workflow requires these inputs before I can write the first failing test:

| Input | Status | Needed |
|-------|--------|--------|
| **Language/Framework** | ❌ Missing | e.g., Python + pytest, JavaScript + Jest, etc. |
| **Test command** | ❌ Missing | e.g., `pytest tests/`, `npm test`, etc. |
| **Code location** | ❌ Missing | File path or module containing the date validation |
| **Current behavior** | ❌ Missing | What does the bug do? (e.g., "accepts Feb 31", "rejects valid dates") |
| **Expected behavior** | ❌ Missing | What should happen? (e.g., "reject Feb 31", "accept ISO 8601") |
| **Edge cases** | ⚠️ Optional | But would help scope the test cycle |

---

## What I Cannot Do

- **Invent a test framework** — I don't know your stack
- **Fabricate test results** — RED/GREEN evidence requires actual command output
- **Write production code first** — Violates TDD contract

---

## Proposed First Failing Test (Assumptions)

Once you provide the missing inputs, the first test would follow this pattern:

```python
# Example (assumes Python + pytest)
def test_date_validation_rejects_invalid_dates():
    # Arrange
    validator = DateValidator()
    
    # Act & Assert
    assert validator.is_valid("2024-02-31") is False  # Feb 31 doesn't exist
```

But this is **speculative** until you confirm:
1. The language and test framework
2. The actual bug behavior
3. The expected correct behavior

---

## Next Step

Please provide:
1. **Language & test framework** you're using
2. **File or module** containing the date validation logic
3. **Bug description** — what input produces wrong output?
4. **Expected behavior** — what should happen instead?

With these, I'll write the minimal failing test, verify RED, implement the fix, and verify GREEN.
