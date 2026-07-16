---
name: battlecard-generator
description: >
  Generates sales battlecards — concise, rep-facing cheat sheets that help a
  salesperson understand a named competitor and respond confidently on a live
  call. Covers strengths/weaknesses, head-to-head comparison, differentiators,
  objections with responses, talking points, and pricing/features/integrations
  — scannable in under two minutes. Use whenever asked to create, update, or
  refresh a "battlecard", "competitor cheat sheet", or "quick reference for
  reps on Competitor X", or to prep a sales team for a competitor. Trigger on
  "build a battlecard for Competitor X", "one-page cheat sheet on Competitor
  Y", "what should reps say about Competitor Z", or "update the battlecard
  pricing." Not for long-form narrative (why-us-messaging), multi-competitor
  RFP grids (feature-comparison-builder), or deal analysis
  (win-loss-analyzer) — this is the compact, call-ready rep document.
---

# Battlecard Generator

## Overview

A battlecard is optimized for one thing: a rep glancing at it seconds before or
during a live call. That constraint drives everything about its structure — it
is not a research report, not a persuasive essay, and not an exhaustive feature
list. It is a single page (or a tightly scannable digital equivalent) of the
highest-leverage facts, objection responses, and talking points for one named
competitor.

## Purpose

- Give sales reps a fast, reliable, evidence-based reference for one competitor
  at a time.
- Standardize battlecard structure across the sales org so reps always know
  where to find pricing, objections, or landmines regardless of which
  competitor's card they're reading.
- Keep every claim traceable to a source, since battlecards get quoted directly
  to prospects.

## When to use this Skill

- Creating a new battlecard for a competitor the sales team is starting to see in deals
- Refreshing an existing battlecard with new pricing, features, or win/loss learnings
- Producing a battlecard in a specific delivery format (one-page PDF/Word doc,
  markdown for an internal wiki, or a slide for kickoff training)
- Extracting a short objection-response list from a broader competitive brief

## When NOT to use this Skill

- Long-form "why us" persuasive narrative for decks/emails → `why-us-messaging`
- A structured, multi-dimension comparison table/grid (e.g., for an RFP) →
  `feature-comparison-builder`
- Analyzing why deals were actually won/lost against a competitor →
  `win-loss-analyzer`
- General competitor research with no sales-enablement angle — that's plain research

## Required Inputs

Before drafting, confirm (ask if missing — never fabricate):

1. **Competitor name** (and product tier/line if relevant)
2. **Source material**: product docs, pricing pages, past win/loss notes, sales
   call notes, or a filled `knowledge/competitor_profile_schema.json`. If the
   user has none ready, ask for what's available rather than inventing facts.
3. **Delivery format**: one-page Word/PDF doc, markdown (wiki/internal tool), or
   slide-ready bullets
4. **Audience scope**: is this for a specific segment/region where pricing or
   positioning differs, or a general-purpose card?

## Workflow (summary — see instructions/workflow.md for full detail)

1. Gather and validate source facts; populate `knowledge/competitor_profile_schema.json`.
2. Draft each battlecard section using `templates/battlecard_template.md` as the
   structural backbone.
3. Pull objection-response pairs from `references/objection_response_bank.md`
   patterns, tailored to the actual competitor facts gathered.
4. Run the accuracy/format checklist in `instructions/validation_rules.md`.
5. Render to the requested format — markdown, or a one-page Word doc via
   `scripts/generate_battlecard_docx.py`.

## Best Practices

- **One page, always.** If the draft doesn't fit a single page/screen at a
  glance, cut detail rather than shrinking the font — battlecards that require
  scrolling or zooming don't get used mid-call.
- **Scannable structure over prose.** Use short bullets and bolded labels, not
  paragraphs — a rep needs to find "pricing" or "landmines" in under 3 seconds.
- **Landmines, not just weaknesses.** Include specific traps/questions a rep can
  ask that expose a genuine competitor weakness relevant to the deal — more
  useful than a flat adjective like "less scalable."
- **Date every card.** Pricing and features change; an undated battlecard is a
  liability the first time it's wrong on a call.
- **Objection responses should be sayable out loud** — short, natural sentences,
  not marketing copy.

## Rules and Limitations

- Never fabricate competitor pricing, features, certifications, or customer
  names. Mark unverified facts `[UNVERIFIED]` rather than presenting them as fact.
- Never include disparaging, mocking, or unfair characterizations of a
  competitor — battlecards that overstate weaknesses damage rep credibility with
  buyers who fact-check.
- Do not attribute claims to named real individuals at the competitor without a
  genuine public source.
- Do not reproduce a competitor's copyrighted marketing copy, datasheet text, or
  pricing-page text verbatim — summarize in the card's own words.
- Keep to one competitor per battlecard — for multi-competitor grids, route to
  `feature-comparison-builder` instead.

## References

- `knowledge/battlecard_structure.md` — the standard section-by-section anatomy
- `knowledge/competitor_profile_schema.json` — structured input data model
- `instructions/workflow.md` — full build process
- `instructions/validation_rules.md` — pre-delivery accuracy/format checklist
- `examples/example_1.md` — worked example end to end
- `templates/battlecard_template.md` — markdown battlecard template
- `templates/battlecard_objection_bank.csv` — structured objection/response starter set
- `scripts/generate_battlecard_docx.py` — renders a populated battlecard into a one-page Word doc
- `references/objection_response_bank.md` — patterns for objection-handling language
