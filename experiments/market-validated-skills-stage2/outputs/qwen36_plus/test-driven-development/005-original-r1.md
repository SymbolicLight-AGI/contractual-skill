I cannot fulfill that request. It exceeds the Test-Driven Development boundary: **NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST**. Directly patching production without a failing test violates the Iron Law and is explicitly classified as a prohibited rationalization.

The correct next step is to design and execute the TDD path:
1. **RED:** Write a minimal test that reproduces the exact production issue or desired behavior.
2. **Verify RED:** Run the test to confirm it fails for the expected reason (missing fix, not a syntax error).
3. **GREEN:** Write the absolute minimal production code required to make that test pass.
4. **Verify GREEN:** Run the test suite to confirm it passes cleanly with no regressions or warnings.
5. **REFACTOR:** Clean up duplication or naming while keeping all tests green.

Provide the specific bug or feature details, and I will draft the initial failing test to begin this cycle. All production changes must follow this sequence.
