To apply Test-Driven Development to a date-validation bug, I need to start with a **failing test** that reproduces the exact bug. Right now I don’t have enough details to write that test.

I need from you:

- **The bug:** What specific input is handled incorrectly? (e.g., “accepts 30 February,” “rejects valid leap year dates,” “ignores timezone,” etc.)
- **Language and test framework:** Are we working in JavaScript with Jest, Python with pytest, or something else?
- **Current (buggy) behaviour:** What does the validation do now?
- **Expected behaviour:** What should it do instead?
- **Any edge cases** you want covered (leap years, different date formats, boundaries like 1900 or 2100, etc.)

Without these, any TDD cycle I describe would be guessing. That would break the TDD rule: no production code without a failing test that first proves the bug. I won’t invent a scenario.

Please share these details, and I’ll walk you through writing the exact failing test, verifying it fails for the right reason, then implementing the minimal fix.
