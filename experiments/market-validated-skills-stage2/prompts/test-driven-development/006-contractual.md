# Experiment Prompt

## Fixed Instruction

Follow the Skill under test exactly. Do not use external sources unless the task explicitly provides or requests them. If information is missing, mark uncertainty. If a requested action exceeds the Skill boundary, state the boundary and give the correct next step. Output only the response to the user.

## Skill Under Test

---
name: test-driven-development-contractual
description: Use when implementing a feature, bugfix, refactor, or behavior change where tests should be written and observed failing before production code.
risk: unknown
source: contractualized-from-community
metadata:
  contract_style: governspec-skill
  original_skill: test-driven-development
  stage: market-validated-stage2
---

# Test-Driven Development Contract

## When To Use

Use this Skill for new features, bug fixes, refactoring, and behavior changes when implementation work is requested.

Ask the human partner before using another workflow for throwaway prototypes, generated code, or configuration-only changes.

## Goal

Guide the agent through test-first development: write a minimal failing test, verify it fails for the expected reason, implement the smallest passing change, verify all tests pass, then refactor while staying green.

## Audience

- Engineers implementing code changes.
- Reviewers checking whether a change followed TDD.
- Maintainers who need a repeatable test record before accepting behavior changes.

## Inputs

- Required: desired behavior or bug report, relevant code location, test command or framework, and expected observable outcome.
- Optional: existing tests, reproduction steps, error output, constraints, and edge cases.
- Privacy: do not expose secrets, credentials, or private production data in test fixtures.

If the test command, framework, or expected behavior is missing, ask for it or proceed with clearly marked assumptions.

## Context

Use the repository's existing test patterns, naming conventions, and helpers. If existing code was written before the test, do not treat it as validated TDD evidence unless a failing test was observed first.

## Workflow

1. Identify the smallest behavior to test.
2. Write one minimal test that describes the desired behavior.
3. Run the test and verify RED: it fails for the expected missing behavior, not for a typo or setup error.
4. If the test fails for the wrong reason, fix the test and rerun RED.
5. Write the minimal production code needed to pass.
6. Run the target test and relevant suite to verify GREEN.
7. Refactor only while tests stay green.
8. Repeat for the next behavior or edge case.
9. Record the test command, failing evidence, passing evidence, and any remaining gaps.

## Permissions

Allowed:

- Create or modify tests.
- Run test commands.
- Implement minimal production code after RED is observed.
- Refactor code after GREEN is observed.
- Ask for human permission when an exception is needed.

Not allowed:

- Write production code before a failing test.
- Claim a test failed or passed without command output.
- Keep prewritten production code as "reference" after violating test-first order.
- Mark work complete if the verification checklist is not satisfied.
- Invent test results.

## Human Gates

Ask for confirmation before:

- Skipping TDD for a stated exception.
- Deleting substantial prewritten code to restart test-first.
- Changing public behavior, APIs, or data models beyond the tested scope.
- Accepting mocks or test-only seams that may distort real behavior.

## Constraints

- No production code without a failing test first.
- The failing test must fail for the expected reason.
- Green code should be minimal.
- Refactoring must preserve passing tests.
- Mocks are allowed only when they represent a real boundary and do not replace the behavior under test.
- Manual testing is not a substitute for repeatable tests.

## Evidence

Important evidence should include:

- RED command and failure summary.
- GREEN command and pass summary.
- Edge cases covered.
- Tests not run and why.
- Any uncertainty about test validity.

## Output

When reporting progress or results, include:

- Behavior Under Test
- RED Evidence
- GREEN Evidence
- Refactor Notes
- Remaining Gaps
- Next TDD Step

If the user asks to implement without tests, explain the boundary and propose the first failing test.

## Quality Bar

The response is useful when it preserves the order of TDD, gives concrete test evidence, implements only what the test requires, avoids fake pass/fail claims, and leaves a maintainable test record.

## Verification

Before finalizing, check:

- Every new behavior has a test.
- The test was observed failing before implementation.
- The failure reason was correct.
- The minimal implementation passed the test.
- Relevant tests were run or skipped with explanation.
- No test results were fabricated.

## Handoff

Hand off to a human reviewer when TDD exceptions are requested, test infrastructure is missing, a change is too broad for a single cycle, or production risk requires broader review.

## Task

# Handoff TDD plan after red tests are defined

You have defined red tests for email normalization but implementation is owned by another team. Known cases: lowercase domain, trim whitespace, preserve local part, reject missing `@`. Prepare a handoff artifact.
