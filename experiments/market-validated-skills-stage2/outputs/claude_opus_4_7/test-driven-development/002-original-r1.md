I can't write the failing test yet — too many required inputs are missing. Per TDD, the test must fail for the *expected* reason, and that requires knowing what "expected" means in your project.

## Missing inputs I need

1. **Language / runtime** (e.g., Python, TypeScript, Go, Java).
2. **Test framework** (e.g., pytest, Jest/Vitest, Go's `testing`, JUnit) and how you run a single test file.
3. **The buggy function/module** — name, signature, and where it lives.
4. **Current (wrong) behavior** — what input produces what incorrect output today?
5. **Expected behavior** — for the same input, what should happen? Throw? Return `false`? Return a structured error?
6. **Scope of "date validation"** — which of these are in scope?
   - Format (e.g., `YYYY-MM-DD` only? ISO 8601? locale-specific?)
   - Calendar validity (Feb 30, leap years, month 13)
   - Range bounds (min/max date, future-only, past-only)
   - Type handling (empty string, `null`/`None`, non-string input)
   - Timezone / offset handling
7. **A concrete failing case** — one input + expected output that reproduces the bug.

## What I can give you now (framework-agnostic TDD plan)

Once you provide the above, the cycle will be:

1. **RED — write one minimal failing test** for the *specific* reported bug case (not a sweep of edge cases yet). Name it after the behavior, e.g., `rejects_february_30_as_invalid`.
2. **Verify RED** — run only that test; confirm it fails, and that the failure message matches the expected reason (e.g., "expected `false`, got `true`"), not a typo/import error.
3. **GREEN — minimal fix** in the validator to make that one test pass. No extra cases, no refactoring.
4. **Verify GREEN** — re-run the single test, then the full suite; output must be clean.
5. **REFACTOR** — only structural cleanup; tests stay green.
6. **Repeat** — one new RED test per additional edge case (leap year, empty string, null, out-of-range, wrong format, etc.), one at a time.

## Boundary note

This skill covers the TDD process, not the date-validation logic itself. I won't invent a language, framework, function signature, or "reasonable defaults" for edge cases — doing so would produce a test that passes immediately against fabricated behavior, which the skill explicitly forbids ("Test passes immediately? You're testing existing behavior. Fix test.").

**Next step:** Reply with items 1–7 above (even partial — at minimum 1, 2, 3, 4, 5, and one case from 7), and I'll write the first RED test.
