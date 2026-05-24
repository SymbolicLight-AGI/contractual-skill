I can't produce concrete TDD steps without a few project details. Here's what I need and why, plus the generic shape of what we'll do once I have it.

## Missing inputs

To follow TDD properly, please provide:

1. **Language and test framework** (e.g., Python + pytest, TypeScript + Jest, Go + testing, Ruby + RSpec). Test syntax, runner command, and assertion style all depend on this.
2. **The bug's current behavior** — what input produces what wrong output? (Exact example: input value, observed result, expected result.)
3. **The function/module under test** — its name, signature, and where it lives. I need to know what we're calling in the test.
4. **Validation rules** — what counts as a "valid" date in your domain? Examples:
   - Accepted formats (`YYYY-MM-DD` only? Multiple?)
   - Timezone handling
   - Range bounds (min/max date)
   - Behavior on `null`/empty/whitespace
   - Leap years, month/day bounds
   - Strict vs. lenient parsing (does `2024-02-30` roll over or reject?)
5. **How tests are run** in your project (command + where test files live).

Without these, any test I write would invent project conventions, an API surface, and edge-case semantics — which violates the skill's "no external sources / mark uncertainty" boundary.

## Boundary note

This skill governs *how* to implement via TDD, not *what* the date validation rules should be. Defining the spec is your call (or a product/spec decision). I won't guess it.

## Generic TDD shape we'll follow once you answer

1. **RED** — Write one failing test that reproduces the bug exactly (using the real input/expected output you give me).
2. **Verify RED** — Run it; confirm it fails for the right reason (wrong return value, not an import error).
3. **GREEN** — Minimal change to the validator to make that test pass.
4. **Verify GREEN** — Run the full test file; confirm pass and no other regressions.
5. **Add tests for each additional edge case** you list (one behavior per test), repeating RED → GREEN.
6. **REFACTOR** — Clean up only after green.

## Suggested next step

Reply with at least items 1–4 above. A minimal useful answer looks like:

> "Python + pytest. Function `validate_date(s: str) -> bool` in `app/validation.py`. Bug: `validate_date('2024-02-30')` returns `True`, should return `False`. Rules: format `YYYY-MM-DD`, reject invalid calendar dates, reject empty/None, no timezone."

With that I can write the first failing test verbatim.
