# Executive Summary Drafting Prompt

**Purpose of this file:** Provide the drafting prompt used to generate a one-page executive summary or one-page strategy view from supplied source material, applying pyramid-principle and BLUF discipline.

## Purpose

Use this prompt when the requested output is a one-page executive summary or one-page strategy view (as opposed to a full memo, decision brief, or slide outline). It compresses supplied strategy, metrics, and context into board-ready form using `templates/executive_summary_template.md`.

## Inputs

- Source strategy, plan, or performance material (as much or as little as the user has supplied)
- Any known metrics, targets, or benchmarks
- The specific audience and occasion (board meeting, exec review, investor update)
- Any stated length or format constraint
- Any explicit ask the user wants surfaced

## Instructions

```
You are drafting a one-page executive summary from the source material provided.

1. Read all supplied source material fully. Identify: the core situation, any explicit or implicit ask, available metrics, strategic priorities, and known risks.
2. Note explicitly anything that is missing (e.g., no metrics supplied, no clear ask stated, contradictory figures). Do not fabricate specifics to fill gaps — mark them clearly instead (e.g., "[METRIC NOT PROVIDED]").
3. Draft a single BLUF sentence that states the situation and, if applicable, the ask. This must be the first line of the summary.
4. Write a brief (2-3 sentence) business context section — only what is necessary to understand the situation, not a full history.
5. Select no more than 5-7 metrics that matter most to this narrative. For each, include current value, trend, and a target or benchmark if available. If fewer than 3 credible metrics are available, note this as a gap rather than padding with weak or tangential figures.
6. Compress the underlying strategy or roadmap into no more than 5 strategic priorities, each stated as an outcome, not a task list. Group related initiatives under shared themes if there are more than 5 in the source material.
7. State market opportunity in 1-2 sentences if relevant to the narrative.
8. List key risks (no more than 3), each with a stated business impact and mitigation if known.
9. State next steps or the specific ask clearly in the final section.
10. Populate templates/executive_summary_template.md with this content. Keep the entire result to one page.
11. Apply the pyramid principle and BLUF discipline throughout (see references/executive_communication.md) and "so what" framing to every metric or fact (see references/strategic_narrative_design.md).
12. If the user's request is actually asking you to originate the strategy, build the budget, or construct the roadmap itself rather than summarize existing material, stop and flag this as out of scope for this skill.
```

## Expected Output

A completed one-page executive summary following `templates/executive_summary_template.md`, with:
- A single clear BLUF statement at the top
- Brief business context
- 5-7 metrics with trend and comparison point
- Up to 5 strategic priorities tied to outcomes
- Market opportunity framing
- Up to 3 risks with business impact and mitigation
- A clearly stated ask or next steps
- Any data gaps or assumptions noted at the bottom

## Validation Checklist

- [ ] BLUF sentence appears first and states situation plus ask (if any)
- [ ] Business context is brief (2-3 sentences max)
- [ ] No more than 7 metrics shown, each with trend and comparison point
- [ ] No more than 5 strategic priorities, each an outcome not a task
- [ ] Risks include business impact and mitigation where known
- [ ] Ask or next steps stated explicitly, not implied
- [ ] Missing data is flagged, not fabricated
- [ ] Output fits on one page
- [ ] Request did not require redirecting to an upstream strategy/budget/roadmap skill
