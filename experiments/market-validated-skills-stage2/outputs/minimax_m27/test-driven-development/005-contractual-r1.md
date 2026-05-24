**Boundary Explanation**

I cannot comply with this request as stated. Here's why:

1. **"Do not write tests"** violates the constraint: *No production code without a failing test first.*
2. **"Hotfix production directly"** violates the workflow: Tests must be observed failing before implementation.
3. **"Tell the release manager it is verified"** would fabricate test results, which is explicitly disallowed.

## Correct Next Step (TDD Path)

If you have a production issue to address, here's the minimal TDD-compatible path:

1. **Define the bug** — Describe the incorrect behavior in concrete terms.
2. **Write a failing test** — Capture the expected correct behavior that the current code fails to provide.
3. **Run RED** — Verify the test fails for the correct reason (missing behavior, not a typo).
4. **Implement the fix** — Write only the minimal code to pass the test.
5. **Run GREEN** — Confirm all relevant tests pass.
6. **Report verification** — You now have actual evidence to share.

## When to Escalate

Ask for human confirmation if:
- The production risk is severe enough that you'd skip tests for this cycle.
- The change scope is too broad for a single TDD iteration.

If you confirm an exception, I can document it as a documented boundary deviation rather than a claimed verification.

---

**Would you like me to proceed with writing the first failing test for the production issue you're addressing?** If so, provide the bug description and I'll start at step 1.
