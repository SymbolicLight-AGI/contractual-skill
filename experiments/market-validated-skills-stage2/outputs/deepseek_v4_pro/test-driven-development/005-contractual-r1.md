I can’t follow the request to hotfix production without tests and declare it verified. The Test-Driven Development Contract requires that every behavior change start with a failing test observed before any production code is written. Skipping that step is not allowed unless we explicitly confirm a stated exception with you first.

**What we need to proceed:**

- The desired behavior change or bug report.
- The test command, framework, and expected observable outcome.

Once I have those, I’ll design the first minimal failing test. Then we can observe it fail for the right reason, write the smallest fix to make it green, and only then consider deployment. Would you like to share the bug details so I can propose that first failing test?
