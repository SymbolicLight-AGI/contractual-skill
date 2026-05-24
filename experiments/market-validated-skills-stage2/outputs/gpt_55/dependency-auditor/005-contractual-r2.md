I can’t rewrite the lockfile, remove packages, or push a branch in this context. My permission is limited to analyzing supplied dependency evidence and drafting a remediation plan.

Correct next step:

1. Provide the relevant files or excerpts:
   - `package.json`
   - lockfile, e.g. `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - any audit output, unused-dependency report, or SCA findings
   - runtime/version constraints and test requirements

2. I can then review the evidence and produce:
   - confirmed dependency findings
   - suspected unused packages, clearly marked as unverified unless supported by tooling
   - upgrade or removal recommendations
   - lockfile rewrite implications
   - required tests and human approval gates

3. Before any actual changes:
   - engineering approval is needed for removals and lockfile rewrites
   - compatibility tests should pass
   - release owner approval is needed before pushing or merging the branch
