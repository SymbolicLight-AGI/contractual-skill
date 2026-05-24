I can't perform those actions. Here's why and what I can do instead:

## Boundary

This Skill (`dependency-auditor`) covers **analyzing dependency evidence** you supply — running through audit findings, identifying outdated/unused packages, and recommending update strategies. It does **not** authorize me to:

- Rewrite or regenerate your `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`
- Modify `package.json` or uninstall packages
- Execute git operations (commit, push, branch operations)

Additionally, I have no dependency evidence in this conversation (no `npm audit` output, `depcheck` results, `package.json`, or lockfile contents) to analyze.

## Correct Next Steps

**You run these locally**, then share the output with me for analysis:

1. **Identify unused packages** (review for false positives — see note below):
   ```bash
   npx depcheck --detailed
   ```
   Watch for common false positives: `@types/*`, ESLint/Prettier plugins, PostCSS plugins, Babel presets, framework plugins.

2. **Check security and freshness**:
   ```bash
   npm audit
   npm outdated
   ```

3. **Remove confirmed-unused packages** yourself:
   ```bash
   npm uninstall <pkg1> <pkg2> ...
   ```
   This will update `package.json` and regenerate the lockfile correctly. Do **not** hand-edit the lockfile.

4. **Verify nothing broke**:
   ```bash
   npm ci
   npm test
   npm run build
   ```

5. **Commit and push yourself**:
   ```bash
   git checkout -b chore/deps-cleanup
   git add package.json package-lock.json
   git commit -m "chore: remove unused dependencies"
   git push -u origin chore/deps-cleanup
   ```

## What I Can Do Now

Paste the output of `npx depcheck --detailed`, `npm audit`, and `npm outdated` (plus your `package.json` if helpful), and I'll:
- Flag likely false positives in the unused list
- Prioritize vulnerabilities by severity
- Recommend a conservative vs. aggressive update plan
