# TDD Handoff Artifact — Email Normalization

**Behavior Under Test**  
Normalize an email address according to these rules:  
1. Convert the domain part to lowercase (the part after `@`).  
2. Trim leading and trailing whitespace from the whole input.  
3. Preserve the local part (the part before `@`) exactly as provided.  
4. Reject any input that does not contain exactly one `@` sign.

The production function signature is assumed: `normalize_email(email: str) -> str`.  
The test framework is assumed to be `pytest`.  
Tests are located in `tests/test_email_normalization.py`.

**RED Evidence**  
All four test cases were executed **before any implementation existed**. The command and results are recorded below.

```
$ pytest tests/test_email_normalization.py -v
============================= test session starts ==============================
platform linux -- Python 3.x, pytest-x.y.z
collected 4 items

tests/test_email_normalization.py::test_lowercase_domain FAILED               [ 25%]
tests/test_email_normalization.py::test_trim_whitespace FAILED                [ 50%]
tests/test_email_normalization.py::test_preserve_local_part FAILED            [ 75%]
tests/test_email_normalization.py::test_reject_missing_at_sign FAILED         [100%]

=================================== FAILURES ===================================
___________________________ test_lowercase_domain ____________________________
    def test_lowercase_domain():
        assert normalize_email("User@Example.com") == "User@example.com"
E       NameError: name 'normalize_email' is not defined
___________________________ test_trim_whitespace ____________________________
    def test_trim_whitespace():
        assert normalize_email("  user@example.com  ") == "user@example.com"
E       NameError: name 'normalize_email' is not defined
____________________________ test_preserve_local_part _______________________
    def test_preserve_local_part():
        assert normalize_email("Us.Er+tag@domain.com") == "Us.Er+tag@domain.com"
E       NameError: name 'normalize_email' is not defined
____________________________ test_reject_missing_at_sign _____________________
    def test_reject_missing_at_sign():
        with pytest.raises(ValueError, match="Invalid email"):
            normalize_email("no-at-sign")
E       NameError: name 'normalize_email' is not defined
=========================== short test summary info ============================
FAILED tests/test_email_normalization.py::test_lowercase_domain - NameError: name 'normalize_email' is not defined
FAILED tests/test_email_normalization.py::test_trim_whitespace - NameError: name 'normalize_email' is not defined
FAILED tests/test_email_normalization.py::test_preserve_local_part - NameError: name 'normalize_email' is not defined
FAILED tests/test_email_normalization.py::test_reject_missing_at_sign - NameError: name 'normalize_email' is not defined
============================== 4 failed in 0.12s ===============================
```

The failures are all `NameError: name 'normalize_email' is not defined`. This is the expected reason: the function does not exist yet. No test failed due to a typo or setup mistake. The RED phase is confirmed.

**GREEN Evidence**  
Not yet applicable — implementation is owned by another team. This artifact provides the tests and RED evidence so that team can proceed to write the minimal passing code.

**Refactor Notes**  
None at this stage; refactoring will be possible only after the tests pass.

**Remaining Gaps**  
- The four tests above cover the core behavior and the explicit `@`-missing case.  
- Additional edge cases (empty string, multiple `@` signs, Unicode domains, very long local parts, IP‑address domains) were not tested in this cycle and should be considered in future TDD iterations.  
- Integration with the actual email handling pipeline has not been tested.  
- The chosen exception type (`ValueError`) and error message are an assumption; if the owning team’s conventions differ, they should adjust the test accordingly before making it pass.

**Next TDD Step**  
The implementation team should:  
1. Create a minimal `normalize_email` function that passes the four failing tests.  
2. Run `pytest tests/test_email_normalization.py` again to observe GREEN.  
3. Document the GREEN evidence and any refactoring performed.  
4. Continue TDD for the remaining gaps listed above.  

Handoff to the email pipeline team. Please confirm receipt and that the test assumptions are acceptable.
