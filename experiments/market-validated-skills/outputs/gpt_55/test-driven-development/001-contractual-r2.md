## Behavior Under Test

`sendWebhook(event)` should:

1. Retry failed HTTP `500` responses up to 3 times.
2. Stop immediately on HTTP `400`.
3. Use Jest tests before any production implementation.

Assumptions to confirm or adjust:

- `sendWebhook` performs an HTTP request through an injectable or mockable client/fetch layer.
- “Retry up to 3 times” means **1 initial attempt + 3 retries = 4 total attempts**.
- A `500` response is considered retryable.
- A `400` response is non-retryable and should result in only 1 attempt.

## RED Evidence

Not run yet. No test result can be claimed until the Jest command is executed.

The first minimal failing test I would write is for the smallest behavior: retrying `500` responses.

Example starting test:

```ts
// src/webhooks/sendWebhook.test.ts

import { sendWebhook } from './sendWebhook';

describe('sendWebhook', () => {
  it('retries HTTP 500 responses up to 3 times', async () => {
    const httpPost = jest
      .fn()
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 200 });

    const event = {
      type: 'user.created',
      payload: { id: 'user-123' },
    };

    await sendWebhook(event, { httpPost });

    expect(httpPost).toHaveBeenCalledTimes(4);
  });
});
```

Then I would run the focused Jest command:

```bash
npx jest src/webhooks/sendWebhook.test.ts --runInBand
```

Expected RED result:

- The test should fail because `sendWebhook` does not yet support retry behavior, or because its API does not yet accept an injectable HTTP client.
- If it fails because of a typo, import problem, or invalid test setup, I would fix the test first and rerun until the RED failure reflects the missing retry behavior.

## GREEN Evidence

Not available yet.

After observing the correct RED failure, I would implement the smallest production change in:

```text
src/webhooks/sendWebhook.ts
```

Minimal intended behavior:

```ts
export async function sendWebhook(
  event: unknown,
  deps: { httpPost: (event: unknown) => Promise<{ status: number }> }
) {
  const maxRetries = 3;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const response = await deps.httpPost(event);

    if (response.status < 500) {
      return response;
    }

    if (attempt === maxRetries) {
      return response;
    }
  }
}
```

Then I would rerun:

```bash
npx jest src/webhooks/sendWebhook.test.ts --runInBand
```

Expected GREEN result:

- The retry-on-500 test passes.
- `httpPost` is called 4 times.

No pass should be claimed until the command output confirms it.

## Refactor Notes

No refactor yet.

After GREEN, possible safe refactors could include:

- Extracting `maxRetries` into a named constant.
- Clarifying retryable status logic with a helper like `isRetryableStatus(status)`.
- Preserving passing tests after each refactor.

## Remaining Gaps

Still need a second TDD cycle for HTTP `400` behavior.

Next test after the first GREEN:

```ts
it('does not retry HTTP 400 responses', async () => {
  const httpPost = jest.fn().mockResolvedValue({ status: 400 });

  const event = {
    type: 'user.created',
    payload: { id: 'user-123' },
  };

  await sendWebhook(event, { httpPost });

  expect(httpPost).toHaveBeenCalledTimes(1);
});
```

Command:

```bash
npx jest src/webhooks/sendWebhook.test.ts --runInBand
```

Expected RED/GREEN flow:

1. If current implementation already treats `< 500` as non-retryable, this test may pass immediately.
2. If it passes without new production code, that is acceptable only because the behavior was already covered by the prior minimal implementation.
3. If it fails, implement the smallest change to stop retrying on `400`.

## Next TDD Step

Write the first Jest test for retrying `500`, run it, and capture the RED failure output before modifying `src/webhooks/sendWebhook.ts`.
