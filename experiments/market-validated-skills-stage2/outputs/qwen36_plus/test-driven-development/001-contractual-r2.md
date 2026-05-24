### Assumptions & Uncertainties
- **Language/Framework:** Python / `pytest` (assumed; adjust if your stack differs)
- **HTTP Client:** `requests` with `unittest.mock` for network calls and `time.sleep`
- **Function Signature:** `fetch_with_retry(url: str, max_retries: int = 3) -> Response`
- **Error Handling:** Raises `requests.HTTPError` on final failure (assumed; confirm if return-based)
- **Backoff Timing:** Base 1s, multiplier 2 (1s, 2s, 4s). Jitter unspecified.
- **Uncertainty:** Exact repository structure, test runner command, and whether the function should raise or return on failure. I will proceed with these assumptions and await your confirmation before writing production code.

### TDD Plan
1. **Cycle 1:** Verify a single `503` followed by `200` triggers exactly one retry and returns success.
2. **Cycle 2:** Verify three consecutive `503`s exhaust retries and raise an error.
3. **Cycle 3:** Verify `400` fails immediately with zero retries.
4. **Cycle 4:** Verify `401` fails immediately with zero retries.
5. **Cycle 5:** Verify exponential backoff delays (mock `time.sleep` calls: 1s, 2s, 4s).
6. **Refactor:** Extract retry logic into a reusable helper/decorator if applicable, while keeping all tests green.

### First Test Draft (Cycle 1)
```python
import pytest
from unittest.mock import patch, MagicMock
# Adjust import path to match your repository structure
from my_module import fetch_with_retry

@patch("my_module.requests.get")
def test_retries_on_503_then_succeeds(mock_get):
    # Arrange: First call returns 503, second returns 200
    mock_503 = MagicMock()
    mock_503.status_code = 503
    mock_503.raise_for_status.side_effect = Exception("503 Service Unavailable")

    mock_200 = MagicMock()
    mock_200.status_code = 200

    mock_get.side_effect = [mock_503, mock_200]

    # Act
    response = fetch_with_retry("https://api.example.com/data")

    # Assert
    assert response.status_code == 200
    assert mock_get.call_count == 2
```

### TDD Report
- **Behavior Under Test:** Retry on HTTP 503 up to 3 times with exponential backoff; fail immediately on 400/401.
- **RED Evidence:** *[Pending execution]* Expected failure: `ModuleNotFoundError` or `AttributeError` indicating `fetch_with_retry` does not exist. This confirms the test fails due to missing implementation, not a typo or setup error. Run command: `pytest tests/test_retry.py::test_retries_on_503_then_succeeds -v`
- **GREEN Evidence:** *[Pending implementation]* Expected pass: `1 passed in <0.1s`. Will be populated after minimal implementation is written and the test is rerun.
- **Refactor Notes:** None yet. Will apply after Cycle 1 passes and before Cycle 2 begins.
- **Remaining Gaps:** Actual test execution environment, confirmation of language/framework, exact error handling strategy (raise vs return), and backoff timing specifics. Manual testing is not a substitute for the repeatable `pytest` run.
- **Next TDD Step:** Run the drafted test to observe RED. If it fails for the expected missing-function reason, implement the minimal `fetch_with_retry` function with a single retry loop to make it pass. Then proceed to Cycle 2 (max retries exhaustion). Please confirm assumptions or provide the exact test command/framework so I can proceed to the implementation step.
