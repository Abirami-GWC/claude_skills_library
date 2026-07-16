---
name: win-loss-analyzer
description: >
  Analyzes historical CRM/sales data to identify why deals were won or lost
  against named competitors — surfacing win/loss reasons, patterns by
  industry, customer size, region, or product line, recurring objections, and
  competitor strengths influencing buying decisions. Produces executive
  summaries, charts, and recommendations for sales leadership. Use when the
  user provides deal records, CRM exports, or win/loss notes, or asks to
  analyze patterns in why the company beats or loses to a competitor. Trigger
  on "analyze our win/loss data", "why do we keep losing to Competitor X",
  "patterns by industry or region in our losses", or "executive summary and
  charts for the QBR." Works only from real supplied deal data — never
  fabricates outcomes. Not for forward-looking messaging (why-us-messaging),
  rep cheat sheets (battlecard-generator), or feature grids
  (feature-comparison-builder) — this is retrospective, data-driven analysis.
---

# Win/Loss Analyzer

## Overview

Win/loss analysis is retrospective and data-driven, not persuasive. Its value
is honest pattern-finding — including uncomfortable patterns — segmented across
the dimensions that actually matter to sales leadership: competitor, industry,
customer size, region, and product line. The output should be something a VP
of Sales can open before a QBR and immediately act on.

## Purpose

- Turn raw deal records (CRM exports, spreadsheets, interview notes) into a
  structured report: win rate by competitor, categorized reasons, multi-cut
  pattern detection (industry/size/region/product), and recommendations.
- Distinguish signal from noise — flag when a sample size (overall or within a
  specific cut) is too small to support a claimed pattern.
- Produce leadership-ready output: an executive summary, supporting charts,
  and specific, owned recommendations — not just a restated data dump.

## When to use this Skill

- User supplies or references a CRM export / spreadsheet of closed deals with
  competitor, industry, region, size, and outcome fields
- User supplies win/loss interview notes or call transcripts for qualitative
  theme extraction
- "Why do we lose to X" / "what's driving losses in [segment]" questions
  backed by actual data
- Building a recurring win/loss report — with executive summary and charts —
  for QBRs or leadership reviews

## When NOT to use this Skill

- No real deal data available and the user wants hypothetical/anecdotal
  competitive positioning → `why-us-messaging`
- A compact rep-facing cheat sheet → `battlecard-generator`
- Structured point-in-time feature/pricing comparison → `feature-comparison-builder`

## Required Inputs

1. **Deal-level data**: at minimum, outcome (won/lost), competitor. Ideally
   also industry, customer size/segment, region, product line, and a reason
   code per deal. See `templates/deal_record_schema.csv`.
2. **Time range and scope** — ask if not specified.
3. Optional: raw interview notes/transcripts for qualitative theme extraction.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Confirm scope (time range, segment/competitor focus) and ingest data.
2. Normalize records into the schema in `templates/deal_record_schema.csv`,
   categorizing each reason using `knowledge/loss_reason_taxonomy.json`.
3. Compute win rates and reason distributions, cut by competitor, industry,
   customer size, region, and product line via `scripts/analyze_winloss.py`.
4. Check statistical caution per `references/statistical_significance_notes.md`
   before stating any pattern as a firm conclusion — this applies with extra
   force to multi-dimension cuts, which shrink sample size fast.
5. Extract qualitative themes from any interview notes/transcripts supplied.
6. Generate supporting charts via `scripts/generate_winloss_charts.py`.
7. Assemble the report using `templates/win_loss_report.md`, including an
   executive summary suitable for leadership.

## Best Practices

- **Report honestly, including uncomfortable findings.**
- **Always show sample size** next to any win-rate or pattern claim.
- **Separate quantitative categorization from qualitative color.**
- **Distinguish correlation from cause**, especially across industry/region/size
  cuts — a pattern by region could reflect where deals originated, not an
  actual competitive weakness there.
- **Recommendations should be specific and owned** — tie each to the finding
  that motivated it and name a likely owner (Product / Marketing / Sales / Pricing).
- **Lead the report with the executive summary** — leadership reads that
  first and may read nothing else; it must stand alone.

## Rules and Limitations

- Never fabricate or extrapolate deal records that weren't supplied.
- Never state a pattern as statistically meaningful without checking sample
  size, especially for multi-dimension cuts (e.g., "losses to Competitor X in
  EMEA healthcare enterprise deals") which can shrink to n=2 fast.
- Do not name individual reps, buyers, or contacts in a report intended for
  broad circulation unless the user explicitly wants that level of detail.
- Do not use this analysis to write competitor-facing content directly — its
  output feeds `why-us-messaging`, `battlecard-generator`, or
  `feature-comparison-builder`, but isn't itself buyer-facing collateral.

## References

- `knowledge/analysis_framework.md` — categorize → quantify → qualify → recommend
- `knowledge/loss_reason_taxonomy.json` — standard taxonomy for coding reasons
- `instructions/workflow.md` — full step-by-step process
- `instructions/interview_questions.md` — win/loss interview question bank
- `examples/example_1.md` — worked example with multi-dimension pattern detection
- `templates/win_loss_report.md` — final report structure with executive summary
- `templates/deal_record_schema.csv` — expected input data shape
- `scripts/analyze_winloss.py` — computes win rates/distributions, multi-dimension cuts
- `scripts/generate_winloss_charts.py` — generates supporting chart images from a deals CSV
- `references/statistical_significance_notes.md` — sample-size caution guidance
