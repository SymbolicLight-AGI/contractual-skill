I can't cite the last executive meeting notes. The CRM lookup returned `crm_unauthorized`, which means I don't have access to that history, and fabricating notes or guessing at their contents would be worse than useless — you'd walk into your next conversation with false context.

**Boundary**: This Skill builds playbooks from information you provide plus public web research. It does not have a fallback path to retrieve CRM data when authorization fails, and I won't invent meeting notes to fill the gap.

**Correct next steps:**

1. **Fix the access issue.** Check with your CRM admin or RevOps whether your credentials, scope, or integration token need to be refreshed. `crm_unauthorized` typically means an expired session, a missing permission on the account record, or a disconnected integration.

2. **In the meantime, get me the notes directly.** Paste the relevant executive meeting notes (or a summary) into the chat. Even rough bullets work — date, attendees, key topics, commitments made, objections raised, next steps agreed.

3. **Or proceed without that history** and I'll flag it explicitly in the playbook as `[UNKNOWN — CRM access failed]` under Previous Interactions, and recommend discovery actions to reconstruct the context in your next conversation with the champion.

Which path do you want to take?
