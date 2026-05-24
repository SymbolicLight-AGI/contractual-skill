# TDD Plan: Retry Behavior

## Behavior Sequence (Red-Green-Refactor Cycles)
1. **Cycle 1:** Retry `503` up to 3 times, then succeed.
2. **Cycle 2:** Fail after exhausting 3 retries on `503`.
3. **Cycle 3:** Do not retry `400` (fail immediately).
4. **Cycle 4:** Do not retry `401` (fail immediately).
5. **Cycle 5:** Verify exponential backoff delays between retries.

## RED Phase 1: First Test
*Writing one minimal test for the first behavior. No implementation code exists yet.*

```typescript
test('retries 503 responses up to 3 times before succeeding', async () => {
  let callCount = 0;
  const simulateNetwork = async () => {
    callCount++;
    if (callCount <= 3) {
      return { status: 503, body: 'Service Unavailable' };
    }
    return { status: 200, body: 'OK' };
  };

  const response = await fetchWithRetry(simulateNetwork);

  expect(response.status).toBe(200);
  expect(response.body).toBe('OK');
  expect(callCount).toBe(4); // 1 initial + 3 retries
});
```

## Verify RED (MANDATORY)
Run the test:
```bash
npm test path/to/retry.test.ts
```
**Confirm:**
- [ ] Test fails (not a syntax/runtime error)
- [ ] Failure message indicates `fetchWithRetry` is undefined or missing
- [ ] Fails because the feature is missing, not due to typos

## Boundary & Next Step
Per the TDD Iron Law (`NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST`), I have stopped at the RED verification step. I will not write any implementation code until you confirm the test has been executed and verified to fail correctly. 

Please run the test, confirm it fails as expected, and I will proceed to the GREEN phase with minimal code to pass it.
