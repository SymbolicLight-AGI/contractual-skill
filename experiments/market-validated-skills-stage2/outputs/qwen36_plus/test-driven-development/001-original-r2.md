## TDD Plan: Retry Behavior

### Planned Test Sequence (Red-Green-Refactor Cycles)
1. **Baseline:** Returns successful response immediately on `200`.
2. **Retry Trigger:** Retries exactly once when first attempt returns `503`, succeeds on second.
3. **Max Retries:** Retries up to 3 times on consecutive `503`s, then throws/fails.
4. **No Retry (400):** Fails immediately on `400` without retrying.
5. **No Retry (401):** Fails immediately on `401` without retrying.
6. **Exponential Backoff:** Verifies delay increases between retries (e.g., `1s`, `2s`, `4s`).

---

## Cycle 1: RED - Write Failing Test

```typescript
test('retries once on 503 and returns success on second attempt', async () => {
  let callCount = 0;
  const simulateRequest = async () => {
    callCount++;
    if (callCount === 1) return { status: 503, body: 'Service Unavailable' };
    return { status: 200, body: 'OK' };
  };

  const result = await fetchWithRetry(simulateRequest);

  expect(result.status).toBe(200);
  expect(result.body).toBe('OK');
  expect(callCount).toBe(2);
});
```

---

## Verify RED

Run the test:
```bash
npm test path/to/retry.test.ts
```

**Confirm:**
- [ ] Test fails (not errors)
- [ ] Failure message indicates `fetchWithRetry` is undefined or does not retry (expected behavior missing)
- [ ] Fails because the feature is missing, not due to syntax/typos

---

## Boundary & Next Step

**Boundary:** Per the Iron Law (`NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST`), I will not write any implementation code at this stage. Writing `fetchWithRetry` now would violate TDD.

**Correct Next Step:** Execute the test above. Once you confirm it fails for the expected reason (missing retry logic), reply with the failure output. I will then proceed to **GREEN** with the minimal code required to pass this single test.
