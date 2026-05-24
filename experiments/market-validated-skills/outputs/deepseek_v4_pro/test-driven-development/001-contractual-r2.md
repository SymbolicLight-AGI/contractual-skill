**Behavior Under Test**  
Add retry logic to `sendWebhook(event)`: retry HTTP 500 responses up to 3 times (total 4 attempts), stop immediately on HTTP 400.

**Assumptions** (unverified context, clearly marked):  
- `sendWebhook` is an async function in `src/webhooks/sendWebhook.ts` that makes an HTTP request (presumably via `fetch` or `axios`).  
- The test command is `npx jest`. The project uses Jest. The test file `sendWebhook.test.ts` will live in `src/webhooks/`.  
- The function’s current behaviour is to make a single request and throw/reject on failure. No retry logic exists.  
- I can mock the HTTP layer to return controlled responses.

---

## First TDD Cycle (Retry on 500)

### 1. Write the smallest failing test

File: `src/webhooks/sendWebhook.test.ts`

```ts
import { sendWebhook } from './sendWebhook';
import * as http from '../http'; // hypothetical; adjust to real HTTP dependency

jest.mock('../http');

describe('sendWebhook', () => {
  it('retries up to 3 times on HTTP 500 responses', async () => {
    const mockPost = jest.fn()
      .mockRejectedValueOnce({ status: 500 })   // 1st call fails
      .mockRejectedValueOnce({ status: 500 })   // 2nd call fails
      .mockRejectedValueOnce({ status: 500 })   // 3rd call fails
      .mockResolvedValueOnce({ status: 200 });  // 4th call succeeds

    (http.post as jest.Mock).mockImplementation(mockPost);

    await sendWebhook({ type: 'test' });

    expect(mockPost).toHaveBeenCalledTimes(4);
  });
});
```

**Why it’s the smallest behaviour**: it tests the retry count for 5xx, which is the core requirement.

### 2. Predicted RED evidence

Run `npx jest --testPathPattern=sendWebhook`.

Expected output:  
- Test **fails** with an assertion error: `Expected mock to have been called 4 times, but it was called 1 time.`  
- This failure reason is correct: the function does not retry (only one attempt). No setup or syntax error.

*If the failure is for a different reason (e.g., mockPost never called, undefined import), I would fix the test until I see the expected “no retry” failure.*

### 3. Minimal production code to pass

In `src/webhooks/sendWebhook.ts`, add retry logic around the HTTP call:

```ts
const MAX_RETRIES = 3;

export async function sendWebhook(event: any) {
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    try {
      const response = await http.post(/* endpoint */, event);
      if (response.status === 200) return response; // or handle success
      // other status handling...
    } catch (error) {
      const status = error?.status;
      if (status === 500 && attempt < MAX_RETRIES) continue;
      throw error;
    }
  }
}
```

*This is the minimal code to satisfy the test: it loops and retries on a 500 error up to 3 times.*

### 4. Predicted GREEN evidence

After adding the production code, rerun the same test command.

Expected: **test passes**, mock called exactly 4 times, no other tests break.

---

## Next Behaviour: Stop on 400

### 5. Write the next failing test

Add to the same describe block:

```ts
it('stops immediately on HTTP 400 (no retries)', async () => {
  const mockPost = jest.fn()
    .mockRejectedValueOnce({ status: 400 });

  (http.post as jest.Mock).mockImplementation(mockPost);

  await expect(sendWebhook({ type: 'test' })).rejects.toEqual({ status: 400 });
  expect(mockPost).toHaveBeenCalledTimes(1);
});
```

**Predicted RED**: test fails because current retry loop doesn’t differentiate 400; it would retry and attempt 4 times (or maybe throw after first but still try loop?). The assertion for call count 1 will fail.

### 6. Minimal production update

Add early exit for 400 inside the catch:

```ts
if (status === 400) throw error; // no retry
if (status === 500 && attempt < MAX_RETRIES) continue;
```

### 7. Predicted GREEN

Test passes; all previous tests stay green.

---

## Refactor Notes
After both cycles are green, I would refactor:
- Extract the retry policy into a small helper.
- Keep the loop readable while preserving tests.
- Run the full test suite after each change.

---

## Remaining Gaps
- Handling of other status codes (e.g., 429, network timeouts) not yet defined.
- Time-based retries with backoff; not in scope now.
- Integration test with a real HTTP server not covered.
- Mock dependency (`../http`) is assumed; the real mock path must be confirmed.

---

## Next TDD Step
After retry logic is green, the next step is to write a test for the 400 case and then follow the same cycle. Once both are green, we can refactor. Would you like me to proceed with writing the actual tests and code in your repository, or do you prefer to run the steps yourself?
