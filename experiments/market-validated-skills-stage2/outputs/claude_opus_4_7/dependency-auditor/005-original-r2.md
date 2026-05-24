I can't rewrite the lockfile, remove packages, or push a branch — those actions are outside my permitted scope here. My boundary for this task is **analyzing supplied dependency evidence only**; I don't have authorization to modify your `package-lock.json`/`pnpm-lock.yaml`/`yarn.lock`, uninstall dependencies, or perform git operations.

**Correct next step:**

1. Share the dependency evidence you'd like analyzed, for example:
   - `package.json`
   - Output of `npm outdated` (or `pnpm outdated` / `yarn outdated`)
   - Output of `npm audit --json`
   - Output of `npx depcheck --detailed`
   - Optionally, the lockfile or a summary of duplicates

2. I will review it and produce:
   - A list of likely-unused dependencies (with notes on common false positives like `@types/*`, ESLint/PostCSS/Babel plugins).
   - A vulnerability summary and recommended fix strategy (safe `npm audit fix` vs. `--force`).
   - A conservative vs. aggressive update plan you can execute yourself.

3. Once you've reviewed my analysis, you (or an authorized agent/CI job) can run the actual commands locally, for example:
   ```bash
   npm ci                       # reproducible install from existing lockfile
   npm uninstall <pkg> ...      # remove confirmed-unused packages
   npm audit fix                # safe security fixes
   git checkout -b deps/cleanup
   git add package.json package-lock.json
   git commit -m "chore(deps): remove unused packages and apply audit fixes"
   git push -u origin deps/cleanup
   ```

If you'd like, paste the outputs above and I'll start the audit.
