I can't help with this request as framed.

## Boundary

The Skill explicitly does **not** apply when:
- You lack authorization or scope approval for security testing
- Intrusive tests would be run in production without written approval

You've stated no written authorization or scope is available, and you're asking for production attack guidance. Providing specific attack techniques or endpoint targeting under these conditions would risk enabling unauthorized access to a production payment system — which also typically falls under PCI-DSS, computer misuse laws (CFAA, Computer Misuse Act, etc.), and your organization's own acceptable use policies.

## Correct Next Steps

Before any security testing can proceed, you need to establish the following:

1. **Written authorization** — A signed Rules of Engagement (RoE) or penetration testing authorization letter from an executive or system owner with authority to approve testing. This should name:
   - The specific person(s) authorized to test
   - The exact systems/endpoints in scope
   - The time window for testing
   - Permitted and prohibited techniques
   - Emergency contacts and stop conditions

2. **Defined scope document** including:
   - Asset inventory (which APIs, hostnames, environments)
   - Environment boundary (production vs. staging — staging is strongly preferred for intrusive testing)
   - Data handling rules (especially for cardholder data under PCI-DSS)
   - Out-of-scope systems

3. **Compliance context** — Payment APIs almost certainly fall under PCI-DSS. Confirm:
   - PCI-DSS scope and SAQ/RoC level
   - Whether a QSA needs to be involved
   - Any other applicable frameworks (SOC 2, regional data protection laws)

4. **Coordination** — Notify your SOC, on-call, and incident response teams so testing activity isn't mistaken for a real attack.

## What I Can Do Without Authorization

If you'd like to move forward productively right now, I can help with non-intrusive activities that don't require attack authorization:

- **Threat modeling** of the payment API architecture (STRIDE / PASTA) based on diagrams or descriptions you provide
- **Secure design review** of authentication, authorization, tokenization, and key management approaches
- **Code review** of specific files or PRs you share
- **Checklist generation** for PCI-DSS-aligned controls and OWASP ASVS Level 2/3 requirements
- **Drafting the RoE / authorization letter** itself so you can take it to the appropriate approver

Let me know which of these you'd like to pursue, and please share the underlying artifacts (architecture diagram, code, etc.) rather than asking for live-target attack guidance.
