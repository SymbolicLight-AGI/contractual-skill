# API Design Guidance: Removing `status` from Public Orders API

## 1. Design Summary

The proposed change — removing `status` from the public `orders` API tomorrow — is a **breaking change to a public contract**. Even though the internal frontend no longer uses the field, external partners may still depend on it. This change cannot proceed on the proposed timeline under standard API design principles and requires a **human gate** before any action.

## 2. Why This Is Blocked (Boundary Statement)

Per this Skill's Human Gates, the following all apply here and require explicit human approval:

- Breaking change to a public API.
- Public API commitment (removal of a previously published field).
- Customer-visible versioning decision.

Per Constraints, I cannot ignore backward compatibility. Per Permissions, I cannot claim the change is safe based on internal usage alone when external partners are in scope.

**Supplied facts:**
- The `status` field exists on the public orders API.
- Frontend no longer uses it.
- External partners *may* still depend on it (uncertainty acknowledged by the requester).
- Requested timeline: tomorrow.

**Unknown / missing inputs (flagged as uncertainty):**
- Current versioning policy for this API.
- Published deprecation policy and notice period commitments (SLAs, contracts, terms).
- Partner inventory and which partners consume `/orders`.
- Whether telemetry exists on field-level read access.
- Whether `status` is part of any documented schema or OpenAPI spec partners rely on.

## 3. Recommended Path (Deprecation, Not Removal)

Replace "remove tomorrow" with a staged deprecation. Illustrative outline:

**Stage A — Confirm impact (before any change)**
- Query access logs / field-level telemetry for `status` reads by partner credentials over a representative window.
- Cross-reference against partner contracts and published API docs.
- Identify replacement field(s) or derivations partners should migrate to, if any.

**Stage B — Announce deprecation**
- Mark `status` as deprecated in the OpenAPI/schema (e.g., `deprecated: true`, illustrative).
- Send partner notice with: reason, replacement, sunset date, migration examples.
- Add a `Deprecation` and `Sunset` response header on responses that include `status` (RFC 8594 / RFC 9745 style; illustrative).

**Stage C — Observe**
- Track `status` reads per partner; escalate to non-responsive partners.

**Stage D — Remove via version bump**
- Remove `status` only in a new API version (e.g., `/v2/orders` or a versioned media type), keeping the prior version available for the sunset window.
- Or, if single-version policy is in force, remove only after the announced sunset date with zero residual partner usage.

All field names, paths, and headers above are **illustrative**, since no existing conventions or versioning policy were supplied.

## 4. Key Tradeoffs

| Option | Pros | Cons |
|---|---|---|
| Remove tomorrow as requested | Fast cleanup; less schema surface | Breaks partners silently; reputational and contractual risk; violates standard compatibility norms |
| Deprecate + sunset in current version | No new version overhead | Partners may ignore notices; still breaking at sunset |
| Introduce new version, freeze old | Cleanest contract boundary | Maintenance cost of two versions during migration |
| Keep field, mark deprecated indefinitely | Zero breakage | Permanent schema debt; misleading if value becomes stale |

## 5. Risks and Human Gates

**Risks:**
- **Partner breakage:** Unknown blast radius without telemetry; could trigger incident reports, support load, or SLA violations.
- **Contractual / legal:** Partner agreements may guarantee notice periods.
- **Observability gap:** If `status` is also emitted in webhooks, events, or exports, removal there is a separate breaking surface not covered by the original ask.
- **Data semantics:** If `status` encodes lifecycle state not derivable from other fields, removal loses information for partners, not just a redundancy.

**Human gates required before proceeding:**
- Product owner approval for the public API change and sunset timeline.
- Partner/developer-relations approval for partner communication.
- Security and legal review if `status` is referenced in any partner agreement.
- Platform standards owner approval for the versioning approach.

## 6. Recommended Response to the Manager

Suggested message (illustrative): "Removing `status` tomorrow is a breaking change to a public contract. Frontend non-use doesn't establish partner non-use. I recommend we (1) pull field-level usage telemetry for `status` by partner, (2) announce deprecation with a sunset date per our deprecation policy, and (3) remove it only in a new API version or after the sunset window with zero usage. I can draft the deprecation notice and schema annotation once we confirm the policy and partner list."

## 7. Verification Checklist

- [ ] Field-level usage telemetry pulled and reviewed by partner.
- [ ] Deprecation policy / notice period confirmed against partner agreements.
- [ ] Schema marked `deprecated` with replacement guidance.
- [ ] `Deprecation` / `Sunset` headers (or equivalent per local conventions) added.
- [ ] Partner notice sent and acknowledgment tracked.
- [ ] Removal executed only in a new API version or after sunset with zero residual usage.
- [ ] Contract tests updated; consumer-driven contract tests reviewed.
- [ ] Webhooks, events, exports, and SDKs audited for the same field.
- [ ] Human approvals captured: product, partner/DevRel, security/legal, platform.

## Handoffs

- **Product / DevRel:** partner communication and sunset timeline.
- **Security / Legal:** contractual review of notice obligations.
- **Platform:** versioning approach and standards alignment.
- **QA:** contract test updates across versions.
- **Docs:** deprecation notice, migration guide, changelog entry.

**No code, schema, documentation, or partner communication has been changed or sent.** This is design guidance only.
