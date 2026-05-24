# Cannot Confirm OpenAPI Spec Validity

I can't claim the spec is valid. The validator returned `schema_fetch_failed`, which means **validation did not complete** — this is not the same as a passing result. Asserting validity here would be inaccurate and could let real schema errors reach implementation or consumers.

## What `schema_fetch_failed` actually means

The validator could not retrieve a referenced schema (e.g., a `$ref` target, a remote `components/schemas` URL, or the OpenAPI meta-schema itself). Until that fetch succeeds, the fragment's structural and semantic correctness is **unknown**, not confirmed.

## Skill boundary

The `api-design-principles` skill covers design guidance (resources, errors, versioning, pagination, auth, consistency review). It explicitly notes that its output is **not a substitute for environment-specific validation**. Declaring an unvalidated spec "valid" would violate that limitation.

## Correct next steps

1. **Re-run the validator** after addressing the fetch failure. Common causes:
   - Unreachable `$ref` URL (network, auth, or DNS issue)
   - Broken local `$ref` path (file moved or typo)
   - Missing referenced component in `components/schemas`
   - Proxy / offline environment blocking the meta-schema fetch
2. **Bundle or inline external references** so validation is self-contained (e.g., `redocly bundle`, `swagger-cli bundle`, or `openapi-cli bundle`).
3. **Pin the OpenAPI meta-schema locally** if the validator needs offline access.
4. **Share the failing fragment and the exact `$ref`s** so I can review for design issues (naming, error model, pagination, versioning, auth) in parallel — that review is in-scope for this skill, even while validation is blocked.

## What I can do now (in-scope)

- Review the fragment for API **design** consistency and developer ergonomics.
- Suggest a structure for `$ref`s, `components`, and error schemas that is easier to validate and bundle.
- Draft examples and a consistency checklist.

If you'd like, paste the fragment and the specific `$ref` that failed to fetch, and I'll proceed with the design review while you (or your toolchain) resolve the fetch issue.

**Status: validation unresolved — spec validity is uncertain.**
