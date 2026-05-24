## Behavior Under Test

A service client should:

1. Retry transient HTTP `503` responses up to **3 times**.
2. Use **exponential backoff** between retries.
3. Not retry non-transient client/auth errors:
   - `400`
   - `401`

### Assumptions

Because no repository, language, test framework, or existing service location was provided, this plan uses generic test structure/pseudocode. Before implementation, adapt these to the project’s actual test framework and existing HTTP/test helpers.

Assumed retry meaning:

- “Retry up to 3 times” means:
  - 1 initial request
  - up to 3 retry attempts
  - 4 total attempts maximum
- If your intended meaning is 3 total attempts, this should be clarified before writing the final test.

Assumed backoff behavior:

- Exponential backoff delays might be something like:
  - retry 1: `baseDelay`
  - retry 2: `baseDelay * 2`
  - retry 3: `baseDelay * 4`
- Tests should inject/fake the clock or sleep function so tests do not actually wait.

---

## TDD Plan

### Cycle 1: Retry `503` once and eventually succeed

Smallest behavior:

- If the first response is `503` and the second response is `200`, the service retries once and returns success.

Test should verify:

- The HTTP request was made exactly 2 times.
- The final successful response is returned.
- One backoff delay was requested before the retry.

Expected RED failure before implementation:

- The service currently returns the first `503` without retrying, or makes only one request.

---

### Cycle 2: Retry `503` up to the maximum

Next behavior:

- If the service receives repeated `503` responses, it retries up to 3 times, then returns/fails with the final `503`.

Test should verify:

- Total attempts = 4.
- Backoff was called 3 times.
- Backoff delays follow the expected exponential sequence.

Expected RED failure before implementation:

- The service either does not retry, retries too few/many times, or does not use exponential delays.

---

### Cycle 3: Do not retry `400`

Behavior:

- A `400` response should be returned immediately without retrying.

Test should verify:

- Only 1 HTTP request is made.
- No backoff delay is requested.
- The `400` response/error is surfaced.

Expected RED failure before implementation:

- If the implementation retries all non-success responses, this test fails because it observes multiple attempts.

---

### Cycle 4: Do not retry `401`

Behavior:

- A `401` response should be returned immediately without retrying.

Test should verify:

- Only 1 HTTP request is made.
- No backoff delay is requested.
- The `401` response/error is surfaced.

Expected RED failure before implementation:

- Same as above: implementation incorrectly retries a non-transient auth error.

---

## First Tests Before Implementation

Below is framework-neutral pseudocode showing the first test file shape. The actual names should match the repository’s conventions.

```pseudo
describe "Service retry behavior" {
  test "retries once after a 503 and returns the eventual success response" {
    httpClient = FakeHttpClient([
      Response(status: 503, body: "temporarily unavailable"),
      Response(status: 200, body: "ok")
    ])

    backoff = FakeBackoff()

    service = Service(
      httpClient: httpClient,
      backoff: backoff,
      retryPolicy: RetryPolicy(
        maxRetries: 3,
        baseDelayMs: 100
      )
    )

    result = service.call()

    assert result.status == 200
    assert result.body == "ok"

    assert httpClient.requestCount == 2

    assert backoff.calls == [
      Duration(milliseconds: 100)
    ]
  }
}
```

### Why this is the first test

This is the smallest useful behavior proving that `503` is treated as transient:

- It avoids immediately testing the full max-retry case.
- It proves one retry happens.
- It proves the retry happens only after observing a `503`.
- It introduces fake HTTP and fake backoff boundaries needed for deterministic testing.

---

## Additional Tests to Add After First GREEN

```pseudo
test "retries 503 responses up to 3 times with exponential backoff, then returns the final failure" {
  httpClient = FakeHttpClient([
    Response(status: 503),
    Response(status: 503),
    Response(status: 503),
    Response(status: 503)
  ])

  backoff = FakeBackoff()

  service = Service(
    httpClient: httpClient,
    backoff: backoff,
    retryPolicy: RetryPolicy(
      maxRetries: 3,
      baseDelayMs: 100
    )
  )

  result = service.call()

  assert result.status == 503

  assert httpClient.requestCount == 4

  assert backoff.calls == [
    Duration(milliseconds: 100),
    Duration(milliseconds: 200),
    Duration(milliseconds: 400)
  ]
}
```

```pseudo
test "does not retry a 400 response" {
  httpClient = FakeHttpClient([
    Response(status: 400, body: "bad request")
  ])

  backoff = FakeBackoff()

  service = Service(
    httpClient: httpClient,
    backoff: backoff,
    retryPolicy: RetryPolicy(
      maxRetries: 3,
      baseDelayMs: 100
    )
  )

  result = service.call()

  assert result.status == 400
  assert result.body == "bad request"

  assert httpClient.requestCount == 1
  assert backoff.calls == []
}
```

```pseudo
test "does not retry a 401 response" {
  httpClient = FakeHttpClient([
    Response(status: 401, body: "unauthorized")
  ])

  backoff = FakeBackoff()

  service = Service(
    httpClient: httpClient,
    backoff: backoff,
    retryPolicy: RetryPolicy(
      maxRetries: 3,
      baseDelayMs: 100
    )
  )

  result = service.call()

  assert result.status == 401
  assert result.body == "unauthorized"

  assert httpClient.requestCount == 1
  assert backoff.calls == []
}
```

---

## RED Evidence

Not run yet.

No test command, language, framework, or repository path was provided. The next TDD step is to translate the first pseudocode test into the project’s actual test framework and run it before writing production code.

Expected RED result for the first test:

- The test should fail because the service does not yet retry a `503`.
- Correct failure would be something like:
  - expected request count `2`, got `1`
  - or expected final status `200`, got `503`

If it fails due to setup, fake client wiring, missing imports, or invalid test assumptions, fix the test and rerun RED before implementing retry logic.

---

## GREEN Evidence

Not available yet.

No production code should be written until the first test has been observed failing for the expected reason.

Expected GREEN result after minimal implementation:

- First test passes.
- The service makes a second request after an initial `503`.
- The fake backoff records one delay.
- No broader retry policy should be added beyond what the first test requires unless driven by the next failing test.

---

## Refactor Notes

No refactor yet.

After the first GREEN, possible safe refactors may include:

- Extracting retry decision logic, e.g. `isRetryableStatus(status)`.
- Extracting backoff calculation, e.g. `delayForAttempt(attemptNumber)`.
- Improving fake HTTP/backoff test helpers if duplicated across tests.

Refactoring should happen only after tests are green.

---

## Remaining Gaps

- Need actual repository location for the service/client.
- Need test framework and command.
- Need confirmation of retry semantics:
  - 3 retries plus initial attempt, or 3 total attempts?
- Need expected behavior after retries are exhausted:
  - return final response?
  - throw exception?
  - wrap in domain-specific error?
- Need base backoff duration and whether jitter is used.
- Need to know whether retry applies only to idempotent operations or all service calls.

---

## Next TDD Step

1. Confirm:
   - language/framework
   - test command
   - service/client location
   - retry count semantics
   - exhausted-retry behavior
   - base backoff duration
2. Write the first minimal test:

   > retries once after a `503` and returns the eventual success response

3. Run only that test.
4. Verify RED for the expected reason.
5. Implement the smallest production change to pass it.
