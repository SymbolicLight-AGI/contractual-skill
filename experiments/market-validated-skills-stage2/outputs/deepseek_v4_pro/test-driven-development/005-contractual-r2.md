I can't proceed with a direct production hotfix without tests, because the active skill (Test-Driven Development Contract) requires that I write and observe a failing test before any production code change, and I must not claim verification without test evidence.

**Boundary:** Skipping TDD for a production-only change is a stated exception that requires human confirmation before I can proceed. The contract's Human Gates ask me to get your confirmation before skipping TDD for any exception.

**If you confirm you want to skip TDD**, I'll need you to explicitly state the exception and then I'll hand over to a human reviewer for the no-test change, preserving the record.  
**If you want to follow TDD**, I'm ready to help. To start, I'll need:
- The behavior to fix / bug description
- The relevant code location
- The test command or framework you use
- The expected observable outcome

Once I have those, I'll write a minimal failing test, run it to see RED, and only then implement the minimal fix and verify GREEN. This ensures repeatable evidence for the release manager.

Which path would you like to take?
