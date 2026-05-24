## Behavior Under Test

Service retry policy for HTTP responses:

1. Retries transient `503 Service Unavailable` responses.
2. Retries at most **3 times** after the initial attempt.
3. Uses **exponential backoff** between retries.
4. Does **not** retry non-transient client/auth failures:
   - `400 Bad Request`
   - `401 Unauthorized`

Assumptions, because repository details were not provided:

- The service has an HTTP client boundary that can be stubbed or faked.
- Backoff can be tested without real sleeping by injecting a clock/sleeper/timer.
- “Up to 3 times” means:
  - 1 initial request
  - up to 3 retry attempts
  - maximum 4 total calls
- The exact backoff sequence is not specified. I will assume something like `baseDelay`, `baseDelay * 2`, `baseDelay * 4`, unless the product requirement says otherwise.

---

## TDD Plan

### Cycle 1: Do not retry `400`

Smallest behavior: a `400` response is returned immediately with no retry.

Test intent:

```text
Given the downstream service returns 400
When the service call is made
Then the HTTP client is called exactly once
And the 400 response/error is returned
And no backoff delay is scheduled
```

Expected RED failure before implementation:

- The current code may retry all failures, or
- There may be no retry policy yet, or
- There may be no way to observe retry count/backoff.

---

### Cycle 2: Do not retry `401`

Smallest behavior: a `401` response is returned immediately with no retry.

Test intent:

```text
Given the downstream service returns 401
When the service call is made
Then the HTTP client is called exactly once
And the 401 response/error is returned
And no backoff delay is scheduled
```

Expected RED failure before implementation:

- Same as above, depending on current behavior.

---

### Cycle 3: Retry one transient `503` and eventually succeed

Smallest positive retry behavior: one retry happens after a transient `503`.

Test intent:

```text
Given the downstream service returns 503, then 200
When the service call is made
Then the HTTP client is called twice
And the final 200 response is returned
And one backoff delay is scheduled
```

This avoids testing the full max retry count immediately and proves basic retry behavior.

---

### Cycle 4: Retry `503` up to 3 times

Full retry limit behavior.

Test intent:

```text
Given the downstream service returns 503, 503, 503, then 200
When the service call is made
Then the HTTP client is called 4 times total
And the final 200 response is returned
And three backoff delays are scheduled
```

This confirms that the service allows three retries after the initial attempt.

---

### Cycle 5: Stop after 3 retries when `503` persists

Retry exhaustion behavior.

Test intent:

```text
Given the downstream service returns 503 repeatedly
When the service call is made
Then the HTTP client is called 4 times total
And the final failure/503 is returned or raised
And no fourth retry is attempted
```

Need confirmation on expected observable outcome:

- Should the service return the final `503` response?
- Or raise a retry-exhausted exception?
- Or wrap the error in a domain-specific failure?

---

### Cycle 6: Verify exponential backoff sequence

Backoff behavior.

Test intent:

```text
Given the downstream service returns 503, 503, 503, then 200
When the service call is made
Then the recorded delays are baseDelay, baseDelay * 2, baseDelay * 4
```

This should use an injected fake sleeper/timer, not real sleeping.

Need confirmation on:

- Base delay value.
- Whether jitter is expected.
- Whether delays are capped.

If jitter exists, test should verify bounds or injected deterministic jitter, not exact raw values.

---

## First Tests Before Implementation

Below is framework-neutral pseudocode. It should be adapted to the repository’s actual language, test framework, naming conventions, and HTTP client abstraction.

### Test 1: Does not retry `400`

```pseudo
test "does not retry 400 responses" {
  fakeHttpClient = new FakeHttpClient([
    response(status: 400, body: "bad request")
  ])

  fakeSleeper = new FakeSleeper()

  service = new Service(
    httpClient: fakeHttpClient,
    sleeper: fakeSleeper,
    retryPolicy: RetryPolicy(maxRetries: 3, baseDelayMs: 100)
  )

  result = service.callDownstream()

  assert result.status == 400
  assert fakeHttpClient.callCount == 1
  assert fakeSleeper.delays == []
}
```

