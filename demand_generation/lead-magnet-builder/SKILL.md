---
name: lead-magnet-builder
description: >
  Drafts gated content offers — guides, checklists, templates, and
  interactive calculators — exchanged for a prospect's contact info, plus the
  landing page copy to promote and gate them. Use when the user wants a
  downloadable guide, checklist, worksheet, or calculator/quiz as a
  lead-gen asset, or landing page copy for one. Trigger on "create a lead
  magnet about X", "build a checklist we can gate behind a form", "make an
  ROI calculator for our website", "draft a guide prospects can download for
  their email", or "write landing page copy for our gated offer." Not for the
  broader campaign strategy (campaign-multiplier), repurposing existing
  long-form content into a lead magnet (content-repurposer), or scheduling
  the launch (campaign-calendar-builder) — this produces the gated asset and
  its landing page copy.
---

# Lead Magnet Builder

## Overview

A lead magnet only works if it's genuinely useful enough that someone will
trade their contact information for it — a thin, generic PDF gated behind a
form converts poorly and damages trust. This skill focuses on building offers
with real, specific value: checklists people can actually use, calculators
that give a real number back, guides with genuinely actionable steps — not
padded content designed to look substantial.

## Purpose

- Produce gated offers (guides, checklists, templates, interactive calculators)
  built around one clear, specific value proposition.
- Build the landing page copy that accompanies the offer, focused on what the
  prospect gets, not just what the company wants to promote.
- For calculators specifically, produce an actual working interactive tool
  (HTML), not just a description of what a calculator would do.
- Keep every offer scoped to something completable — a lead magnet promising
  "the complete guide to X" that's actually 400 words disappoints and burns trust.

## When to use this Skill

- Drafting a checklist, guide, worksheet, or template as a gated offer
- Building an interactive ROI/savings/pricing calculator for the website
- Writing the landing page copy (headline, value bullets, form) for a gated offer
- Refreshing an underperforming existing lead magnet

## When NOT to use this Skill

- Defining the campaign strategy the lead magnet fits into → `campaign-multiplier`
- Turning an existing long-form asset (blog, webinar) into repurposed content
  pieces → `content-repurposer` (though a lead magnet can itself become a
  repurposing source afterward)
- Scheduling the launch/promotion timeline → `campaign-calendar-builder`

## Required Inputs

1. **Topic/problem** the lead magnet addresses, and the target persona
2. **Format**: guide, checklist, template/worksheet, or calculator — see
   `knowledge/lead_magnet_types.md` for which format fits which use case if undecided
3. **The specific value** the offer delivers — what will the reader walk away
   able to do that they couldn't before? A vague topic isn't enough to start drafting.
4. For calculators specifically: the actual inputs, formula/logic, and output
   the calculator should compute — ask for this explicitly if not supplied;
   never invent a business formula (pricing logic, ROI assumptions) without
   confirming it with the user.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Confirm topic, persona, format, and the specific value delivered.
2. Select the right format for the value using `knowledge/lead_magnet_types.md`.
3. Draft the offer content using the matching template — scoped to something
   genuinely completable, not padded.
4. For calculators, confirm the exact formula/logic with the user, then build
   using `scripts/build_calculator_html.py`.
5. Draft landing page copy using `templates/landing_page_copy_template.md`
   and `references/gating_and_conversion_best_practices.md`.
6. Validate with `instructions/validation_rules.md`.

## Best Practices

- **One clear promise, fully delivered.** State exactly what the reader gets
  in the title/headline, and make sure the content actually delivers that —
  don't oversell scope the content doesn't cover.
- **Checklists must be genuinely actionable** — each item should be something
  concrete the reader can check off, not a restated goal ("improve SEO" is not
  a checklist item; "add alt text to all images" is).
- **Calculators need real logic, not a fake output.** Never ship a calculator
  that returns a canned or placeholder number — confirm the actual
  formula/data with the user before building.
- **Landing page copy sells the outcome, not the format.** "Get the
  checklist" is weaker than "Know exactly what to fix before your next audit."

## Rules and Limitations

- Never fabricate a business formula, pricing assumption, or ROI calculation
  logic for a calculator — this must come from the user or their supplied data.
- Never pad content to appear more substantial than the actual value — a
  focused 2-page checklist that's genuinely useful beats an inflated 15-page
  guide with filler.
- Do not make unverifiable or exaggerated promises in landing page copy (e.g.
  "guaranteed results") — see `references/gating_and_conversion_best_practices.md`.
- Do not collect more form fields than necessary for the stated follow-up —
  flag if the user's requested form is asking for more than the offer justifies.

## References

- `knowledge/lead_magnet_types.md` — format types and which use case fits each
- `instructions/workflow.md` — full step-by-step process
- `instructions/validation_rules.md` — pre-delivery checklist
- `examples/example_1.md` — worked example (checklist)
- `examples/example_2.md` — worked example (interactive calculator)
- `templates/guide_template.md`, `templates/checklist_template.md`,
  `templates/worksheet_template.md`, `templates/quiz_assessment_template.md`,
  `templates/landing_page_copy_template.md`
- `scripts/build_calculator_html.py` — generates a working interactive
  calculator widget from a confirmed formula/input spec
- `references/gating_and_conversion_best_practices.md` — form design and
  landing-page conversion guidance
