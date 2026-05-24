# TDD Workflow: Date Validation (Empty Dates Rejected)

I can follow a test-first workflow, but I need a few inputs before I can produce real RED/GREEN evidence. Per the Skill, I won't fabricate test results or write production code before observing a failing test.

## Behavior Under Test

Reject empty date inputs in a date validation routine.

- Input: an "empty" date value (needs clarification — see below).
- Expected outcome: validation fails / returns an error indicating the date is required.

## Missing Inputs (Blocking)

1. **Repository / code location** — Where does the date validator live (or should live)? Path and function/module name.
2. **Test framework and command** — e.g., `pytest`, `jest`, `go test`, `rspec`, plus the exact command to run a single test.
3. **Language / existing patterns** — So new tests follow repo conventions.
4. **Definition of "empty"** — Any of: `""`, `null`/`None`/`undefined`, whitespace-only, missing field? Please list which cases must be rejected.
5. **Expected error contract** — Exception type? Returned error object? Boolean + message? Exact wording, or is wording free?
6. **Edge cases in/out of scope** — Whitespace, invalid formats, far-future/past dates, timezone strings, etc.

## Proposed First Failing Test (pending your confirmation)

Once you supply the above, the smallest first test would be something like:

- Name: `rejects_empty_string_date`
- Arrange: call the validator with `""`.
- Assert: validator reports failure (exact assertion form depends on the error contract).

I will then:

1. Run the test command → capture RED output (must fail because the behavior is missing, not due to import/typo).
2. Implement the minimal code to reject `""`.
3. Re-run → capture GREEN output.
4. Repeat for each additional "empty" case you list (`null`, whitespace, missing field), one test at a time.

## RED Evidence

Not produced yet — cannot run tests without the framework, command, and repo location. I will not invent output.

## GREEN Evidence

Not produced yet — production code is not allowed before observed RED.

## Refactor Notes

N/A until GREEN is reached.

## Remaining Gaps

- Framework, command, repo path unknown.
- "Empty" semantics unspecified.
- Error contract unspecified.

## Next TDD Step

Please provide:

- Test command + framework
- Validator location (or confirm "create new module at <path>")
- Which inputs count as "empty"
- Error/return contract

With those, I will write one minimal failing test, run it, and share the actual RED output before writing any implementation.

## Handoff Note

If this repository has no test infrastructure yet, that is a Skill handoff condition — setting up a framework is outside a single TDD cycle and should be confirmed with you (or a reviewer) before proceeding.
