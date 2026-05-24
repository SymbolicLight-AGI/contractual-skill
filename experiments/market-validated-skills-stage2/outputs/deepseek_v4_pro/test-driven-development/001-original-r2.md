## TDD Plan for Retry Behavior

I’ll follow the full Red-Green-Refactor cycle, building the feature incrementally, test by test. The plan is to start with the simplest behavior and work toward the full requirement.

### Test Cases (in implementation order)

1. **Success on first attempt (no retry)**
   - Given a request that returns `200` on the first call, the function returns the response immediately.
   - No retries, no backoff.

2. **Retries on `503` and succeeds on second attempt (1 retry)**
   - First attempt returns `503` (transient), second returns `200`. The function makes exactly 2 calls and returns success.

3. **Retries up to 3 times on `503` and then fails**
   - Three `503` responses then a final `503`. The function throws/rejects after exhausting 3 retries (4 total attempts: initial + 3 retries).

4. **Does not retry on `400`**
   - First attempt returns `400`. The function immediately throws/rejects without retrying.

5. **Does not retry on `401`**
   - First attempt returns `401`. Same immediate failure, no retry.

6. **Exponential backoff between retries**
   - After each `503`, the function waits before retrying: delays should follow an exponential pattern (e.g., 100ms, 200ms, 400ms) or a similar configurable sequence.
   - We can test this by injecting a mock `delay`/`sleep` function and asserting the arguments.

After each test is written (RED), I’ll verify it fails for the right reason, then write the minimal implementation to pass (GREEN), and refactor only when tests are green.

---

### First Tests (RED Phase)

I’ll start with the two simplest tests that establish the API and core retry loop. These will be written first, before any production code exists.

#### Test file: `retry-fetch.test.ts`

```typescript
// Assume the function under test will be named fetchWithRetry
// Signature: fetchWithRetry(url: string, options?: RequestInit): Promise<Response>

import { fetchWithRetry } from './retry-fetch';

describe('fetchWithRetry', () => {
  test('returns successful response on first attempt without retrying', async () => {
    // Arrange: a fetch that succeeds immediately
    const response = new Response('ok', { status: 200 });
    const mockFetch = jest.fn().mockResolvedValue(response);
    // Dependency injection: pass fetch as optional function or use module mocking
    // We'll assume the function can accept a custom fetch for testing.

    // Act
    const result = await fetchWithRetry('http://example.com', {}, mockFetch);

    // Assert
    expect(result).toBe(response);
    expect(mockFetch).toHaveBeenCalledTimes(1);
  });

  test('retries on 503 and succeeds on second attempt', async () => {
    // Arrange: first call returns 503, second returns 200
    const goodResponse = new Response('ok', { status: 200 });
    const badResponse = new Response('Service Unavailable', { status: 503 });
    const mockFetch = jest.fn()
      .mockResolvedValueOnce(badResponse)
      .mockResolvedValueOnce(goodResponse);

    // Act
    const result = await fetchWithRetry('http://example.com', {}, mockFetch);

    // Assert
    expect(result).toBe(goodResponse);
    expect(mockFetch).toHaveBeenCalledTimes(2);
  });
});
```

**Note:** These first tests use a mock `fetch` function that is directly passed to `fetchWithRetry` to keep them realistic yet controllable. This avoids hard-to-manage network mocks and follows the principle of “real code (no mocks unless unavoidable)” – mocking the HTTP layer is unavoidable for unit tests, but we are testing the retry logic itself.

#### Expected RED failure

- **Test 1:** `fetchWithRetry is not defined` (ReferenceError) – correct, feature doesn’t exist yet.
- **Test 2:** same error (or fails because function doesn’t exist).  
  Once a stub is created, both tests will fail with assertion errors (e.g., `expected 1 call but received 0`) demonstrating they test the right behavior.

I will run `npm test retry-fetch.test.ts` to watch both fail, then proceed to GREEN by implementing minimal code for each.

After implementing both tests and seeing them pass, I’ll write the next failing test (up to 3 retries) and continue the cycle. No code written ahead of the tests, and each increment is strictly driven by a single failing test.

---

### Refactoring Notes (post-GREEN)
After each green state, I will:
- Remove duplication (e.g., retry loop structure).
- Extract constants (max retries, status code checks).
- Rename variables for clarity.
- Ensure tests stay green.

The exponential backoff test (test 6) will be introduced later, following the same cycle. The TDD approach guarantees that every line of production code has been preceded by a failing test, proving it correctly implements the required behavior.
