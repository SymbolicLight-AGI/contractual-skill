I cannot claim the specification is valid or proceed while the validator reports a `schema_fetch_failed` error.

**Boundary:** I do not override validation failures or assert contract validity when schema references cannot be resolved. Proceeding without a fully resolvable spec violates the requirement for explicit, testable API contracts.

**Correct Next Step:** 
1. Audit all `$ref` paths in the OpenAPI document to ensure they point to existing, accessible files or URLs.
2. Resolve missing files, incorrect paths, or network/permission restrictions blocking schema retrieval.
3. Re-run the validator. Once it passes, I can review the design for resource modeling, error semantics, pagination, and developer ergonomics.

**Risks & Human Gates:** 
- *Risk:* Ignoring unresolved references will generate invalid client SDKs, cause runtime contract mismatches, and break downstream integrations.
- *Human Gate:* Platform/Engineering lead must approve the resolved spec before it is committed to the public contract or used for SDK generation.

**Verification Checklist:**
- [ ] All `$ref` pointers resolve successfully in local and CI environments.
- [ ] Validator returns zero errors/warnings.
- [ ] Schema shapes are explicitly defined and match consumer expectations.
- [ ] Contract tests are drafted to validate request/response payloads against the resolved spec.
