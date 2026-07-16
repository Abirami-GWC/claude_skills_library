---
name: feature-comparison-builder
description: >
  Builds accurate, structured feature/pricing comparison tables between this
  product and one or more named competitors, covering features, pricing,
  integrations, security, scalability, AI capabilities, deployment, support,
  and licensing. Produces side-by-side grids marking gaps and advantages,
  marks unknown info instead of guessing, supports multiple competitors at
  once, and exports to markdown, CSV, interactive HTML, or Word/PDF. Use when
  asked for a "comparison table", "feature matrix", "vs. chart", "pricing
  comparison grid", "RFP response grid", or to compare named
  features/pricing/security across vendors. Trigger on "build a feature
  comparison table for us vs Competitor X and Y", "pricing comparison chart",
  "fill out this RFP grid", or "compare our AI capabilities to Competitor Z."
  Not for narrative messaging (why-us-messaging), rep cheat sheets
  (battlecard-generator), or win/loss analysis (win-loss-analyzer) — this is
  structured, checkable, tabular comparisons.
---

# Feature Comparison Builder

## Overview

A comparison table lives or dies on accuracy — it's the artifact most likely to
be fact-checked by a buyer, screenshotted, or used in a signed RFP response.
Unlike narrative messaging, there is very little room for framing; the job is
precise, sourced, cell-by-cell accuracy across every listed vendor, presented clearly.

## Purpose

- Produce accurate, well-sourced comparison matrices across the standard
  dimension categories: Features, Pricing, Integrations, Security &
  Compliance, Scalability, AI Capabilities, Deployment, Support, and Licensing.
- Support **multiple competitors simultaneously** in one matrix, not just a
  single head-to-head.
- Support multiple output formats: markdown table, CSV, interactive HTML
  widget, or a presentation-ready Word/PDF export.
- Make it structurally easy to keep the matrix current (dated, sourced, versioned).

## When to use this Skill

- "Build a comparison table of us vs. [Competitor A] and [Competitor B] on
  [dimensions]"
- Filling in a vendor-comparison section of an RFP response
- Building a "compare us" page for a website or sales deck
- Comparing AI/ML capabilities, scalability limits, or licensing models across vendors
- Turning messy feature notes into a clean, presentation-ready matrix

## When NOT to use this Skill

- Persuasive, persona-tailored narrative → `why-us-messaging`
- A compact single-competitor rep cheat-sheet → `battlecard-generator`
- Aggregate analysis of why deals are won or lost → `win-loss-analyzer`

## Required Inputs

1. **Competitors to include** — one or more named vendors (this skill natively
   supports N-way comparisons, not just 1-vs-1)
2. **Dimensions to compare** — from the standard categories in
   `knowledge/comparison_dimensions.md`, or a custom set the user specifies. If
   unspecified, propose the standard set and confirm.
3. **Source data** for each cell — supplied by the user, pulled from uploaded
   documents, or explicitly marked unknown. Never invent a competitor's
   feature-support status.
4. **Output format(s)**: markdown table / CSV / interactive HTML widget /
   presentation-ready Word or PDF export.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Confirm competitors (N-way), dimensions, and desired output format(s).
2. Populate the matrix using `knowledge/comparison_matrix_schema.json` as the
   data model, marking every cell's support level and source.
3. Validate with `instructions/data_validation.md` (no unsourced cells
   presented as fact; consistent rating scale; no missing vendor).
4. Render to the requested format:
   - Markdown → `templates/comparison_table.md`
   - CSV → `templates/comparison_table.csv`
   - Interactive/HTML → `scripts/build_comparison_html.py`
   - Presentation-ready Word/PDF → `scripts/build_comparison_docx.py`
5. Deliver, noting the as-of date and flagging any `Unknown` cells for follow-up.

## Best Practices

- Use a **consistent rating scale** across every cell (see
  `knowledge/scoring_legend.md`) — never mix symbols with free-text ratings.
- **Date-stamp** every comparison — competitive facts, especially pricing and
  AI-capability claims, go stale fast.
- Keep dimension names **neutral and outcome-based**, not phrased to favor one vendor.
- When a feature exists under a different name, tier, or model (paid add-on,
  regional availability), reflect that nuance in the cell rather than a flat ❌.
- For **AI capabilities** specifically, distinguish "generally available,"
  "beta/preview," and "roadmap-announced" — these are not equivalent and
  conflating them is a common accuracy failure (see
  `references/ai_capability_comparison_notes.md`).
- For an RFP response, match the exact dimension wording the RFP requested.

## Rules and Limitations

- Never mark a competitor cell "Unsupported" without a source; if unknown, mark
  `Unknown` — a wrong "No" is a credibility and potentially legal risk,
  especially in a signed RFP response.
- Do not fabricate pricing numbers; mark `Not publicly available` if unsourced.
- Do not reproduce a competitor's copyrighted marketing materials, datasheets,
  or pricing pages verbatim — summarize facts in the table's own words.
- Interactive HTML widgets and generated documents must not fabricate data —
  all rendered output must trace back to the sourced matrix built in Step 2.

## References

- `knowledge/comparison_matrix_schema.json` — the data model for a comparison matrix
- `knowledge/scoring_legend.md` — standard rating scale
- `knowledge/comparison_dimensions.md` — the standard dimension category set
  (Features, Pricing, Integrations, Security & Compliance, Scalability, AI
  Capabilities, Deployment, Support, Licensing)
- `instructions/workflow.md` — full build process
- `instructions/data_validation.md` — pre-delivery accuracy checklist
- `examples/example_1.md` — worked example (3-vendor comparison, multiple dimension categories)
- `templates/comparison_table.md`, `templates/comparison_table.csv`
- `scripts/build_comparison_html.py` — renders an interactive HTML comparison widget
- `scripts/build_comparison_docx.py` — renders a presentation-ready Word comparison document
- `scripts/validate_matrix.py` — automated checks for the JSON matrix before rendering
- `references/pricing_comparison_guidelines.md` — special handling notes for pricing rows
- `references/ai_capability_comparison_notes.md` — special handling notes for AI/ML capability rows
