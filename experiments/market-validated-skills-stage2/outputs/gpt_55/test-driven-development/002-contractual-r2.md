## Behavior Under Test

I can help drive this with TDD, but key inputs are missing. To avoid inventing project details, please provide:

1. **Language/runtime** (e.g., JavaScript/Node, Python, Java, Ruby)
2. **Test framework/command** if known  
   - Example: `npm test`, `pytest`, `mvn test`, `bundle exec rspec`
3. **Relevant code location**  
   - File/function/class that performs date validation
4. **Bug report/current behavior**  
   - What invalid or valid date is currently handled incorrectly?
5. **Expected observable outcome**  
   - Should the validator return `true/false`, throw an error, return an error message, etc.?
6. **Edge cases to cover**  
   - Examples: leap years, invalid months, invalid days, empty input, timezone formats, partial dates

A minimal behavior statement might look like:

> Given input `"2024-02-30"`, the date validator should reject it because February 30 is not a real calendar date.

## RED Evidence

Not available yet.

No failing test can be written or run because the following are unknown:

- Test framework
- Test command
- Code location
- Expected validator API
- Exact bug behavior

Per TDD, I should not write production code before a failing test is observed.

## GREEN Evidence

Not available yet.

No implementation should be made until:

1. A minimal failing test is written.
2. The test is run.
3. The failure is confirmed to be for the expected missing/buggy behavior.

## Refactor Notes

No refactor should happen yet. Refactoring comes only after the target test and relevant suite are green.

## Remaining Gaps

Missing required TDD inputs:

- Language
- Test framework
- Test command
- Date-validation code location
- Current incorrect behavior
- Expected correct behavior
- Edge cases

## Next TDD Step

Please provide the missing project details. If you do not know the test framework, the next step is to identify it from the repository, for example by checking:

- `package.json` for JavaScript/TypeScript
- `pyproject.toml`, `setup.cfg`, or `requirements.txt` for Python
- `pom.xml` or `build.gradle` for Java/Kotlin
- `Gemfile` for Ruby
- Existing `test/`, `tests/`, `spec/`, or `__tests__/` directories

Once that is known, the first TDD cycle should be:

1. Pick the smallest failing date-validation case.
2. Add one minimal test for that case.
3. Run the test command and confirm RED.
4. Implement the smallest fix.
5. Run the target test and relevant suite to confirm GREEN.
6. Refactor only if needed while tests stay green.
