I can't publish docs or send customer communications — that's outside what I'm permitted to do here. My scope is limited to **designing and reviewing the API** (resources, errors, versioning, pagination, auth, examples, and consistency checks).

## Boundary
- ❌ Publishing documentation to a developer portal or public site
- ❌ Announcing availability to customers (email, status page, marketing)
- ❌ Confirming "live" status — I have no visibility into deployment, staging, or production readiness

## Correct next steps

1. **Confirm readiness before any announcement.** "Live" requires:
   - Deployed and smoke-tested in production
   - Auth, rate limits, and error contracts verified against the spec
   - SLAs, support channels, and changelog in place
   - Sign-off from engineering, security, and product

2. **Route the publish/announce work to the right owners:**
   - Docs publishing → Developer Experience / Technical Writing team
   - Customer announcement → Product Marketing / Customer Success
   - Deployment verification → Platform / SRE team

3. **What I *can* do right now** (just ask):
   - Review the partner API spec for consistency, naming, errors, versioning, pagination, and auth
   - Produce a pre-launch design checklist you can run against before publishing
   - Draft reference examples and a changelog entry for the docs team to publish
   - Flag breaking-change risks or backward-compatibility issues

If you'd like, share the current spec or OpenAPI/GraphQL schema and I'll run a design review against it.
