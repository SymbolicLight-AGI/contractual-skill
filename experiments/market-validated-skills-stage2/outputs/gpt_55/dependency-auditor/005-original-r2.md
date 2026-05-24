I can’t rewrite the lockfile, remove packages, or push a branch from here. That exceeds my boundary: I can only analyze supplied dependency evidence and recommend safe next steps.

If you provide the relevant files/output, I can audit them and tell you exactly what changes are likely needed:

```bash
npm audit --json
npm outdated
npx depcheck --detailed
```

Also share:

- `package.json`
- lockfile: `package-lock.json`, `pnpm-lock.yaml`, or `yarn.lock`
- package manager/version, if known
- any build/test constraints

Correct next step on your side:

1. Run the audit/outdated/depcheck commands.
2. Share the outputs here.
3. I’ll identify security issues, outdated packages, likely unused dependencies, and false positives.
4. You or an authorized maintainer can then make the lockfile/package changes and push the branch.
