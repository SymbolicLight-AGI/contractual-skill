1. **Design summary**

Removing `status` from the public orders API tomorrow is a **breaking API change** and should not proceed without human approval and a compatibility plan.

The fact that the frontend no longer uses `status` is not sufficient justification to remove it from a **public API**, because external partners may still depend on it. Public API contracts must be managed based on all consumers, not only first-party frontend usage.

Recommended guidance: **do not remove `status` tomorrow**. Instead, deprecate it, communicate the change, measure external usage if possible, and remove it only in a future version or after an agreed migration window.

---

2. **Proposed API shape**

Current public response should remain compatible:

```json
{
  "id": "order_123",
  "status": "shipped",
  "created_at": "2026-05-24T10:00:00Z"
}
```

Recommended options:

### Option A: Keep `status` in the current API version

Maintain the existing contract:

```http
GET /orders/{order_id}
```

Response continues to include:

```json
{
  "status": "shipped"
}
```

If the field is no longer preferred, mark it as deprecated in API documentation:

```yaml
status:
  type: string
  deprecated: true
  description: Deprecated. Use the replacement field or endpoint if one exists.
```

Only do this if there is a clear replacement. If no replacement exists, do not deprecate until the future contract is defined.

---

### Option B: Remove `status` only in a new version

If the business decision is to remove the field, introduce a new public contract, for example:

```http
GET /v2/orders/{order_id}
```

Response:

```json
{
  "id": "order_123",
  "created_at": "2026-05-24T10:00:00Z"
}
```

Keep the existing version stable:

```http
GET /v1/orders/{order_id}
```

Response:

```json
{
  "id": "order_123",
  "status": "shipped",
  "created_at": "2026-05-24T10:00:00Z"
}
```

This avoids silently breaking existing integrations.

---

### Option C: Temporary compatibility behavior

If the field must stop being used internally, preserve the public schema while changing backend implementation, for example:

- Continue returning `status` with the last known valid value.
- Map it from another internal state field.
- Return a documented fallback only if semantically correct.

Do **not** return misleading or fake status values just to satisfy the schema.

---

3. **Key tradeoffs**

### Removing `status` tomorrow

**Pros**
- Simplifies the response schema.
- Aligns with current frontend usage.
- May reduce internal maintenance if the field is hard to compute.

**Cons**
- Breaks external partner integrations.
- Violates expectations of public API stability.
- Can cause runtime parsing failures, missing workflow state, or partner-side business logic errors.
- Creates support burden and trust issues.
- Requires approval for a breaking public API change.

This is not recommended without a formal migration plan.

---

### Keeping `status`

**Pros**
- Preserves backward compatibility.
- Avoids partner disruption.
- Gives time to collect usage data and communicate deprecation.
- Maintains public API trust.

**Cons**
- Keeps a field that the first-party frontend no longer needs.
- May require continued support of legacy semantics.

This is the safest default.

---

### Versioning the change

**Pros**
- Allows cleanup without breaking existing consumers.
- Gives partners an explicit migration path.
- Makes the contract change visible and reviewable.

**Cons**
- Requires maintaining multiple versions temporarily.
- Requires documentation, testing, and migration support.

This is appropriate if the field truly needs to be removed.

---

4. **Risks and human gates**

### Risks

- **Partner compatibility risk:** External partners may rely on `status` for order lifecycle handling.
- **Operational risk:** Removing the field may cause elevated API errors, support tickets, or failed partner workflows.
- **Contract risk:** Public API consumers may treat the response schema as stable.
- **Observability gap:** If field-level usage is not measured, we do not know who depends on it.
- **Documentation risk:** If docs still mention `status`, the API and documentation will diverge.
- **Semantic risk:** If `status` has no replacement, removing it may remove necessary business state from the API.

### Human gates required

This change requires approval before proceeding because it is:

- A **breaking public API change**.
- A **customer/partner-visible contract change**.
- Potentially a **versioning and migration decision**.

Required reviewers:

- Product owner for partner impact and migration timeline.
- API/platform owner for versioning and compatibility standards.
- Partner/integration team for external dependency review.
- Documentation owner for deprecation and migration guidance.
- QA for contract and regression coverage.
- Support/customer success if partners may need notification.

---

5. **Verification checklist**

Before any removal is approved:

- Confirm whether `status` is part of the documented public API contract.
- Identify all known consumers, including external partners.
- Check API logs, schema validation data, SDK usage, or partner feedback for dependency on `status`.
- Define whether there is a replacement field or endpoint.
- Decide whether the change requires a new API version.
- Publish deprecation notice if applicable.
- Provide a migration guide and timeline.
- Add or update contract tests for both old and new behavior.
- Validate documentation, SDKs, examples, and OpenAPI schemas.
- Monitor usage and errors after any staged rollout.
- Obtain explicit approval for the breaking change and migration plan.

**Recommendation:** Do not remove `status` from the existing public orders API tomorrow. Keep it for backward compatibility, mark it deprecated only if there is a replacement and approved timeline, and remove it only through a versioned or formally approved migration path.
