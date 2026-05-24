# TDD Plan: Retry Behavior for Transient 503 Responses

## Scope Clarification

Before drafting tests, I'm flagging missing inputs the Skill says to surface:

**Unknowns (please confirm before implementation):**
- **Language/framework** — I'll draft in TypeScript/Jest to match the Skill's examples; confirm or specify otherwise.
- **Backoff parameters** — "Exponential" base delay and multiplier are unspecified. I'll assume base=100ms, factor=2 (100, 200, 400) as a placeholder.
- **"Up to 3 times"** — Interpreted as 3 *retries* (4 total attempts). Confirm whether it means 3 total attempts instead.
- **Retry surface** — Does "non-retryable" mean return the response, or throw? I'll assume return the response as-is so the caller can handle it.
- **Other 5xx / network errors / timeouts** — Out of scope per the task; tests will only assert 503 retry and 400/401 non-retry. Other codes are undefined behavior until specified.
- **Time control** — Tests must control time (fake timers) to avoid real waits and to assert backoff durations.

I will not invent answers beyond these placeholders; flag any that need different values.

---

## TDD Plan (test order)

Tests will be added one at a time, each following RED → Verify RED → GREEN → Verify GREEN → REFACTOR. Order is chosen so each test forces minimal new behavior:

1. **Success on first try** — returns response, no retry, no delay. (Forces the basic call-through path.)
2. **Non-retryable `400` is returned immediately** — exactly one attempt. (Forces non-retry branch.)
3. **Non-retryable `401` is returned immediately** — exactly one attempt. (Forces the predicate to cover 401, not just "not 503".)
4. **`503` then `200` — retries once and succeeds** — two attempts total. (Forces the retry loop.)
5. **`503`, `503`, `200` — retries twice and succeeds** — three attempts total. (Forces loop to continue past one retry.)
6. **Persistent `503` — stops after 3 retries (4 attempts) and returns the last `503`** — bounds the retry count. (Forces the cap.)
7. **Exponential backoff delays between `503` retries** — asserts delays of 100ms, 200ms, 400ms via fake timers. (Forces backoff schedule, not just any delay.)
8. **No delay before the first attempt** — asserts attempt 1 fires synchronously (or on next tick), not after backoff. (Guards against off-by-one in delay schedule.)

Refactor opportunities to watch for after green: extract `isRetryable(status)`, extract `backoffDelay(attempt)`.

---

## First Tests (RED stage)

Wished-for API:

```ts
// retryRequest(send, { maxRetries, baseDelayMs, factor }, sleep?)
// - send: () => Promise<{ status: number, body?: unknown }>
// - returns the final Response (retryable or not)
const response = await retryRequest(send);
```

```ts
// retry.test.ts
import { retryRequest } from './retry';

function recordingSleep() {
  const delays: number[] = [];
  const fn = (ms: number) => { delays.push(ms); return Promise.resolve(); };
  return { fn, delays };
}

test('returns response immediately on first success (no retry, no delay)', async () => {
  let attempts = 0;
  const send = async () => { attempts++; return { status: 200, body: 'ok' }; };
  const sleep = recordingSleep();

  const result = await retryRequest(send, { maxRetries: 3, baseDelayMs: 100, factor: 2 }, sleep.fn);

  expect(result.status).toBe(200);
  expect(attempts).toBe(1);
  expect(sleep.delays).toEqual([]);
});

test('does not retry on 400; returns it after one attempt', async () => {
  let attempts = 0;
  const send = async () => { attempts++; return { status: 400 }; };
  const sleep = recordingSleep();

  const result = await retryRequest(send, { maxRetries: 3, baseDelayMs: 100, factor: 2 }, sleep.fn);

  expect(result.status).toBe(400);
  expect(attempts).toBe(1);
  expect(sleep.delays).toEqual([]);
});

test('does not retry on 401; returns it after one attempt', async () => {
  let attempts = 0;
  const send = async () => { attempts++; return { status: 401 }; };
  const sleep = recordingSleep();

  const result = await retryRequest(send, { maxRetries: 3, baseDelayMs: 100, factor: 2 }, sleep.fn);

  expect(result.status).toBe(401);
  expect(attempts).toBe(1);
  expect(sleep.delays).toEqual([]);
});

test('retries 503 once then succeeds', async () => {
  const statuses = [503, 200];
  let attempts = 0;
  const send = async () => { const s = statuses[attempts++]; return { status: s }; };
  const sleep = recordingSleep();

  const result = await retryRequest(send, { maxRetries: 3, baseDelayMs: 100, factor: 2 }, sleep.fn);

  expect(result.status).toBe(200);
  expect(attempts).toBe(2);
  expect(sleep.delays).toEqual([100]);
});

test('gives up after 3 retries on persistent 503 and returns last 503', async () => {
  let attempts = 0;
  const send = async () => { attempts++; return { status: 503 }; };
  const sleep = recordingSleep();

  const result = await retryRequest(send, { maxRetries: 3, baseDelayMs: 100, factor: 2 }, sleep.fn);

  expect(result.status).toBe(503);
  expect(attempts).toBe(4); // 1 initial + 3 retries
  expect(sleep.delays).toEqual([100, 200, 400]);
});
```

Notes on these tests per the Skill:
- **Real code, injected sleep.** `sleep` is injected, not jest-mocked — we assert the *recorded* delays (real behavior), not mock call shape. This avoids the "tests the mock, not the code" anti-pattern.
- **One behavior per test.** No "and" in names.
- **Intent visible.** Each test states the contract a reader can rely on.

---

## Mandatory next step: Verify RED

Per the Iron Law, I will **not** write `retryRequest` yet. The next action is:

```
$ npm test retry.test.ts
```

Expected failure: module `./retry` does not exist (or `retryRequest` is undefined). If any test fails for a different reason (e.g., typo) or passes, I stop and fix the test before implementing.

Only after each test fails for the *expected* reason do I write the minimal code to turn it green, one test at a time — not all at once.

## Boundary note

This Skill covers the TDD process and the first tests. **It does not authorize me to write the implementation in the same step.** Implementation comes only after you (a) confirm the unknowns listed above and (b) I observe each test fail correctly. Please confirm the parameters and language/framework so I can proceed to Verify RED.
