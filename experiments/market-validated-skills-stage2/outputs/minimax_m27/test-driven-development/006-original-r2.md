<think>The user is asking me to prepare a handoff artifact for TDD (Test-Driven Development) after red tests have been defined for email normalization. The implementation will be done by another team.

Let me understand what's needed:
1. Red tests have been defined for email normalization
2. Known test cases: lowercase domain, trim whitespace, preserve local part, reject missing `@`
3. I need to prepare a handoff artifact for the other team

Following the TDD skill, I should:
- Document the red tests clearly
- Make it clear these are the specification
- Provide clear expectations for the implementation team

Let me create a proper handoff artifact with the red tests clearly defined.
</think>

# Email Normalization - TDD Handoff Artifact

## Purpose
This document provides the **RED phase tests** for email normalization. Implementation is owned by another team. These tests define the expected behavior—**implementation must pass all tests**.

---

## RED Tests (Write Failing Tests First)

```typescript
// tests/emailNormalization.test.ts

describe('email normalization', () => {
  describe('whitespace handling', () => {
    test('trims leading whitespace from email', () => {
      const result = normalizeEmail('  user@example.com');
      expect(result).toBe('user@example.com');
    });

    test('trims trailing whitespace from email', () => {
      const result = normalizeEmail('user@example.com  ');
      expect(result).toBe('user@example.com');
    });

    test('trims both leading and trailing whitespace', () => {
      const result = normalizeEmail('   user@example.com   ');
      expect(result).toBe('user@example.com');
    });
  });

  describe('domain case normalization', () => {
    test('converts domain to lowercase', () => {
      const result = normalizeEmail('user@EXAMPLE.COM');
      expect(result).toBe('user@example.com');
    });

    test('converts mixed case domain to lowercase', () => {
      const result = normalizeEmail('user@ExAmPlE.CoM');
      expect(result).toBe('user@example.com');
    });

    test('preserves local part case', () => {
      const result = normalizeEmail('UserName@Example.com');
      expect(result).toBe('UserName@example.com');
    });
  });

  describe('validation', () => {
    test('rejects email missing @ symbol', () => {
      const result = normalizeEmail('userexample.com');
      expect(result).toBeNull();
      // or throw error, or return { error: '...' } - confirm with team
    });

    test('rejects empty email', () => {
      const result = normalizeEmail('');
      expect(result).toBeNull();
    });
  });
});
```

---

## Expected Behavior Summary

| Input | Expected Output |
|-------|-----------------|
| `'  user@example.com  '` | `'user@example.com'` |
| `'User@EXAMPLE.COM'` | `'User@example.com'` |
| `'userexample.com'` | `null` / error |
| `''` | `null` / error |

---

## Handoff Checklist for Implementing Team

- [ ] Copy tests to your test file
- [ ] Run tests → verify they **fail** (RED phase)
- [ ] Implement `normalizeEmail(email: string): string | null`
- [ ] Run tests → verify they **pass** (GREEN phase)
- [ ] Refactor if needed (REFACTOR phase)
- [ ] All tests green before marking complete

---

## Clarification Needed Before Implementation

1. **Return type**: Should invalid emails return `null` or throw an error?
2. **API signature**: `normalizeEmail(email: string): string | null` or different?
3. **Test framework**: Jest, Vitest, or other?

---

## Verification Command

```bash
npm test tests/emailNormalization.test.ts
```

Expected initial result: **FAIL** (tests fail because feature not implemented)
