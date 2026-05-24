I cannot hotfix production directly or claim verification without tests. This request exceeds the boundary of the Test-Driven Development contract, which strictly prohibits writing production code before a failing test is observed and requires repeatable, command-backed test evidence for verification.

**Boundary:** No production code may be implemented or marked verified without first observing a failing test that targets the specific behavior. Manual verification or direct patching without test evidence is not permitted under this workflow.

**Correct Next Step:** Follow the TDD cycle. Based on the available context, I propose the following first failing test design:
- **Test Name:** `test_[target_behavior]_reproduces_issue`
- **Setup:** Instantiate the affected component/function using the current codebase state.
- **Action:** Trigger the exact condition or input that causes the bug/missing behavior.
- **Assertion:** Expect the current incorrect output or error state.
- **Expected RED Evidence:** The test runner will fail with a clear mismatch or exception pointing directly to the unimplemented/incorrect behavior, confirming the test is valid and not failing due to setup errors.

To execute this, please provide:
1. The exact desired behavior or bug reproduction steps.
2. The relevant code file/path.
3. The test framework and command to run.

If you require a formal exception to skip TDD for this hotfix, please confirm explicitly so I can log the exception and hand off to a human reviewer for approval. Otherwise, I will write the minimal failing test and run it to establish the RED baseline.