Expected initial RED:

```text
Fails because the current implementation retries 400, does not expose retry control, or lacks the desired retry behavior.
```

If it fails due to test setup, missing fake client wiring, or incorrect assumptions about return shape, fix the test before writing production code.

---

### Test 2: Does not retry `401`

```pseudo
test "does not retry 401 responses" {
  fakeHttpClient = new FakeHttpClient([
    response(status: 401, body: "unauthorized")
  ])

  fakeSleeper = new FakeSleeper()

  service = new Service(
    httpClient: fakeHttpClient,
    sleeper: fakeSleeper,
    retryPolicy: RetryPolicy(maxRetries: 3, baseDelayMs: 100)
  )

  result = service.callDownstream()

  assert result.status == 401
  assert fakeHttpClient.callCount == 1
  assert fakeSleeper.delays == []
}
```

Expected initial RED:

```text
Fails because the current implementation retries 401, does not distinguish retryable from non-retryable statuses, or lacks retry behavior.
```

---

### Test 3: Retries a single `503` and succeeds

```pseudo
test "retries a transient 503 once and returns successful response" {
  fakeHttpClient = new FakeHttpClient([
    response(status: 503, body: "unavailable"),
    response(status: 200, body: "ok")
  ])

  fakeSleeper = new FakeSleeper()

  service = new Service(
    httpClient: fakeHttpClient,
    sleeper: fakeSleeper,
    retryPolicy: RetryPolicy(maxRetries: 3, baseDelayMs: 100)
  )

  result = service.callDownstream()

  assert result.status == 200
  assert result.body == "ok"
  assert fakeHttpClient.callCount == 2
  assert fakeSleeper.delays == [100]
}
```

Expected initial RED:

```text
Fails because the service does not retry 503 yet, does not use backoff, or does not make the sleeper observable.
```

---

## RED Evidence

Not run yet.

Missing required execution details:

- Repository/code location.
- Language and test framework.
- Existing test command.
- Current service API and HTTP abstraction.
- Expected final behavior after retry exhaustion.

Before implementation, the next TDD action is to add the first minimal test to the existing test suite and run the relevant test command to observe RED.

Example evidence format once run:

```text
RED command:
<test command>

RED result:
<failure summary>

Expected failure reason:
The service retried/did not retry contrary to the requested behavior.
```

---

## GREEN Evidence

Not available yet because implementation has not started.

The implementation should not begin until at least one failing test has been observed for the expected reason.

Expected future evidence format:

```text
GREEN command:
<test command>

GREEN result:
<pass summary>
```

---

## Refactor Notes

No refactor yet.

Potential refactor after GREEN:

- Extract retryability rule into a small function, for example:

```pseudo
isRetryableStatus(status) {
  return status == 503
}
```

- Extract backoff calculation:

```pseudo
delayForAttempt(attemptNumber) {
  return baseDelayMs * 2^(attemptNumber - 1)
}
```

- Keep sleeper/timer injectable to avoid real delays in tests.

Refactoring should only happen after tests pass.

---

## Remaining Gaps

Need clarification before completing the TDD design:

1. Test framework and command.
2. Exact service method/API under test.
3. Whether retries apply to returned HTTP responses, thrown HTTP exceptions, or both.
4. Expected result after all retries fail.
5. Backoff base delay.
6. Whether jitter or max delay cap is required.
7. Whether retry count means:
   - 3 retries plus initial attempt, or
   - 3 total attempts.

Current assumption: **3 retries plus the initial attempt**, for **4 total calls**.

---

## Next TDD Step

Add the first minimal test:

```text
does not retry 400 responses
```

Then run only that test and verify RED for the expected reason before writing production code.
