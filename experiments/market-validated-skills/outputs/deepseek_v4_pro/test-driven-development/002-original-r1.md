I'll follow test-driven development for the empty-date validation. Right now we're in the **RED** phase — I need to write a failing test before any production code.

Below is the test I’d write, using Jest syntax because the actual test framework wasn’t specified. (I’ve assumed an error message of `'Date required'` — that wording isn’t confirmed yet.)

```typescript
// file: tests/dateValidation.test.ts (exact path unknown)
import { validateDate } from '../src/dateValidation'; // module unknown

test('rejects empty date', () => {
  const result = validateDate({ date: '' });
  expect(result.error).toBe('Date required');
});
```

**What I must do next:** Verify that this test fails for the correct reason (feature not yet implemented). However, I’m missing:

- **Test framework & project setup** — e.g., Jest, Vitest, Mocha. I need to know which framework you’re using and how to run tests (e.g., `npm test`, `npx jest`, etc.).
- **Repository path** — where to place the test file.
- **Expected error wording** — is `'Date required'` the right message, or would you prefer something else?

Without that information, I can’t execute the test to confirm it fails before writing implementation code. That would break the TDD cycle.

**Next step:** Please provide the test framework and exact run command, the file location for tests, and confirm the error message you want. Once I have that, I’ll run the test to see it fail, then proceed to the GREEN phase with minimal code.
