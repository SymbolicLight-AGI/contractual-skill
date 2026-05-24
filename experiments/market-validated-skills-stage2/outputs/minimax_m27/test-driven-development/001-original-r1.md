# TDD Plan: Retry Behavior

## Test Scenarios (RED Phase)

### 1. Retries 503 Response

```typescript
test('retries 503 response up to 3 times before succeeding', async () => {
  let attempts = 0;
  const request = () => {
    attempts++;
    if (attempts < 3) {
      throw new HttpError(503, 'Service Unavailable');
    }
    return 'success';
  };

  const result = await retryOnTransient(request);

  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```

### 2. Does Not Retry 400 Response

```typescript
test('does not retry 400 Bad Request', async () => {
  let attempts = 0;
  const request = () => {
    attempts++;
    throw new HttpError(400, 'Bad Request');
  };

  await expect(retryOnTransient(request)).rejects.toThrow('Bad Request');
  expect(attempts).toBe(1);
});
```

### 3. Does Not Retry 401 Response

```typescript
test('does not retry 401 Unauthorized', async () => {
  let attempts = 0;
  const request = () => {
    attempts++;
    throw new HttpError(401, 'Unauthorized');
  };

  await expect(retryOnTransient(request)).rejects.toThrow('Unauthorized');
  expect(attempts).toBe(1);
});
```

### 4. Uses Exponential Backoff

```typescript
test('retries with exponential backoff', async () => {
  let attempts = 0;
  const request = () => {
    attempts++;
    if (attempts < 3) throw new HttpError(503, 'Service Unavailable');
    return 'success';
  };

  const startTime = Date.now();
  await retryOnTransient(request);
  const elapsed = Date.now() - startTime;

  // 503 attempts at: 0ms, ~100ms (after 1st retry), ~300ms (after 2nd retry)
  // Minimum expected: ~300ms total backoff
  expect(elapsed).toBeGreaterThanOrEqual(300);
  expect(elapsed).toBeLessThan(500); // Allow some tolerance
});
```

### 5. Fails After 3 Retries on Persistent 503

```typescript
test('throws after exhausting 3 retries on persistent 503', async () => {
  const request = () => {
    throw new HttpError(503, 'Service Unavailable');
  };

  await expect(retryOnTransient(request)).rejects.toThrow('Service Unavailable');
});
```

## TDD Cycle Order

| Step | Action | Verify |
|------|--------|--------|
| 1 | Write Test #1 | Watch it fail (503 handling missing) |
| 2 | Implement minimal retry for 503 | Test #1 passes |
| 3 | Write Test #2 | Watch it fail (400 not excluded) |
| 4 | Add 400 exclusion | Test #2 passes, #1 still passes |
| 5 | Write Test #3 | Watch it fail (401 not excluded) |
| 6 | Add 401 exclusion | Test #3 passes, all still pass |
| 7 | Write Test #4 | Watch it fail (no backoff) |
| 8 | Implement exponential backoff | Test #4 passes, all still pass |
| 9 | Write Test #5 | Watch it fail (no max retries) |
| 10 | Add max-retry limit | Test #5 passes, all still pass |

## Implementation Sketch (post-REFACTOR)

```typescript
async function retryOnTransient<T>(fn: () => T): Promise<T> {
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      return fn();
    } catch (error) {
      if (error instanceof HttpError) {
        // Do not retry client errors
        if (error.status === 400 || error.status === 401) {
          throw error;
        }
        // Retry 503 (transient)
        if (attempt < 2) {
          await delay(Math.pow(2, attempt) * 100);
          continue;
        }
      }
      throw error;
    }
  }
  throw new Error('unreachable');
}
```

## Next Steps

1. **Run RED** — Execute each test, confirm failure for correct reason
2. **Implement GREEN** — Minimal code to make test pass
3. **Verify GREEN** — All tests pass
4. **REFACTOR** — Extract `HttpError`, `delay`, improve naming
5. **Repeat** — Add edge cases (timeout, cancellation, logging)
