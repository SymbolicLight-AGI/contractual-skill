[UNCERTAINTY MARKED]
- Programming language: Unknown
- Test framework: Unknown
- Current bug behavior: Unknown
- Expected validation rules/edge cases: Unknown

Because these details are missing, I cannot generate runnable code. Below is the exact TDD workflow you must follow for a date-validation bug, using framework-agnostic placeholders. Provide the missing details to receive concrete test and implementation code.

---

### 1. RED - Write Failing Test
Create a new test file. Write **one** minimal test that targets the specific date-validation bug or missing rule.

```text
test('rejects [specific-invalid-date-case]', () => {
  const result = validateDate('[invalid-input]');
  expect(result.isValid).toBe(false);
  expect(result.error).toBe('[expected-error-message]');
});
```
**Rules:** One behavior per test. Clear, descriptive name. Use real validation logic, not mocks.

### 2. VERIFY RED - Watch It Fail
Run your test command: `[test-runner] [test-file-path]`
- Confirm the test **fails** (does not error/crash)
- Confirm the failure message matches the missing validation
- Confirm it fails because the feature is absent, not due to typos or missing imports
- **If it passes:** You are testing existing behavior. Adjust the test to target the actual bug.
- **If it errors:** Fix syntax/import issues, re-run until it fails correctly.

### 3. GREEN - Minimal Code
Write the simplest possible production code to make the test pass. Do not add extra rules, formatting, or edge cases.

```text
function validateDate(input) {
  if (input === '[invalid-input]') {
    return { isValid: false, error: '[expected-error-message]' };
  }
  return { isValid: true };
}
```
**Rules:** Just enough to pass. No over-engineering. No YAGNI.

### 4. VERIFY GREEN - Watch It Pass
Run: `[test-runner] [test-file-path]`
- Confirm the test passes
- Confirm all other tests still pass
- Confirm output is pristine (no warnings, deprecations, or errors)
- **If it fails:** Fix production code, never the test.

### 5. REFACTOR - Clean Up
Only after green:
- Improve variable/function names
- Remove duplication
- Extract shared validation helpers
- Keep all tests green. Do not add new behavior.

### 6. REPEAT
Write the next failing test for the next edge case (e.g., leap years, future dates, timezone offsets, `null`/`undefined`, malformed strings). Repeat the cycle until all validation requirements are covered.

---

### Verification Checklist
- [ ] Every validation rule has a dedicated test
- [ ] Watched each test fail before writing code
- [ ] Each failure was for the expected reason (missing validation)
- [ ] Wrote minimal code per test
- [ ] All tests pass with pristine output
- [ ] No mocks used unless unavoidable
- [ ] Edge cases covered systematically

**Next Step:** Provide the language, test framework, exact bug behavior, and expected validation rules. I will generate the exact failing test, implementation, and verification commands following this cycle without deviation.
