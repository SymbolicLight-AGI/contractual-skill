# Handoff Artifact: Red Tests for Email Normalization

**Function under test:** `normalizeEmail(email: string): string`  
*(Assumed to exist as a stub so the test can compile/run and fail on assertions.)*

---

## Red Tests (Failing – Implementation Missing)

```typescript
// emailNormalization.test.ts
import { normalizeEmail } from './emailNormalization'; // adjust path

describe('normalizeEmail', () => {
  test('lowercases the domain part', () => {
    const email = 'User@Example.Com';
    const result = normalizeEmail(email);
    expect(result).toBe('User@example.com');
  });

  test('trims leading and trailing whitespace', () => {
    const email = '  user@example.com  ';
    const result = normalizeEmail(email);
    expect(result).toBe('user@example.com');
  });

  test('preserves the local part as-is (case sensitivity)', () => {
    const email = 'My.Long-Tag+news@domain.org';
    const result = normalizeEmail(email);
    expect(result).toBe('My.Long-Tag+news@domain.org');
  });

  test('rejects email missing @ symbol', () => {
    const invalidEmail = 'userexample.com';
    // Expect the function to throw an error or return a specific value;
    // we choose a thrown error here.
    expect(() => normalizeEmail(invalidEmail)).toThrow(
      'Invalid email: missing @'
    );
    // Alternative: if the function returns a custom error object, adjust expectation.
  });
});
```

---

## Instructions for the Implementation Team

This is a strict **Test-Driven Development** handoff. You are receiving the failing tests only—no production code has been written yet.

**Follow this order exactly:**

### 1. RED – Verify the Tests Fail

```bash
npm test -- emailNormalization.test.ts
```

**Checklist for RED verification:**
- [ ] All four tests **fail** (not error due to compilation/syntax issues).
- [ ] Each failure is an **assertion failure** that clearly shows missing behavior (e.g., “expected 'User@example.com', got …”), not a typo or runtime error.
- [ ] Specifically ensure:
  - lowercase test: domain is not lowercased.
  - trim test: whitespace remains.
  - local part test: local part is unchanged (if it currently fails for another reason, that’s fine as long as you see it doesn’t meet the requirement).
  - missing @ test: throws (or returns) the expected rejection.

If a test passes or errors unexpectedly, **fix the test setup** before moving on. Never write production code until every new test fails correctly.

### 2. GREEN – Minimal Implementation

Write the **simplest code possible** inside `normalizeEmail` to make exactly one test pass at a time.  
- No extra features, no refactoring other code, no “improvements”.
- After each change, run the full test suite and confirm all tests pass (new + existing).

### 3. REFACTOR – Clean Up

Only after **all tests are green**, refactor:
- Remove duplication
- Improve naming
- Extract helper functions

Keep all tests green during refactoring. Do not add new behavior.

### 4. Repeat

If additional edge cases arise later, write new failing tests first and repeat the cycle.

---

## Why This Matters

You must **watch each test fail** before fixing it. Otherwise, you cannot be sure the test actually validates the missing behavior. A test that passes immediately is useless—it may test the wrong thing, or not test at all.

**No implementation code without a failing test. No exceptions.**

---

*Prepared for handoff in the RED phase of the TDD cycle.*
