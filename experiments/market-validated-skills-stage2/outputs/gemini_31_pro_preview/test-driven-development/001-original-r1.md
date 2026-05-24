### TDD Plan: Retry Behavior

Following the strict Red-Green-Refactor cycle, we will implement this feature by writing one minimal test at a time, watching it fail, and writing only the code necessary to pass it. 

Here is the sequence of behaviors we will test:

1. **Baseline:** Executes operation successfully without retrying.
2. **Retry Success:** Retries a `503` error and succeeds on a subsequent attempt.
3. **Retry Limit:** Retries a `503` error exactly 3 times (4 total attempts) before finally failing.
4. **No Retry (400):** Fails immediately on a `400` error without retrying.
5. **No Retry (401):** Fails immediately on a `401` error without retrying.
6. **Backoff:** Applies exponential backoff delays between `503` retries.

---

### Step 1: RED - Write the First Failing Test

We start with the baseline behavior to define our wished-for API. 

**`retry.test.ts`**
```typescript
import { executeWithRetry } from './retry';

test('executes operation successfully without retrying', async () => {
  let attempts = 0;
  const operation = async () => {
    attempts++;
    return 'success';
  };

  const result = await executeWithRetry(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(1);
});
```

### Step 2: Verify RED - Watch It Fail

**MANDATORY NEXT STEP:** 
Run your test runner (e.g., `npm test`). 

You must confirm that this test fails because `executeWithRetry` is not defined or does not return the expected result. 

**Do not write any production code until you have seen this test fail.** 

Once you confirm the failure, write the absolute minimal code in `retry.ts` to make this single test pass (GREEN), verify it passes, and then we will move to the second test in the plan (testing the `503` retry logic).
