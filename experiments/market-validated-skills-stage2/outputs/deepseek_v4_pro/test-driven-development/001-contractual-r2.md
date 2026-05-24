## Behavior Under Test

**Retry on transient 503 responses, no retry on 400/401**  
When an HTTP call receives a `503 Service Unavailable`, the service automatically retries the request up to **3 times** with **exponential backoff** between attempts. When the response is `400 Bad Request` or `401 Unauthorized`, the service does **not** retry and returns the failure immediately.

---

## TDD Plan (outline)

I’ll work through the TDD workflow in small, testable increments:

| # | Smallest behavior | Expected RED | Minimal implementation |
|---|-------------------|-------------|------------------------|
| 1 | A single 503 triggers one retry and eventually succeeds | Test fails because no retry logic exists | Wrap the call with one retry on 503 |
| 2 | Exactly 3 retries attempted; after 3 failures, stop and propagate the last error | Test fails for missing retry limit | Add a retry counter, limit to 3 |
| 3 | Delays follow exponential backoff (e.g. 1s, 2s, 4s) | Test fails for fixed/no delay | Use configurable backoff (mock `time.sleep`) |
| 4 | 400 and 401 responses never retry | Test fails because any error triggers retry | Only retry on 503 (status check) |
| (Edge cases) | 0 retries configurable, max retries configurable, other 5xx? (will note in gaps) |

I’ll first focus on behaviors 1 and 4 as they form the core contract.

---

## First Tests (drafted, with assumptions)

**Assumptions** (clearly marked to proceed with TDD when infrastructure is confirmed):  
- Language: Python 3.11+  
- Test framework: `pytest` (with `pytest-mock` for mocking)  
- Code location: `src/http_client.py` with a function `fetch_with_retry(url, max_retries=3, backoff_base=1.0)` that wraps `requests.get`.  
- Test file: `tests/test_http_client.py`  
- Test command: `pytest tests/test_http_client.py -v`  

If these assumptions are incorrect, please provide the actual tooling and file paths.

### Test 1: Retry on 503 succeeds on second attempt

```python
# tests/test_http_client.py
import pytest
from src.http_client import fetch_with_retry

def test_retries_on_503_and_succeeds(mocker):
    # Arrange
    mock_get = mocker.patch("src.http_client.requests.get")
    fake_response_503 = mocker.Mock(status_code=503, ok=False)
    fake_response_200 = mocker.Mock(status_code=200, ok=True)
    mock_get.side_effect = [fake_response_503, fake_response_200]

    # Act
    result = fetch_with_retry("http://example.com")

    # Assert
    assert result.status_code == 200
    assert mock_get.call_count == 2
```

**Expected RED output:**

- The test runner reports a failure because `fetch_with_retry` is not yet defined *or* because it does not retry (only calls `requests.get` once and raises on the 503).
- The failure reason must be the missing retry behavior, not a simple `NameError` – if `fetch_with_retry` doesn’t exist, the first RED will be a `ModuleNotFoundError` or `ImportError`. Once the import is added (with a stub), the test will fail on the assertion `call_count == 2`.

### Test 4 (parallel first step): No retry on 400 or 401

```python
def test_no_retry_on_400(mocker):
    mock_get = mocker.patch("src.http_client.requests.get")
    fake_response_400 = mocker.Mock(status_code=400, ok=False)
    mock_get.return_value = fake_response_400

    result = fetch_with_retry("http://example.com")

    assert result.status_code == 400
    mock_get.assert_called_once()
```

```python
def test_no_retry_on_401(mocker):
    mock_get = mocker.patch("src.http_client.requests.get")
    fake_response_401 = mocker.Mock(status_code=401, ok=False)
    mock_get.return_value = fake_response_401

    result = fetch_with_retry("http://example.com")

    assert result.status_code == 401
    mock_get.assert_called_once()
```

**Expected RED:** The retry logic may currently retry on any error, so `call_count` will be >1. The test will fail because the implementation does not yet check for 400/401.

---

## Gaps / Unknowns (remaining after first tests)

- Exact backoff formula (base × 2^attempt? capped?)
- Whether a final failure after 3 retries raises an exception or returns the last response
- Configuration options (max_retries, backoff base) – TDD can add those as separate behaviours
- Treatment of other 5xx codes – out of scope for now, but will note in future cycles

---

## Missing Inputs – Human Handoff

To move from planning to actual **RED observation**, I need:

1. **Test command and runner** (e.g., `pytest --no-header -q`, `npm test -- …`, etc.)
2. **Exact file path(s)** where the production and test code will live
3. **Confirmation or correction** of the assumptions (language, framework, function signature)

**Next TDD step once you provide those:** I will write the first failing test, run it, capture the RED evidence, then implement the minimal passing code. Please confirm or provide the details.
