## Behavior Under Test

I can guide the TDD cycle, but the required inputs are missing. To avoid inventing project details, I need:

1. **Language/runtime**  
   Example: JavaScript/TypeScript, Python, Java, Ruby, Go, etc.

2. **Relevant code location**  
   Example: `src/validators/date.ts`, `app/models/event.rb`, etc.

3. **Test framework and test command**  
   Example: `pytest`, `npm test`, `jest`, `go test ./...`, etc.

4. **Current buggy behavior**  
   Example: `"2024-02-31"` is currently accepted as valid.

5. **Expected observable behavior**  
   Example: `"2024-02-31"` should be rejected.

6. **Relevant edge cases**  
   Examples:
   - Leap years: `2024-02-29` valid, `2023-02-29` invalid
   - Invalid months: `2024-13-01`
   - Invalid days: `2024-04-31`
   - Empty string/null
   - Time zones, if applicable
   - Accepted format: ISO `YYYY-MM-DD`, locale date, timestamp, etc.

## RED Evidence

None yet.

Per the TDD contract, I should not write production code until a failing test has been written and observed failing for the expected reason.

The first step is to define one minimal failing test once the missing project details are known.

## GREEN Evidence

None yet.

No implementation should be done before RED evidence exists.

## Refactor Notes

No refactoring yet.

Refactoring can happen only after the target test and relevant suite are green.

## Remaining Gaps

Missing required information:

- Language
- Test framework
- Test command
- Code location
- Current behavior
- Expected behavior
- Date format and edge cases

## Next TDD Step

Please provide the missing details. If you want to start with a minimal example, answer these:

```text
Language:
Test framework:
Test command:
Date validator file/function:
Current invalid input that incorrectly passes:
Expected result:
Accepted date format:
```

Then the TDD sequence will be:

1. Write one minimal test for the date-validation bug.
2. Run the test and confirm it fails for the expected reason.
3. Implement the smallest production change to pass.
4. Run the target test and relevant suite.
5. Refactor only if tests stay green.
6. Record RED/GREEN evidence and remaining edge cases.
