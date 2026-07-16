---
name: Board Deck Narrative
description: Condenses an existing GTM strategy, plan, or set of business inputs into an executive-ready board presentation narrative — including executive summary, strategic narrative, business context, key metrics, market opportunity, risks, strategic priorities, investment justification, and next steps. Use when the user needs to compress detailed strategy, planning, budget, or roadmap material into a concise board-level or executive-level story. Do not use this skill to originate GTM strategy, build budget models, or create a detailed quarterly roadmap from scratch — it consumes those outputs, it does not produce them.
---

# Board Deck Narrative

## Purpose

This skill turns already-developed GTM strategy, planning, budget, and roadmap material into a concise, board-ready or executive-ready narrative. It is a **compression and framing** capability: it takes detailed, often lengthy source material and reshapes it into the small set of artifacts a board or executive audience actually needs to make a decision — an executive summary, a strategic narrative, a one-page strategy view, a decision summary, and/or a presentation outline.

The skill does not invent strategy, does not model budgets, and does not build roadmaps. It assumes those exist (or that the user has enough raw input to summarize) and focuses entirely on **narrative construction, prioritization, and executive framing**.

## Business Value

- Saves executives and GTM leaders hours of manual slide/summary writing before board meetings.
- Reduces the risk of boards receiving unfocused, overly detailed, or poorly sequenced narratives.
- Improves decision velocity by structuring asks (budget, pivot approval, strategy sign-off) using recognizable board-decision patterns.
- Creates consistency across board cycles — the same rigor and structure every quarter, regardless of who wrote the underlying material.

## Activation Conditions

Invoke this skill when the user has (or references) underlying strategy, planning, performance, or budget content and wants it **condensed, reframed, or packaged** for a board, executive team, investor, or senior leadership audience.

Good signals this skill applies:
- The user has substantial source material (a strategy doc, plan, spreadsheet of metrics, roadmap) and wants a short, high-altitude version of it.
- The audience is explicitly a board, executive committee, investors, or senior leadership.
- The desired output is a summary, narrative, one-pager, decision brief, or presentation outline — not a full detailed plan.

## Trigger Examples

- "Turn this GTM plan into a board summary."
- "I need a one-page strategy narrative for our board meeting next week."
- "Summarize our Q3 performance and the pivot rationale for the executive team."
- "Draft the executive summary slide for the board deck based on this data."
- "We're asking the board to approve a 20% budget increase — help me write the narrative."
- "Condense this 40-page roadmap into 3 strategic priorities for leadership."
- "Write a decision brief for the board on whether to exit this segment."
- "Help me explain underperformance to the board without burying them in detail."

## When NOT To Use

This skill is strictly a **narrative condensation and framing** capability. Do not use it, and do not let it attempt, the following (these belong to other skills that this skill consumes as inputs):

- **Originating GTM strategy** (e.g., "build our go-to-market strategy from scratch," "figure out which segments to target") — that is the job of a GTM Strategy Builder skill. This skill only narrates a strategy that already exists or is supplied by the user.
- **Building budget models or financial allocation** (e.g., "model our marketing budget by channel," "calculate ROI scenarios") — that is the job of a Budget Allocator skill. This skill only references budget conclusions/asks that are handed to it.
- **Creating a detailed quarterly roadmap** (e.g., "build our Q3 roadmap with owners and dates") — that is the job of a Quarterly Roadmap Planner skill. This skill only compresses a roadmap's headline priorities into board-level language.
- Generating net-new market research, competitive analysis, or financial forecasts. If numbers or claims are missing, this skill flags gaps rather than inventing data.

If a request is primarily "build/create/model the underlying strategy/budget/roadmap" rather than "summarize/narrate/present it," redirect the user to the appropriate upstream skill first, or ask them to supply the output of that skill before proceeding.

## Scope

In scope:
- Executive summary and BLUF framing
- Strategic narrative arc (context, conflict/tension, resolution)
- Business context and market opportunity framing
- Key metrics selection and presentation for an executive audience
- Risk articulation at board altitude
- Strategic priority compression (many initiatives to a handful of priorities)
- Investment justification / ask framing (budget increase, resource ask, strategic pivot approval)
- Next steps and decision requests

Out of scope:
- Strategy formulation, segmentation, positioning decisions
- Budget modeling, financial forecasting, ROI calculation
- Detailed roadmap sequencing, resourcing, or project planning
- Legal, compliance, or regulatory review of disclosures

## Inputs

- Source strategy, plan, or roadmap material (full documents, bullet notes, or partial drafts)
- Performance data and metrics (structured or unstructured, e.g., pasted numbers, tables, dashboards descriptions)
- Context on the board/audience (cadence, prior decisions, known sensitivities, decision being requested)
- The specific ask or purpose of this board interaction (e.g., approve budget, report on performance, approve pivot)
- Any known constraints (page/slide limits, time allotted, confidentiality level)

When inputs are incomplete, follow the gap-handling guidance in Error Handling below rather than fabricating specifics.

## Outputs

- **Board Summary** — a condensed narrative overview suitable for board pre-reading or a cover memo (see `templates/board_memo_template.md`)
- **Executive Narrative** — the story arc connecting context, challenge, and resolution (see `templates/executive_summary_template.md`)
- **One-page Strategy** — a single-page distillation of strategic priorities and rationale (see `templates/executive_summary_template.md`)
- **Decision Summary** — options, recommendation, and rationale for a specific ask (see `templates/decision_brief_template.md`)
- **Presentation Outline** — a slide-by-slide or section-by-section outline for a board deck (see `templates/presentation_outline_template.md`)

