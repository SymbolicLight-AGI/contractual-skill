We’ll start a single TDD cycle for the smallest retry behavior: when a 500 response occurs, `sendWebhook` retries and eventually succeeds.

### Behavior Under Test
`sendWebhook(event)` retries after a 500 response and resolves with the success response once a retry succeeds.

Assumptions (confirmed with you if needed):
- The project uses Jest and we can mock `fetch` globally.
- We’ll create a minimal placeholder `sendWebhook` that does a single HTTP request without retry so the test can run and fail for the correct missing behavior.
- The test file lives at `src/webhooks/sendWebhook.test.ts`.

---

### RED: Failing Test for a Single Retry on 500

**Test** (`src/webhooks/sendWebhook.test.ts`)
```ts
import { sendWebhook } from './sendWebhook';

describe('sendWebhook retry behavior', () => {
  beforeEach(() => {
    jest.resetAllMocks();
    // Simulate fetch returning a 500 on the first call, then a 200
    global.fetch = jest
      .fn()
      .mockResolvedValueOnce(new Response(null, { status: 500 }))   // first call → 500
      .mockResolvedValueOnce(new Response(null, { status: 200 }));  // retry → 200
  });

  test('retries once on 500 and eventually succeeds', async () => {
    const result = await sendWebhook({ id: 1 });

    // The function should have called fetch twice (initial + one retry)
    expect(global.fetch).toHaveBeenCalledTimes(2);
    expect(result.status).toBe(200);
  });
});
```

**Run command**
```bash
npx jest src/webhooks/sendWebhook.test.ts
```

**Expected RED output**
- Test fails because `sendWebhook` currently calls `fetch` only once (the placeholder).  
- The assertion `toHaveBeenCalledTimes(2)` fails with **Received number of calls: 1**.  
- This is the expected failure reason: the production code does not retry on 500.

---

### GREEN: Minimal Implementation to Pass

After confirming the test fails for the right reason, we add the minimal retry logic:

```ts
// src/webhooks/sendWebhook.ts (minimal change)
export async function sendWebhook(event: unknown) {
  let attempts = 0;
  const maxRetries = 1; // only handle the single retry case first
  while (attempts <= maxRetries) {
    const response = await fetch('https://example.com', {
      method: 'POST',
      body: JSON.stringify(event),
    });
    if (response.status === 500 && attempts < maxRetries) {
      attempts++;
      continue;
    }
    return response; // 200 or non-retryable
  }
  // Fallback – should not be reached in this test
  throw new Error('Retries exhausted');
}
```

**Run the same test command** to verify GREEN.

**Expected GREEN output**
- Test passes: `fetch` is called 2 times, result status is 200.

---

### Refactor Notes
- No immediate refactor needed; the loop is the simplest expression.
- After more cycles, we’ll extract retry parameters and error handling.

---

### Remaining Gaps
- **Max 3 retries**: Next cycle should test that after 3 retries (all 500) the function either rejects or returns the last 500.
- **No retry on 400**: Separate test verifying that a 400 response returns immediately without retry.
- **Exponential backoff / delays**: Out of scope for this first step; can be added later.
- **Edge cases**: Network errors vs HTTP errors, non‑500 retryable statuses, request timeout.

---

### Next TDD Step
1. Add a test for the 3‑retry limit (e.g., mock three 500s and then a final 500, expect 4 total calls and the rejected/returned 500).  
2. Run RED → implement loop up to 3 → GREEN.  
3. Add a test for 400: mock a 400, assert only 1 call and the 400 response returned.  

Would you like me to proceed with the next cycle, or adjust the scope?
