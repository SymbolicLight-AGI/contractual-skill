<think>The user wants me to demonstrate how to start with TDD for implementing retry behavior on a webhook function. Let me follow the TDD skill strictly.

The task is to:
1. Add retry behavior to `sendWebhook(event)`
2. Retry failed HTTP 500 responses up to 3 times
3. Stop immediately on HTTP 400

Since this is TDD, I need to start with the RED phase - writing a failing test first.

Let me write a minimal failing test that demonstrates the desired behavior:

1. Test that HTTP 500 is retried up to 3 times
2. Test that HTTP 400 stops immediately (no retry)

I should NOT write any production code yet. Just the test.

Let me write the test file:
</think>

# Starting with TDD: RED Phase

Following the TDD skill, I'll begin with **RED** - writing a failing test before any production code.

## Step 1: Write the Failing Test

```typescript
// src/webhooks/__tests__/sendWebhook.test.ts

describe('sendWebhook', () => {
  test('retries HTTP 500 responses up to 3 times', async () => {
    let callCount = 0;
    const mockFetch = async () => {
      callCount++;
      if (callCount < 3) {
        return { ok: false, status: 500, statusText: 'Internal Server Error' };
      }
      return { ok: true, status: 200, statusText: 'OK' };
    };

    const result = await sendWebhook({ type: 'order.created' }, mockFetch);

    expect(result.ok).toBe(true);
    expect(callCount).toBe(3);
  });

  test('stops immediately on HTTP 400 without retrying', async () => {
    let callCount = 0;
    const mockFetch = async () => {
      callCount++;
      return { ok: false, status: 400, statusText: 'Bad Request' };
    };

    const result = await sendWebhook({ type: 'order.created' }, mockFetch);

    expect(result.ok).toBe(false);
    expect(result.status).toBe(400);
    expect(callCount).toBe(1);
  });
});
```

## Step 2: Verify It Fails

```bash
npm test src/webhooks/__tests__/sendWebhook.test.ts
```

**Expected output:**
```
FAIL: Cannot find 'sendWebhook' or its default export
```

The test fails because the function doesn't exist yet—exactly what we want.

---

## Next Step

Once you confirm the test fails for the right reason (missing function, not typos), I'll write **minimal production code** to make it pass (GREEN phase).

**Do you want me to proceed to GREEN, or would you like to review the test design first?**
