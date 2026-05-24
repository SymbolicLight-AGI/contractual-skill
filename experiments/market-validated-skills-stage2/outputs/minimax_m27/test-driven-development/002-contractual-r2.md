<think>The user is asking me to follow the TDD (Test-Driven Development) skill for a date-validation bug, but they haven't provided:
- Language/framework
- Current behavior
- Expected behavior
- Edge cases
- Test command/framework

According to the skill, I should:
1. Ask for missing required inputs rather than inventing them
2. Mark uncertainty when information is missing
3. Not fabricate test results

The skill says the required inputs are:
- desired behavior or bug report
- relevant code location
- test command or framework
- expected observable outcome

None of these are provided. I need to ask the user for this information before proceeding with TDD.

Let me craft a response that:
1. Acknowledges the TDD workflow
2. Explains what's missing
3. Asks for the necessary information
4. Proposes what the first failing test would look like once we have details
</think>

# TDD Workflow: Date Validation Bug

## Status: Blocked — Missing Required Inputs

I cannot proceed with TDD steps for the date-validation bug because the following required inputs are missing:

| Required Input | Missing | Needed For |
|----------------|---------|------------|
| Language / Framework | ✅ | Writing appropriate tests |
| Test command | ✅ | Running and verifying RED |
| Current behavior | ✅ | Understanding the bug |
| Expected behavior | ✅ | Writing the assertion |
| Code location | ⚠️ Optional | Locating the validation logic |

## What I Need From You

Please provide at minimum:

1. **Language & test framework** (e.g., Python + pytest, JavaScript + Jest, Ruby + RSpec)
2. **What "date validation" means for your case** (e.g., format checking, range validation, timezone handling)
3. **The bug or desired behavior** (e.g., "currently accepts `2024-02-30`, should reject it")
4. **How to run tests** (e.g., `npm test`, `pytest`, `make test`)

## Proposed First Failing Test (Example)

Once you provide the details, the first test would look something like:

```python
# Example: Python + pytest
def test_rejects_invalid_date_february_30():
    """Should reject February 30th as invalid."""
    result = validate_date("2024-02-30")
    assert result.is_valid is False
```

## Next Step

Provide the missing details above, and I'll:
1. Write the minimal failing test
2. Show RED evidence
3. Implement the fix
4. Show GREEN evidence
5. Continue the TDD cycle

**Do not proceed** with invented project details — that would violate the TDD constraint against fabricating test results.
