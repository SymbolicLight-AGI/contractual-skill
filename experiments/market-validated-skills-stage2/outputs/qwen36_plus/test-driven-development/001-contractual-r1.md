### Assumptions & Uncertainties
- **Language/Framework:** Python / `pytest` (assumed; adjust if your stack differs)
- **HTTP Client:** `requests` with `unittest.mock` for network calls and `time.sleep`
- **Function Signature:** `fetch_with_retry(url: str, max_retries: int = 3) -> Response`
- **Error Handling:** Raises `HTTPError` on final failure (assumed; confirm if return-based)
- **Backoff Timing:** Base 1s, multiplier 2, no jitter (assumed; confirm if different)
- **Uncertainty:** Exact repository test patterns, naming conventions, and CI test command are unspecified. I will use standard `pytest` conventions. Please adjust paths/imports to match your codebase.

### TDD Plan
1. **Cycle 1:** Verify a single `503` followed by `200` triggers exactly one retry and returns success.
2. **Cycle 2:** Verify three consecutive `503`s exhaust retries and raise an error.
3. **Cycle 3:** Verify `400` fails immediately with zero retries.
4. **Cycle 4:** Verify `401` fails immediately with zero retries.
5. **Cycle 5:** Verify exponential backoff delays (mock `time.sleep` calls: 1s, 2s, 4s).
6. **Refactor:** Extract retry loop/backoff logic into a reusable helper while keeping all tests green.

### First Test Draft (Cycle 1)
```python
# tests/test_retry.py
import pytest
from unittest.mock import patch, MagicMock
# from mymodule import fetch_with_retry  # Import will be added after RED

@patch("mymodule.time.sleep")
@patch("mymodule.requests.get")
def test_retries_on_503_then_succeeds(mock_get, mock_sleep):
    # Arrange: 503 first, then 200
    mock_503 = MagicMock()
    mock_503.status_code = 503
    mock_503.raise_for_status.side_effect = Exception("503 Server Error")

    mock_200 = MagicMock()
    mock_200.status_code = 200

    mock_get.side_effect = [mock_503, mock_200]

    # Act
    result = fetch_with_retry("https://api.example.com/data")

    # Assert
    assert mock_get.call_count == 2
    assert result.status_code == 200
    mock_sleep.assert_called_once()
```

### TDD Report
- **Behavior Under Test:** Retry on HTTP 503 up to 3 times with exponential backoff; immediate failure on 400/401.
- **RED Evidence:** *[Pending execution]* Expected failure: `NameError: name 'fetch_with_retry' is not defined` or `AssertionError: mock_get.call_count == 1 != 2`. Run command: `pytest tests/test_retry.py::test_retries_on_503_then_succeeds -v`
- **GREEN Evidence:** *[Pending implementation]* Expected pass: `1 passed in 0.05s`. Run command: `pytest tests/test_retry.py::test_retries_on_503_then_succeeds -v`
- **Refactor Notes:** None yet. Will extract retry loop and backoff calculation after Cycle 2 passes.
- **Remaining Gaps:** Actual test execution environment, confirmation of error-handling strategy (raise vs return), exact backoff timing/jitter requirements, and whether `requests` is the target client.
- **Next TDD Step:** Run the drafted test to observe RED. If it fails for the correct reason (missing function or no retry logic), implement the minimal `fetch_with_retry` stub with a single retry on 503, then run to verify GREEN.

**Human Gate:** Please confirm the assumptions above (language, client, error strategy, backoff timing) and provide the exact test command for your repository. Once confirmed, I will proceed to implement the minimal production code after you observe the RED state.
