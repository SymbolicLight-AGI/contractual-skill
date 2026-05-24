I would start with **one RED test** for the retry-on-500 behavior before touching `src/webhooks/sendWebhook.ts`.

One uncertainty to clarify first: “retry up to 3 times” usually means **1 initial attempt + 3 retries = 4 total HTTP calls**. I’ll assume that unless you mean **3 total attempts**.

### RED: add the first failing Jest test

Create:

```ts
// src/webhooks/sendWebhook.test.ts
import { sendWebhook } from './sendWebhook';

describe('sendWebhook', () => {
  beforeEach(() => {
    jest.restoreAllMocks();
    process.env.WEBHOOK_URL = 'https://example.com/webhook';
  });

  test('retries HTTP 500 responses up to 3 times before succeeding', async () => {
    const fetchSpy = jest
      .spyOn(global, 'fetch')
      .mockResolvedValueOnce(new Response(null, { status: 500 }))
      .mockResolvedValueOnce(new Response(null, { status: 500 }))
      .mockResolvedValueOnce(new Response(null, { status: 500 }))
      .mockResolvedValueOnce(new Response(null, { status: 200 }));

    await expect(
      sendWebhook({ id: 'evt_1', type: 'user.created' })
    ).resolves.toBeUndefined();

    expect(fetchSpy).toHaveBeenCalledTimes(4);
  });
});
```

This uses a mocked `fetch` because real HTTP is an external side effect, so mocking is unavoidable here. The test still exercises the real `sendWebhook` behavior.

### Verify RED

Run only this test:

```bash
npm test -- src/webhooks/sendWebhook.test.ts
```

Expected failure, assuming `sendWebhook` currently sends only once or has no retry behavior:

```text
Expected number of calls: 4
Received number of calls: 1
```

If it fails because of a typo, import error, or missing setup, I would fix that until the test fails specifically because retry behavior is missing.

Only after watching that correct failure would I write the minimal production code to make this test pass. Then I’d add the next RED test for:

```ts
test('does not retry HTTP 400 responses', async () => {
  // expect exactly 1 fetch call
});
```
