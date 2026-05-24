# TDD Plan: Retry Behavior

Following the Iron Law of TDD (**NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST**), we will implement this feature one behavior at a time using the Red-Green-Refactor cycle. 

## Step 1: The Test Plan
We will break the requirements down into minimal, single-behavior tests. We will write and pass them strictly in this order:

1. **Test 1:** Retries a `503` error up to 3 times and succeeds.
2. **Test 2:** Fails and throws the error if a `503` occurs more than 3 times (1 initial attempt + 3 retries = 4 total attempts).
3. **Test 3:** Does not retry on a `400` error (fails immediately after 1 attempt).
4. **Test 4:** Does not retry on a `401` error (fails immediately after 1 attempt).
5. **Test 5:** Applies exponential backoff between retries (verifying the delay timing).

---

## Step 2: The First RED Test

We start with the first behavior: retrying a `503` response. 

Create your test file (e.g., `retry.test.ts`) and add the following minimal test. **Do not write the `retryOperation` implementation yet.**

```typescript
test('retries 503 response up to 3 times', async () => {
  let attempts = 0;
  const operation = async () => {
    attempts++;
    if (attempts <= 3) {
      const error = new Error('Service Unavailable');
      (error as any).status = 503;
      throw error;
    }
    return 'success';
  };

  // We expect it to fail 3 times with a 503, then succeed on the 4th attempt
  const result = await retryOperation(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(4); // 1 initial try + 3 retries
});
```

---

## Step 3: Verify RED (Your Next Action)

Before writing any production code, you **must** watch this test fail to confirm it is testing the right thing.

Run your test runner:
```bash
npm test
```

**Expected Result:** 
The test should fail (either because `retryOperation` is undefined, or if a dummy function exists, it fails because it doesn't catch the error and retry, resulting in an unhandled `503` exception).

**Next Steps:**
1. Run the test and verify the failure.
2. Once you see the red failure, write the **minimal** code in `retryOperation` to make this specific test pass (GREEN). Do not add the `400`/`401` logic or the exponential backoff yet.
3. Once GREEN, move to Test 2 in the plan.
