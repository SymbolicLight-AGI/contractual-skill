# API Design Guidance: Gating the Removal of `status` from Public Orders API

## Recommendation: Do not remove `status` tomorrow

Removing a field from a **public** API on a one-day timeline is a breaking change that violates standard API versioning and deprecation principles, regardless of internal frontend usage. External partners are part of the consumer set, and their contracts must be honored.

## Step 1 — Define consumers and constraints

- **Internal frontend**: confirmed no longer using `status`.
- **External partners**: usage unknown — this is the critical gap. Removal without evidence of non-use will break partner integrations.
- **Constraint**: Public API ⇒ stability is part of the contract.

**Action**: Before any removal decision, instrument the endpoint to measure actual `status` field consumption (request logs, field-selection telemetry, or partner survey). Mark this as **required input** — without it, the removal cannot be safely scheduled.

## Step 2 — Apply the breaking-change gate

A field removal is a breaking change. It should pass through:

1. **Deprecation announcement** — mark `status` deprecated in the spec/docs (OpenAPI `deprecated: true`, response header `Deprecation: true`, optional `Sunset` header with a target date).
2. **Communication** — notify partners via changelog, email, and developer portal. Industry norm: **6–12 months** notice for public APIs; minimum 90 days for low-traffic fields with confirmed low usage.
3. **Telemetry window** — measure usage during the deprecation period; only proceed when usage drops to acceptable threshold (often zero for partner APIs).
4. **Versioning** — if removal is urgent, introduce a new version (`/v2/orders`) that omits `status`, and keep `/v1/orders` intact until sunset.

## Step 3 — Suggested response to the manager

> "Removing `status` tomorrow would break any external partner relying on it, and we don't yet have evidence they don't. I recommend we instead:
> 1. Mark `status` as deprecated in the response (header + docs) **this week**.
> 2. Turn on usage telemetry for the field.
> 3. Announce a sunset date to partners — minimum 90 days, ideally aligned with our standard deprecation policy.
> 4. Remove the field after the sunset date, or sooner only if telemetry confirms zero external usage.
>
> If we need the field gone faster for an internal reason (cost, security, data correctness), tell me the driver — that may justify a `/v2` cutover or an emergency sunset, but it still shouldn't be a same-day public removal."

## Step 4 — Validate with examples

**Deprecation response (during transition):**
```http
HTTP/1.1 200 OK
Deprecation: true
Sunset: Wed, 27 May 2026 23:59:59 GMT
Link: <https://api.example.com/docs/deprecations#orders-status>; rel="deprecation"
Content-Type: application/json

{
  "id": "ord_123",
  "status": "shipped",          // deprecated — use `state` or remove from clients
  "state": "shipped",
  ...
}
```

**OpenAPI fragment:**
```yaml
Order:
  properties:
    status:
      type: string
      deprecated: true
      description: "Deprecated 2026-02-27, sunset 2026-05-27. Use `state`."
```

## Consistency review checklist

- [ ] Deprecation documented in changelog and OpenAPI/GraphQL schema.
- [ ] Partners notified through committed channel (email, portal).
- [ ] Telemetry confirms zero/acceptable usage before removal.
- [ ] Sunset date respected; removal lands in a versioned or clearly communicated release.
- [ ] Internal frontend already migrated off `status` (confirmed).

## Uncertainty / missing inputs

- **External partner usage of `status`** — unknown; must be measured or surveyed.
- **Team's existing deprecation policy / SLA with partners** — not provided; recommendations above use common industry defaults.
- **Reason for the one-day timeline** — not provided; if there's a security or data-integrity driver, the plan changes (still versioned, but accelerated with direct partner outreach).

## Boundary note

This skill covers API design guidance (versioning, deprecation, contract design). It does not cover executing the change, modifying production systems, or contacting partners on your behalf — those are next steps for the implementing team after the deprecation plan is approved.
