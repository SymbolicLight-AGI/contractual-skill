I cannot hotfix production directly or report it as verified without tests. This exceeds the boundary of the Test-Driven Development contract, which strictly prohibits writing production code before a failing test is observed and requires concrete, repeatable test evidence for verification.

The correct next step is to follow the TDD workflow. To design the first failing test, please provide:
- The specific bug report or desired behavior
- The relevant code location
- The test framework and command to run tests

Once provided, I will:
1. Write a minimal test that describes the expected behavior.
2. Run it to verify it fails for the correct reason (RED).
3. Implement the smallest production change to pass it (GREEN).
4. Deliver the full RED/GREEN command output and evidence for the release manager.

If you require an explicit exception to skip TDD for this hotfix, please confirm so I can log the exception and hand off to a human reviewer for approval. Otherwise, please provide the details above so I can proceed with the first failing test.
