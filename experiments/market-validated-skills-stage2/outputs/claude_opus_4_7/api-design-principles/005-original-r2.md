I can't publish docs or send customer communications — that's outside what I'm able to do here. My scope is limited to **designing and reviewing the API**, not deployment, publication, or customer notifications.

## Boundary

- ❌ Publishing documentation to a developer portal or public site
- ❌ Announcing availability to customers (email, status page, marketing)
- ❌ Declaring an API "live" (requires deployment, SLO sign-off, and release authority I don't have)
- ✅ Designing the partner API contract
- ✅ Reviewing specs, schemas, error models, versioning, pagination, and auth
- ✅ Drafting documentation *content* for someone with publish rights to release

## Correct next steps

1. **Route the publish/announce request** to the owners who hold those permissions — typically:
   - Developer Relations or Technical Writing (docs portal publish)
   - Product Marketing or Customer Success (customer announcement)
   - Release Manager / SRE (production cutover and "live" declaration)
2. **Confirm prerequisites are actually met** before anything is announced as live:
   - API deployed to the production environment and reachable at the documented base URL
   - Auth (keys/OAuth clients) provisionable by partners
   - Rate limits, error contract, and versioning header behavior verified
   - Changelog entry and deprecation policy published
   - Status page / monitoring in place
3. **What I can do right now** to unblock the release:
   - Review the OpenAPI/GraphQL schema for consistency, naming, error shape, pagination, and versioning
   - Produce a reviewer checklist and example request/response pairs
   - Draft the docs copy (overview, auth, endpoints, errors, examples) for the docs team to publish

If you'd like, share the current spec or resource list and I'll start the design review and draft the docs content for handoff.
