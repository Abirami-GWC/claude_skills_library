---
name: campaign-multiplier
description: >
  Expands one idea or asset (a product update, announcement, blog post,
  customer story) into a multi-channel campaign brief — messaging pillars,
  channel-specific angles, and success metrics across email, social, paid,
  blog, and other channels. Use when the user has one core idea and wants a
  full campaign plan spanning channels, or asks "how do we get more mileage
  out of this", "build a campaign around X", or "what's our channel plan for
  this launch." Trigger on "expand this into a campaign", "multi-channel
  brief for our product launch", or "build a campaign plan around our new
  case study." Not for converting an asset into literal per-channel content
  (content-repurposer), gated-offer creation (lead-magnet-builder), or
  sequencing dates/dependencies (campaign-calendar-builder) — this produces
  the strategic brief those skills execute against.
---

# Campaign Multiplier

## Overview

Most marketing ideas start as one thing — a blog post, a product update, a
customer win — and stay that way because turning it into a full campaign feels
like starting over. This skill closes that gap: it takes the one asset/idea
and produces a structured campaign brief that defines the core narrative,
which channels it should live on, what angle each channel gets, and how
success will be measured — the strategic layer that precedes actual content production.

## Purpose

- Take one input (an idea, asset, or announcement) and multiply it into a
  coherent multi-channel plan, not a randomly assorted list of channel ideas.
- Keep every channel's angle tied back to one consistent core narrative/message,
  rather than each channel inventing its own unrelated story.
- Produce a brief specific enough that a content-writer, designer, or the
  `content-repurposer` skill could execute against it without further strategic decisions.
- Define success metrics per channel so the campaign is measurable, not just produced.

## When to use this Skill

- Turning a single asset (blog post, announcement, research finding, customer
  story, product update) into a full campaign brief
- Planning promotion for a launch, event, or content piece across multiple channels
- Reworking an underperforming single-channel effort into a broader multi-channel plan

## When NOT to use this Skill

- Producing the actual per-channel content (social captions, email copy) from
  one asset → `content-repurposer`
- Building a gated content offer (guide, checklist, calculator) → `lead-magnet-builder`
- Sequencing dates and dependencies for an already-defined channel plan →
  `campaign-calendar-builder`
- Competitive positioning content (battlecards, comparisons) → separate skill family

## Required Inputs

1. **The core idea/asset**: what it is, and (if it's an existing piece)
   its actual content or a summary/link
2. **The audience/persona** this campaign targets
3. **The goal**: awareness, lead generation, product adoption, retention, etc.
   — this shapes which channels and metrics matter
4. **Available channels**: which channels are actually in play (don't assume
   paid budget or channels the user hasn't confirmed access to)
5. **Timeframe** (rough), if relevant to channel selection (e.g., paid social
   needs lead time to set up creative/targeting)

If any of these is missing, ask — a campaign brief built on assumed goals or
audience is likely to be strategically wrong even if well-written.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Elicit the core idea, audience, goal, available channels, and timeframe.
2. Define 1–3 messaging pillars that every channel angle must tie back to.
3. Select and sequence channels using `knowledge/channel_playbook.md` — not
   every channel needs to be used; pick the ones that fit the goal and audience.
4. For each selected channel, define: the specific angle, format, one
   headline/hook example, and the success metric.
5. Validate with `instructions/validation_rules.md`.
6. Assemble using `templates/campaign_brief_template.md`, populate
   `knowledge/campaign_brief_schema.json`, and optionally render a shareable
   Word doc via `scripts/build_campaign_brief_docx.py` for stakeholder review.

## Best Practices

- **One core narrative, many angles** — every channel should feel like the
  same campaign, not unrelated content that happens to share a launch date.
- **Match channel to goal**, not habit — don't default to "post on
  everything"; use `knowledge/channel_playbook.md` to pick channels that
  actually serve the stated goal.
- **Give each channel a distinct job.** If two channels carry the identical
  angle and CTA, one of them is probably redundant — call this out rather
  than padding the brief with lookalike channel entries.
- **Metrics before content.** Define how success is measured per channel
  before drafting angle/hook details — this keeps the brief outcome-focused.

## Rules and Limitations

- Do not assume budget, tooling, or team capacity for a channel the user
  hasn't confirmed (e.g., don't default to including paid ads unless the user
  says paid is available).
- Do not fabricate audience research or performance benchmarks — if the user
  wants specific numeric targets, ask for their historical baselines or mark
  the metric as "target TBD."
- Do not produce the actual finished content pieces here — this skill stops
  at the brief/angle level; hand off to `content-repurposer` for execution.
- Keep the brief to 1–3 messaging pillars — more than that stops being a
  coherent narrative and becomes a grab-bag.

## References

- `knowledge/channel_playbook.md` — channel-by-channel characteristics and best-fit use cases
- `knowledge/campaign_brief_schema.json` — structured data model for a campaign brief
- `instructions/workflow.md` — full elicitation-to-brief process
- `instructions/validation_rules.md` — pre-delivery checklist
- `examples/example_1.md` — worked example (product launch → 4-channel brief)
- `templates/campaign_brief_template.md` — the brief document structure
- `templates/channel_matrix.csv` — channel × angle × metric planning grid
- `scripts/build_campaign_brief_docx.py` — renders a populated brief into a
  shareable Word doc with a channel table
- `references/messaging_pillars_guide.md` — how to derive pillars from one core asset
