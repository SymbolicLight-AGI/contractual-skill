## TDD Plan: Retry Behavior

### Requirement

A service should:

1. Retry transient `503` responses.
2. Retry up to 3 times.
3. Use exponential backoff between retries.
4. Not retry `400`.
5. Not retry `401`.

### Uncertainties

The task does not specify:

- Language/framework
- Existing service API
- Test runner
- Whether “up to 3 times” means:
  - 3 total attempts, or
  - 1 initial attempt + 3 retries = 4 total attempts

I will assume TypeScript/Jest-style tests and interpret “retry up to 3 times” as **3 retries after the initial request**, for **4 total attempts**. If your project defines this differently, adjust the expected attempt count before implementation.

---

# TDD Sequence

## Test 1 — RED

Start with the core behavior: retry `503` until success.

```ts
test('retries 503 responses up to 3 times before succeeding', async () => {
  let attempts = 0;

  const request = async () => {
    attempts++;

    if (attempts < 4) {
      return {
        status: 503,
        body: 'Service Unavailable',
      };
    }

    return {
      status: 200,
      body: 'ok',
    };
  };

  const result = await callWithRetry(request);

  expect(result).toEqual({
    status: 200,
    body: 'ok',
  });

  expect(attempts).toBe(4);
});
```

### Verify RED

Run only this test:

```bash
npm test -- retry
```

Expected failure:

- `callWithRetry` does not exist, or
- `callWithRetry` does not retry yet, causing the result to be the first `503`

The failure should prove the missing behavior is retrying `503`.

Do not implement until this test fails for the expected reason.

---

## Test 2 — RED

Once Test 1 is green, add the next behavior: stop after the maximum retry count.

```ts
test('returns the final 503 response after 3 failed retries', async () => {
  let attempts = 0;

  const request = async () => {
    attempts++;

    return {
      status: 503,
      body: 'Service Unavailable',
    };
  };

  const result = await callWithRetry(request);

  expect(result).toEqual({
    status: 503,
    body: 'Service Unavailable',
  });

  expect(attempts).toBe(4);
});
```

### Verify RED

Expected failure:

- The function may retry forever,
- retry too few times,
- retry too many times,
- or throw instead of returning the final response.

Implement only enough to pass this test.

---

## Test 3 — RED

Next, verify that `400` is not retried.

```ts
test('does not retry 400 responses', async () => {
  let attempts = 0;

  const request = async () => {
    attempts++;

    return {
      status: 400,
      body: 'Bad Request',
    };
  };

  const result = await callWithRetry(request);

  expect(result).toEqual({
    status: 400,
    body: 'Bad Request',
  });

  expect(attempts).toBe(1);
});
```

### Verify RED

Expected failure:

- If the implementation retries all non-200 responses, attempts will be greater than `1`.

Implement only enough to avoid retrying `400`.

---

## Test 4 — RED

Then verify that `401` is not retried.

```ts
test('does not retry 401 responses', async () => {
  let attempts = 0;

  const request = async () => {
    attempts++;

    return {
      status: 401,
      body: 'Unauthorized',
    };
  };

  const result = await callWithRetry(request);

  expect(result).toEqual({
    status: 401,
    body: 'Unauthorized',
  });

  expect(attempts).toBe(1);
});
```

### Verify RED

Expected failure:

- If the implementation retries unauthorized responses, attempts will be greater than `1`.

Implement only enough to avoid retrying `401`.

---

## Test 5 — RED

Finally, test exponential backoff. This should use fake timers or an injected delay function to avoid slow tests.

Prefer dependency injection so the test checks real retry behavior without waiting.

```ts
test('uses exponential backoff between 503 retries', async () => {
  const delays: number[] = [];
  let attempts = 0;

  const request = async () => {
    attempts++;

    if (attempts < 4) {
      return {
        status: 503,
        body: 'Service Unavailable',
      };
    }

    return {
      status: 200,
      body: 'ok',
    };
  };

  const delay = async (ms: number) => {
    delays.push(ms);
  };

  const result = await callWithRetry(request, {
    delay,
    baseDelayMs: 100,
  });

  expect(result).toEqual({
    status: 200,
    body: 'ok',
  });

  expect(delays).toEqual([100, 200, 400]);
});
```

### Verify RED

Expected failure:

- No delay function is called,
- delays are constant,
- delays are incorrect,
- or backoff happens the wrong number of times.

Implement only enough to produce exponential backoff.

---

# First Tests to Write Now

The first test should be only the smallest behavior: retry `503` until success.

```ts
test('retries 503 responses up to 3 times before succeeding', async () => {
  let attempts = 0;

  const request = async () => {
    attempts++;

    if (attempts < 4) {
      return {
        status: 503,
        body: 'Service Unavailable',
      };
    }

    return {
      status: 200,
      body: 'ok',
    };
  };

  const result = await callWithRetry(request);

  expect(result).toEqual({
    status: 200,
    body: 'ok',
  });

  expect(attempts).toBe(4);
});
```

Run it and confirm it fails before writing production code:

```bash
npm test -- retry
```

Only after watching this fail for the expected reason should implementation begin.
