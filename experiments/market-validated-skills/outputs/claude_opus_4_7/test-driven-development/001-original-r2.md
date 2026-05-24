# TDD Plan for `sendWebhook` Retry Behavior

Following the Iron Law: **no production code until a failing test exists.** I'll start with RED, one behavior at a time.

## Step 1: Identify the behaviors to test

Breaking the requirement into minimal, independent behaviors:

1. Returns successfully on first attempt when HTTP succeeds (baseline)
2. Retries on HTTP 500 and succeeds on a later attempt
3. Retries HTTP 500 responses up to 3 times total, then gives up
4. Stops immediately on HTTP 400 (no retry)

I'll write one test, watch it fail, make it pass, then move to the next.

## Step 2: First RED — start with the most central behavior

I'll start with behavior #2 (retry-then-succeed on 500), because it forces the retry mechanism into existence. The "success on first attempt" test would pass trivially against a non-retrying implementation, so it isn't the strongest forcing function.

**File:** `src/webhooks/sendWebhook.test.ts`

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

Notes on the test:
- Uses a real function as the HTTP client (dependency injection), not a Jest mock — per the Skill, prefer real code.
- Tests behavior (eventual success + attempt count), not implementation details.
- Single behavior, clear name.
- The `httpClient` parameter is a wished-for API; I'm letting the test drive the design.

## Step 3: Verify RED (mandatory)

```bash
npx jest src/webhooks/sendWebhook.test.ts
```

Expected failure: module `./sendWebhook` does not export `sendWebhook` (or the file is empty). That's an *error*, not a clean assertion failure, so I'll create the minimum scaffold to turn the error into a real test failure:

```typescript
// src/webhooks/sendWebhook.ts
export async function sendWebhook(_event: unknown, _opts?: unknown): Promise<{ status: number }> {
  return { status: 0 };
}
```

Re-run. Expected failure now:
```
Expected: 200
Received: 0
```

That's a correct RED: the test fails because the retry feature is missing, not because of a typo.

## Step 4: GREEN — minimal implementation

Only after I see the correct red:

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

Just enough to pass. No backoff, no logging, no config — YAGNI.

## Step 5: Verify GREEN

Run the test, confirm it passes, confirm output is pristine (no warnings).

## Step 6: REFACTOR

With one test there's little to clean up. I'd revisit naming and types but add no behavior.

## Step 7: Next RED — drive out the remaining behaviors, one test at a time

In order:

1. **Stops immediately on HTTP 400** — assert `attempts === 1` when the client returns `{ status: 400 }`. This will currently pass (since 400 ≠ 500 falls through the loop), so I need to think carefully: it actually *does* exercise the "no retry on non-500" path. I'll write it to lock the behavior in as a regression guard, and verify it fails first by temporarily expecting different behavior… **no — that violates the spirit of the rules.** Instead: this test passing immediately is a Red Flag per the Skill. The honest move is to recognize my GREEN already covers this behavior. I'll note it as a characterization test and flag the issue:

   > **Uncertainty / Skill tension:** Behavior #4 may pass on the first run because the minimal GREEN code already handles it. The Skill says "Test passes immediately? You're testing existing behavior." The clean resolution is to drive behavior #4 *before* behavior #2 (start with 400-stops, which forces a non-retrying impl; then 500-retries forces retries). If I were redoing this, I'd reorder: test 400-stop first, then 500-retry. I'd like your call on whether to restart with that ordering.

2. **Gives up after 3 attempts on persistent 500** — client always returns 500; assert `result.status === 500` and `attempts === 3`. This will fail against the current GREEN (which returns the last response, status 500 — actually it passes too). I need a sharper assertion: assert that `sendWebhook` does **not** make a 4th call. That will pass against current code. So this behavior is also already covered.

   This tells me my initial test was *too strong* — it pinned down most of the spec in one go. A more disciplined sequence would have been smaller increments.

## Boundary note

This Skill covers *how* to do TDD. It does not cover:
- Choosing an HTTP library (`fetch`, `axios`, etc.) — needs your input.
- Whether retries should use backoff/jitter — not in the stated requirement; I'll skip per YAGNI unless you add it.
- Whether other status codes (502, 503, 504, network errors) should also retry — **the requirement only says "HTTP 500"; I'll mark this as an explicit assumption.** Please confirm.

## Recommended next step

Confirm:
1. The DI shape for `httpClient` is acceptable, or specify the HTTP library you want (I'll redesign the first test accordingly).
2. Whether to restart with smaller increments (400-stop test first), per the tension I flagged above.
3. Retry scope: literal HTTP 500 only, or all 5xx?

Once confirmed, I'll write test #1, watch it fail, and proceed through the cycle.
