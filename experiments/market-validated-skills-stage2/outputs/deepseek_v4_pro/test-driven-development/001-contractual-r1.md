## TDD Plan: Retry Behavior for HTTP Client

### Behavior Under Test
When the service calls an external HTTP endpoint, it must:
- Retry on transient `503 Service Unavailable` responses up to **3 total attempts** with **exponential backoff** (delay doubles each retry).
- **Not** retry on client errors `400 Bad Request` or `401 Unauthorized`.

### Assumptions & Open Questions
- **Language / Framework:** Not specified. The plan assumes a language with a popular testing framework (e.g., Python + `pytest`, JavaScript + `Jest`, Java + JUnit). I will draft the first test in Python/pytest style as a concrete example; adapt to your stack.
- **HTTP client:** The retry logic is assumed to be a wrapper around a real HTTP client (e.g., `requests`, `axios`). The test will use a mock client to control responses.
- **Backoff measurement:** Exponential backoff involves time delays. Tests will mock the clock or verify delay durations are passed to a scheduler without real waiting.
- **Test command:** Not provided. I’ll assume `pytest tests/retry_test.py` (adjust accordingly).

**Missing information?** Please confirm your tech stack, test runner, and project location so the first test can be written to match your conventions.

### TDD Plan (Red → Green → Refactor Cycles)

**Cycle 1: Retry on 503 until success**
- **Test:** Given a mock that returns `503` for the first two requests and `200` on the third, the call succeeds and the total request count is 3.
- **RED:** The test fails because no retry logic exists (single attempt, fails).
- **GREEN:** Implement minimal loop: catch `503`, retry up to 3 times, return final response.
- **Refactor:** none yet.

**Cycle 2: No retry on 400**
- **Test:** Mock returns `400`. Call fails immediately with `400`, no retries, exactly 1 request.
- **RED:** Current code retries all failures or doesn’t distinguish. Test fails (wrong number of attempts).
- **GREEN:** Add condition: only retry `503`.
- **Refactor:** extract status-check helper.

**Cycle 3: No retry on 401**
- **Test:** Mock returns `401`. Same as 400: single attempt, no retry.
- **RED:** If logic only checks for `503`, test passes; but we write it to ensure coverage. Confirm it passes if already handled; if not, iterate.
- **GREEN/Refactor:** Ensure `401` is handled, possibly via explicit list of retryable codes.

**Cycle 4: Exponential backoff pattern**
- **Test:** Intercept delays passed to a scheduler. With mock clock, call retries on `503` twice; assert delays are `1s`, `2s`, `4s` (base × 2^(retry-1)).
- **RED:** Delay is constant or missing.
- **GREEN:** Implement exponential backoff formula.
- **Refactor:** extract delay calculator.

**Cycle 5: Maximum attempts = 3**
- **Test:** Mock returns `503` forever. Call fails after third attempt, total requests = 3.
- **RED:** Currently may loop indefinitely or stop early.
- **GREEN:** Ensure loop stops after `max_retries + 1` total requests.
- **Refactor:** none.

**Edge Cases to consider later:**
- Retry on network errors (connection timeout) if required (not in spec – skip initially).
- Jitter added to backoff.
- Retries and idempotency key.

### First Test Draft (Cycle 1)

I’ll draft the test in Python using `pytest` and `unittest.mock`. If your language differs, I can translate.

```python
# tests/test_retry.py
import pytest
from unittest.mock import MagicMock, call
from my_service.http_client import make_request_with_retry

def test_retries_on_503_and_succeeds():
    # Arrange
    mock_client = MagicMock()
    # First two calls raise 503, third returns a 200 response
    mock_client.request.side_effect = [
        MagicMock(status_code=503),
        MagicMock(status_code=503),
        MagicMock(status_code=200, text="OK")
    ]
    # Use a fake sleep that records delays without waiting
    fake_sleep = MagicMock()

    # Act
    response = make_request_with_retry(
        client=mock_client,
        method="GET",
        url="https://example.com",
        max_retries=3,
        sleep=fake_sleep   # injectable clock
    )

    # Assert
    assert response.status_code == 200
    assert mock_client.request.call_count == 3
    # Expect two delays between the three attempts (1s, 2s)
    fake_sleep.assert_has_calls([call(1.0), call(2.0)], any_order=False)
```

**Expected RED failure:** No `make_request_with_retry` function exists, or it does not retry → test raises an error or assertion about call_count (1 instead of 3).

### Test Command
```bash
pytest tests/test_retry.py -v -k "test_retries_on_503"
```

### Next TDD Step
1. Confirm tech stack and adjust the test skeleton to match your project.
2. Set up the test file and dependency (mock client, retry module).
3. Run the test and observe RED (attach the command output).
4. Implement minimal code to pass.
5. Run to GREEN, then proceed to Cycle 2.

**Remaining Gaps:**  
- No test evidence yet (RED/GREEN).  
- Test infrastructure and exact framework still need confirmation.  
- Backoff formula and max retries not yet covered.

Once you confirm the stack, I can refine the first test and proceed to execute the RED phase under the TDD contract.
