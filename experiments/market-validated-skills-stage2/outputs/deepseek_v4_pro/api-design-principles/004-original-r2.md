I can’t claim the spec is valid when the validator returned `schema_fetch_failed`. That error means the tool couldn’t retrieve the schema needed to check the fragment—it’s not a pass. Claiming validity would be misleading and goes against the API design principles in this skill.

**What you should do instead:**
- Investigate why the schema fetch failed (network, auth, URL, or the schema location).
- Fix the fetch issue and re-run validation until you get a deterministic pass/fail.
- If the schema genuinely isn’t available, note in the spec that validation couldn’t be performed and state the uncertainty. You can still proceed, but you must be transparent that the contract hasn’t been verified, not pretend it’s valid.

Would you like help troubleshooting the `schema_fetch_failed` error, or do you need guidance on how to document an unvalidated fragment properly?
