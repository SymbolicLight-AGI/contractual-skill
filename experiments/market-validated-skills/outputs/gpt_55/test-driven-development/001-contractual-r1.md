Behavior Under Test  
- First TDD slice: `sendWebhook(event)` retries failed HTTP `500` responses up to 3 times.  
- Expected observable outcome: the HTTP call is attempted 4 total times: 1 initial attempt + 3 retries.  
- Next slice after that: HTTP `400` stops immediately with no retries.

Assumptions / Uncertainty  
- Jest is the test framework.  
- I would follow existing test/mocking patterns in the repo.  
- I do not yet know whether `sendWebhook` uses `fetch`, `axios`, or another HTTP client, so the exact mock may need to match the existing implementation boundary.  
- I will not write production code until the retry test is observed failing for the expected reason.

First Minimal Test I Would Write

```ts
// src/webhooks/sendWebhook.test.ts

import { sendWebhook } from './sendWebhook';

describe('sendWebhook', () => {
  beforeEach(() => {
    jest.resetAllMocks();
  });

  it('retries HTTP 500 responses up to 3 times', async () => {
    const fetchMock = jest.fn()
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 500 })
      .mockResolvedValueOnce({ status: 500 });

    global.fetch = fetchMock as unknown as typeof fetch;

    const event = {
      url: 'https://example.com/webhook',
      payload: { id: 'evt_123' },
    };

    await sendWebhook(event);

    expect(fetchMock).toHaveBeenCalledTimes(4);
  });
});
```

RED Evidence  
- Not run yet.  
- Planned command:

```bash
npx jest src/webhooks/sendWebhook.test.ts
```

Expected RED failure  
- If `sendWebhook` currently sends only once, the expected failure would be similar to:

```text
Expected number of calls: 4
Received number of calls: 1
```

- That would be the correct failure reason because it shows missing retry behavior.  
- If the failure is instead due to import errors, wrong event shape, or incorrect HTTP mocking, I would fix the test setup first and rerun RED before touching production code.

Minimal GREEN Implementation After RED  
Only after observing the correct RED failure, I would make the smallest production change in:

```text
src/webhooks/sendWebhook.ts
```

Conceptually:

```ts
const maxRetries = 3;

for (let attempt = 0; attempt <= maxRetries; attempt++) {
  const response = await fetch(event.url, {
    method: 'POST',
    body: JSON.stringify(event.payload),
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (response.status !== 500) {
    return response;
  }
}
```

This is intentionally minimal for the first behavior. I would avoid adding broader status handling until covered by tests.

GREEN Evidence  
- Not available yet because the test has not been run and production code has not been changed.  
- Planned verification command after implementation:

```bash
npx jest src/webhooks/sendWebhook.test.ts
```

Next TDD Step  
After the `500` retry test is RED, implemented, and GREEN, I would add the second test:

```ts
it('does not retry HTTP 400 responses', async () => {
  const fetchMock = jest.fn()
    .mockResolvedValueOnce({ status: 400 });

  global.fetch = fetchMock as unknown as typeof fetch;

  const event = {
    url: 'https://example.com/webhook',
    payload: { id: 'evt_123' },
  };

  await sendWebhook(event);

  expect(fetchMock).toHaveBeenCalledTimes(1);
});
```

Then I would run:

```bash
npx jest src/webhooks/sendWebhook.test.ts
```

Expected RED for the second test  
- If the initial retry implementation retries all failures, this test should fail because `400` would be retried incorrectly.  
- Correct failure would be something like:

```text
Expected number of calls: 1
Received number of calls: 4
```

Then I would minimally adjust production code so only `500` retries and `400` returns immediately.

Refactor Notes  
- No refactor yet.  
- After both tests pass, possible safe refactors could include extracting `MAX_RETRIES = 3` or isolating retry decision logic, but only while tests remain green.

Remaining Gaps  
- Exact HTTP client/mock boundary is uncertain.  
- Exact `event` shape is uncertain.  
- We have not yet tested eventual success after one or more `500` responses.  
- We have not yet tested network exceptions, if those should be retried.  
- We have not yet tested delays/backoff, if required.
