<think>The user wants me to create a TDD plan for retry behavior with specific requirements:
- Retry transient 503 responses up to 3 times
- Use exponential backoff
- Do NOT retry 400 or 401 responses

Following TDD principles, I need to:
1. Write failing tests first (RED phase)
2. NOT write any implementation code yet
3. Plan out the test cases and the approach

Let me draft the TDD plan with the first tests.

Based on the skill, I should:
- Write tests that describe the desired behavior
- Make sure tests are minimal, clear, and show intent
- One behavior per test
- No mocks unless unavoidable

Let me think about the test cases needed:

1. **503 response - should retry up to 3 times**
   - Test that 503 is retried
   - Test that it retries exactly 3 times before giving up
   - Test that exponential backoff is used

2. **400 response - should NOT retry**
   - Test that 400 fails immediately without retry

3. **401 response - should NOT retry**
   - Test that 401 fails immediately without retry

4. **Success (200) - should NOT retry**
   - Test that success returns immediately

5. **Exponential backoff behavior**
   - Test that delays increase (e.g., 100ms, 200ms, 400ms)

Let me write the first tests following TDD principles - these should be the RED phase tests that will fail until implementation exists.
</think>

# TDD Plan: Retry Behavior

## Test Cases to Write

### 1. Non-Retryable Responses (400, 401)

```typescript
test('does not retry 400 Bad Request', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ status: 400 });
  
  await retryOn503(mockFetch, { url: '/api/test' });
  
  expect(mockFetch).toHaveBeenCalledTimes(1);
});

test('does not retry 401 Unauthorized', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ status: 401 });
  
  await retryOn503(mockFetch, { url: '/api/test' });
  
  expect(mockFetch).toHaveBeenCalledTimes(1);
});
```

### 2. Retryable 503 Response

```typescript
test('retries 503 up to 3 times before failing', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ status: 503 });
  
  await expect(retryOn503(mockFetch, { url: '/api/test' }))
    .rejects.toThrow('Max retries exceeded');
  
  expect(mockFetch).toHaveBeenCalledTimes(3);
});

test('succeeds on 503 then 200', async () => {
  const mockFetch = jest.fn()
    .mockResolvedValueOnce({ status: 503 })
    .mockResolvedValueOnce({ status: 200, body: 'data' });
  
  const result = await retryOn503(mockFetch, { url: '/api/test' });
  
  expect(result).toEqual({ status: 200, body: 'data' });
  expect(mockFetch).toHaveBeenCalledTimes(2);
});
```

### 3. Exponential Backoff Timing

```typescript
test('uses exponential backoff between retries', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ status: 503 });
  const start = Date.now();
  
  await expect(retryOn503(mockFetch, { url: '/api/test' }))
    .rejects.toThrow();
  
  const elapsed = Date.now() - start;
  // 100ms + 200ms + 400ms = ~700ms minimum
  expect(elapsed).toBeGreaterThanOrEqual(700);
});
```

## Execution Order

| Step | Action |
|------|--------|
| 1 | Write all tests above (RED) |
| 2 | Run tests → verify they fail with "function not defined" |
| 3 | Implement minimal `retryOn503` stub |
| 4 | Run tests → verify failures are about behavior, not errors |
| 5 | Implement retry logic with exponential backoff |
| 6 | Run tests → verify all pass (GREEN) |
| 7 | Refactor if needed |

## Next Tests (After First Cycle)

- `succeeds on third retry`
- `passes through non-503 success responses`
- `accepts custom maxRetries option`
- `accepts custom baseDelay option`

---

**Ready to write the first test file?**
