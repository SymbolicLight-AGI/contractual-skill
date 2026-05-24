# TDD Handoff Artifact: Email Normalization

## Context
- **Feature:** Email normalization
- **Current State:** Red tests defined. Implementation pending.
- **Ownership:** Implementation code is owned by the receiving team.
- **Known Requirements:** Lowercase domain, trim whitespace, preserve local part case, reject missing `@`.

## ⚠️ Mandatory TDD Execution Protocol
Per the Test-Driven Development skill, the following rules apply without exception:
1. **NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.**
2. **Verify RED:** Run the tests below. Confirm they fail for the expected reason (missing feature, not syntax/import errors).
3. **GREEN:** Write the absolute minimal code to pass *one* test at a time. Do not add features, refactor other code, or over-engineer.
4. **Verify GREEN:** Confirm the test passes and all previous tests remain green. Output must be pristine.
5. **REFACTOR:** Clean up duplication, improve names, or extract helpers *only after* green. Keep tests green.
6. **If you write implementation code before verifying a failing test, delete it. Start over.**

## Red Tests (Awaiting Verification)
*[Note: Test framework, file structure, and exact API contract are unspecified. Adjust imports, syntax, and error handling to match your environment.]*

```typescript
import { normalizeEmail } from './normalizeEmail'; // Adjust path as needed

test('trims leading and trailing whitespace from email', () => {
  const result = normalizeEmail('  user@example.com  ');
  expect(result).toBe('user@example.com');
});

test('lowercases the domain part of the email', () => {
  const result = normalizeEmail('user@EXAMPLE.COM');
  expect(result).toBe('user@example.com');
});

test('preserves the local part case', () => {
  const result = normalizeEmail('User@Example.com');
  expect(result).toBe('User@example.com');
});

test('rejects email missing @ symbol', () => {
  expect(() => normalizeEmail('invalidemail')).toThrow('Invalid email: missing @');
});
```

## Execution Plan for Receiving Team

### 1. Verify RED
- Run the test suite.
- Confirm each test fails with a clear, expected error (e.g., `TypeError: normalizeEmail is not a function` or `Expected: ... Received: undefined`).
- **Test passes?** You are testing existing behavior or the test is incorrect. Fix the test.
- **Test errors?** Fix syntax/import errors, re-run until it fails correctly.

### 2. GREEN (Iterate per test)
- Select one failing test.
- Write the simplest possible implementation to make it pass.
- Run the test. Confirm it passes.
- Repeat for the next test. Do not implement multiple cases at once.

### 3. REFACTOR
- Only after all tests are green, clean up duplication, improve naming, or extract helpers.
- Run tests after every refactor to ensure they stay green. Do not add behavior.

## Verification Checklist
Before marking implementation complete, confirm:
- [ ] Every test was watched to fail before implementation
- [ ] Each failure was for the expected reason (feature missing, not typo)
- [ ] Minimal code was written per test
- [ ] All tests pass with pristine output (no warnings/errors)
- [ ] Tests use real code (mocks only if strictly unavoidable)
- [ ] Known edge cases are covered

## Uncertainties & Boundaries
- **Uncertainty:** Test framework, runner commands, and exact file paths are not provided. Adjust `npm test` equivalents and import paths to your stack.
- **Uncertainty:** API signature assumes `normalizeEmail(input: string): string` and throws on invalid input. Change to your team's contract (e.g., return `{ error: string }`) if required.
- **Boundary:** This artifact contains only tests and the TDD execution plan. Writing implementation code without first verifying a failing test violates the TDD skill boundary. If you have already written implementation code, delete it and begin the RED cycle.

## Next Step
Run the tests. Verify they fail correctly. Begin the GREEN cycle for the first test.
