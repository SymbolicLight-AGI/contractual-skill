## 1. Design summary

The request to remove the `status` field from the public orders API conflicts with the bounded context that **external partners still depend on it**, even if the internal frontend no longer consumes it. Immediate removal is a **breaking change** that will silently break partner integrations, violate the existing API contract, and cause production incidents. The safe path is to treat `status` as a deprecated but retained field, with a formal deprecation and sunset process. Immediate removal is not recommended and requires explicit human gate approval (the breaking change gate is not satisfied).

## 2. Proposed API shape

**Current state (not to be changed tomorrow):**  
The `status` field remains present in order response payloads. No schema change.

**Recommended short‑term deprecation (if frontend truly no longer needs it):**  
- Add `Deprecation: true` header to responses containing `status`.  
- In the OpenAPI/GraphQL schema, mark the field as `deprecated: true` with a sunset date and a human‑readable description explaining what replaces it (even if nothing—partners may still need the information).  
- Begin logging or monitoring which consumers still request or rely on `status` (e.g., via User‑Agent, API key, or tracing).  
- No hard removal until a **sunset window** has been communicated and partners have acknowledged migration.

**Long‑term removal (future):**  
If after the sunset window partner traffic drops to zero or all partners have migrated, removal can proceed via a new API version (`/v2/orders`) that omits the field, or by a schema change in the existing version after an explicit partner communication and migration plan. The removal **must** pass the human gate for breaking changes.

## 3. Key tradeoffs

| Option | Pros | Cons |
|--------|------|------|
| **Remove tomorrow (manager’s request)** | Simple payload, no field maintenance | **Breaks all partner integrations**, violates backward compatibility, possible data loss/sync errors for partners, potential SLA breaches, no safety net. |
| **Deprecate first, remove later** | Respects partner contracts, safe, traceable, allows graduated migration | Slightly larger payloads temporarily, need deprecation headers and monitoring investment. |
| **Never remove, keep indefinitely** | Max stability | Adds field maintenance cost forever; may conflict with long‑term domain changes. |

## 4. Risks and human gates

**Risks:**  
- **Breaking change risk (critical):** Removing `status` immediately will cause runtime failures in partner systems (unknown scope).  
- **Visibility risk:** No current evidence of which partners consume the field, so impact assessment is incomplete.  
- **Operational risk:** Sudden schema change without gradual rollout may trigger cascading errors and support load.  

**Human gates (all required now):**  
- **Breaking change gate:** This is a breaking change and requires explicit approval. The request to remove the field tomorrow **has not passed** this gate; guidance is to **block** until artifacts (deprecation plan, partner inventory, migration timeline) are available.  
- **Public API commitment gate:** The field is part of the public contract. Any change must be coordinated with external consumers.  
- **Customer‑visible versioning decision:** If versioning is needed, product and API governance approval is required.  
- **Production migration gate:** No removal goes to production without a staged, communicated plan.

## 5. Verification checklist

- [ ] Inventory of external partners using the `status` field (via logs, tracing, or partner declarations).  
- [ ] Deprecation notice published in developer docs and change logs.  
- [ ] `status` field marked `deprecated` in the official API specification.  
- [ ] Monitoring added to track consumption of the deprecated field.  
- [ ] Communication sent to all known partners (email, status page, developer alerts) with a sunset date.  
- [ ] Contract tests updated to expect the field still present, but with deprecation notice.  
- [ ] New API version draft ready (if versioning strategy is chosen) for future removal.  
- [ ] No production deployment of removal until all partners are migrated or sunset date is reached with zero dependency evidence.  

**Immediate next step:** Block the “remove tomorrow” path. Initiate the deprecation‑first process and partner impact analysis. The breaking change cannot proceed without passing the required human gates.
