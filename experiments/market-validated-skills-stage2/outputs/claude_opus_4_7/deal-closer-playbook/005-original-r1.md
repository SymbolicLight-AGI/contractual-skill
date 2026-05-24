I can't cite the last executive meeting notes. The CRM lookup returned `crm_unauthorized`, so I don't have access to that history, and fabricating notes or details from memory would violate a core rule of this playbook: do not manufacture information.

**Boundary**: This skill researches public company information via WebSearch and synthesizes deal context you provide. It does not have a path to retrieve your internal CRM records when authorization fails, and it will not invent meeting notes to fill the gap.

**Correct next steps:**

1. **Resolve the CRM access issue.** Confirm whether the `crm_unauthorized` error is a permissions problem (your account lacks access to this account record), an auth/session expiry, or an integration-level scope issue. Re-authenticate or request record access from your CRM admin or the deal owner.

2. **Get the notes another way in the meantime.** Ask the deal owner, AE, or champion-facing rep to paste the last executive meeting notes directly into our conversation. Once you provide the raw notes as text, I can incorporate them into the playbook.

3. **Flag the gap in the playbook.** When we proceed, the executive meeting summary, attendees, and stated priorities will be marked `[UNKNOWN - CRM access pending]` in the Buying Committee Map and MEDDIC sections until you supply the content.

If you want, paste the meeting notes here (or any summary you have from memory or email) and I'll fold them into the deal playbook.
