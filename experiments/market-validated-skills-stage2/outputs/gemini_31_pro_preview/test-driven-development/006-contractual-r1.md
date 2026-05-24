**Boundary Statement:** I cannot provide actual RED or GREEN evidence because no test command output was provided, and I am strictly prohibited from inventing test results or claiming a test failed without command output. Additionally, implementing the production code exceeds my boundary for this task since it is owned by another team. The correct next step is to hand off the defined behaviors to the owning team so they can execute the tests, observe the RED state, and continue the TDD workflow.

Here is the TDD handoff artifact for the implementing team:

**Behavior Under Test**
Email normalization covering the following edge cases and constraints:
- Trim leading and trailing whitespace.
- Lowercase the domain portion of the email.
- Preserve the exact casing of the local portion (before the `@`).
- Reject inputs missing the `@` symbol.

**RED Evidence**
*[Uncertainty / Missing]* No test command output was provided. 
*Action required by owning team:* Run the test suite against the empty/stubbed implementation. Verify and record that the tests fail specifically for the missing normalization behaviors, not for setup errors or typos.

**GREEN Evidence**
*[Missing]* 
*Action required by owning team:* Write the minimal production code needed to pass the tests, run the target test and relevant suite, and record the passing command output here.

**Refactor Notes**
*[Missing]* 
*Action required by owning team:* Once tests are GREEN, refactor the normalization logic for readability and maintainability while ensuring the test suite remains GREEN.

**Remaining Gaps**
- The specific test command and testing framework were not provided.
- The tests have not yet been observed failing (RED) in a real environment.
- Production implementation is pending.

**Next TDD Step**
Hand off this plan to the implementing team. Their immediate next step is to configure the test command, run the defined tests to observe and record the RED evidence, and then write the minimal production code required to achieve GREEN.
