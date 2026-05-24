I can’t perform that request. This Skill is limited to analyzing supplied dependency evidence and recommending actions—it cannot modify lockfiles, remove packages, or push branches. Those changes require your direct action or a separate process with the appropriate permissions.

What I can do right now:
- Review the lockfile and dependency manifests you provide, highlight packages that appear unused (based on the evidence), and suggest safe removal targets.
- Recommend an upgrade/pinning plan, with compatibility testing steps.
- Prepare a prioritized list of changes for your review.

If you’d like that analysis, please supply:
- The package manifest(s) (e.g., `package.json`, `requirements.txt`)
- The current lockfile excerpt
- Any additional context (runtime, production vs dev, business criticality)

Then I’ll give you a risk-assessed plan that you can use to make the changes manually and push when ready.
