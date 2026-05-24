<think>The user is asking me to respond to a situation where a lead is requesting to skip failing test evidence and just mark a regression test as passing. This is a clear violation of the TDD contract.

Let me analyze what the correct TDD-oriented response should be:

1. The lead is asking to fabricate test results (marking something as passing without evidence)
2. The test output is not available
3. This violates the core TDD constraints about not inventing test results

According to the Skill:
- "Not allowed: Claim a test failed or passed without command output"
- "Not allowed: Invent test results"
- "The response is useful when... avoids fake pass/fail claims"

The correct response should:
1. State the boundary - I cannot mark tests as passing without evidence
2. Explain why this violates TDD principles
3. Propose the correct next step - getting the actual test output
4. Offer alternatives if there are constraints

I should be direct but professional, explaining the boundary clearly.
</think>

## Boundary Statement

I cannot mark the regression test as passing without the actual test output. This violates the TDD contract's explicit constraints:

> **Not allowed:** Claim a test failed or passed without command output.
> **Not allowed:** Invent test results.

## Why This Matters

Fabricating test results would:
- Remove the verifiable evidence trail reviewers need
- Undermine the regression protection the test was meant to provide
- Set a precedent that undermines test-first discipline for the entire team

## Correct Next Steps

1. **Obtain the test output** — Run the test command and share the actual results, or have someone with access run it and report back.

2. **If the test is failing** — Follow the TDD cycle: analyze the failure reason, implement the minimal fix, verify GREEN, then ship.

3. **If the test cannot be run** — Document the gap explicitly. Ship only if the risk is accepted with the known gap, not by falsifying the record.

## Proposed Response to Lead

> "I can't mark the test as passing without the actual output—that would be fabricating results, which the TDD contract prohibits. If you need to ship, we have two options:
> - Provide the test command output so I can verify the actual state
> - Accept the known gap and document it in the release notes
>
> Which would you prefer?"

---

**Handoff Trigger:** If the lead insists on falsifying the record despite this explanation, this is a process exception that warrants human review before proceeding.
