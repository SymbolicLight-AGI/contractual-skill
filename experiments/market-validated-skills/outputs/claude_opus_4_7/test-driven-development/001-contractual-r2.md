# TDD Plan for `sendWebhook(event)` Retry Behavior

## Behavior Under Test

First slice: **`sendWebhook` retries an HTTP 500 response and succeeds on the second attempt.**

This is the smallest meaningful behavior that forces retry logic to exist. Once it passes, subsequent cycles will cover the 3-attempt cap and the immediate stop on 400.

## Inputs / Assumptions

- Test runner: Jest (confirmed).
- Test file: `src/webhooks/sendWebhook.test.ts` (assumed, following the colocated `*.test.ts` convention common in TS/Jest projects — flag if your repo uses `__tests__/`).
- The HTTP client used inside `sendWebhook` is **unknown**. I will assume `sendWebhook` takes an injectable HTTP function or that we mock the module it imports. **Please confirm** which boundary to mock; otherwise I will introduce dependency injection as part of the GREEN step, which is a public-shape decision that needs your sign-off (see Human Gates).
- `event` shape is **unknown**. I will use a placeholder `{ id: "evt_1", payload: {} }` in the test and treat the shape as out-of-scope for this slice.

## Proposed TDD Cycle 1

### Step 1 — Write the failing test (RED)

```ts
// src/webhooks/sendWebhook.test.ts
import { sendWebhook } from "./sendWebhook";

describe("sendWebhook retry behavior", () => {
  it("retries once after an HTTP 500 and resolves when the retry succeeds", async () => {
    const httpClient = jest
      .fn()
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 200 });

    const result = await sendWebhook(
      { id: "evt_1", payload: {} },
      { httpClient }
    );

    expect(httpClient).toHaveBeenCalledTimes(2);
    expect(result.status).toBe(200);
  });
});
```

### Step 2 — Run and observe RED

Command:

```
npx jest src/webhooks/sendWebhook.test.ts
```

Expected failure reason: `sendWebhook` does not exist yet (module not found) or does not accept an `httpClient` option. **I have not run this command — no real RED evidence exists yet.** I will not claim a failure I did not observe.

### Step 3 — Verify failure reason

The failure must be "missing implementation," not a typo, bad import path, or Jest config error. If the failure is wrong, fix the test and rerun before writing any production code.

### Step 4 — Minimal GREEN implementation

After confirmed RED, write the smallest code in `src/webhooks/sendWebhook.ts` that retries once on 500 and returns on 200. Do **not** preemptively add the 3-retry cap or 400 handling — those belong to later cycles.

### Step 5 — Run GREEN

```
npx jest src/webhooks/sendWebhook.test.ts
```

### Step 6 — Refactor

Only if green: extract retry helper, clarify naming. Rerun tests after each change.

## Subsequent Cycles (not yet started)

1. **Cycle 2:** Stops after 3 attempts when all return 500 (asserts call count = 3, final result/throw behavior — need your decision: throw or return last response?).
2. **Cycle 3:** Stops immediately on HTTP 400 (asserts call count = 1, no retry).
3. **Cycle 4 (edge):** Non-500, non-400, non-2xx response — behavior **undefined by spec**, needs clarification.
4. **Cycle 5 (edge):** Network/thrown errors vs. HTTP error responses — also unspecified.

## RED Evidence

None yet. Will be captured after you confirm the open questions below and I run Jest.

## GREEN Evidence

None yet.

## Refactor Notes

N/A until GREEN.

## Remaining Gaps

- HTTP client boundary / injection shape needs confirmation (Human Gate: public API decision).
- `event` type unknown.
- On exhausted retries: throw or return last response?
- Behavior on 4xx other than 400, and on thrown network errors, is unspecified.
- Backoff/delay between retries not mentioned — assumed none for now.

## Next TDD Step

1. Confirm the HTTP boundary (inject `httpClient`, mock a module, or use `fetch` + `jest.spyOn`).
2. Confirm exhausted-retry behavior (throw vs. return).
3. Then I will write the test above, run it, and report real RED output before any production code is written.
