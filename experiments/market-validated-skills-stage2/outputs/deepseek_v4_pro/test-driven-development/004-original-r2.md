I cannot write a summary claiming the tests passed. The `npm test` command failed with `npm: command not found`, so I never saw the test run, let alone fail or pass. Skipping the verification step or fabricating results violates the TDD process.

Honest status: The test command could not execute. The next step is to ensure `npm` is installed and available in the environment, then re-run `npm test -- retry.spec.ts` to observe a real test result. Only after that can we proceed to implement any code.
