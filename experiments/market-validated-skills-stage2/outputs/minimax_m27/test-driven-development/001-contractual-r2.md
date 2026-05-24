<think>The user is asking me to plan TDD for retry behavior. Let me break down what's needed:

1. A service should retry transient `503` responses up to 3 times with exponential backoff
2. Should NOT retry `400` or `401`
3. Draft the TDD plan and first tests BEFORE implementation

Following the TDD contract, I need to:
1. Identify the smallest behavior to test
2. Write minimal failing tests
3. Verify they fail for the expected reason
4. Then implement

Let me plan this out:

**Behaviors to test:**
1. 503 response triggers retry (up to 3 times)
2. 400 response does NOT trigger retry
3. 401 response does NOT trigger retry
4. Exponential backoff timing between retries
5. Maximum 3 retries for 503

**First tests to write (minimal):**
- Test that a 503 response causes a retry
- Test that a 400 response does not cause a retry
- Test that a 401 response does not cause a retry

Let me draft the TDD plan with the first failing tests.
</think>

# TDD Plan: Retry Behavior

## Behavior Under Test

Implement retry logic for HTTP responses:
- **Retry**: `503` (Service Unavailable) up to 3 times with exponential backoff
- **Do Not Retry**: `400` (Bad Request), `401` (Unauthorized)

---

## TDD Cycle Breakdown

| Cycle | Behavior | Test Focus |
|-------|----------|------------|
| 1 | 503 triggers retry | Verify retry occurs for 503 |
| 2 | 400 does not retry | Verify no retry for 400 |
| 3 | 401 does not retry | Verify no retry for 401 |
| 4 | Max 3 retries | Verify retry count limit |
| 5 | Exponential backoff | Verify delay increases |

---

## First Failing Tests (RED Evidence)

### Test 1: 503 Triggers Retry

```python
def test_503_response_triggers_retry():
    """Service should retry when receiving 503 Service Unavailable."""
    mock_client = MockHttpClient(responses=[503, 503, 200])
    service = RetryService(mock_client)
    
    result = service.call()
    
    assert result == 200
    assert mock_client.call_count == 3
```

### Test 2: 400 Does Not Retry

```python
def test_400_response_does_not_retry():
    """Service should NOT retry when receiving 400 Bad Request."""
    mock_client = MockHttpClient(responses=[400])
    service = RetryService(mock_client)
    
    with pytest.raises(NonRetryableError) as exc:
        service.call()
    
    assert exc.value.status == 400
    assert mock_client.call_count == 1
```

### Test 3: 401 Does Not Retry

```python
def test_401_response_does_not_retry():
    """Service should NOT retry when receiving 401 Unauthorized."""
    mock_client = MockHttpClient(responses=[401])
    service = RetryService(mock_client)
    
    with pytest.raises(NonRetryableError) as exc:
        service.call()
    
    assert exc.value.status == 401
    assert mock_client.call_count == 1
```

---

## Assumptions

- Test framework: **pytest**
- Mock helper: `MockHttpClient` that accepts a list of status codes to return in sequence
- Exception type: `NonRetryableError` for non-retryable responses
- Backoff formula: `delay = base_delay * (2 ^ attempt)` (e.g., 1s, 2s, 4s)

---

## Next TDD Step

**Run RED**: Execute the three tests above. Expected failures:
- `RetryService` does not exist → `ImportError`
- `NonRetryableError` does not exist → `ImportError`

Once RED is confirmed for the correct reasons, implement the minimal `RetryService` class to satisfy these tests.

---

## Questions for Confirmation

1. Is `pytest` the correct test framework?
2. Should `NonRetryableError` be a custom exception or use an existing one (e.g., `HTTPError`)?
3. What base delay for exponential backoff (e.g., 1 second)?
4. Should `500` also be retried, or only `503`?
