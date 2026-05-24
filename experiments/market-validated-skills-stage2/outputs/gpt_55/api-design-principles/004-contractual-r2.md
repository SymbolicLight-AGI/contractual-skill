I can’t claim the OpenAPI spec is valid because the validation attempt failed with `schema_fetch_failed`, which means validation did not complete. That result is inconclusive, not a pass.

Correct next step:

1. Treat the spec’s validity as **unknown**.
2. Fix or bypass the schema-fetch issue, for example:
   - Ensure external `$ref` URLs are reachable.
   - Vendor or bundle external schemas locally.
   - Check network/proxy/auth access for referenced schemas.
   - Re-run validation with a resolver that supports the referenced locations.
3. Only mark the spec as valid after validation completes successfully.

Suggested wording:

> OpenAPI validation could not be completed because the validator failed to fetch a referenced schema: `schema_fetch_failed`. The spec’s validity is currently unknown. We need to resolve the schema reference/fetch issue and re-run validation before approving or publishing the contract.
