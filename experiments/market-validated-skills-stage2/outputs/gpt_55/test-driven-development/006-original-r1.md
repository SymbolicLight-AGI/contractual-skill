## TDD Handoff: Email Normalization

### Scope

Implementation is owned by another team. This handoff defines the intended behavior and the red tests that should drive implementation.

### TDD Boundary

No production implementation should be written until the receiving team has:

1. Added the tests below or equivalent behavior-focused tests.
2. Run them against the current implementation.
3. Confirmed they fail for the expected reason.
4. Implemented the minimal code required to pass.
5. Re-run the full relevant test suite and confirmed all tests pass.

---

## Target Behavior

Email normalization should:

1. Lowercase the domain portion.
2. Trim leading and trailing whitespace.
3. Preserve the local part exactly as provided, except for surrounding whitespace removal.
4. Reject emails missing `@`.

---

## Proposed Red Tests

Assumed API, to be confirmed by implementation team:

```ts
normalizeEmail(input: string): string
```

If the actual API differs, adapt the test calls while preserving the same behavior assertions.

---

### 1. Lowercases the domain

```ts
test('lowercases the email domain', () => {
  const result = normalizeEmail('User@EXAMPLE.COM');

  expect(result).toBe('User@example.com');
});
```

Expected initial failure:

```text
Expected: "User@example.com"
Received: "User@EXAMPLE.COM"
```

Failure should indicate that domain normalization is missing.

---

### 2. Trims surrounding whitespace

```ts
test('trims surrounding whitespace from email', () => {
  const result = normalizeEmail('  user@example.com  ');

  expect(result).toBe('user@example.com');
});
```

Expected initial failure:

```text
Expected: "user@example.com"
Received: "  user@example.com  "
```

Failure should indicate that surrounding whitespace is not being removed.

---

### 3. Preserves local part casing

```ts
test('preserves local part casing', () => {
  const result = normalizeEmail('First.Last@EXAMPLE.COM');

  expect(result).toBe('First.Last@example.com');
});
```

Expected initial failure, if current implementation lowercases the whole email:

```text
Expected: "First.Last@example.com"
Received: "first.last@example.com"
```

Failure should indicate that the local part is being changed incorrectly.

---

### 4. Rejects email missing at sign

```ts
test('rejects email missing at sign', () => {
  expect(() => normalizeEmail('user.example.com')).toThrow();
});
```

If the project uses typed/domain errors, prefer the project-standard assertion, for example:

```ts
test('rejects email missing at sign', () => {
  expect(() => normalizeEmail('user.example.com')).toThrow('Email must contain @');
});
```

Expected initial failure:

```text
Expected function to throw
Received function did not throw
```

Failure should indicate that invalid email structure is not being rejected.

---

## Verification Requirements for Receiving Team

Before implementation:

- [ ] Add one behavior-focused test at a time.
- [ ] Run the specific test file.
- [ ] Confirm each test fails before writing implementation.
- [ ] Confirm failure is due to missing behavior, not typo/setup/import error.

During implementation:

- [ ] Write only the minimal production code needed to pass the current failing test.
- [ ] Do not add behavior not covered by tests.
- [ ] Do not rewrite unrelated normalization or validation logic.

After implementation:

- [ ] All new tests pass.
- [ ] Existing tests still pass.
- [ ] Test output is clean: no unexpected warnings or errors.
- [ ] Local part preservation is confirmed.
- [ ] Domain lowercasing is confirmed.
- [ ] Whitespace trimming is confirmed.
- [ ] Missing `@` rejection is confirmed.

---

## Open Questions / Uncertainties

The following details are not specified and should be confirmed before or during implementation:

1. Should multiple `@` characters be rejected?
2. Should empty local part, e.g. `@example.com`, be rejected?
3. Should empty domain, e.g. `user@`, be rejected?
4. Should internal whitespace be rejected or preserved?
5. What exact error type/message should be used for invalid emails?
6. Should Unicode or internationalized domain names be supported?

These should not be implemented unless the receiving team adds failing tests for the agreed behavior first.
