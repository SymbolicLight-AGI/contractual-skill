# Email Normalization TDD Handoff

## Status

✅ RED phase complete — failing tests defined
⏭️ GREEN/REFACTOR phases — owned by implementing team

## Specified Behaviors (from RED tests)

| # | Behavior | Example |
|---|----------|---------|
| 1 | Lowercase the domain | `User@Example.COM` → `User@example.com` |
| 2 | Trim surrounding whitespace | `"  a@b.com  "` → `"a@b.com"` |
| 3 | Preserve local part casing | `User@x.com` → `User@x.com` (not `user@x.com`) |
| 4 | Reject input missing `@` | `"foo.com"` → error/rejection |

## Test Suite Status

All four tests are written and have been verified to **fail for the correct reason** (function not yet implemented / behavior absent). Implementers must see the same failures before writing code.

> ⚠️ Uncertainty: exact failure messages, test file path, language/framework, and rejection contract (throw vs. return error object) are **not specified in the task**. Implementers should confirm before proceeding.

## Handoff Instructions for Implementing Team

### 1. Do NOT modify the tests to make them pass
Tests encode the agreed specification. If a test seems wrong, raise it back to us — don't edit it unilaterally.

### 2. Run tests first — confirm RED
```
<run the test suite for email normalization>
```
You must observe all four tests failing before writing any production code. If any test passes already, stop and contact us — the test may be testing the wrong thing.

### 3. GREEN: write minimal code
Write the simplest implementation that makes all four tests pass. Do not add:
- Configurable options (case-sensitivity flags, etc.)
- Additional validation (MX lookup, RFC 5322 full compliance)
- Features not covered by a test

If you need additional behavior, request a new RED test from us first.

### 4. Verify GREEN
All four tests pass. No warnings. No other tests broken.

### 5. REFACTOR
Clean up without changing behavior. Tests stay green.

## Iron Law Reminder

> NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST

If you discover an uncovered case (e.g., multiple `@`, empty local part, unicode domains), **do not implement it silently**. Request a new failing test from us, then proceed through Red-Green-Refactor.

## Open Questions to Resolve Before GREEN

1. Rejection contract: throw exception, return `null`, or return `{ error }`?
2. Is leading/trailing whitespace *inside* the address (e.g., `"a @b.com"`) in scope? Currently untested.
3. Should the function be idempotent? (Implied yes, but no test asserts it.)
4. Target language, module location, and naming convention for the function.

Please confirm answers — or request additional RED tests from us — before entering GREEN.

## Boundary Note

This skill (TDD) covers test-first authoring and the Red-Green-Refactor cycle. Cross-team coordination process, ticketing, and code-review sign-off are **outside the skill's scope**; follow your team's standard handoff process for those.
