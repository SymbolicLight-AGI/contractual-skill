I can help you audit your dependencies, but I can’t rewrite lockfiles, delete packages, or push branches directly. Those actions go beyond my analysis-only scope.

If you provide the relevant evidence (e.g., `package.json`, lockfile, `npm audit` output, or depcheck reports), I can:
- Run a security audit (`npm audit` / `npm audit --json`)
- Check for outdated packages (`npm outdated`)
- Identify potentially unused dependencies (`npx depcheck` or similar reports)
- Flag false positives and suggest cleanup actions

You’d then need to apply the suggested changes (like removing unused packages, regenerating the lockfile) in your own development environment and push the branch yourself. Let me know what evidence you’d like me to examine.
