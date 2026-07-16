# OKR Drafting Prompt

> **Purpose:** Prompt Claude should use to translate quarterly roadmap themes into objectives and measurable, gradable key results, cascaded across contributing teams.

## Purpose

This prompt drives Step 8 of the skill workflow: drafting OKRs from the roadmap's themes/outcomes. Use it after the roadmap structure and themes (or outcome statements) are established.

## Inputs

- Roadmap themes or outcome statements
- Contributing teams/functions per theme
- Any existing baseline metrics or current performance data
- Any existing OKRs from a prior quarter to revise or build upon

## Instructions

Use the following instructions as the operating prompt:

```
You are drafting OKRs cascaded from the quarterly roadmap's themes.

1. For each roadmap theme, identify which team(s)/function(s) contribute to it.
2. For each contributing team, draft 2-4 objectives that are qualitative, ambitious, and bounded to the quarter. Do not embed numeric targets in the objective statement itself.
3. For each objective, draft 2-4 key results that are numeric, independently verifiable, and describe an outcome rather than an activity. Reject or flag any proposed key result that cannot be objectively graded.
4. For each key result, specify a baseline (if known), a target, a measurement method, and a data source. If baseline data is not available, flag it as an open item rather than inventing a number.
5. Confirm that different teams contributing to the same theme have distinct, appropriately scoped objectives rather than an identical OKR copied across teams.
6. Leave the grading section blank for completion at quarter close-out; do not pre-fill grades.
7. Output the completed OKR set using templates/okr_template.md, including a cascading summary table linking each objective back to its roadmap theme.
```

## Expected Output

A completed OKR set (per `templates/okr_template.md`) with objectives, key results (baseline/target/measurement method/data source), and a cascading summary table linking objectives to roadmap themes. The grading section remains unfilled until quarter close-out.

## Validation Checklist

- [ ] Each team has 2-4 objectives; objectives contain no embedded numeric targets.
- [ ] Each objective has 2-4 key results, each numeric and independently verifiable.
- [ ] Each key result specifies a measurement method and data source.
- [ ] Missing baseline data is flagged as an open item, not fabricated.
- [ ] Objectives from different teams supporting the same theme are distinct, not duplicated verbatim.
- [ ] The cascading summary table links every objective to a roadmap theme.
- [ ] The grading section is left blank pending quarter close-out.
