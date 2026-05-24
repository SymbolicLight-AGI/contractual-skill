<think>The user is asking me to prepare a handoff artifact for TDD tests that have been defined (red tests) for email normalization. The implementation will be done by another team.

Let me understand what's needed:
- Tests are already written (RED phase complete)
- Implementation is owned by another team
- Known test cases: lowercase domain, trim whitespace, preserve local part, reject missing `@`

I need to create a handoff artifact that clearly communicates:
1. What tests exist (the RED tests)
2. What behavior they're testing
3. What the expected outcomes are
4. Any context needed for implementation

This is a documentation/handoff task, not a coding task. I should create a clear artifact that the other team can use to implement the feature following TDD principles.

Let me structure this as a proper handoff document.
</think>

# Email Normalization - TDD Handoff Artifact

## Status
**Phase:** RED complete (tests defined, implementation pending)
**Owner:** [Your Team] → [Receiving Team]

---

## Test File Location
```
src/utils/emailNormalization.test.ts
```

---

## RED Tests (Failing)

### 1. Lowercase Domain
```typescript
test('normalizes domain to lowercase', () => {
  expect(normalizeEmail('User@EXAMPLE.COM')).toBe('user@example.com');
  expect(normalizeEmail('test@MiXeD.Case.COM')).toBe('test@mixed.case.com');
});
```

### 2. Trim Whitespace
```typescript
test('trims leading and trailing whitespace', () => {
  expect(normalizeEmail('  user@example.com  ')).toBe('user@example.com');
  expect(normalizeEmail('\tadmin@test.org\n')).toBe('admin@test.org');
});
```

### 3. Preserve Local Part
```typescript
test('preserves local part case', () => {
  expect(normalizeEmail('User.Name@example.com')).toBe('user.name@example.com');
  // Local part should remain as-is (before @)
});
```

### 4. Reject Missing @
```typescript
test('rejects email without @ symbol', () => {
  expect(() => normalizeEmail('userexample.com')).toThrow('Invalid email: missing @');
  expect(() => normalizeEmail('noemail')).toThrow('Invalid email: missing @');
});
```

---

## Expected Signature
```typescript
function normalizeEmail(email: string): string
```

---

## Implementation Notes

| Test | Expected Behavior |
|------|-------------------|
| Domain lowercase | Only the portion after `@` gets lowercased |
| Whitespace trim | Remove all leading/trailing whitespace before processing |
| Local part | Preserve exactly as provided (no case change) |
| Missing @ | Throw error with message `'Invalid email: missing @'` |

---

## Verification Checklist for Receiving Team

- [ ] Run tests: `npm test src/utils/emailNormalization.test.ts`
- [ ] Confirm all 4 tests fail (RED phase)
- [ ] Implement minimal code to pass each test
- [ ] Run tests again: confirm all pass (GREEN phase)
- [ ] Refactor if needed (tests stay green)
- [ ] No new behavior beyond these 4 cases

---

## Boundary
This handoff covers only email normalization. Do not add:
- Email format validation (beyond missing `@`)
- Domain resolution
- Email sending

If additional cases are needed, request new RED tests before implementation.

---

## Contact
[Your team contact info for questions]
