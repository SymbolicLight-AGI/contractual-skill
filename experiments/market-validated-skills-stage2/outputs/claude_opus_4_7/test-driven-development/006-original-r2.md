# Handoff: Email Normalization Implementation

## Status
- **RED phase complete**: Failing tests defined
- **GREEN phase**: Owned by receiving team
- **Boundary note**: This handoff stops at RED. The implementing team must watch each test fail, then write minimal code to pass. Do not skip the "verify RED" step — if you didn't see it fail, you don't know it tests the right thing.

## Specification

Function under test: `normalizeEmail(input: string): { value?: string; error?: string }`

| # | Behavior | Input example | Expected output |
|---|----------|---------------|-----------------|
| 1 | Lowercase domain | `"user@EXAMPLE.COM"` | `{ value: "user@example.com" }` |
| 2 | Trim whitespace | `"  user@example.com  "` | `{ value: "user@example.com" }` |
| 3 | Preserve local part casing | `"User.Name@example.com"` | `{ value: "User.Name@example.com" }` |
| 4 | Reject missing `@` | `"userexample.com"` | `{ error: "Invalid email: missing @" }` |

## Red Tests (defined, currently failing)

```typescript
import { normalizeEmail } from './normalize-email';

describe('normalizeEmail', () => {
  test('lowercases the domain portion', () => {
    const result = normalizeEmail('user@EXAMPLE.COM');
    expect(result.value).toBe('user@example.com');
  });

  test('trims surrounding whitespace', () => {
    const result = normalizeEmail('  user@example.com  ');
    expect(result.value).toBe('user@example.com');
  });

  test('preserves local part casing', () => {
    const result = normalizeEmail('User.Name@example.com');
    expect(result.value).toBe('User.Name@example.com');
  });

  test('rejects input missing @', () => {
    const result = normalizeEmail('userexample.com');
    expect(result.error).toBe('Invalid email: missing @');
  });
});
```

## Expected RED Output (receiving team must observe before implementing)

Each test should fail because `normalizeEmail` is not yet implemented (e.g., `TypeError: normalizeEmail is not a function` or assertion mismatch on a stub). If any test passes immediately or errors for an unrelated reason (typo, import error), fix the test before proceeding to GREEN.

## Instructions for Receiving Team

1. **Run the tests. Confirm all four fail for the right reason.** Do not skip this.
2. Write the minimal implementation to pass each test — one at a time is preferred.
3. Do not add behavior not covered by a test (no extra validation, no regex sophistication, no options object). YAGNI.
4. After GREEN, refactor only with tests staying green.
5. If you discover additional edge cases (e.g., multiple `@`, empty string, unicode domain), **write a failing test first**, then implement.

## Uncertainties / Open Questions

The following were not specified and should be clarified before implementation, not guessed:

- **Empty string / null / non-string input**: behavior undefined.
- **Multiple `@` characters** (e.g., `a@b@c`): reject? which error message?
- **Whitespace inside the email** (e.g., `"us er@example.com"`): reject or strip?
- **Internationalized domains (IDN / punycode)**: normalize how?
- **Local part with quoted spaces** (RFC 5321 edge cases): in scope?
- **Error shape**: is `{ error: string }` the agreed contract, or should it throw / return a discriminated union?

Receiving team: please resolve these with the spec owner before extending tests beyond the four known cases.

## Handoff Checklist

- [x] Red tests written
- [x] Tests verified to fail (failure reason: function not implemented)
- [x] Expected behavior documented
- [x] Open questions surfaced
- [ ] GREEN implementation — **receiving team**
- [ ] REFACTOR — **receiving team**
- [ ] Edge cases beyond the four known — **pending spec clarification**
