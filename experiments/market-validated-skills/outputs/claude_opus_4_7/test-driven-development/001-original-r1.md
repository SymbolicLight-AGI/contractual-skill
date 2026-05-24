# TDD Plan for `sendWebhook(event)` Retry Behavior

Following the Iron Law: **NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.** I'll start with RED and write one test for one behavior at a time.

## Test List (one behavior per test)

I see at least these behaviors to drive out:
1. Retries on HTTP 500 and succeeds if a later attempt returns 2xx
2. Retries HTTP 500 up to 3 times total, then gives up
3. Stops immediately on HTTP 400 (no retry)
4. Returns successfully on first 2xx without retrying

I'll start with #3 (the most distinctive rule) or #1 — either works. I'll show #1 first since it establishes the retry mechanism, then #3.

## Step 1 — RED: Write the first failing test

File: `src/webhooks/sendWebhook.test.ts`

```typescript
import { sendWebhook } from './sendWebhook';

describe('sendWebhook', () => {
  test('retries on HTTP 500 and returns success when a later attempt succeeds', async () => {
    let attempts = 0;
    const httpClient = async (_event: unknown) => {
      attempts++;
      if (attempts < 3) return { status: 500 };
      return { status: 200 };
    };

    const result = await sendWebhook({ id: 'evt_1' }, { httpClient });

    expect(result.status).toBe(200);
    expect(attempts).toBe(3);
  });
});
```

Notes on this test:
- Uses a real function (not a Jest mock) as the injected client — keeps the test about real behavior.
- Demonstrates the wished-for API: `sendWebhook(event, { httpClient })`. Dependency injection makes HTTP behavior testable without mocking `fetch` globally.
- One behavior, clear name.

## Step 2 — Verify RED (MANDATORY)

```bash
npx jest src/webhooks/sendWebhook.test.ts
```

Expected failure: module not found / `sendWebhook` is not exported. I will then create the file with just enough scaffolding so the failure becomes a *behavior* failure, not an import error:

```typescript
// src/webhooks/sendWebhook.ts
export async function sendWebhook(_event: unknown, _opts?: unknown): Promise<{ status: number }> {
  throw new Error('not implemented');
}
```

Re-run. The test must fail because the assertion isn't met (e.g., "expected 200, got thrown error"), not because of a typo. Only then proceed.

## Step 3 — GREEN: Minimal code

```typescript
type HttpResponse = { status: number };
type HttpClient = (event: unknown) => Promise<HttpResponse>;

export async function sendWebhook(
  event: unknown,
  opts: { httpClient: HttpClient }
): Promise<HttpResponse> {
  let last: HttpResponse | undefined;
  for (let i = 0; i < 3; i++) {
    last = await opts.httpClient(event);
    if (last.status !== 500) return last;
  }
  return last!;
}
```

Just enough to pass the one test. No backoff, no logging, no configurable max — YAGNI.

## Step 4 — Verify GREEN

Re-run Jest. Confirm:
- The test passes.
- No other tests broke.
- Output is clean (no warnings).

## Step 5 — REFACTOR

Only if needed, and only while staying green. Probably nothing to do yet at this size.

## Step 6 — Next RED

Now write the next failing test, one at a time:

```typescript
test('stops immediately on HTTP 400 without retrying', async () => {
  let attempts = 0;
  const httpClient = async () => {
    attempts++;
    return { status: 400 };
  };

  const result = await sendWebhook({ id: 'evt_2' }, { httpClient });

  expect(result.status).toBe(400);
  expect(attempts).toBe(1);
});
```

Verify it fails (current code already returns on non-500, so this should pass immediately — which is a **red flag**: a test that passes without new code didn't drive new behavior). If it passes immediately, I'd reconsider whether this test actually exercises distinct logic, or pick a sharper assertion (e.g., that a 4xx is returned even if the next call *would have* succeeded). For example:

```typescript
test('does not retry after HTTP 400 even if next attempt would succeed', async () => {
  const responses = [{ status: 400 }, { status: 200 }];
  let attempts = 0;
  const httpClient = async () => responses[attempts++];

  const result = await sendWebhook({ id: 'evt_3' }, { httpClient });

  expect(result.status).toBe(400);
  expect(attempts).toBe(1);
});
```

This is still satisfied by current code, confirming the 400 behavior is already covered by "only retry on 500." Good — that means my third test should target an *un*covered behavior, such as "after 3 consecutive 500s, return the last 500" or "throws/returns failure after max retries."

```typescript
test('returns the failing 500 response after 3 unsuccessful attempts', async () => {
  let attempts = 0;
  const httpClient = async () => {
    attempts++;
    return { status: 500 };
  };

  const result = await sendWebhook({ id: 'evt_4' }, { httpClient });

  expect(result.status).toBe(500);
  expect(attempts).toBe(3);
});
```

Run → verify it fails or passes appropriately → minimal code change if needed → green → repeat.

## Uncertainties / Boundary Notes

A few things were not specified in the task. I would normally ask before coding, but flagging them here:

- **Behavior on exhaustion**: Should `sendWebhook` *return* the final failed response, *throw*, or both? I assumed "return the last response." Please confirm.
- **Other status codes**: Only 500 and 400 were specified. Should other 5xx codes (502, 503, 504) also retry? Should other 4xx codes also stop immediately? I assumed "retry only on 500, return any non-500."
- **Delay / backoff between retries**: Not specified. I've assumed none. If backoff is required, that's a separate failing test.
- **Existing `sendWebhook.ts`**: The task says no production code has been written yet, so I'm creating the file fresh. If a stub already exists with non-trivial logic, per the Iron Law I would delete it before starting.

If you confirm those points (or accept my assumptions), I'll proceed through the cycle starting with the RED step above.
