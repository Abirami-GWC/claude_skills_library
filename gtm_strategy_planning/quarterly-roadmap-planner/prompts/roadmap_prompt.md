# Roadmap Prompt

> **Purpose:** Prompt Claude should use to generate a quarterly roadmap from a GTM strategy or initiative list, applying the correct structuring approach and prioritization.

## Purpose

This prompt drives Step 3-4 of the skill workflow: prioritizing initiatives and structuring them into a quarterly roadmap. Use it once the user has provided (or the conversation contains) a strategy summary or initiative list and a planning horizon.

## Inputs

- GTM strategy summary, business objective, or initiative list
- Planning horizon (quarter or custom time-boxed period)
- Known constraints: team size/capacity, hard deadlines, existing commitments
- Known stakeholders/functions involved
- Any prioritization framework preference (optional — Claude selects if not specified)

## Instructions

Use the following instructions as the operating prompt:

```
You are building a quarterly roadmap from the strategy/initiatives provided.

1. List every candidate initiative mentioned or implied by the input. If the list seems incomplete, ask the user to confirm completeness before proceeding.
2. Select a prioritization framework (RICE, MoSCoW, Value vs. Effort, or Weighted Scoring) based on the decision context, per references/prioritization_frameworks.md. State which framework you chose and why in one or two sentences.
3. Apply the chosen framework to rank or categorize the initiatives. Show the scoring/categorization inputs transparently.
4. Select a roadmap structuring approach (theme-based, date-based, outcome-based, or a hybrid) per references/roadmap_framework.md, based on scope certainty, presence of hard deadlines, and audience. State which approach you chose and why.
5. Group the prioritized initiatives into the chosen structure using templates/quarterly_roadmap_template.md as the format.
6. Check the total initiative effort against stated team capacity (including reserved buffer). If the plan appears overcommitted, flag it explicitly and recommend deferral or de-scoping candidates rather than silently fitting everything in.
7. Do not fabricate company names, real dates, or real staff names not provided by the user — use role-based placeholders and flag open items.
8. Output the completed roadmap using the quarterly roadmap template structure.
```

## Expected Output

A completed quarterly roadmap (per `templates/quarterly_roadmap_template.md`) including: chosen structure with rationale, chosen prioritization framework with rationale and transparent scoring, themes/outcomes/dates as appropriate, a cross-functional timeline view, a dependency summary, a success metrics summary, and an overcommitment check.

## Validation Checklist

- [ ] Every initiative from the input appears in the prioritization step before appearing in the roadmap.
- [ ] The chosen prioritization framework is stated along with a brief rationale.
- [ ] The chosen roadmap structure is stated along with a brief rationale.
- [ ] No more than 3-5 top-level themes are used if a theme-based structure is chosen.
- [ ] Every roadmap row has an owner role, even if marked TBD.
- [ ] Cross-functional dependencies are listed explicitly with upstream/downstream owners and required-by dates.
- [ ] An overcommitment check has been performed and flagged if applicable.
- [ ] No fabricated company names, real personal names, or invented real-world facts appear in the output.
