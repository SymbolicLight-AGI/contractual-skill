<think>The user is asking me to plan TDD for retry behavior. Let me follow the TDD contract properly.

The task is to:
1. Draft a TDD plan for retry behavior
2. Write first tests before implementation

The behavior to test:
- Retry transient `503` responses up to 3 times with exponential backoff
- Do NOT retry `400` or `401`

Following the TDD workflow, I need to:
1. Identify the smallest behavior to test
2. Write one minimal test that describes the desired behavior
3. Run the test and verify RED (but since this is a plan, I should draft the tests)
4. Continue the cycle

Since this is asking for a "plan" and "first tests", I should:
1. Create a TDD plan
2. Write the first failing tests
3. Show what the RED state would look like

Let me structure this as a proper TDD plan with concrete test examples.

I should ask about:
- Test framework being used
- Test command
- Relevant code location

But since this is a planning exercise, I can make reasonable assumptions and state them clearly.

Let me draft:
1. The TDD plan/cycle
2. First tests (minimal, one at a time)
3. What RED would look like
4. What minimal implementation would look like
</think>

# TDD Plan: Retry Behavior

## Assumptions (please confirm or correct)

- **Test framework**: pytest (common, readable)
- **Test location**: `tests/test_retry_behavior.py`
- **Code location**: `src/retry_service.py` or similar
- **Test command**: `pytest tests/test_retry_behavior.py -v`

If these are incorrect, please provide the actual framework and paths.

---

## Behavior Under Test

A retry mechanism that:
1. Retries `503 Service Unavailable` up to 3 times with exponential backoff
2. Does NOT retry `400 Bad Request`
3. Does NOT retry `401 Unauthorized`
4. Returns success after a successful retry
5. Returns failure after exhausting retries

---

## TDD Cycle 1: Do Not Retry 400

### RED Evidence (Test Draft)

```python
# tests/test_retry_behavior.py
import pytest
from src.retry_service import retry_on_transient

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_does_not_retry_400_bad_request():
    """400 should be returned immediately without retries."""
    call_count = 0
    
    def failing_400():
        nonlocal call_count
        call_count += 1
        return MockResponse(400)
    
    result = retry_on_transient(failing_400)
    
    assert call_count == 1, "Function should be called exactly once for 400"
    assert result.status_code == 400
```

**Expected RED**: `AssertionError: assert 3 == 1` (currently retries 3 times before failing)

---

## TDD Cycle 2: Do Not Retry 401

### RED Evidence (Test Draft)

```python
def test_does_not_retry_401_unauthorized():
    """401 should be returned immediately without retries."""
    call_count = 0
    
    def failing_401():
        nonlocal call_count
        call_count += 1
        return MockResponse(401)
    
    result = retry_on_transient(failing_401)
    
    assert call_count == 1, "Function should be called exactly once for 401"
    assert result.status_code == 401
```

**Expected RED**: `AssertionError: assert 3 == 1`

---

## TDD Cycle 3: Retry 503 Up To 3 Times

### RED Evidence (Test Draft)

```python
def test_retries_503_up_to_3_times():
    """503 should be retried exactly 3 times before returning failure."""
    call_count = 0
    
    def always_503():
        nonlocal call_count
        call_count += 1
        return MockResponse(503)
    
    result = retry_on_transient(always_503)
    
    assert call_count == 4, "Function should be called 4 times (1 initial + 3 retries)"
    assert result.status_code == 503
```

**Expected RED**: `AssertionError: assert 1 == 4` (no retry logic exists yet)

---

## TDD Cycle 4: Succeeds After Retry

### RED Evidence (Test Draft)

```python
def test_succeeds_on_retry_after_503():
    """Should return success if 503 succeeds on retry."""
    call_count = 0
    
    def succeed_on_third_try():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            return MockResponse(503)
        return MockResponse(200)
    
    result = retry_on_transient(succeed_on_third_try)
    
    assert call_count == 3
    assert result.status_code == 200
```

**Expected RED**: `AssertionError: assert 1 == 3`

---

## TDD Cycle 5: Exponential Backoff (Optional/Advanced)

```python
def test_exponential_backoff_timing():
    """Retries should have increasing delays (exponential backoff)."""
    import time
    
    call_times = []
    
    def record_time():
        call_times.append(time.time())
        return MockResponse(503)
    
    retry_on_transient(record_time, max_retries=3)
    
    # Check delays increase exponentially
    delay_1 = call_times[1] - call_times[0]
    delay_2 = call_times[2] - call_times[1]
    delay_3 = call_times[3] - call_times[2]
    
    assert delay_2 > delay_1 * 0.8  # Roughly 2x
    assert delay_3 > delay_2 * 0.8  # Roughly 2x
```

---

## Minimal Implementation Sketch (After RED)

```python
# src/retry_service.py
import time

RETRYABLE_CODES = {503}
NON_RETRYABLE_CODES = {400, 401}
MAX_RETRIES = 3
BASE_DELAY = 0.1  # seconds

def retry_on_transient(func, max_retries=MAX_RETRIES):
    for attempt in range(max_retries + 1):
        response = func()
        if response.status_code in NON_RETRYABLE_CODES:
            return response
        if response.status_code not in RETRYABLE_CODES:
            return response
        if attempt < max_retries:
            time.sleep(BASE_DELAY * (2 ** attempt))  # Exponential backoff
    return response
```

---

## Remaining Gaps

| Gap | Status |
|-----|--------|
| Backoff timing verification | Not yet tested |
| Configurable max_retries | Not yet exposed |
| Configurable retryable codes | Not yet exposed |
| Thread safety | Out of scope for now |

---

## Next TDD Step

**Confirm**: Is pytest the correct framework? What is the actual test command and file structure?

Once confirmed, I will:
1. Create the test file with Cycle 1's test
2. Run it and show RED evidence
3. Implement minimal code to pass
4. Show GREEN evidence
5. Proceed to Cycle 2

Shall I proceed with the first RED cycle?
