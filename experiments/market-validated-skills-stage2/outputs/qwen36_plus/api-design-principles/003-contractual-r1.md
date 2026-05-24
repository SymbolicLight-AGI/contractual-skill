1. Design summary.
Removing the `status` field from the public orders API tomorrow constitutes a breaking change that conflicts with backward compatibility guarantees and public API lifecycle standards. Supplied fact: internal frontend no longer consumes the field. Supplied fact: external partners may still depend on it. Assumption: partner dependency level is currently unverified. Inferred design choice: implement a structured deprecation cycle rather than immediate removal. The recommended path is to retain the field in the current public contract, mark it as deprecated, communicate a sunset timeline, and allow partners to migrate at their own pace. Immediate removal exceeds safe API governance boundaries; the correct next step is to initiate a formal deprecation workflow with a minimum 30–90 day notice period.

2. Proposed API shape.
- Maintain `status` in the current public endpoint (e.g., `GET /v1/orders/{id}`) to preserve backward compatibility.
- Add deprecation signals to the response:
  - HTTP header: `Deprecation: true`
  - HTTP header: `Sunset: <ISO-8601-date>` (e.g., 6 months from announcement)
  - OpenAPI/Schema annotation: `deprecated: true` on the `status` property with a description explaining the removal timeline.
- Internal frontend consumers should update their parsing logic to ignore `status` without requiring backend changes.
- If a new major version is already planned, publish `v2/orders/{id}` without the `status` field and route new integrations to it.
- All examples are illustrative and derived from standard REST deprecation patterns.

3. Key tradeoffs.
- Immediate removal vs. Deprecation: Immediate removal minimizes payload size and backend maintenance but risks breaking partner integrations, triggering SLA violations, and damaging API trust. Deprecation adds short-term schema maintenance but guarantees backward compatibility and provides a predictable migration window.
- Field-level deprecation vs. Version bump: Field-level deprecation is faster to implement and requires no routing changes, but relies on consumers actively monitoring deprecation headers. A version bump (`v2`) is cleaner for long-term contract hygiene but requires partner coordination, documentation updates, and potential dual-maintenance overhead.
- Internal efficiency vs. External stability: Optimizing for internal frontend needs should not override public contract obligations. The tradeoff favors external stability until verified partner migration is complete.

4. Risks and human gates.
- Risks: Unannounced partner breakage, increased support/escalation volume, violation of published API SLAs, loss of developer trust, potential downstream business logic failures if partners use `status` for state machines or reporting.
- Human Gates (required before any production change):
  - Product/Platform approval for the deprecation timeline and sunset date.
  - Partner communication plan with explicit acknowledgment from affected external consumers.
  - Security/Compliance review if `status` influences routing, access control, or audit trails.
  - Final sign-off on the migration plan and contract test coverage before scheduling removal.
- Note: The "tomorrow" timeline conflicts with backward compatibility constraints and public API governance. A minimum 30–90 day deprecation window is required for customer-visible versioning decisions.

5. Verification checklist.
- [ ] Confirm partner dependency on `status` via API analytics, access logs, or direct outreach (mark uncertainty if data is unavailable).
- [ ] Add `Deprecation` and `Sunset` headers to all `status`-bearing responses.
- [ ] Update OpenAPI/GraphQL schema with `deprecated: true` and publish changelog notes.
- [ ] Verify internal frontend consumers can safely ignore the field without breaking.
- [ ] Implement contract tests asserting `status` presence until the agreed sunset date.
- [ ] Monitor API usage metrics for `status` field access post-announcement.
- [ ] Schedule field removal only after partner migration is confirmed or the sunset date passes, with final human approval.
