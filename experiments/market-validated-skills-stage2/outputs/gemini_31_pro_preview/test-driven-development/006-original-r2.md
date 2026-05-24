**Skill Boundary Exceeded:** The request asks to hand off a batch of pre-defined RED tests for another team to implement. The TDD skill strictly dictates an iterative cycle: Write *one* failing test (RED), verify it fails, write minimal code to pass (GREEN), verify it passes, REFACTOR, and then *Repeat* for the next test. Batching multiple RED tests and splitting the test-writing from the implementation across teams violates this iterative feedback loop and the rule to write the "simplest code to pass the test" one behavior at a time.

**Correct Next Step:** Hand off the *requirements* to the implementing team so they can execute the full TDD cycle themselves, or hand off only the *first* RED test to start their cycle, followed by the requirements for their subsequent cycles. 

Below is the correct handoff artifact enforcing the TDD skill rules.

***

# Handoff Artifact: Email Normalization TDD Plan

## The Iron Law for Implementing Team
**NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.**
Do not write the implementation for all cases at once. You must follow the Red-Green-Refactor cycle strictly, one behavior at a time.

## Cycle 1: Lowercase Domain

**1. RED - Write Failing Test**
Add this single test to your suite:
```typescript
test('lowercases the domain part of the email', () => {
  expect(normalizeEmail('user@EXAMPLE.COM')).toBe('user@example.com');
});
```

**2. Verify RED - Watch It Fail (MANDATORY)**
Run the test. Confirm it fails because the normalization logic is missing, not due to a typo.

**3. GREEN - Minimal Code**
Write the absolute simplest code to make *only* this test pass. Do not add logic for whitespace or validation yet (YAGNI).

**4. Verify GREEN - Watch It Pass**
Run the test. Confirm it passes and output is pristine.

**5. REFACTOR**
Clean up the code if necessary. Keep the test green.

---

## Subsequent Cycles

Once Cycle 1 is complete, repeat the exact same 5-step process (Red -> Verify Red -> Green -> Verify Green -> Refactor) for each of the remaining requirements, **one at a time**:

### Cycle 2: Trim Whitespace
*   **RED:** Write one minimal test asserting that leading and trailing whitespace is removed (e.g., `'  user@example.com  '` becomes `'user@example.com'`).
*   **Verify RED:** Watch it fail.
*   **GREEN:** Add minimal code to trim whitespace.
*   **Verify GREEN:** Watch it pass.
*   **REFACTOR.**

### Cycle 3: Preserve Local Part
*   **RED:** Write one minimal test asserting that the casing before the `@` is untouched (e.g., `'Mixed.Case.User@example.com'` remains `'Mixed.Case.User@example.com'`).
*   **Verify RED:** Watch it fail.
*   **GREEN:** Add minimal code to ensure the local part is preserved.
*   **Verify GREEN:** Watch it pass.
*   **REFACTOR.**

### Cycle 4: Reject Missing `@`
*   **RED:** Write one minimal test asserting that an email without an `@` throws an expected error.
*   **Verify RED:** Watch it fail.
*   **GREEN:** Add minimal validation code to throw the error.
*   **Verify GREEN:** Watch it pass.
*   **REFACTOR.**

## Verification Checklist Before Completion
- [ ] Every behavior has a test.
- [ ] You watched each test fail *before* writing the implementation for it.
- [ ] You wrote minimal code to pass each test.
- [ ] All tests pass with pristine output.
