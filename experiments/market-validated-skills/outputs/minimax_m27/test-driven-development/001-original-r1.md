# TDD Approach for Retry Behavior

Here's how I would start with TDD for this feature:

---

## RED - Write the First Failing Test

```typescript
// src/webhooks/__tests__/sendWebhook.test.ts

describe('sendWebhook', () => {
  it('retries on HTTP 500 failures up to 3 times', async () => {
    const mockFetch = jest.fn()
      .mockResolvedValueOnce({ ok: false, status: 500 })
      .mockResolvedValueOnce({ ok: false, status: 500 })
      .mockResolvedValueOnce({ ok: true, status: 200 });

    const result = await sendWebhook({ type: 'order.created' }, mockFetch);

    expect(result.ok).toBe(true);
    expect(mockFetch).toHaveBeenCalledTimes(3);
  });
});
```

### Verify RED - Watch It Fail

```bash
npm test src/webhooks/__tests__/sendWebhook.test.ts
```

**Expected output:**
```
FAIL: Cannot find module 'src/webhooks/sendWebhook'
```

The test fails because the production code doesn't exist yet. This is correct.

---

## Next Step (Before GREEN)

Write the remaining tests:

```typescript
it('stops immediately on HTTP 400', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ ok: false, status: 400 });

  const result = await sendWebhook({ type: 'order.created' }, mockFetch);

  expect(result.ok).toBe(false);
  expect(mockFetch).toHaveBeenCalledTimes(1); // No retries
});

it('returns immediately on success', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ ok: true, status: 200 });

  const result = await sendWebhook({ type: 'order.created' }, mockFetch);

  expect(result.ok).toBe(true);
  expect(mockFetch).toHaveBeenCalledTimes(1);
});

it('throws after 3 consecutive 500 errors', async () => {
  const mockFetch = jest.fn().mockResolvedValue({ ok: false, status: 500 });

  await expect(sendWebhook({ type: 'order.created' }, mockFetch))
    .rejects.toThrow('Webhook failed after 3 attempts');

  expect(mockFetch).toHaveBeenCalledTimes(3);
});
```

---

## GREEN - Minimal Code

```typescript
// src/webhooks/sendWebhook.ts

export async function sendWebhook(
  event: { type: string },
  fetch: (url: string, opts: object) => Promise<{ ok: boolean; status: number }>
): Promise<{ ok: boolean }> {
  const maxRetries = 3;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const response = await fetch('/webhook', { body: JSON.stringify(event) });

    if (response.ok) {
      return response;
    }

    if (response.status === 400) {
      return response; // Stop immediately
    }

    if (attempt === maxRetries) {
      throw new Error('Webhook failed after 3 attempts');
    }
  }

  throw new Error('unreachable');
}
```

---

## Verify GREEN - Watch It Pass

```bash
npm test src/webhooks/__tests__/sendWebhook.test.ts
```

**Expected output:**
```
PASS
```

---

## REFACTOR

No refactoring needed yet—the implementation is already minimal.

---

## Summary

| Phase | Action |
|-------|--------|
| **RED** | Wrote 4 failing tests (retry 3x, stop on 400, success path, throws after 3 fails) |
| **Verify RED** | Confirmed tests fail with "module not found" |
| **GREEN** | Wrote minimal retry logic with status code checks |
| **Verify GREEN** | All tests pass |

This approach:
- Forces you to define behavior before implementation
- Catches edge cases (what if all 3 attempts fail?)
- Documents the API through tests
- Prevents over-engineering (no backoff, no config options yet)
