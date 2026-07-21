# Risk Assessment Prompt

> **Purpose:** Prompt Claude should use to build or update a RAID-style risk register for a quarterly roadmap, including critical path re-evaluation and cross-functional dependency mapping.

## Purpose

This prompt drives Step 9 of the skill workflow (and supports mid-quarter revision in Step 12): assessing risks, assumptions, issues, and dependencies against the roadmap and milestone plan. Use it after the milestone plan exists, and re-run it at the mid-quarter review or whenever new information emerges.

## Inputs

- The quarterly roadmap and milestone plan
- Any known risks, assumptions, or issues already raised by the user
- Known cross-functional dependencies
- Any prior RAID log to update rather than rebuild

## Instructions

Use the following instructions as the operating prompt:

```
You are building or updating a RAID-style risk register for this quarterly roadmap.

1. Review the roadmap and milestone plan. Identify risks (potential future problems), assumptions (unproven beliefs the plan relies on), issues (problems that have already occurred), and dependencies (cross-team handoffs), per references/risk_and_dependency_management.md.
2. For each risk, assign likelihood, impact, an accountable owner role, a mitigation plan, and a contingency plan.
3. For each assumption, assign a confidence level, an owner role, note what is affected if the assumption proves false, and a validation plan.
4. For each issue, assign an owner role, describe the impact, and set a resolution plan with a target resolution date.
5. For each dependency, name the upstream owner, the downstream owner, and a required-by date; state whether it sits on the critical path.
6. Re-evaluate the critical path: list the current ordered sequence of milestones that determines the roadmap's minimum completion time, and identify which milestones have float instead.
7. If this is a mid-quarter update, clearly separate newly identified items from previously logged items, and note any items that have closed since the last review.
8. Output the completed register using templates/risk_register_template.md.
```

## Expected Output

A completed or updated RAID log (per `templates/risk_register_template.md`) with risks, assumptions, issues, and dependencies each assigned a single accountable owner, plus a current critical path summary and a review log entry.

## Validation Checklist

- [ ] Every risk has likelihood, impact, an owner role, a mitigation plan, and a contingency plan.
- [ ] Every assumption has a confidence level, an owner role, and a validation plan.
- [ ] Every issue has an owner role, an impact description, and a resolution plan with a target date.
- [ ] Every dependency names an upstream owner, downstream owner, and required-by date.
- [ ] The critical path is explicitly listed and distinguished from items with float.
- [ ] No risk, assumption, issue, or dependency is left without a single accountable owner.
- [ ] If updating an existing log, new items and closed items are clearly distinguished from prior entries.
