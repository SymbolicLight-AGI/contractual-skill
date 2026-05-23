# OpenSpec Explore Skill Contract Affordance

This is a deterministic offline check. It evaluates whether each Skill document contains explicit signals needed by the five explore-mode tasks. It does not measure live model behavior.

## Summary

| Variant | Mean score | Task rows |
| --- | ---: | ---: |
| original | 61.8 | 5 |
| contractual | 100.0 | 5 |

## Per Task

| Task | Variant | Score | Covered | Missing |
| --- | --- | ---: | --- | --- |
| 001 | original | 65 | explore_options;visualize;ask_clarifying;offer_capture;no_implementation |  |
| 002 | original | 65 | inspect_codebase;ground_claims;identify_risks;ask_clarifying;no_implementation |  |
| 003 | original | 65 | read_openspec_artifacts;offer_capture;distinguish_facts;identify_risks;no_auto_capture |  |
| 004 | original | 49 | no_implementation;handoff_next_step;no_auto_capture | human_gate |
| 005 | original | 65 | compare_tradeoffs;recommend_when_ready;identify_unknowns;ground_claims |  |
| 001 | contractual | 100 | explore_options;visualize;ask_clarifying;offer_capture;no_implementation |  |
| 002 | contractual | 100 | inspect_codebase;ground_claims;identify_risks;ask_clarifying;no_implementation |  |
| 003 | contractual | 100 | read_openspec_artifacts;offer_capture;distinguish_facts;identify_risks;no_auto_capture |  |
| 004 | contractual | 100 | no_implementation;human_gate;handoff_next_step;no_auto_capture |  |
| 005 | contractual | 100 | compare_tradeoffs;recommend_when_ready;identify_unknowns;ground_claims |  |
