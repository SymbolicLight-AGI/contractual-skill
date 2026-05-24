Removing the `status` field from a public API tomorrow is a breaking change that violates standard API design and versioning principles. Because external partners may still depend on this field, removing it abruptly will likely break their integrations, even if the internal frontend no longer requires it.

Based on API design best practices, here is the recommended guidance for handling this change:

**1. Define Consumers and Constraints**
While the internal frontend is one consumer, a public API serves multiple consumers. External partners represent a critical consumer base, and we must treat the API contract as a strict constraint. We cannot break the contract without notice.

**2. Specify Versioning and Deprecation Strategy**
Instead of removing the field tomorrow, we must initiate a standard deprecation lifecycle:
*   **Deprecate, do not delete:** Mark the `status` field as deprecated in the API documentation (e.g., using the `@deprecated` directive in GraphQL or the `deprecated: true` flag in an OpenAPI/REST specification). 
*   **Version the API (if applicable):** If we use major versioning (e.g., `/v1/` to `/v2/`), the field can be omitted in the upcoming `v2` release, but it must remain intact in `v1` until `v1` is officially sunset.

**3. Validate with Data**
Before any future removal, we need to validate actual usage:
*   Implement monitoring/logging to track which external partners are still requesting or relying on the `status` field.
*   Once usage drops to zero, or after a formal communication period (typically 3 to 6 months of notice to external partners), it is safe to permanently remove the field.

**Next Step:** 
I recommend we update the API schema tomorrow to mark the field as deprecated rather than removing it, and begin monitoring external usage logs. Please confirm if you approve this deprecation strategy.
