**Uncertainty Marked:** Missing programming language, test framework, current bug behavior, validation rules, and project structure. I cannot generate exact syntax or commands without these details.

Below is the strict TDD workflow for a date-validation bug, parameterized for your stack. Replace bracketed items with your project specifics.

### 1. RED – Write Failing Test
Create one minimal test that demonstrates the exact missing validation or bug.
```[language]
test('[clear behavior name, e.g., rejects invalid date format]', () => {
  // Arrange
  const input = '[invalid_date_value]';
  // Act
  const result = validateDate(input);
  // Assert
  expect(result).toBe('[expected_error_or_false]');
});
```

### 2. VERIFY RED – Watch It Fail
**MANDATORY. Never skip.**
```bash
[test-framework-command] path/to/test.[ext]
```
Confirm:
- [ ] Test fails (does not error/crash)
- [ ] Failure message matches the missing validation
- [ ] Fails because the feature is missing, not due to typos or setup issues
*If it passes:* You are testing existing behavior. Adjust the test to target the actual bug.
*If it errors:* Fix the test setup, then re-run until it fails correctly.

### 3. GREEN – Minimal Code
Write only the simplest code to make the test pass. Do not add extra validation, formatting, or configuration.
```[language]
function validateDate(input: [type]): [return_type] {
  // Minimal check to satisfy the failing test
  if ([condition_matching_test]) {
    return [expected_error_or_false];
  }
  return [default_valid_result];
}
```

### 4. VERIFY GREEN – Watch It Pass
**MANDATORY.**
```bash
[test-framework-command] path/to/test.[ext]
```
Confirm:
- [ ] Test passes
- [ ] All other tests still pass
- [ ] Output is pristine (no warnings/errors)
*If it fails:* Fix the implementation, not the test.

### 5. REFACTOR – Clean Up
Only after green:
- Extract validation logic if duplicated
- Improve variable/function names
- Keep all tests green. Do not add new behavior.

### Repeat
Write the next failing test for the next edge case (e.g., future dates, leap years, timezone offsets, null/undefined). Follow the exact cycle again.

### Verification Checklist
- [ ] Every validation rule has a dedicated failing test first
- [ ] Watched each test fail before writing implementation
- [ ] Each failure was expected (missing logic, not syntax)
- [ ] Wrote minimal code per test
- [ ] All tests pass with pristine output
- [ ] Tests use real validation logic (mocks only if unavoidable)
- [ ] Edge cases covered systematically

**Next Step:** Provide the missing details (language, test framework, exact bug description, and validation rules) so I can generate the precise test and implementation code. Until then, follow the cycle above exactly. Do not write production code before a failing test. If you have already written code, delete it and start from RED.
