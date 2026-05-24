## TDD Plan for Retry Behavior

The sequence of tests, each following RED‑GREEN‑REFACTOR and building the feature incrementally:

1. **Success on retry** – Retries a `503` response up to 3 total attempts (initial + 2 retries) and returns the successful response on the third attempt.
2. **Exhaust retries** – After 3 total `503` responses, returns the last `503` (no more retries) and does not throw.
3. **No retry on 400** – A `400` response fails immediately; it is not retried.
4. **No retry on 401** – A `401` response fails immediately; it is not retried.
5. **Exponential backoff** – Between each `503` retry, a delay is applied that doubles each attempt (e.g., 1 s, 2 s, 4 s). Use fake timers to avoid real waits.

The first test (RED) focuses on the simplest happy path: `retries 503 up to 3 times and returns success`.

---

## First Test (RED)

```typescript
// retryRequest.test.ts
import { describe, test, expect } from '@jest/globals';
// Note: retryRequest will be created later; this import will fail initially.
import { retryRequest } from './retryRequest';

describe('retryRequest', () => {
  test('retries 503 up to 3 total attempts and returns success', async () => {
    // Simulate a request function that returns:
    //   503 on the first 2 calls
    //   200 on the 3rd call
    let attempts = 0;
    const makeRequest = async (): Promise<{ status: number; body: string }> => {
      attempts++;
      if (attempts < 3) {
        return { status: 503, body: '' };
      }
      return { status: 200, body: 'OK' };
    };

    const result = await retryRequest(makeRequest);

    expect(result.status).toBe(200);
    expect(result.body).toBe('OK');
    expect(attempts).toBe(3); // initial + 2 retries
  });
});
```

### Verify RED: Run the test and watch it fail

**Expected command:**
```bash
npm test retryRequest.test.ts
```

**Expected failure:**  
The test will error because `retryRequest` is not yet defined (module not found or function not exported). No production code exists.

**Why this is correct:**  
The test fails for the right reason – the feature is missing. This proves that, when implemented, the test will validate retry-on-503 behavior. Once we move to GREEN, we will write the minimal code to make this test pass (a 3‑attempt loop that retries on `503` and returns on any other status).
