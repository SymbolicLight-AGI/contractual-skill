Assumptions / uncertainty:
- Language/test framework is not specified. I’ll draft examples in TypeScript with Jest-style tests.
- The service API is not specified. I’ll use a wished-for API to drive design:
  - `requestWithRetry(sendRequest, options)`
  - `sendRequest` is an injected async function returning `{ status: number, body?: unknown }`
  - Backoff is injected as `sleep(ms)` so tests can observe delays without real waiting.

Boundary: this is only the TDD plan and first tests before implementation. No production implementation code should be written until the first test is run and verified RED.

## TDD Plan

### Behavior list

1. Retries transient `503` responses up to 3 times.
2. Uses exponential backoff between retries.
3. Eventually returns the successful response if a retry succeeds.
4. Stops after the retry limit and returns/throws the final `503` response.
5. Does not retry `400`.
6. Does not retry `401`.

### Red-Green sequence

#### Test 1 — RED

Write a minimal failing test proving that `503` is retried and succeeds on a later attempt.

Expected RED result:
- Test fails because `requestWithRetry` does not exist yet, or because it only calls once.

#### GREEN

Implement the smallest possible `requestWithRetry` behavior to retry `503` until success, enough to pass this one test.

#### Test 2 — RED

Add a test proving exponential backoff delays are used between `503` retries.

Expected RED result:
- Test fails because no backoff is called, or wrong delay values are used.

#### GREEN

Add minimal backoff behavior.

#### Test 3 — RED

Add a test proving it stops after 3 retries.

Expected RED result:
- Test fails because it retries too many times or never stops.

#### GREEN

Add retry limit.

#### Test 4 — RED

Add a test proving `400` is not retried.

#### Test 5 — RED

Add a test proving `401` is not retried.

## First Tests

```typescript
import { requestWithRetry } from './requestWithRetry';

describe('requestWithRetry', () => {
  test('retries 503 responses and returns the first successful response', async () => {
    const responses = [
      { status: 503 },
      { status: 503 },
      { status: 200, body: { ok: true } },
    ];

    let attempts = 0;

    const sendRequest = async () => {
      const response = responses[attempts];
      attempts++;
      return response;
    };

    const sleep = async () => {};

    const result = await requestWithRetry(sendRequest, { sleep });

    expect(result).toEqual({ status: 200, body: { ok: true } });
    expect(attempts).toBe(3);
  });
});
```

Expected first RED result:

```text
FAIL requestWithRetry
  retries 503 responses and returns the first successful response

Cannot find module './requestWithRetry'
```

or, if the function exists but has no retry behavior:

```text
Expected attempts to be 3, received 1
```

That is an acceptable RED only if the failure is caused by missing retry behavior, not by a typo or test setup error.

## Next Tests After First GREEN

```typescript
test('waits with exponential backoff between 503 retries', async () => {
  const responses = [
    { status: 503 },
    { status: 503 },
    { status: 503 },
    { status: 200 },
  ];

  let attempts = 0;
  const delays: number[] = [];

  const sendRequest = async () => {
    const response = responses[attempts];
    attempts++;
    return response;
  };

  const sleep = async (ms: number) => {
    delays.push(ms);
  };

  await requestWithRetry(sendRequest, {
    sleep,
    initialBackoffMs: 100,
  });

  expect(delays).toEqual([100, 200, 400]);
});
```

```typescript
test('stops retrying 503 responses after 3 retries', async () => {
  let attempts = 0;

  const sendRequest = async () => {
    attempts++;
    return { status: 503 };
  };

  const sleep = async () => {};

  const result = await requestWithRetry(sendRequest, { sleep });

  expect(result).toEqual({ status: 503 });
  expect(attempts).toBe(4);
});
```

```typescript
test('does not retry 400 responses', async () => {
  let attempts = 0;

  const sendRequest = async () => {
    attempts++;
    return { status: 400 };
  };

  const sleep = async () => {
    throw new Error('sleep should not be called for 400 responses');
  };

  const result = await requestWithRetry(sendRequest, { sleep });

  expect(result).toEqual({ status: 400 });
  expect(attempts).toBe(1);
});
```

```typescript
test('does not retry 401 responses', async () => {
  let attempts = 0;

  const sendRequest = async () => {
    attempts++;
    return { status: 401 };
  };

  const sleep = async () => {
    throw new Error('sleep should not be called for 401 responses');
  };

  const result = await requestWithRetry(sendRequest, { sleep });

  expect(result).toEqual({ status: 401 });
  expect(attempts).toBe(1);
});
```

## Verification checklist for this TDD work

Before implementation is considered complete:

- Run the first test and verify it fails for the expected reason.
- Implement only enough retry behavior to pass the first test.
- Run the test again and verify it passes.
- Add the next failing test.
- Repeat Red-Green-Refactor.
- Do not implement retry limits, backoff, or non-retryable status handling before there is a failing test for each behavior.
