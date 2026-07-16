# Workflow: Building a Battlecard

## Step 1 — Confirm scope and gather source material

Ask (if not already known):
- Competitor name and, if relevant, which product line/tier
- Segment/region scope (general-purpose card, or tailored to one segment)
- Delivery format: markdown, one-page Word doc, or slide-ready bullets

Gather facts from, in priority order:
1. Documents/data the user supplies in this conversation
2. Facts the user directly confirms in chat
3. A previously filled `knowledge/competitor_profile_schema.json` from an
   earlier session, if the user references "the existing card"
4. Publicly available competitor documentation the user points to, or that has
   already been fetched in this session (never guess at facts not sourced this way)

If critical sections have no source material (e.g., no known weaknesses, no
objections), ask one focused follow-up rather than inventing plausible content.

## Step 2 — Populate the profile schema

Fill `knowledge/competitor_profile_schema.json`'s fields for this competitor.
Every weakness needs a paired landmine question where possible. Every
differentiator needs a proof point, not just an assertion.

## Step 3 — Draft using the standard structure

Follow the section order in `knowledge/battlecard_structure.md` exactly —
consistency across cards is what makes them fast to use. Use
`templates/battlecard_template.md` as the drafting scaffold.

For objection/response pairs, check `references/objection_response_bank.md`
for proven patterns, then tailor the specific wording to this competitor's
actual facts — never paste a generic pattern without adapting it to what's true here.

## Step 4 — Validate

Run every item in `instructions/validation_rules.md`. Do not proceed to
rendering with unresolved sourcing gaps — mark them `[UNVERIFIED]` and flag to
the user, or ask for the missing detail.

## Step 5 — Render to the requested format

- **Markdown** (wiki/internal tool): deliver `templates/battlecard_template.md`
  filled in, inline or as a file depending on length conventions.
- **One-page Word doc**: run `scripts/generate_battlecard_docx.py` against the
  populated data. Verify it actually fits one page — if content overflows,
  cut detail (see Best Practices in SKILL.md) rather than shrinking fonts
  below readability.
- **Slide-ready bullets**: condense each section to slide-bullet length
  (headline + 1 sub-bullet max per point).

## Step 6 — Deliver with dating and sourcing visible

Always show the `as_of_date` prominently, and keep a sources footer/appendix
even in the trimmed one-page version (can be small print) so the card can be
audited and refreshed later.

## Common mistakes to avoid

- **Overflowing one page**: prevention — Step 5 explicit page-fit check; cut
  content, don't shrink fonts.
- **Guessing competitor weaknesses without a source**: prevention — Step 1
  hard rule; mark `[UNVERIFIED]` instead.
- **Stale, undated cards**: prevention — Step 6 always surfaces `as_of_date`.
- **Objection responses that read like marketing copy, not something a rep
  would actually say**: prevention — Step 3 requires "sayable out loud" phrasing,
  checked again in validation.
- **Omitting genuine competitor strengths to make the card feel more
  favorable**: prevention — `battlecard_structure.md` §4 requires this section
  and treats its omission as a structural defect, not an optional cut.
