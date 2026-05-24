I can’t mark the regression test as passing without seeing it fail first and then pass after the fix.

Under TDD, the required evidence is:

1. A regression test that reproduces the bug.
2. Verified RED: the test fails for the expected reason.
3. Minimal fix.
4. Verified GREEN: the regression test and relevant suite pass.
5. Clean output with no unexpected errors or warnings.

Since the test output is not available, the correct report status is:

> Regression test status: **Not verified / evidence unavailable**  
> Shipping recommendation: **Do not ship until the regression test is run and passing output is captured.**

Next step: run the regression test and attach the output. If the test cannot be run, we should document that as a blocker or explicit release risk, not mark it as passing.
