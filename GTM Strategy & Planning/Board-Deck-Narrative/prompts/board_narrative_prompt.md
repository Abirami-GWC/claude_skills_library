# Board Narrative Drafting Prompt

**Purpose of this file:** Provide the drafting prompt used to generate a fuller board narrative (board memo or presentation outline) using the context-conflict-resolution arc and board-reporting norms.

## Purpose

Use this prompt when the requested output is a board memo or presentation outline (multi-section narrative), as opposed to a single one-page summary or a narrow decision brief. It applies strategic narrative design and board-reporting norms to shape the full story, using `templates/board_memo_template.md` and/or `templates/presentation_outline_template.md`.

## Inputs

- Source strategy, plan, performance, budget, or roadmap material
- Context on the board's cadence and any prior commitments or decisions being followed up on
- The situation type (steady progress, course correction, underperformance, pivot, investment ask)
- Any explicit ask(s) to be included, labeled by decision type (For Decision / For Information / For Discussion)
- Stated length or slide-count constraints

## Instructions

```
You are drafting a board narrative (memo or presentation outline) from the source material provided.

1. Determine the situation type: steady progress, course correction, underperformance, pivot, or investment ask. This determines the narrative arc to use (see references/strategic_narrative_design.md).
2. Read all supplied source material. Identify: prior commitments or decisions to reference, current performance, strategic priorities, risks, and any explicit ask.
3. Classify each piece of content as For Information, For Decision, or For Discussion (see references/board_reporting.md). Do not blend a decision ask into general narrative text — call it out distinctly.
4. Build the narrative using the context-conflict-resolution arc appropriate to the situation type:
   - State context briefly (a few sentences).
   - Name the central tension or challenge honestly — do not omit or soften it, especially for underperformance or pivot narratives.
   - Present the resolution: action taken, results achieved, or recommendation being made.
5. Select metrics per references/business_metrics.md — no more than 5-7, each with trend and comparison point, anchored around a north star metric if one is identifiable.
6. Compress underlying initiatives into no more than 5 strategic priorities, grouped by outcome/theme.
7. State risks in business-impact terms with mitigation, per references/board_reporting.md.
8. If there is an explicit ask, structure it using references/decision_frameworks.md: recommendation, alternatives considered (including status quo), rationale, risk-adjusted framing, and cost of inaction.
9. Populate templates/board_memo_template.md (for a memo) or templates/presentation_outline_template.md (for a slide outline), or both if requested.
10. Apply "so what" framing to every fact and metric, and BLUF discipline at the top of the document (see references/executive_communication.md and references/strategic_narrative_design.md).
11. Note any missing data, contradictory inputs, or assumptions explicitly rather than filling gaps silently.
12. If the underlying request is actually to originate strategy, model a budget, or build a detailed roadmap, stop and flag this as out of scope, and describe what input is needed from the appropriate upstream skill instead.
```

## Expected Output

A completed board memo and/or presentation outline, with:
- Clear labeling of For Information / For Decision / For Discussion content
- A narrative built on the context-conflict-resolution arc matching the situation type
- A curated metrics set with trend and comparison
- Up to 5 strategic priorities tied to outcomes
- Risks stated with business impact and mitigation
- Any explicit ask structured with options, recommendation, rationale, and risk-adjusted framing
- Noted data gaps or assumptions

## Validation Checklist

- [ ] Situation type identified and correct narrative arc applied
- [ ] Content clearly labeled For Information / For Decision / For Discussion where relevant
- [ ] Central tension or challenge named honestly, not softened or omitted
- [ ] Metrics limited to 5-7 with trend and comparison point
- [ ] Strategic priorities limited to 5, grouped by outcome
- [ ] Risks include business impact and mitigation
- [ ] Any ask includes alternatives, recommendation, rationale, and risk-adjusted framing
- [ ] Prior board commitments referenced if relevant
- [ ] Data gaps and assumptions explicitly noted
- [ ] Output respects stated length/slide constraints
