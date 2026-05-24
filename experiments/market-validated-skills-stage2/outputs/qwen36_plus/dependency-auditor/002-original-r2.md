**Uncertainty:** I cannot determine if your dependency tree is safe based solely on the package names `express`, `react`, and `axios`. Without specific versions, a lockfile, `package.json` context, or runtime environment details, I cannot verify security vulnerabilities, transitive dependency paths, or actual exposure risks.

**Boundary:** The `dependency-auditor` skill requires a concrete project context (lockfile, `package.json`, or raw audit output) to execute security audits, check for outdated packages, or identify unused dependencies. Auditing isolated package names without version constraints or a dependency tree exceeds this boundary.

**Correct Next Step:** To perform a valid audit, please provide your `package.json` and lockfile (`package-lock.json`, `yarn.lock`, or `pnpm-lock.yaml`), or run the following commands in your project root and share the output:
1. `npm audit --json` (security vulnerabilities)
2. `npm outdated` (package freshness)
3. `npx depcheck` (unused dependencies)

Once you provide the lockfile or command output, I will analyze it against the security, freshness, and cleanliness checklists and recommend a safe, version-specific update strategy.
