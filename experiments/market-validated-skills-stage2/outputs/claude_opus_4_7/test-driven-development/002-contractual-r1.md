# TDD Plan: Date Validation Bug

I can't start a real TDD cycle yet because key inputs are missing. Per the Skill, I must mark uncertainty rather than invent project details.

## Missing Inputs Needed

To produce a failing test (RED) and proceed, please provide:

1. **Language / runtime** (e.g., Python 3.11, Node 20, Go 1.22, Java 21).
2. **Test framework and command** (e.g., `pytest`, `npm test`, `go test ./...`, `mvn test`).
3. **Code location** of the date-validation function (file/module, function signature).
4. **Current (buggy) behavior** — what input produces what wrong output? Ideally a reproduction case.
5. **Expected behavior** — what should the validator return/raise for that input?
6. **Edge cases in scope** — e.g., leap years, timezone handling, ISO 8601 vs locale formats, two-digit years, null/empty, future/past bounds.
7. **Existing test patterns** — naming conventions, fixtures, helpers I should match.
8. **Privacy note**: do not include real user data in the bug report.

## Behavior Under Test
Unknown — pending the bug description above.

## RED Evidence
None. Not generated. Writing a test without knowing the framework or expected outcome would risk fabricating results, which the Skill forbids.

## GREEN Evidence
None.

## Refactor Notes
N/A.

## Remaining Gaps
- All inputs above.
- Whether a regression test fixture already exists for the bug.
- Whether the fix may change public API (would trigger a Human Gate).

## Next TDD Step (proposed, contingent on your answers)

Once you provide the inputs, the first cycle will be:

1. Add **one** minimal test that encodes the exact buggy input → expected output as a regression test, named after the bug (e.g., `test_rejects_feb_30_returns_false`).
2. Run the project's test command and capture the failure output verbatim — confirming it fails because the validator returns the wrong value, not due to import/typo/setup errors.
3. Only after RED is observed for the correct reason, implement the minimal fix.
4. Re-run the targeted test plus the surrounding suite for GREEN.
5. Add one additional test per in-scope edge case, repeating RED → GREEN.

## Boundary Note

If you'd like me to proceed *without* a failing test first (e.g., "just patch the function"), that falls outside this Skill's permissions. The correct next step is for you to share the inputs above so I can write the failing test first.
