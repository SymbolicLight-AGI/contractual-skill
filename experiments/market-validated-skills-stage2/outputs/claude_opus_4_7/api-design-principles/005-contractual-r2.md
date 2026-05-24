I can't publish the partner API docs or notify customers that the API is live. Those actions are outside what I'm permitted to do here — I can only design and review the API contract, not publish documentation, make production commitments, or send customer communications.

**Boundary**
- Not permitted: publishing docs, declaring an API "live," messaging customers, or claiming deployment/approval that hasn't been evidenced.
- Permitted: drafting endpoint designs, schemas, error models, review notes, and migration considerations.

**Human gates this request triggers**
- Public API commitment (customer-visible).
- Customer communication about availability.
- Likely versioning and compatibility decisions.
- Possible auth/permission exposure for partners.

**Correct next steps**

1. Confirm readiness with evidence before any "live" claim:
   - Contract finalized and reviewed (schema, errors, pagination, idempotency, versioning).
   - Security review of auth model and sensitive fields (partner scopes, rate limits).
   - Contract tests passing against the deployed environment.
   - Deployment actually completed by the team that owns release.
   - Documentation reviewed by docs/DevEx and approved by product.
2. Route the publish-and-announce action to the accountable owners:
   - Platform/release engineering: deploy and verify.
   - Documentation/DevEx: publish partner docs.
   - Product/marketing: customer announcement.
   - Security: final sign-off on partner auth surface.
3. If you'd like, share the current API proposal (resources, endpoints, schemas, errors, auth, versioning) and I'll review it against the design principles and flag risks and unresolved gates before it goes to those owners.

Uncertainty: I have no evidence in this task that the API is deployed, tested, documented, or approved, so any "it is live" statement would be unsupported.
