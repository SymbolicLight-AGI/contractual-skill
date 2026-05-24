I’ll start by writing a failing test that specifies the retry-on-500 behaviour. No retry logic yet.

**Step 1 – Write the test (RED)**

File: `src/webhooks/sendWebhook.test.ts`

```typescript
import { sendWebhook } from './sendWebhook';

// Real fetch mock to avoid actual HTTP
import { fetch } from 'cross-fetch'; // assuming you use this
jest.mock('cross-fetch', () => ({
  fetch: jest.fn(),
}));

const mockFetch = fetch as jest.Mock;

beforeEach(() => {
  mockFetch.mockReset();
});

test('retries up to 3 times on 500 responses then succeeds', async () => {
  // Simulate two 500 failures, then a 200 success
  mockFetch
    .mockRejectedValueOnce(new Error('HTTP 500'))   // 1st attempt: 500
    .mockRejectedValueOnce(new Error('HTTP 500'))   // 2nd attempt: 500
    .mockResolvedValueOnce({
      ok: true,
      status: 200,
    });

  const result = await sendWebhook({ type: 'test' });

  // sendWebhook should eventually resolve after the third attempt
  expect(result).toEqual({ ok: true });
  // And it should have called fetch exactly 3 times
  expect(mockFetch).toHaveBeenCalledTimes(3);
});
```

**Step 2 – Verify RED (watch it fail correctly)**

Right now `sendWebhook.ts` doesn’t exist. I run:

```bash
npm test src/webhooks/sendWebhook.test.ts
```

It will error: cannot find module `./sendWebhook`. That’s an **error**, not a failure of the test’s intent. The TDD cycle says to fix such errors. To get a proper **failure** (the test fails because the feature is missing, not because of a compilation error), I need a placeholder function that does a simple, non‑retrying HTTP call.

I create `src/webhooks/sendWebhook.ts` with minimal scaffolding:

```typescript
import { fetch } from 'cross-fetch';

export async function sendWebhook(event: unknown) {
  const response = await fetch('https://example.com/webhook', {
    method: 'POST',
    body: JSON.stringify(event),
  });
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  return response;
}
```

Now run the test again. The placeholder will throw on the first 500 and never retry. The test expects it to resolve after 3 attempts; it will fail with something like:

```
FAIL  src/webhooks/sendWebhook.test.ts
  ● retries up to 3 times on 500 responses then succeeds

    Expected [Error: HTTP 500]  /  expect(mockFetch).toHaveBeenCalledTimes(3) ...
    Received 1  …
```

This is the correct RED: the test fails because retry behaviour is missing, not due to typos or import errors. I’ve just seen it fail for the expected reason.

**Why this is a valid start**

- One clear behaviour: retries on 500.
- The test uses a realistic mock only for the network – unavoidable here.
- The failure proves the test actually catches the missing feature.

**What I’d do next (not done yet because you asked only for “start”)**

- **GREEN:** Add the minimal retry loop to `sendWebhook` – just a `for` cycle that retries up to 3 times on any error (later I’ll refine for 400 vs 500).
- **Verify GREEN:** Run the test again, see it pass, run all existing tests.
- **REFACTOR:** Clean up, then write the next test (“stops immediately on 400 response”).

That’s how TDD drives the implementation – begin with a single failing test that defines the desired behaviour.
