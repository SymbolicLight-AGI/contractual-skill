1. Design summary.
The request to remove the `status` field from the public orders API tomorrow exceeds the API governance boundary for backward compatibility and public contract stability. Immediate removal of a field from a public API without a deprecation window violates standard API design principles and risks breaking external partner integrations. The correct next step is to initiate a structured deprecation cycle: retain the field in the current public contract, mark it as deprecated, communicate a sunset timeline, and only remove it after partner migration and usage verification.

2. Proposed API shape.
- **Current Contract (`v1/orders/{id}`)**: Retain `status` in the response schema. Add deprecation metadata to signal upcoming removal.
- **Deprecation Headers (Illustrative)**:
  `Deprecation: true`
  `Sunset: <ISO-8601-date>`
  `Link: <migration-guide-url>; rel="deprecation"`
- **Schema Annotation (OpenAPI/JSON Schema)**: Mark `status` with `deprecated: true` and add a description explaining the sunset date and replacement (if any).
- **Future State**: After the sunset date and confirmed zero partner usage, remove `status` from `v1` or introduce `v2/orders/{id}` without the field. Internal services can ignore the field immediately via internal DTO mapping.

3. Key tradeoffs.
- **Immediate removal vs. Deprecation cycle**: Immediate removal minimizes payload size and internal maintenance but breaks backward compatibility, triggers partner failures, and damages API trust. Deprecation adds short-term overhead but preserves contract stability and provides a predictable migration path.
- **Field-level deprecation vs. Major version bump**: Field-level deprecation keeps consumers on the same base URL and requires only schema/header updates. A major version (`v2`) cleanly isolates the change but forces consumers to update integration endpoints and authentication scopes, increasing migration friction.
- **Assumption/Uncertainty**: It is supplied that the frontend no longer uses `status`. It is uncertain whether external partners actively consume it; this must be verified via API gateway logs and partner registry data before finalizing the sunset date.

4. Risks and human gates.
- **Risks**: Unannounced partner integration failures, SLA breaches, increased support volume, contractual penalties, and loss of developer trust. Removing a field without observability into partner usage creates blind spots for impact assessment.
- **Human Gates (Required before any removal)**:
  - Product/Platform approval for breaking change policy and minimum deprecation window (typically 30–90 days for public APIs).
  - Partner/Developer Relations sign-off on communication plan, impact assessment, and migration documentation.
  - Legal/Compliance review if `status` relates to audit trails, data retention, or partner SLAs.
  - Explicit approval of the sunset date and post-sunset removal plan.
  - *Note*: The "tomorrow" timeline cannot be approved under standard API governance. A minimum deprecation period is required.

5. Verification checklist.
- [ ] Query API gateway/analytics to confirm or refute external partner usage of `status`.
- [ ] Add `Deprecation` and `Sunset` headers to all `v1/orders` responses containing the field.
- [ ] Update OpenAPI/contract documentation to mark `status` as deprecated with clear migration guidance.
- [ ] Notify all registered API consumers via developer portal, email, and changelog.
- [ ] Implement contract tests to assert `status` remains present and correctly formatted until the sunset date.
- [ ] Monitor error rates, 4xx/5xx spikes, and partner support tickets post-announcement.
- [ ] Schedule field removal only after the sunset date passes and usage metrics confirm zero external consumption.
