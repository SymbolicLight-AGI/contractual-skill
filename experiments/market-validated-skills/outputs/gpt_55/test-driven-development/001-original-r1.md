I would start with **one RED test** and no retry implementation.

Two uncertainties I’d clarify first:

1. “Retry up to 3 times” could mean:
   - **3 retries after the first attempt** = 4 total HTTP calls, or
   - **3 total attempts**.
   
   I’ll assume **3 retries after the initial attempt**.

2. I don’t know how `sendWebhook(event)` discovers the webhook URL. I’ll assume it reads `process.env.WEBHOOK_URL`. If the real API differs, I’d adapt the test to the intended public API before writing production code.

## RED: first failing test

Create `src/webhooks/sendWebhook.test.ts`:

```ts
import { createServer, Server } from 'node:http';
import { AddressInfo } from 'node:net';
import { sendWebhook } from './sendWebhook';

function startWebhookServer(
  handler: Parameters<typeof createServer>[0],
): Promise<{ url: string; close: () => Promise<void> }> {
  return new Promise((resolve) => {
    const server: Server = createServer(handler);

    server.listen(0, () => {
      const address = server.address() as AddressInfo;

      resolve({
        url: `http://127.0.0.1:${address.port}`,
        close: () =>
          new Promise((closeResolve, closeReject) => {
            server.close((error) => {
              if (error) closeReject(error);
              else closeResolve();
            });
          }),
      });
    });
  });
}

test('retries HTTP 500 responses three times before succeeding', async () => {
  let attempts = 0;

  const server = await startWebhookServer((_req, res) => {
    attempts += 1;

    if (attempts < 4) {
      res.statusCode = 500;
      res.end('server error');
      return;
    }

    res.statusCode = 200;
    res.end('ok');
  });

  const previousWebhookUrl = process.env.WEBHOOK_URL;
  process.env.WEBHOOK_URL = server.url;

  try {
    await sendWebhook({
      id: 'evt_123',
      type: 'user.created',
    });

    expect(attempts).toBe(4);
  } finally {
    if (previousWebhookUrl === undefined) {
      delete process.env.WEBHOOK_URL;
    } else {
      process.env.WEBHOOK_URL = previousWebhookUrl;
    }

    await server.close();
  }
});
```

This uses a real local HTTP server instead of mocking HTTP behavior.

## Verify RED

Run only this test:

```bash
npx jest src/webhooks/sendWebhook.test.ts --runInBand
```

Expected outcome at this stage: the test must fail.

If `sendWebhook.ts` does not exist yet, the first failure may be an import/compile error. I would fix only the test harness issue with the smallest possible stub, for example exporting `sendWebhook`, then rerun until the test fails for the expected reason: the HTTP request is not retried.

A correct RED failure would look conceptually like:

```txt
Expected: 4
Received: 1
```

or:

```txt
Expected: 4
Received: 0
```

That proves the test is checking the missing retry behavior.

Only after watching that fail correctly would I write the minimal production code in `src/webhooks/sendWebhook.ts` to make this one test pass.

## Next test after GREEN

After the 500 retry test passes, I’d add the next RED test for the 400 behavior:

```ts
test('does not retry HTTP 400 responses', async () => {
  let attempts = 0;

  const server = await startWebhookServer((_req, res) => {
    attempts += 1;
    res.statusCode = 400;
    res.end('bad request');
  });

  const previousWebhookUrl = process.env.WEBHOOK_URL;
  process.env.WEBHOOK_URL = server.url;

  try {
    await expect(
      sendWebhook({
        id: 'evt_123',
        type: 'user.created',
      }),
    ).rejects.toThrow();

    expect(attempts).toBe(1);
  } finally {
    if (previousWebhookUrl === undefined) {
      delete process.env.WEBHOOK_URL;
    } else {
      process.env.WEBHOOK_URL = previousWebhookUrl;
    }

    await server.close();
  }
});
```

I would not write the HTTP 400 stopping logic until I had watched this second test fail for the expected reason.
