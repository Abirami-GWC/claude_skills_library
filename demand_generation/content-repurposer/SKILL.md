---
name: content-repurposer
description: >
  Turns one long-form asset (blog post, webinar transcript, whitepaper,
  podcast episode, report) into multiple finished, platform-appropriate
  content pieces — social posts, email snippets, a short video/reel script,
  an infographic outline — each adapted to its channel's conventions, not
  just cut down from the source. Use when the user has one long-form piece
  and wants ready-to-post content for other channels. Trigger on "turn this
  blog post into social posts", "repurpose this webinar into an email and
  LinkedIn posts", "give me 5 tweets from this article", or "what else can
  we get out of this content." Not for defining the overall channel strategy
  (campaign-multiplier), building gated offers from scratch
  (lead-magnet-builder), or scheduling (campaign-calendar-builder) — this
  produces the actual finished, channel-ready pieces from one source asset.
---

# Content Repurposer

## Overview

Repurposing done badly is just the same paragraph pasted into five boxes of
different sizes. Done well, each output respects its channel's actual
conventions — a LinkedIn post reads differently from a tweet, which reads
differently from an email subject line — while staying faithful to the source
material's substance and never overclaiming beyond what the source actually says.

## Purpose

- Convert one long-form asset into multiple genuinely platform-native pieces,
  not truncated copies of the same paragraph.
- Preserve the source's factual accuracy and nuance — repurposing must not
  introduce claims the original didn't make.
- Respect each platform's format constraints (length, tone, structural
  conventions) from `references/platform_specs.md`.
- Stay within copyright bounds — paraphrase and extract ideas, never
  reproduce the original at length verbatim across multiple outputs.

## When to use this Skill

- Turning a blog post into a thread, LinkedIn post, and email snippet
- Turning a webinar or podcast transcript into short clips' worth of quotes,
  social posts, and a summary email
- Turning a long report/whitepaper into an infographic outline and a series
  of social posts
- "What else can we get out of this" requests for any existing long-form asset

## When NOT to use this Skill

- Defining the overall channel strategy/brief before content exists →
  `campaign-multiplier`
- Building a new gated offer (guide, checklist, calculator) from scratch →
  `lead-magnet-builder`
- Scheduling/sequencing the repurposed pieces across a timeline →
  `campaign-calendar-builder`

## Required Inputs

1. **The source asset** — full text, a transcript, or an uploaded document.
   If only a link or summary is available, ask for the actual content or
   fetch it, since repurposing from a vague summary risks drifting from the source.
2. **Target formats/channels** — which outputs are needed (social platform(s),
   email, video script, infographic outline, etc.). If unspecified, propose a
   sensible default set and confirm.
3. Optional: brand voice/tone notes, if the user has specific guidelines.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Ingest the source asset in full; identify via
   `scripts/extract_key_points.py` or manual read the core claims, strongest
   quotes/stats, and structural sections.
2. Confirm target formats; look up each format's constraints in
   `references/platform_specs.md`.
3. Draft each output per `knowledge/format_conversion_guide.md`'s
   format-specific adaptation guidance — not a shortened copy-paste.
4. Run the fidelity and copyright checklist in `instructions/validation_rules.md`.
5. Deliver all pieces together, each clearly labeled by channel/format.

## Best Practices

- **Adapt, don't shrink.** A LinkedIn post built for LinkedIn reads
  differently from a truncated blog paragraph — restructure for the
  platform's actual reading pattern, don't just cut word count.
- **Lead with the strongest single idea per piece**, not a summary of
  everything — a repurposed piece that tries to cover the whole source ends
  up saying nothing sharply.
- **Preserve nuance and caveats from the source** — repurposing under
  space constraints is not license to drop qualifiers that change the claim's meaning.
- **Vary the angle across pieces**, where multiple pieces target the same
  platform/campaign — five LinkedIn posts that all restate the headline are
  weaker than five posts each surfacing a different point from the source.

## Rules and Limitations

- Never reproduce more than a short (under ~15 words), single quote from the
  source per output piece — paraphrase the rest, per standard copyright practice.
- Never introduce a claim, statistic, or framing the source material doesn't
  actually support.
- Never fabricate a quote or stat attributed to the source that isn't
  actually present in it.
- Do not exceed platform format constraints (character limits, etc.) defined
  in `references/platform_specs.md` — verify length before delivering, don't estimate.
- If the source asset itself is someone else's copyrighted material (not the
  user's own content), flag this and repurpose only via summary/paraphrase,
  not close reproduction.

## References

- `knowledge/format_conversion_guide.md` — how to adapt long-form content per target format
- `instructions/workflow.md` — full step-by-step process
- `instructions/validation_rules.md` — fidelity/copyright/length checklist
- `examples/example_1.md` — worked example (blog post → 4 formats)
- `templates/social_post_template.md`, `templates/thread_template.md`,
  `templates/email_snippet_template.md`, `templates/video_script_template.md`,
  `templates/infographic_outline_template.md`, `templates/quote_graphic_template.md`
- `templates/repurposing_plan.csv` — source-section-to-output-piece planning grid
- `scripts/extract_key_points.py` — pulls candidate quotes/stats/section
  headers from a long text to speed up drafting
- `references/platform_specs.md` — character limits and structural
  conventions per platform/format
