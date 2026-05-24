# TDD Response: Date Validation (Empty Dates Rejected)

## Boundary Notice

I can't run RED/GREEN cycles yet because required inputs are missing. Per the Skill, I'm flagging this rather than fabricating test output or guessing.

## Missing Inputs (please provide)

1. **Repository / code location** — where does the date validation live (file path, module, or language)?
2. **Test framework & command** — e.g., `pytest`, `npm test`, `go test ./...`, `cargo test`. I need the exact command to invoke.
3. **Expected observable outcome on empty input** — specifically:
   - What counts as "empty"? `""`, `null`/`None`, whitespace-only, missing field?
   - How should rejection surface? Thrown exception, returned error value, validation result object?
   - Exact error wording or error type, if it matters.
4. **Entry point** — function signature or API the test should call (e.g., `validateDate(input)` returning `{ok, error}`).

## Behavior Under Test (draft, pending confirmation)

> `validateDate(input)` rejects empty input (to be defined) with a validation error (shape to be defined), without accepting any other change to existing behavior.

## Proposed First Failing Test (illustrative, framework-agnostic pseudocode)

```
test("validateDate rejects empty string with a validation error", () => {
  const result = validateDate("");
  expect(result.ok).toBe(false);
  expect(result.error).toMatch(/empty|required/i);
});
```

Once you confirm framework, signature, and error shape, I will translate this into the repo's idioms.

## Planned TDD Cycle (will execute once inputs arrive)

1. Add the test above (adapted to your framework).
2. Run the test command → capture **RED** output, confirm failure reason is "function missing" or "did not reject empty," not a typo/setup error.
3. Implement the minimal rejection branch in `validateDate`.
4. Rerun → capture **GREEN** output.
5. Add follow-up failing tests for other "empty" cases you confirm (null/undefined, whitespace-only), one at a time.
6. Refactor only while green.

## RED Evidence

None yet — no command was run. I will not fabricate output.

## GREEN Evidence

None yet.

## Refactor Notes

N/A until GREEN is observed.

## Remaining Gaps

- Repo path, framework, test command unknown.
- Definition of "empty" unconfirmed.
- Error contract (exception vs. result object, wording) unconfirmed.
- Existing tests/patterns not yet inspected for conventions.

## Next TDD Step

Please answer the four items under **Missing Inputs**. As soon as you do, I'll write one minimal failing test, run it, and share real RED output before writing any production code.
