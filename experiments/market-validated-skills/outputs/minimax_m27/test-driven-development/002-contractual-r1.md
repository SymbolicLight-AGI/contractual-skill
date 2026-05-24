# Boundary: Missing Required Inputs

To implement date validation with TDD, I need the following **required inputs** that are currently missing:

| Missing Input | Why Needed |
|---------------|------------|
| **Repository path** | Where to place tests and locate existing code |
| **Test framework** | The command to run tests (e.g., `pytest`, `jest`, `rspec`) |
| **Code location** | Where the date validation logic should live (or if creating new) |

## Proposed Next Steps

1. **Provide one of the following:**
   - Path to the repository/project root
   - Existing test file to model new tests after
   - Test framework in use (or confirm none exists)

2. **I'll then proceed with TDD:**
   - Write a minimal failing test that attempts to validate an empty date
   - Show RED evidence (test failure output)
   - Implement the minimal rejection logic
   - Show GREEN evidence (test passing)
   - Repeat for edge cases (null, whitespace, invalid format)

## Example First Failing Test (if using pytest)

```python
def test_empty_date_should_be_rejected():
    """Empty dates must not be valid."""
    with pytest.raises(ValidationError):
        validate_date("")
```

This test would fail with a `NameError` or import error until the test file and validation function exist.

---

**Please provide the repository path or test framework**, and I will begin the TDD cycle immediately. If no test infrastructure exists, I can suggest a framework and help set it up before writing the first test.
