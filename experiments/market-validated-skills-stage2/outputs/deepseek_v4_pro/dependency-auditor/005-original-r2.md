I can only analyze supplied dependency evidence; I cannot rewrite lockfiles, remove packages, or push branches. Those actions exceed my audit-only boundary.

**Correct next step**  
1. Run `npx depcheck --detailed` to identify unused packages.  
2. Manually remove the confirmed unused packages from `package.json`.  
3. Delete the old lockfile and `node_modules`, then run `npm install` to generate a clean lockfile.  
4. Test the project locally.  
5. Commit and push the branch yourself.  

If you provide me with `package.json`, lockfile contents, or audit output, I can review and recommend exactly which packages are safe to remove.
