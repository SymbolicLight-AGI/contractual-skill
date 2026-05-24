<think>The user wants me to demonstrate TDD for implementing retry behavior on a `sendWebhook(event)` function. Let me follow the TDD contract strictly.

Key requirements from the user:
1. Retry failed HTTP 500 responses up to 3 times
2. Stop immediately on HTTP 400
3. Show how to start with TDD

Since no production code exists yet, I need to:
1. First identify the smallest behavior to test
2. Write a minimal failing test
3. Show the RED state
4. Then show what the minimal implementation would be

Let me think about the smallest first behavior:
- The most fundamental behavior is: "When sendWebhook is called and receives HTTP 400, it should NOT retry and should return/throw immediately"

This is the simplest because:
- It doesn't require setting up retry logic
- It defines the "stop" condition
- It's a clear boundary

Let me write a minimal test for this first behavior.

I need to be careful about:
- Not writing production code before a failing test
- Making sure the test fails for the expected reason
- Keeping the test minimal

Let me structure my response following the TDD contract output format.
</think>

# TDD Approach for Retry Behavior

## Behavior Under Test

**First behavior:** When `sendWebhook(event)` receives an HTTP 400 response, it should stop immediately without retrying.

---

## RED Evidence

Here's the minimal failing test I'd write first:

```typescript
// src/webhooks/__tests__/sendWebhook.test.ts
import { sendWebhook } from '../sendWebhook';

describe('sendWebhook retry behavior', () => {
  it('should NOT retry on HTTP 400 and return immediately', async () => {
    // Arrange: Mock fetch to return 400
    const mockFetch = jest.fn().mockResolvedValue({
      ok: false,
      status: 400,
    });
    global.fetch = mockFetch;

    // Act
    const result = await sendWebhook({ type: 'test' });

    // Assert: Should have been called exactly once (no retries)
    expect(mockFetch).toHaveBeenCalledTimes(1);
  });
});
```

**Expected RED output:**
```
FAIL src/webhooks/__tests__/sendWebhook.test.ts
● should NOT retry on HTTP 400 and return immediately

TypeError: sendWebhook is not a function
```

The test fails because `sendWebhook` doesn't exist yet—this is the expected failure reason.

---

## Next TDD Step

Once you confirm this test structure matches your project patterns, I would:

1. **Create minimal stub** in `src/webhooks/sendWebhook.ts`:
   ```typescript
   export const sendWebhook = async (event: unknown) => {
     const response = await fetch('/webhook', {
       method: 'POST',
       body: JSON.stringify(event),
     });
     return response;
   };
   ```

2. **Run test** → Should pass (GREEN) since single call happens by default

3. **Then** write the second failing test for HTTP 500 retries

---

## Questions Before Proceeding

1. Should HTTP 400 throw an error or return a specific result object?
2. What should the return value of `sendWebhook` be? (error object, boolean, or throw?)
3. Is there an existing test file or pattern I should follow for this project?

Once you confirm these, I'll write the next failing test for the 500-retry behavior.
