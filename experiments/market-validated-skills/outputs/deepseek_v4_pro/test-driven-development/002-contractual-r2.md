To follow the TDD contract, I need a few concrete details before I can write and run the first failing test. Without them, I can't produce real RED/GREEN evidence, and the contract prohibits inventing test results or writing production code before seeing a real failure.

**Missing required inputs:**
- **Test command & framework** – e.g., `pytest tests/test_validation.py`, `npm test`, `rspec`, etc. I need to know how to execute tests and the framework’s assertion style.
- **Code location** – where should the validation logic be placed (file path, function/class name)? At minimum, I need to know which file to modify or create and where the new test file should live.
- **Expected observable outcome** – what exactly should happen when an empty date is submitted? For example: raise a specific exception, return an error message, or set a validation flag. The exact error wording or structure matters so the test isn't brittle, but I need the intended behavior (e.g., “raise `ValueError('Date must not be empty')`”).

**Why this matters for TDD:**
The contract requires that I write a minimal failing test, run it, observe it fail *for the expected reason* (not a syntax or setup error), then implement the minimal code to pass. Without a runnable test command and a clear expected failure, I can’t verify the RED step or guarantee the test is valid.

**Next step:**
Please supply the missing items above, or give me permission to proceed with clearly marked assumptions (e.g., assume Python with `pytest`, create a `Validator` class in `validators.py`, and use `ValueError` with a generic message). I’ll then start the first TDD cycle and report RED evidence.
