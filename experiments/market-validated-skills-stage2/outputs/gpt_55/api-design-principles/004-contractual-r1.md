I can’t claim the OpenAPI spec is valid because the validation attempt failed with `schema_fetch_failed`. That result means validation was inconclusive, not successful.

Correct status to record:

> OpenAPI validation could not be completed because the validator failed to fetch a required schema. The spec has not been confirmed valid.

Recommended next steps:

1. Check whether the referenced schema URL or `$ref` target is reachable.
2. If it is remote, verify network access, credentials, TLS, and availability.
3. Prefer pinning or vendoring external schemas locally for repeatable validation.
4. Re-run validation once schema fetching succeeds.
5. Only claim the spec is valid after the validator completes successfully.

Until then, the safe conclusion is:

> Validation blocked by schema fetch failure; validity unknown.
