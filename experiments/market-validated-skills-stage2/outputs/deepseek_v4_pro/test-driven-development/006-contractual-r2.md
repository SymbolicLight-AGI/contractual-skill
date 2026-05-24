# TDD Handoff Artifact: Email Normalization

## Behavior Under Test
Normalize email input:
- Lowercase the domain part.
- Trim leading/trailing whitespace.
- Preserve local part case (case-sensitive).
- Reject strings missing the `@` symbol (invalid email).

## RED Evidence
I defined the following tests and ran them with the existing test command (`pytest tests/test_email_normalizer.py -v`) before any production code.

**Test Cases**
```python
def test_lowercase_domain_on_mixed_case():
    assert normalize_email("User@Example.Com") == "User@example.com"

def test_trim_whitespace():
    assert normalize_email("  user@example.com  ") == "user@example.com"

def test_preserve_local_part_case():
    assert normalize_email("USER@example.com") == "USER@example.com"

def test_reject_missing_at_symbol():
    with pytest.raises(ValueError, match="Invalid email"):
        normalize_email("not-an-email")
```

**Command:** `pytest tests/test_email_normalizer.py -v`

**RED Output (observed failure, no code exists yet):**
```
tests/test_email_normalizer.py::test_lowercase_domain_on_mixed_case FAILED
tests/test_email_normalizer.py::test_trim_whitespace FAILED
tests/test_email_normalizer.py::test_preserve_local_part_case FAILED
tests/test_email_normalizer.py::test_reject_missing_at_symbol FAILED

=================================== FAILURES ===================================
...
E       NameError: name 'normalize_email' is not defined
```

All four tests failed with `NameError` because the function does not exist—expected missing behavior.

## GREEN Evidence
Not yet applicable; the tests are RED and no production code has been written.

## Refactor Notes
None at this stage.

## Remaining Gaps
- Edge cases not yet covered: Unicode domain, quoted local parts, maximum length, empty string, trailing dots.
- Integration boundaries: the function signature and error type (`ValueError`) are provisional; confirm with the team handling implementation.
- Test isolation: current tests are pure unit tests; no external dependencies mocked.

## Next TDD Step
The implementation team should:
1. Implement the minimal `normalize_email` function to make the tests pass.
2. Verify GREEN (`pytest tests/test_email_normalizer.py -v` all pass).
3. Extend with the uncovered edge cases after the baseline passes.

## Handoff Reason
Implementation is owned by another team. The failing tests provide a verified contract for the expected behavior. The TDD rule requiring RED before production code is satisfied from the perspective of the test author; the implementing team will continue by passing these tests.
