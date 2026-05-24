# API Design Guidance: Breaking Change for `status` Field

## Problem Assessment

Removing the `status` field from a public API is a **breaking change** with significant implications:

| Consumer | Impact |
|----------|--------|
| Internal Frontend | ✅ Can remove usage (per manager) |
| External Partners | ❌ **Will break** existing integrations |
| Downstream Services | ⚠️ Likely depends on this field |

---

## Why Immediate Removal Is Problematic

1. **Breaking Change Contract**: Public APIs must maintain backward compatibility or follow a structured deprecation cycle
2. **Partner Dependencies**: External partners may parse, store, or react to the `status` field
3. **Trust & Reliability**: Sudden breaking changes damage developer trust and increase support burden
4. **Grace Period Requirement**: Industry standard is typically 6–12 months notice for breaking changes

---

## Recommended Approach: Deprecation Lifecycle

### Phase 1: Assessment & Communication (Now)

- [ ] **Audit usage**: Confirm which external partners use `status`
- [ ] **Notify partners**: Send advance notice of planned deprecation
- [ ] **Document timeline**: Establish removal date (minimum 90 days, recommend 6–12 months)

### Phase 2: Deprecation Warnings (Immediately)

```
# Add deprecation headers and/or field-level notice
X-API-Deprecation: "status field will be removed on [DATE]"
X-API-Deprecation-Replacement: "orderState or equivalent"
```

- [ ] Return the field with a deprecation flag
- [ ] Log warnings for consumers still using the field

### Phase 3: Versioning Strategy (Before Removal)

```
/v2/orders    ← NEW: Remove status field (if truly unused)
/v1/orders    ← MAINTAIN: Keep status until deprecation ends
```

- [ ] Introduce a new API version without the field
- [ ] Maintain current version with field until sunset date

### Phase 4: Final Removal

- [ ] Remove `status` from `v1` after sunset date
- [ ] Archive old version with documentation

---

## Key Principles Applied

| Principle | Application |
|-----------|-------------|
| **Consumer-First Design** | Partners depend on this field; their needs matter |
| **Change Management** | Breaking changes require versioning + deprecation |
| **Documentation** | Update API docs to reflect deprecation timeline |
| **Communication** | Proactive partner notification prevents friction |

---

## Response to Your Manager

> "I can plan the removal of `status` from the public orders API, but we should follow our deprecation process:
> 
> 1. **Immediately**: Add a deprecation header so partners know when to migrate
> 2. **Short-term**: Create a new API version without the field (if truly unused)
> 3. **Timeline**: Provide partners 6–12 months before removing from the current version
> 
> This approach protects external partnerships while meeting the frontend's needs."

---

## Next Steps

1. Identify which API version(s) expose `status`
2. Determine current partner usage (analytics, support tickets, agreements)
3. Draft deprecation notice for external partners
4. Create tracking ticket for sunset date

Would you like me to elaborate on any specific phase or provide template language for partner communication?
