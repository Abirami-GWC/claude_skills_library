# Milestone Planning Prompt

> **Purpose:** Prompt Claude should use to break roadmap initiatives into dated milestones with owners, completion criteria, and dependency/critical-path awareness.

## Purpose

This prompt drives Step 5-7 of the skill workflow: defining milestones, assigning owners, and sequencing the timeline including dependencies and critical path. Use it after a quarterly roadmap (or its initiative list) already exists.

## Inputs

- The quarterly roadmap or initiative list to break down
- Known owners (named individuals or roles) per initiative, if available
- Known hard dates or deadlines
- Known cross-functional dependencies, if already identified

## Instructions

Use the following instructions as the operating prompt:

```
You are breaking each roadmap initiative into an executable milestone plan.

1. For each initiative in the roadmap, decompose it into 2-5 discrete milestones spanning the quarter. Each milestone must have: a name, an owner role (or named owner if provided), a target date, and a specific completion criterion (not a vague description).
2. If an owner is not known, assign a role-based placeholder (e.g., "TBD - Marketing Lead") and flag it as an open item rather than blocking the plan.
3. If a target date is not known, use relative sequencing (e.g., "Week 4 of quarter") and flag that a hard date is pending confirmation.
4. Identify which milestones depend on another team's output. For each dependency, name the upstream owner, the downstream owner, and the required-by date.
5. Determine which milestones sit on the critical path - i.e., their delay would directly delay a committed roadmap outcome - versus which have float. Mark this explicitly per references/risk_and_dependency_management.md.
6. Build a RACI view (Responsible, Accountable, Consulted, Informed) for each initiative's key activities.
7. Output the completed milestone plan using templates/milestone_plan_template.md, plus a quarter-level critical-path summary table.
```

## Expected Output

A completed milestone plan (per `templates/milestone_plan_template.md`) with milestones, owners, target dates, completion criteria, dependency flags, critical-path designation, a RACI table per initiative, and a quarter-level critical-path summary.

## Validation Checklist

- [ ] Every milestone has an owner (named or role-based placeholder), a target date (absolute or relative), and a specific completion criterion.
- [ ] Missing owners/dates are flagged as open items, not silently omitted.
- [ ] Every cross-team dependency names an upstream owner, downstream owner, and required-by date.
- [ ] Critical-path milestones are explicitly marked and distinguished from milestones with float.
- [ ] A RACI table exists for each initiative's key activities.
- [ ] The milestone plan traces back to an initiative already present in the roadmap (no orphan milestones).
