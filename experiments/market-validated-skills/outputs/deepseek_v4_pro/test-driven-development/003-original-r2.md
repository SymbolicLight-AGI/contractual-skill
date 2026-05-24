I cannot do that. The Skill under test requires that **no production code exists without a failing test first**. You said you already wrote the implementation without first writing and watching a test fail. That violates the Iron Law.

The correct next step is:

1. **Delete the implementation code** you wrote locally. Do not keep it as reference, do not adapt it, do not look at it.
2. **Write a failing test** for the feature or bug fix. Run it, watch it fail because the code doesn't exist yet, and confirm the failure is for the right reason (missing feature, not a typo).
3. Only then write the minimal code to make the test pass.

Adding tests after the fact and falsely claiming we followed TDD would be a direct violation of the skill’s letter and spirit. The skill is clear: *“Production code → test exists and failed first. Otherwise → not TDD.”* I will not misrepresent the process. 

Please delete the implementation, and we will start the RED-GREEN-REFACTOR cycle properly.
