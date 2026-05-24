### Behavior Under Test
Email normalization logic. Target observable outcomes:
- Lowercase the domain portion
- Trim leading/trailing whitespace
- Preserve local part casing exactly
- Reject input missing `@` (raise error or return validation failure)

### RED Evidence
*Status:* Tests defined; execution pending.
*Uncertainty:* Exact test framework, file paths, and run command are not provided. Assuming standard unit test runner (e.g., `pytest`, `jest`, or `junit`).
*Expected RED State (per defined test):*
1. `test_lowercase_domain` → Fails because domain casing is unchanged.
2. `test_trim_whitespace` → Fails because whitespace remains in output.
3. `test_preserve_local_part` → Fails because local part is incorrectly modified/lowercased.
4. `test_reject_missing_at` → Fails because invalid input is accepted or does not trigger expected validation error.
*Verification Required:* Run test suite to confirm each test fails for the expected missing behavior, not for syntax, import, or setup errors. If a test fails for the wrong reason, fix the test first and re-run until RED is confirmed.

### GREEN Evidence
*Status:* Pending implementation by owning team.
*Requirement:* Write minimal production code only after RED is verified. Run the target test and relevant suite to confirm all pass. Provide exact command output showing pass summary before marking GREEN.

### Refactor Notes
*Status:* Deferred until GREEN is achieved.
*Guidance:* Once tests pass, refactor for readability, structure, or performance. Ensure all tests remain green after each incremental change. Do not alter tested behavior during refactoring.

### Remaining Gaps
- Implementation code not yet written.
- Test execution environment, framework, and exact run command missing (marked as uncertainty).
- Edge cases beyond the four known cases not yet specified (e.g., multiple `@` symbols, invalid characters, internationalized domains, empty/null inputs, trailing dots).
- CI/CD pipeline integration for automated regression testing pending.
- Mocking strategy undefined (if external validation services are involved, ensure mocks represent real boundaries and do not replace the normalization logic under test).

### Next TDD Step
1. Hand off test definitions to the implementation team.
2. Team runs tests to verify RED state and correct failure reasons.
3. Implement minimal code to satisfy the first failing test.
4. Run suite to verify GREEN.
5. Repeat for remaining tests.
6. Refactor while staying green.
7. Return GREEN evidence and updated test suite for review.
*Boundary Note:* I cannot execute tests or write production code as implementation ownership resides with another team. Please provide the test command/framework details if automated verification is required prior to handoff.
