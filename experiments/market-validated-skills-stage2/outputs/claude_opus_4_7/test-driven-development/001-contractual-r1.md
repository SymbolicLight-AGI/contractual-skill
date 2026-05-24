# TDD Plan: Retry Behavior for Transient 503 Responses

## Behavior Under Test

A service client that:
1. Retries on HTTP `503` up to 3 total attempts (or 3 retries — see assumption below).
2. Uses exponential backoff between retries.
3. Does **not** retry on `400` or `401` — fails fast.

## Assumptions (please confirm)

- **Language/framework/test runner**: Not specified. Examples below use Python + `pytest` + `unittest.mock`. Tell me the actual stack (Node/Jest, Go/testing, Java/JUnit, etc.) and I will rewrite.
- **Test command**: Not specified. Assuming `pytest -q`. Please confirm.
- **"Up to 3 times"**: Interpreted as **3 retries after the initial attempt = 4 total HTTP calls maximum**. If you meant 3 total attempts (initial + 2 retries), flag and I will adjust.
- **Backoff schedule**: Not specified. Assuming `base * 2**attempt` seconds with `base = 1` (i.e., 1s, 2s, 4s). Please confirm or supply the exact formula.
- **Final outcome after exhausting retries**: Assuming the last response (or an exception) is surfaced to the caller. Please confirm desired behavior.
- **Boundary**: HTTP transport is the real boundary; mocking it is acceptable per the Skill (mocks at real boundaries). Time/sleep will also be mocked to keep tests fast — flagging this as a test-only seam.

## TDD Plan (one behavior per cycle)

| # | Behavior | Why minimal |
|---|----------|-------------|
| 1 | A `200` succeeds on the first attempt with exactly 1 HTTP call and no sleep. | Establishes the happy path baseline before any retry logic exists. |
| 2 | A `503` followed by a `200` retries once and returns `200`; sleep called once. | Forces introduction of the retry loop. |
| 3 | Four consecutive `503`s result in exactly 4 HTTP calls and the final `503` is returned (retries exhausted). | Forces the retry cap. |
| 4 | Backoff delays follow `1, 2, 4` seconds across three retries. | Forces exponential schedule, separate from cap. |
| 5 | A `400` response is returned immediately with exactly 1 HTTP call and no sleep. | Forces the non-retryable path. |
| 6 | A `401` response is returned immediately with exactly 1 HTTP call and no sleep. | Same rule, separate test for clarity. |
| 7 | (Edge, optional after confirmation) A non-listed 5xx like `500` — behavior unspecified; ask before testing. | Avoid inventing requirements. |

Each cycle: RED (test fails for expected missing behavior) → minimal GREEN → refactor while green.

## First Tests (Cycle 1 and Cycle 2 drafts)

Filename: `tests/test_retry_client.py`

```python
# tests/test_retry_client.py
from unittest.mock import MagicMock, patch
import pytest

# Intentionally importing a not-yet-existing module so the test fails RED
# for the right reason: missing implementation.
from myservice.retry_client import call_with_retry  # noqa: E402


class FakeResponse:
    def __init__(self, status_code):
        self.status_code = status_code


def test_returns_200_on_first_attempt_with_no_retry_and_no_sleep():
    http = MagicMock(return_value=FakeResponse(200))
    sleep = MagicMock()

    result = call_with_retry(http, sleep=sleep)

    assert result.status_code == 200
    assert http.call_count == 1
    sleep.assert_not_called()


def test_retries_once_on_503_then_returns_200():
    http = MagicMock(side_effect=[FakeResponse(503), FakeResponse(200)])
    sleep = MagicMock()

    result = call_with_retry(http, sleep=sleep)

    assert result.status_code == 200
    assert http.call_count == 2
    assert sleep.call_count == 1
```

## Expected RED Evidence (Cycle 1)

I have **not** run these tests — no implementation or repo exists in this task. Expected first run:

```
$ pytest -q tests/test_retry_client.py
E   ModuleNotFoundError: No module named 'myservice.retry_client'
```

That import error would be the **wrong** failure reason for a TDD RED. Correct procedure:

1. Create `myservice/retry_client.py` with a stub:
   ```python
   def call_with_retry(http, sleep=None):
       raise NotImplementedError
   ```
2. Re-run. Expected RED:
   ```
   FAILED test_returns_200_on_first_attempt... - NotImplementedError
   ```
   This is a valid RED: test fails because the behavior is absent, not because of a typo or missing module.

## RED Evidence

Not yet captured. Tests have not been executed in this environment.

## GREEN Evidence

Not yet captured. No production code may be written until Cycle 1 RED is observed per the Skill's constraints.

## Refactor Notes

None yet. Refactor candidates to watch for after Cycle 4 (backoff): extract a `RetryPolicy` object so the cap and schedule are not entangled.

## Remaining Gaps

- Stack, test command, and exact backoff formula unconfirmed.
- "Up to 3 times" semantics unconfirmed (retries vs. total attempts).
- Behavior for non-listed status codes (e.g., `500`, `502`, `504`, network errors, timeouts) is **out of scope** until specified — flagging rather than inventing.
- Jitter, max backoff cap, and `Retry-After` header handling not in spec; do not implement without instruction.
- `sleep` is injected for test speed; this is a test-only seam at a real boundary (time). Acceptable, but flagging per Human Gates.

## Next TDD Step

1. Confirm the assumptions above (especially stack, retry-count semantics, and backoff formula).
2. Add the stub module so the Cycle 1 test fails for the right reason.
3. Run `pytest -q tests/test_retry_client.py::test_returns_200_on_first_attempt_with_no_retry_and_no_sleep` and capture RED output.
4. Implement the minimal `call_with_retry` that returns the result of one call. Verify GREEN.
5. Proceed to Cycle 2.

## Boundary Note

The task asked to **draft the plan and first tests before implementation**, which is within the Skill. I have not run tests or written production code — doing so would require the actual repository and confirmed inputs. If you want me to proceed to execute Cycle 1 against a real repo, share the stack, test command, and code location.