## Workflow

1. **Clarify the decision context.** Identify the audience (board vs. exec team vs. investors), the specific ask (approve, inform, discuss), time/space constraints, and the board's cadence/history if known.
2. **Inventory the source material.** Read all supplied strategy, metrics, budget, and roadmap content. Note what is present, what is missing, and what looks stale or unverified.
3. **Select the narrative frame.** Choose the arc that fits the situation — steady progress, course correction, underperformance explanation, pivot justification, or investment ask — using `references/strategic_narrative_design.md`.
4. **Apply the pyramid principle / BLUF.** Draft the lead conclusion first, then supporting reasons, then detail, per `references/executive_communication.md`.
5. **Select the metrics that matter.** Choose a small set of leading and lagging indicators appropriate to the ask, using `references/business_metrics.md`. Do not include exhaustive metric dumps.
6. **Compress priorities.** Reduce the underlying roadmap/strategy to 3-5 strategic priorities maximum, each tied to business outcomes, not tasks.
7. **Frame risks and the ask.** Use `references/decision_frameworks.md` to structure any request (budget, approval, pivot) with options, recommendation, and rationale, and to state risks in board-appropriate language (avoid raw operational risk lists).
8. **Draft using the relevant template(s).** Choose from `templates/` based on the requested output format, and adapt the relevant `prompts/` file as a drafting scaffold.
9. **Validate against the checklists.** Run the draft against `checklists/executive_review_checklist.md` and `checklists/quality_checklist.md` before presenting it.
10. **Flag gaps and assumptions.** Explicitly call out any missing data, unverified claims, or assumptions made during compression, rather than silently filling gaps.
11. **Deliver the output** in the format requested (board summary, narrative, one-pager, decision summary, or presentation outline), sized to the stated constraints (e.g., "one page," "10 slides," "5-minute read").

## Reasoning Guidelines

- Always lead with the conclusion or ask (BLUF) — never bury the recommendation on the last page.
- Match "altitude": boards need strategic implications, not operational detail. When in doubt, remove a layer of detail, not add one.
- Every metric included should answer "so what does this mean for the decision," not just "what happened."
- Every risk stated should include its business implication and, where available, the mitigation or the reason it is being surfaced now.
- When compressing many initiatives into 3-5 priorities, group by outcome/theme, not by team or system of record.
- Preserve nuance and honesty even under compression — do not smooth over bad news; frame it clearly with context and a path forward.
- If the underlying strategy, budget, or roadmap itself seems incomplete or the user is really asking for those to be built, say so and point to the appropriate upstream skill rather than improvising that content.

## Best Practices

- Keep the executive summary to one page or under 200 words wherever possible.
- Use plain business language; avoid internal jargon, tool names, or system acronyms unless the board is known to use them.
- Anchor every strategic priority to a metric or outcome the board will recognize.
- State the ask explicitly and early — "we are asking the board to approve X" — not implied.
- Use consistent terminology across the executive summary, narrative, and metrics sections.
- When reporting underperformance, pair the explanation with a forward-looking plan, not just root cause.
- Keep confidential or sensitive figures (e.g., churn, layoffs, customer-specific issues) framed at the altitude and precision the audience and distribution list warrant.

## Validation Rules

- The narrative must state a clear BLUF within the first paragraph or slide.
- No more than 5 strategic priorities in any single output.
- Every metric shown must include context (target, trend, or benchmark) — a bare number is not sufficient.
- Every risk listed must include a business impact statement.
- Any ask (budget, approval, pivot) must include at least one alternative option considered, per `references/decision_frameworks.md`.
- Output length must respect any stated constraint (page count, slide count, word limit); if none is stated, default to board-standard brevity (1-2 pages or 8-12 slides).

## Error Handling

- **Missing metrics or data**: state explicitly which figures are unavailable ("[METRIC NOT PROVIDED]") rather than estimating or fabricating numbers. Ask the user for the missing figure if it is decision-critical.
- **Overly long or sparse source material**: if source material is too sparse to support a credible narrative, tell the user what additional input is needed (e.g., at least directional metrics, a stated ask, or a strategy summary) rather than inventing strategic content.
- **Out-of-scope request**: if the user is actually asking for strategy origination, budget modeling, or roadmap construction, say so plainly and describe what input would let this skill proceed once that upstream work exists.
- **Conflicting inputs**: if source material contains contradictory numbers or claims, surface the conflict to the user rather than silently choosing one version.

## Limitations

- Cannot verify the accuracy of figures or claims supplied by the user; it can only flag inconsistency or absence.
- Does not have access to real-time company data, financial systems, or CRM data unless the user supplies it in the conversation.
- Cannot make the underlying business decision — it frames the decision for the board, it does not decide.
- Not a substitute for legal, financial, or regulatory review of board materials.

## Success Criteria

- The output leads with a clear, board-appropriate BLUF.
- Strategic priorities are compressed to 5 or fewer, each tied to a business outcome.
- Metrics included are the ones a board needs to judge progress and risk — not an exhaustive dump.
- Any ask is structured with options, recommendation, and rationale.
- The output respects stated length/format constraints and reads as ready for direct board or executive use with minimal further editing.
