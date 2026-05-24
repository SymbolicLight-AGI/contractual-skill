# TDD Plan: HTTP Retry Behavior

## Behavior Under Test

A service must:
1. Retry transient `503` responses up to 3 times (4 total attempts, or 3 retries after initial — clarification needed).
2. Use exponential backoff between retries.
3. NOT retry `400` (Bad Request).
4. NOT retry `401` (Unauthorized).

## Assumptions (flagged — please confirm)

- "Up to 3 times" = 3 retries after the initial attempt (4 total calls). If interpretation differs, tests must be adjusted.
- Exponential backoff base/factor is unspecified. Assuming base delay `d` with delays `d, 2d, 4d` (e.g., 100ms, 200ms, 400ms). Real value must be injectable to keep tests fast and deterministic.
- Final outcome after exhausted retries: return the last `503` response (or raise). Assuming **return last response** — confirm.
- Language/framework not specified. Drafting tests in Python `pytest` style as a neutral example. **Specify the actual stack (test command + framework) before writing real tests.**
- HTTP client is injectable / mockable at a real boundary (the transport). Mocking at the transport layer is acceptable per the Skill; mocking the retry logic itself is not.

## Missing Inputs

- Repository / language / framework / test command.
- Exact backoff formula and base delay.
- Whether other 5xx codes (500, 502, 504) should also retry — task only specifies 503.
- Whether 429 (rate limit) is in scope — not specified, will not test.
- Behavior on network errors (timeout, connection refused) — not specified, will not test.

## Test List (smallest behavior first)

Each will be implemented one at a time, RED → GREEN → refactor.

1. **Single 200 succeeds with one attempt, no backoff.** (Baseline; ensures retry logic is dormant on success.)
2. **400 response is returned immediately; no retry.**
3. **401 response is returned immediately; no retry.**
4. **Single 503 followed by 200 returns 200 after one retry.**
5. **Three consecutive 503s then 200 returns 200 after three retries (total 4 attempts).**
6. **Four consecutive 503s: returns the final 503; exactly 4 attempts made, no 5th.**
7. **Backoff delays follow exponential schedule** (verified via injected sleeper/clock recording calls).
8. **Non-retryable status after a 503** (e.g., 503 then 401) returns the 401 without further retries.

## First Failing Tests (Draft)

Pseudocode in `pytest`. **Not yet run — not claiming RED until executed in the real repo.**

```python
# tests/test_retry.py
from unittest.mock import MagicMock
import pytest
from myservice.client import call_with_retry  # does not exist yet -> RED

class FakeTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = 0
    def send(self, request):
        self.calls += 1
        return self.responses.pop(0)

class FakeSleeper:
    def __init__(self):
        self.delays = []
    def sleep(self, seconds):
        self.delays.append(seconds)

def make_resp(status):
    r = MagicMock()
    r.status_code = status
    return r

def test_200_returns_immediately_no_retry():
    transport = FakeTransport([make_resp(200)])
    sleeper = FakeSleeper()
    resp = call_with_retry(request=MagicMock(),
                           transport=transport,
                           sleeper=sleeper,
                           base_delay=0.1)
    assert resp.status_code == 200
    assert transport.calls == 1
    assert sleeper.delays == []

def test_400_is_not_retried():
    transport = FakeTransport([make_resp(400)])
    sleeper = FakeSleeper()
    resp = call_with_retry(request=MagicMock(),
                           transport=transport,
                           sleeper=sleeper,
                           base_delay=0.1)
    assert resp.status_code == 400
    assert transport.calls == 1
    assert sleeper.delays == []

def test_401_is_not_retried():
    transport = FakeTransport([make_resp(401)])
    sleeper = FakeSleeper()
    resp = call_with_retry(request=MagicMock(),
                           transport=transport,
                           sleeper=sleeper,
                           base_delay=0.1)
    assert resp.status_code == 401
    assert transport.calls == 1
    assert sleeper.delays == []
```

These three are the smallest first cycle. Tests 4–8 will follow one at a time.

## RED Evidence

**Not yet collected.** No test command was provided, no repository was provided, and no environment was executed against. I cannot fabricate a failure log. Once the stack is confirmed, the first run is expected to fail with `ImportError: cannot import name 'call_with_retry'` — that is the expected RED reason for test 1.

## GREEN Evidence

Not applicable — no implementation written (per the Skill: no production code before observed RED).

## Refactor Notes

None yet.

## Remaining Gaps

- Real test command and framework not confirmed.
- Backoff formula and base delay not specified.
- Behavior on retry exhaustion (return vs. raise) not specified.
- Scope of retryable status codes beyond 503 not specified.
- `FakeTransport` and `FakeSleeper` are test-only seams. They represent real boundaries (network I/O and time), which the Skill permits, but this should be confirmed with the reviewer before locking in — **human gate**.

## Next TDD Step

1. Confirm the open questions above (stack, backoff schedule, exhaustion behavior, transport seam).
2. Place `tests/test_retry.py` in the repo and run the chosen test command.
3. Capture the actual RED output for test 1 (`test_200_returns_immediately_no_retry`) — expected failure: missing module/symbol.
4. Implement the minimal `call_with_retry` that returns the transport's response unchanged (no retry logic yet) to turn test 1 GREEN.
5. Proceed to test 2 (`test_400_is_not_retried`) and continue down the list.

## Boundary Note

This response is a **plan and draft only**. Per the Skill's "Not allowed" clause, I have not claimed any test passed or failed without command output, and no production code has been written. The first real RED must be observed in the target repository before any implementation begins.
