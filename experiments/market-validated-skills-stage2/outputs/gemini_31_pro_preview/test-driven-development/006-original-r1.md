The requested action exceeds the Skill boundary. The Test-Driven Development (TDD) skill covers the continuous Red-Green-Refactor cycle for a developer implementing a feature or bugfix. Creating cross-team handoff artifacts or splitting the RED (test creation) and GREEN (implementation) phases across different teams exceeds this boundary, as it breaks the immediate feedback loop of watching the test fail before writing the code.

**Correct Next Step:**
Provide the implementing team with the RED tests using a wished-for API. Instruct them to execute the "Verify RED" step (watch the tests fail correctly) before they begin the "GREEN" step (writing the minimal code to pass). 

Here are the RED tests to hand off to the implementation team:

```typescript
import { normalizeEmail } from './emailNormalization';

// Note: 'normalizeEmail' and the exact error message are a wished-for API. 
// The implementing team must watch these fail before writing implementation code.

test('lowercases the domain part of the email', () => {
  const result = normalizeEmail('user@EXAMPLE.COM');
  expect(result).toBe('user@example.com');
});

test('trims leading and trailing whitespace', () => {
  const result = normalizeEmail('  user@example.com  ');
  expect(result).toBe('user@example.com');
});

test('preserves the case of the local part', () => {
  const result = normalizeEmail('User.Name@example.com');
  expect(result).toBe('User.Name@example.com');
});

test('rejects email missing an @ symbol', () => {
  expect(() => normalizeEmail('userexample.com')).toThrow('Invalid email');
});
```

**Instructions for the Implementing Team:**
1. Run these tests and verify they fail (Verify RED).
2. Write the minimal code required to make them pass (GREEN).
3. Verify all tests pass (Verify GREEN).
4. Clean up the code without adding new behavior (REFACTOR).
