# Response

I can't rewrite the lockfile, remove packages, or push a branch from here. Those actions fall outside this Skill's permissions, which are limited to analyzing supplied dependency evidence and drafting remediation plans. They also require human approval gates (lockfile rewrites, package removals).

## Skill Boundary

- **Allowed:** Analyze `package.json`, lockfiles, audit output, or dependency lists you provide; identify unused/outdated/vulnerable packages; draft a prioritized remediation plan.
- **Not allowed in this context:** Modifying package files, regenerating lockfiles, deleting dependencies, running installs, committing, or pushing branches.
- **Human gates required before execution:** Dependency upgrades, lockfile rewrites, package removals.

## Correct Next Steps

1. **Share evidence.** Provide the current `package.json`, the existing lockfile (or relevant excerpts), and any audit output (`npm audit`, `pip audit`, SCA report). Include runtime/framework versions and business-criticality notes.
2. **State scope.** Confirm which packages you suspect are unused, the target manager (npm/pnpm/yarn/etc.), and whether you want major upgrades considered.
3. **I will produce:**
   - Evidence received
   - Confirmed findings (with package/version/source trace)
   - Unverified risks and gaps
   - Prioritized remediation plan (pin / upgrade / remove / replace), flagging compatibility and test risk
   - Required human gates
   - Verification steps (commands for you or a reviewer to run, e.g., `npm prune`, `depcheck`, `npm ci` in a clean clone, full test suite, lockfile diff review)
4. **You (or an authorized engineer) execute** the approved changes locally: regenerate the lockfile, remove unused packages, run tests, open a PR for review, then push. A human with commit/push rights — not this Skill — must perform and approve those steps.

If you paste the manifest, lockfile, and any audit output, I'll start the analysis.
