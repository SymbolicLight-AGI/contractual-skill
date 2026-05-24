# TDD Handoff Artifact: Email Normalization

## Status
- **Phase:** RED (Tests defined, awaiting failure verification)
- **Implementation Owner:** Receiving Team
- **Scope:** Email normalization (lowercase domain, trim whitespace, preserve local part, reject missing `@`)

## Red Tests (Defined)
*Note: These tests are written to fail. Do not modify them to pass. Do not write implementation code yet.*

```typescript
test('trims leading and trailing whitespace from email', () => {
  const input = '  User@Example.com  ';
  const result = normalizeEmail(input);
  expect(result).toBe('User@Example.com');
});

test('lowercases the domain part of email', () => {
  const input = 'User@EXAMPLE.COM';
  const result = normalizeEmail(input);
  expect(result).toBe('User@example.com');
});

test('preserves local part casing', () => {
  const input = 'UserName@domain.com';
  const result = normalizeEmail(input);
  expect(result).toBe('UserName@domain.com');
});

test('rejects email missing @ symbol', () => {
  const input = 'invalidemail.com';
  expect(() => normalizeEmail(input)).toThrow('Invalid email format');
});
```

## Mandatory TDD Execution Plan
Follow the Iron Law strictly. **NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.**

1. **VERIFY RED** (MANDATORY)
   - Run the test suite: `[test runner command] path/to/email.test.ts`
   - Confirm each test **fails** (not errors).
   - Confirm failure message matches expected missing behavior.
   - If a test passes immediately, it is testing existing behavior or is incorrectly written. Fix the test. Do not proceed.
   - If a test errors, fix the error, re-run until it fails correctly.

2. **GREEN** (Minimal Code)
   - Write the simplest possible `normalizeEmail` implementation to pass **one** test at a time.
   - Do not add features, handle untested edge cases, or refactor other code.
   - YAGNI applies.

3. **VERIFY GREEN** (MANDATORY)
   - Run the test suite.
   - Confirm the targeted test passes.
   - Confirm all other tests remain green.
   - Confirm output is pristine (no warnings/errors).
   - If it fails, fix the implementation code. Do not change the test.

4. **REFACTOR**
   - Only after all tests are green.
   - Remove duplication, improve names, extract helpers.
   - Keep tests green. Do not add behavior.

5. **REPEAT**
   - Move to the next failing test. Follow the cycle until all are green.

## Verification Checklist
Before marking implementation complete, confirm:
- [ ] Watched each test fail before implementing
- [ ] Each test failed for the expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (no mocks unless unavoidable)
- [ ] Edge cases and errors covered per known requirements

## Uncertainty & Boundaries
- **Uncertainty:** Exact test runner/framework, project structure, and expected error class/message format are unspecified. Replace `[test runner command]` and adjust `toThrow` message if your environment requires it.
- **Boundary:** This artifact covers test definition and TDD execution protocol only. Implementation, deployment, and integration testing are outside this scope.
- **Next Step:** Run the tests to verify RED state. If any test passes immediately or errors, stop and correct the test before writing implementation code.

## Final Rule
```
Production code → test exists and failed first
Otherwise → not TDD
```
No exceptions. If you cannot verify the RED state, do not implement.
