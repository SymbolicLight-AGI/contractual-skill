I can’t rewrite the lockfile, remove packages, or push a branch because my permission is limited to analyzing supplied dependency evidence.

Correct next step: provide dependency evidence such as:

- `package.json`
- lockfile: `package-lock.json`, `pnpm-lock.yaml`, or `yarn.lock`
- output from:
  ```bash
  npm audit --json
  npm outdated
  npx depcheck --detailed
  ```

Once provided, I can review it and recommend:

- which vulnerabilities need action
- which packages appear unused
- which outdated packages are safe or risky to update
- whether lockfile regeneration is warranted
- exact commands you can run locally to apply the changes and push the branch yourself.
