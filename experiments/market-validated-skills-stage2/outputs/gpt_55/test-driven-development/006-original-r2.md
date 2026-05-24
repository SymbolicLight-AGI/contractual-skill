# TDD Handoff: Email Normalization Red Tests

## Scope

Implementation is owned by another team. This handoff defines the expected behavior and red-test coverage for email normalization.

No production implementation should be written until these tests have been run and verified to fail for the expected reasons.

## Feature Under Test

Email normalization should:

1. Lowercase the domain portion of an email address.
2. Trim leading and trailing whitespace.
3. Preserve the local part exactly as provided, except for surrounding whitespace removal.
4. Reject email values missing `@`.

## Red Tests Defined

> File path, test runner, and exact function/module names are uncertain and should be adapted to the owning repository.

Suggested target API:

```ts
normalizeEmail(input: string): string
```

Suggested test file:

```ts
normalizeEmail.test.ts
```

---

## Test 1: Lowercases domain

```ts
test('lowercases the domain part of an email address', () => {
  const result = normalizeEmail('User@EXAMPLE.COM');

  expect(result).toBe('User@example.com');
});
```

### Expected RED Failure

The test should fail because domain normalization is not implemented yet.

Example expected failure:

```text
Expected: "User@example.com"
Received: "User@EXAMPLE.COM"
```

---

## Test 2: Trims surrounding whitespace

```ts
test('trims surrounding whitespace from an email address', () => {
  const result = normalizeEmail('  user@example.com  ');

  expect(result).toBe('user@example.com');
});
```

### Expected RED Failure

The test should fail because whitespace trimming is not implemented yet.

Example expected failure:

```text
Expected: "user@example.com"
Received: "  user@example.com  "
```

---

## Test 3: Preserves local part casing

```ts
test('preserves the local part of an email address', () => {
  const result = normalizeEmail('First.Last+Tag@EXAMPLE.COM');

  expect(result).toBe('First.Last+Tag@example.com');
});
```

### Expected RED Failure

The test should fail if the implementation incorrectly lowercases the full email address or does not lowercase the domain.

Possible expected failures:

```text
Expected: "First.Last+Tag@example.com"
Received: "first.last+tag@example.com"
```

or:

```text
Expected: "First.Last+Tag@example.com"
Received: "First.Last+Tag@EXAMPLE.COM"
```

---

## Test 4: Rejects missing `@`

```ts
test('rejects an email address without an at sign', () => {
  expect(() => normalizeEmail('user.example.com')).toThrow('Email must contain @');
});
```

### Expected RED Failure

The test should fail because validation for missing `@` is not implemented yet.

Example expected failure:

```text
Expected function to throw an error.
Received function did not throw.
```

Error message may be adjusted if the project has an existing validation-error convention.

---

## Required RED Verification

Before implementation begins, run only the relevant test file first.

Example:

```bash
npm test normalizeEmail.test.ts
```

or, depending on the repository:

```bash
npm test -- normalizeEmail.test.ts
```

Confirm all of the following:

- Each new test fails.
- Each failure is due to missing email-normalization behavior.
- No failures are caused by typos, import errors, missing test setup, or incorrect assertions.
- No test passes immediately.

If any test passes immediately, revise the test because it is testing existing behavior rather than driving new behavior.

If any test errors instead of failing an assertion, fix the test setup and rerun until it fails correctly.

---

## Implementation Boundary

Implementation is out of scope for this handoff because it is owned by another team.

The owning team should follow the TDD cycle:

1. Run the red tests and verify expected failures.
2. Implement the minimal production code needed to pass one behavior at a time.
3. Re-run the tests and confirm green.
4. Refactor only after tests are green.
5. Run the full test suite before completion.

---

## Acceptance Criteria

The feature is complete when:

- Domain portion is lowercased.
- Leading and trailing whitespace are removed.
- Local part is preserved exactly after trimming.
- Inputs without `@` are rejected.
- All defined tests pass.
- Existing tests continue to pass.
- Test output is clean with no unexpected warnings or errors.
