I can’t rewrite the lockfile, remove packages, or push a branch in this context. My permission is limited to analyzing supplied dependency evidence and recommending safe remediation steps.

Correct next step:

1. Provide the relevant dependency evidence:
   - `package.json`
   - lockfile excerpt or full lockfile
   - audit/SCA output if available
   - any known runtime or framework constraints

2. I can then:
   - identify direct vs transitive dependencies
   - flag confirmed audit findings from supplied reports
   - identify likely unused or risky dependencies as candidates for owner review
   - propose a prioritized remediation plan

3. Before any actual changes, human approval is required for:
   - lockfile rewrites
   - dependency removals
   - package upgrades
   - release blocking decisions
   - pushing branches or opening PRs

After approval, an authorized maintainer should perform the changes, run tests, review compatibility impact, and push the branch.
