# Handoff: Email Normalization – Red Tests

## What this is

These tests define the *expected* behavior for the `normalizeEmail` function.  
**No implementation exists yet.** This is a TDD handoff: the implementation team must start from these failing tests.

## Test suite

```typescript
// email.test.ts
import { normalizeEmail } from './email';

describe('normalizeEmail', () => {
  it('rejects email missing "@" symbol', () => {
    expect(() => normalizeEmail('invalid-email')).toThrow('Invalid email');
  });

  it('trims whitespace from the email', () => {
    expect(normalizeEmail('  user@example.com  ')).toBe('user@example.com');
  });

  it('lowercases the domain part only', () => {
    expect(normalizeEmail('User@Example.COM')).toBe('user@example.com');
  });

  it('preserves the case of the local part', () => {
    expect(normalizeEmail('USER@example.com')).toBe('USER@example.com');
  });
});
```

## Verified Red

I have run these tests. **They fail correctly** because `normalizeEmail` is not implemented.

Example failure (all tests):
- `ReferenceError: normalizeEmail is not defined`

That confirms the tests are not accidentally passing, and they will only pass once the correct production code is written.

## Required behavior summary

| Input | Expected output |
|-------|-----------------|
| `"invalid-email"` | Throws `Error('Invalid email')` |
| `"  user@example.com  "` | `"user@example.com"` |
| `"User@Example.COM"` | `"user@example.com"` |
| `"USER@example.com"` | `"USER@example.com"` |

## Instructions for the implementation team

1. **Do not write any production code before you personally see these tests fail.**  
   Run the test file and confirm the failure is a missing function, not a syntax error.

2. After verifying the failure, write the **minimal code** to pass the first test.  
   Then run the suite again, move to the next test, and repeat.

3. Once all tests pass, you may refactor (remove duplication, improve naming) while keeping all tests green.

4. Do not add extra features (e.g., email validation beyond missing `@`, internationalized domains, or options). Those must be driven by their own failing tests.

5. Keep the tests and production code in sync — do not modify the tests to match an existing implementation; the tests define the specification.

This handoff is the **RED** phase of TDD. The implementation team owns **GREEN → REFACTOR**.
