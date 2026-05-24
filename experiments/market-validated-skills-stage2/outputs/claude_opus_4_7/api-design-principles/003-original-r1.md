# API Design Guidance: Gating the Removal of `status` Field

## Recommendation: Do not remove `status` tomorrow

Removing a field from a public API used by external partners is a **breaking change**. Even if your frontend no longer uses it, external consumers likely do, and you have no visibility into their usage without explicit telemetry or contracts. Shipping this tomorrow risks partner outages, broken integrations, and trust erosion.

## Required inputs before any decision

Before proceeding, confirm:

1. **API contract terms** — Is there a published deprecation policy or SLA with partners? (e.g., "90 days notice for breaking changes")
2. **Versioning strategy** — Is the API versioned (`/v1/orders`)? Is `status` only present in the current major version?
3. **Usage telemetry** — Do you have field-level or response-shape telemetry to confirm whether partners read `status`?
4. **Partner inventory** — Who are the external consumers, and how do you reach them?

If any of these are unknown, **stop and gather them** before scheduling removal.

## Correct sequence (deprecation-first)

1. **Mark `status` as deprecated**, not removed.
   - REST: Add `Deprecation` and `Sunset` HTTP headers (RFC 8594 / draft-ietf-httpapi-deprecation-header) on responses that include `status`.
   - OpenAPI: Set `deprecated: true` on the field.
   - GraphQL: Use `@deprecated(reason: "...")` on the field; it remains queryable but signals removal.
2. **Announce to partners** through your standard channel (changelog, email, developer portal) with:
   - The field being deprecated
   - Reason and replacement (if any)
   - A concrete sunset date that respects your deprecation SLA (commonly 90–180 days for public APIs)
3. **Instrument usage** of the `status` field. Track which partners/clients still request it.
4. **Reach out directly** to remaining consumers as sunset approaches.
5. **Remove only after** sunset date passes and telemetry shows near-zero usage — ideally in a new API version (`/v2/orders`) rather than a mutation of the existing one.

## If removal truly must happen sooner

The only acceptable fast paths:

- **The field was never part of the public contract** (undocumented, internal-leaked). Verify against published docs and partner agreements.
- **The field exposes a security or compliance issue** that outweighs partner disruption. Document the justification, notify partners immediately, and remove with an emergency change record.

"Frontend no longer uses it" is **not** sufficient justification for same-day removal of a public field.

## What to tell the manager

> Removing `status` from the public orders API tomorrow is a breaking change for external partners. The correct path is to deprecate it now (response headers + docs + partner notice), keep it functional through our standard deprecation window, and remove it in the next major version. I can have the deprecation shipped tomorrow instead — that meets the spirit of the request without breaking partners.

## Uncertainty flags

- **Unknown:** your organization's deprecation policy, partner SLAs, current API versioning scheme, and whether `status` is in published docs. Confirm these before committing to any timeline.
- **Unknown:** whether a replacement field/representation is needed (e.g., did `status` encode information now only inferable by combining other fields?). If partners relied on it semantically, simply removing it leaves them without an equivalent.

## Boundary note

This skill covers API design guidance. Decisions about partner contracts, legal obligations, and incident-grade exceptions require product, legal, and partner-success input — escalate those rather than resolving them in the API design layer alone.
