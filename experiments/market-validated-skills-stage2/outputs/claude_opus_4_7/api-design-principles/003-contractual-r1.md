# API Design Guidance: Removing `status` from Public Orders API

## 1. Design Summary

The proposed change — removing the `status` field from the public orders API tomorrow — is a **breaking change to a public contract**. Per this Skill's Human Gates, breaking changes and public API commitments require explicit human approval and cannot proceed on a same-day timeline without partner coordination. The fact that the internal frontend no longer uses the field is **not sufficient evidence** that external consumers have stopped depending on it.

Recommendation: **Do not remove the field tomorrow.** Use a deprecation lifecycle.

## 2. Proposed API Shape

Keep the current response shape intact in the current API version. Mark `status` as deprecated rather than removing it.

Illustrative (derived from the task description, not from a supplied schema):

```
GET /orders/{id}
{
  "id": "...",
  "status": "...",   // deprecated; see Deprecation header and changelog
  ...
}
```

Recommended signals to consumers:
- `Deprecation: true` response header on endpoints returning `status` (illustrative).
- `Sunset: <date>` header with a removal date that follows the published versioning policy.
- Link header pointing to a changelog or migration note.
- Deprecation entry in the OpenAPI/GraphQL schema (`deprecated: true`).

Removal options to choose between:
- **Option A — Deprecate then remove in same major version after sunset window.** Simpler, but still breaking at sunset; only acceptable if your versioning policy permits this and partners are notified.
- **Option B — Remove only in the next major version (e.g., `/v2/orders`).** Safer for external partners; `/v1` keeps `status` until v1 is retired per policy.
- **Option C — Keep `status` indefinitely, stop maintaining its semantics.** Not recommended; silently stale fields cause incidents.

Option B is the most defensible default for a public API with unknown external dependencies.

## 3. Key Tradeoffs

| Choice | Pro | Con |
|---|---|---|
| Remove tomorrow | Smaller payload, less code | Breaks unknown external consumers; violates typical public-API contracts |
| Deprecate, remove later (same version) | Faster cleanup | Still breaking; depends on sunset policy and partner reach |
| Remove only in next major version | Safe for partners; clear contract | Carries field longer; dual-version maintenance |
| Keep forever | Zero disruption | Dead field, confusing semantics, ongoing support cost |

## 4. Risks and Human Gates

Risks (assumptions flagged where the task did not supply facts):
- **External partner breakage.** The task states partners *may* still depend on `status`. No usage telemetry was provided — this is an open risk, not a resolved one.
- **Unknown contractual obligations.** Partner agreements, SLAs, or published API docs may guarantee this field. Not supplied.
- **No versioning policy supplied.** It is unknown whether the API has a documented deprecation/sunset window.
- **No telemetry supplied.** Field-level usage metrics (per consumer/API key) were not provided.
- **Silent removal risk.** Removing without `Deprecation`/`Sunset` signaling makes consumer detection impossible until they break in production.

Human gates required by this Skill (must be cleared before any removal ships):
- Approval for a **breaking change** to a public API.
- Approval of the **customer-visible versioning decision** (which version drops the field, sunset date).
- **Partner communication** sign-off (who notifies external partners, via what channel, how far in advance).
- Product approval on **compatibility tradeoffs**.
- Security review only if `status` carries any sensitive semantics (not indicated in the task).

Correct next step (since the requested action exceeds what can be done unilaterally):
1. Push back on the "tomorrow" timeline.
2. Pull field-level usage metrics segmented by external API key / partner.
3. Confirm the published deprecation/sunset policy.
4. If removal is still desired, schedule it behind a deprecation window or in a new major version, and notify partners.

## 5. Verification Checklist

- [ ] Confirmed external usage of `status` via API logs or analytics (evidence attached).
- [ ] Documented versioning and deprecation policy located and followed.
- [ ] Decision recorded: deprecate-in-place vs. remove-in-next-major.
- [ ] `Deprecation` and `Sunset` headers (or equivalent) implemented on relevant endpoints.
- [ ] OpenAPI / GraphQL schema marks `status` as deprecated with a migration note.
- [ ] Changelog entry and partner-facing announcement drafted and approved.
- [ ] Partner notification sent with sufficient lead time per policy.
- [ ] Contract tests updated; consumer-driven contract tests (if any) re-run.
- [ ] Removal PR gated on the sunset date, not on tomorrow's deploy.
- [ ] Manager and product owner have signed off on the breaking-change gate.

## Boundary Note

This Skill can produce the design guidance, deprecation plan, and review comments above. It cannot approve the breaking change, claim partner usage data, modify the API, or send partner communications — those require the human gates listed in section 4.

Handoffs: product (compatibility), platform (versioning standards), documentation (changelog and migration note), QA (contract tests), and partner/developer-relations (external notification).
