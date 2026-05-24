# API Design Guidance: Removing a Breaking Field

**Critical Issue:** Removing `status` from the public API tomorrow is a **breaking change** that should **not** proceed without proper deprecation strategy.

---

## Why This Cannot Happen Tomorrow

External partners depend on `status`. Removing it will:
- Break their integrations immediately
- Violate API contract stability expectations
- Potentially cause production failures for partners

---

## Recommended Approach: Deprecation Lifecycle

### Phase 1: Immediate (Now)
| Action | Purpose |
|--------|---------|
| **Do NOT remove the field yet** | Preserve backward compatibility |
| Add `status` to `deprecated` metadata | Signal intent without breaking |
| Announce deprecation via: | |
| - API changelog | |
| - Direct partner communication | |
| - Versioned API headers | |

### Phase 2: Grace Period (Recommended: 3–6 months)
| Action | Purpose |
|--------|---------|
| Continue returning `status` | Maintain partner integrations |
| Add `X-API-Deprecated-Warnings` header | Notify consumers |
| Provide migration guidance | Help partners adapt |
| Consider adding `statusReason` or `orderState` as alternative | Future-proof the field concept |

### Phase 3: Sunset
| Action | Purpose |
|--------|---------|
| Release as new API version (e.g., `v2`) | Isolate breaking change |
| Maintain `v1` with `status` for defined period | Buffer for late adopters |
| Remove only after `v2` adoption is sufficient | Data-driven retirement |

---

## Communication Template to Manager

```
The requested change to remove `status` is a breaking change that cannot be 
implemented tomorrow due to external partner dependencies.

Proposed timeline:
- Day 1–30:   Mark field as deprecated, notify partners
- Month 1–6:  Maintain field with deprecation warnings
- Month 6+:   Remove in new API version, after partner migration verified

If urgency exists, please provide:
1. List of external partners with dependency timelines
2. Business justification for accelerated deprecation
3. Risk acceptance for breaking partner integrations
```

---

## Key Principle

**Public API changes require versioning and deprecation periods.** Never remove fields from public APIs without advance notice and migration windows.
