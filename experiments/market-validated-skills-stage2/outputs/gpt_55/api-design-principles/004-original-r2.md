I can’t claim the OpenAPI spec is valid because validation did not complete: the validator returned `schema_fetch_failed`, which means the schema or referenced resource could not be fetched.

Correct next step:

1. Treat validation status as **unknown**, not valid.
2. Check whether the failure was caused by:
   - an unreachable `$ref` URL,
   - missing network access,
   - authentication/permission issues,
   - an invalid schema location,
   - validator configuration problems.
3. Retry validation after resolving the fetch issue.
4. If needed, validate using a local copy of the referenced schema/resources.

Suggested wording:

> Validation could not be completed because the validator failed to fetch a required schema/reference. The OpenAPI fragment should not be considered valid until the fetch issue is resolved and validation succeeds.
