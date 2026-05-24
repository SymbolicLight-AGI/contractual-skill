# TDD Plan: Retry Behavior

## Scope Clarification

Before drafting tests, I'm flagging missing inputs that affect test design. I'll proceed with stated assumptions, but please confirm or correct:

**Assumptions (please verify):**
- Language/framework: not specified — I'll use TypeScript + Jest pseudocode (adapt to your stack)
- "Exponential backoff" base/multiplier: not specified — assuming base delay `d`, then `d * 2^attempt` (e.g., 100ms, 200ms, 400ms)
- "Up to 3 times" interpreted as: 3 *retry* attempts after the initial call (total 4 calls). Confirm if you mean 3 *total* attempts.
- Behavior on non-retryable status (400/401): return/throw immediately with the response
- Behavior after exhausting retries on 503: throw or return the last 503 response — assuming throw
- Other 5xx codes (500, 502, 504): not specified — **out of scope** until clarified; tests below only cover 503
- Time control: tests will use fake timers to avoid real waits

---

## Test List (RED order)

Each will follow Red → Verify Red → Green → Verify Green → Refactor.

1. Returns successful response on first try (no retries needed)
2. Retries on 503 and succeeds on second attempt
3. Retries up to 3 times on persistent 503, then throws
4. Does NOT retry on 400 — returns/throws immediately after one call
5. Does NOT retry on 401 — returns/throws immediately after one call
6. Uses exponential backoff delays between retries (100ms, 200ms, 400ms)
7. (Edge) Network/throw errors — **deferred, needs clarification**

---

## First Tests (RED phase drafts)

```typescript
// retry.test.ts
import { fetchWithRetry } from './retry';

describe('fetchWithRetry', () => {
  beforeEach(() => jest.useFakeTimers());
  afterEach(() => jest.useRealTimers());

  test('returns response immediately on 200 success', async () => {
    let calls = 0;
    const client = async () => {
      calls++;
      return { status: 200, body: 'ok' };
    };

    const result = await fetchWithRetry(client);

    expect(result.status).toBe(200);
    expect(calls).toBe(1);
  });

  test('retries 503 and succeeds on later attempt', async () => {
    let calls = 0;
    const client = async () => {
      calls++;
      if (calls < 3) return { status: 503, body: 'unavailable' };
      return { status: 200, body: 'ok' };
    };

    const promise = fetchWithRetry(client);
    await jest.runAllTimersAsync();
    const result = await promise;

    expect(result.status).toBe(200);
    expect(calls).toBe(3);
  });

  test('throws after 3 retries on persistent 503', async () => {
    let calls = 0;
    const client = async () => {
      calls++;
      return { status: 503, body: 'unavailable' };
    };

    const promise = fetchWithRetry(client);
    await jest.runAllTimersAsync();

    await expect(promise).rejects.toThrow(/503/);
    expect(calls).toBe(4); // 1 initial + 3 retries
  });

  test('does not retry on 400', async () => {
    let calls = 0;
    const client = async () => {
      calls++;
      return { status: 400, body: 'bad request' };
    };

    const result = await fetchWithRetry(client);

    expect(result.status).toBe(400);
    expect(calls).toBe(1);
  });

  test('does not retry on 401', async () => {
    let calls = 0;
    const client = async () => {
      calls++;
      return { status: 401, body: 'unauthorized' };
    };

    const result = await fetchWithRetry(client);

    expect(result.status).toBe(401);
    expect(calls).toBe(1);
  });

  test('uses exponential backoff between 503 retries', async () => {
    const timestamps: number[] = [];
    const start = Date.now();
    jest.setSystemTime(start);

    const client = async () => {
      timestamps.push(Date.now() - start);
      return { status: 503, body: 'unavailable' };
    };

    const promise = fetchWithRetry(client, { baseDelayMs: 100 });
    await jest.runAllTimersAsync();
    await expect(promise).rejects.toThrow();

    // attempt 0: t=0, attempt 1: t=100, attempt 2: t=300, attempt 3: t=700
    expect(timestamps).toEqual([0, 100, 300, 700]);
  });
});
```

---

## Next Step

1. Save these tests.
2. Run the suite — **verify each fails for the right reason** (function/module does not exist, not a typo). Per the skill: *if you didn't watch the test fail, you don't know if it tests the right thing.*
3. Confirm assumptions above before I write GREEN code.

**Boundary note:** The skill mandates I watch tests fail before writing implementation. I have not executed these tests in this environment, so the RED-verification step is yours to perform (or to run in a follow-up turn where I have shell access). Do not skip it.
