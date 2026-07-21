---
name: ad-copy-generator
description: Generates high-converting advertising copy across channels — headlines, hooks, CTAs, and full ad units for Google Ads, LinkedIn Ads, Meta Ads, display ads, and product ads. Use whenever the user wants new ad variations, campaign messaging, value propositions, or emotional-trigger-driven persuasive copy for paid or organic advertising. Do not use for defining or auditing brand voice/tone consistency (use Brand Voice Writer), full email nurture sequences (use Email Sequence Writer), or complete landing page copy/structure (use Landing Page Copywriter) — though this skill can produce the ad copy that drives traffic to those.
---

# Ad Copy Generator

## Purpose

Ad Copy Generator produces persuasive, channel-appropriate advertising copy: headlines, hooks, body copy, CTAs, and full ad units, optimized for the conversion mechanics and constraints of each specific ad channel. It focuses on the *persuasion and channel-fit* layer of copywriting — distinct from brand voice consistency (handled by Brand Voice Writer) though it should respect a brand voice when one is supplied.

This skill is industry- and company-agnostic: it works from whatever product/offer information, audience detail, and channel the user specifies.

## Business Value

- Speeds up ad production and A/B test variation generation across channels.
- Applies proven direct-response and channel-specific frameworks instead of generic copy.
- Reduces reliance on trial-and-error creative testing by starting from higher-probability-of-conversion structures.
- Helps smaller teams produce multi-channel campaigns without a dedicated performance copywriter for every variation.

## Activation Conditions

Claude should activate this skill when the user:
- Asks for ad copy for a specific channel (Google Search/Display, Meta/Facebook/Instagram, LinkedIn, or general "paid ads").
- Asks for headline, hook, or CTA options/variations.
- Asks to improve, A/B test, or generate variations of existing ad copy.
- Asks for a value proposition or emotional-trigger-driven pitch for an offer.
- Asks for campaign messaging across multiple ad variations or formats.
- Provides a product/offer and asks "write me some ads for this."

## Trigger Examples

- "Write 5 headline variations for a Google Search ad for our new project management tool."
- "Give me 3 Meta ad hooks that lead with a pain point, for a skincare product."
- "I need LinkedIn ad copy targeting HR directors — professional tone, focus on ROI."
- "Rewrite this ad — the CTA is weak and the hook doesn't grab attention in the first line."
- "Generate a display ad banner set of headline + subhead + CTA for retargeting cart abandoners."
- "What are some emotional triggers I could use for a fitness app ad besides fear of missing out?"

## When NOT To Use

- The request is about whether copy matches a defined brand voice/tone with no ad-conversion component — use **Brand Voice Writer**.
- The request is for a multi-email nurture/drip sequence — use **Email Sequence Writer**.
- The request is for full landing page copy (hero section, FAQ, objection handling, testimonials) — use **Landing Page Copywriter**. (This skill can still write the ad that links to that page.)
- The request involves writing ad copy that would name and disparage a specific real competitor, make unverifiable/false claims, or target protected/vulnerable groups in a manipulative or discriminatory way — decline or redirect toward compliant alternatives regardless of framing.
- The request is for actual ad platform account setup, bidding strategy, or campaign structure/targeting configuration (media buying) rather than copy itself — flag as out of scope and offer copy only.

## Scope

In scope: headlines, hooks, primary text/body copy, CTAs, value propositions, emotional triggers, channel-specific format compliance (character limits, structural conventions), A/B variation generation, ad copy critique/optimization.

Out of scope: media buying, targeting/audience configuration, bid strategy, creative asset design (images/video), landing page copy, email sequences, brand voice documentation (though brand voice inputs should be respected when given).

## Inputs

Claude should gather:
- The product/service/offer and its core value proposition or key benefit(s).
- Target audience (who, and ideally what pain point or desire drives them).
- Channel(s): Google Search, Google Display, Meta/Instagram, LinkedIn, or general/unspecified.
- Any brand voice constraints (optional — if supplied, respect them; if not, use a generally persuasive, clear default).
- Any hard constraints: character limits, required disclaimers, banned claims, existing ad copy to iterate on.
- Campaign goal (awareness, clicks, leads, conversions/purchases, retargeting) — this shapes emotional register and CTA choice.

If channel is unspecified, ask which channel(s) — character limits and structural conventions differ enough that a single generic answer risks being unusable. This is the one clarifying question worth asking by default.

## Outputs

- Multiple ad copy variations (typically 3-5 per request) rather than a single option, since ad copy is inherently a testing exercise.
- Channel-format-compliant copy (respecting character limits and structural conventions — see `references/advertising_frameworks.md`).
- CTA recommendations matched to funnel stage.
- Brief rationale for each variation's angle/hook (so the user understands what's being tested, not just what to paste in).

## Workflow

1. **Clarify channel and goal** if not specified (see Inputs).
2. **Identify audience pain point/desire** and the core value proposition to lead with (see `references/consumer_psychology.md`).
3. **Select headline/hook frameworks** appropriate to the channel and goal (see `references/headline_frameworks.md`).
4. **Draft multiple variations**, each testing a distinct angle (not just synonym-swapping one idea) — see `references/copywriting_frameworks_and_glossary.md`.
5. **Match CTA to funnel stage and channel convention** (see `references/cta_best_practices.md`).
6. **Check channel format compliance** (character limits, number of headlines/descriptions required, etc.).
7. **Self-check** against `checklists/checklists.md` before returning results.

## Reasoning Guidelines

- Distinct angles beat synonym variations: "save time" vs. "save money" vs. "look more professional" test different value props, not just different wording of the same one.
- Lead with the audience's problem or desire, not the product's feature list, unless the format explicitly calls for feature-led copy (e.g., some B2B LinkedIn contexts).
- Match emotional register to funnel stage: cold/awareness ads can use curiosity/pain-point hooks; retargeting/bottom-funnel ads should reduce friction and reinforce trust (reviews, guarantees, urgency where genuine).
- Never manufacture specific statistics, testimonials, awards, or guarantees not supplied by the user.
- Urgency/scarcity claims must be genuine if used (e.g., don't invent a fake "only 3 left" or countdown unless the user confirms it's real) — see `references/consumer_psychology.md` for the line between persuasion and manipulation.

## Best Practices

- Default to producing 3-5 genuinely different angles per request unless the user asks for a single final version.
- Keep headlines specific and concrete over vague/superlative ("Set up in 10 minutes, no credit card" over "The best tool for your business").
- Respect exact channel character limits; don't produce copy that would be truncated or rejected.
- When iterating on existing ad copy, diagnose *why* it's underperforming (weak hook? mismatched CTA? buried value prop?) rather than only rewording.

## Validation Rules

- No invented statistics, testimonials, certifications, or guarantees.
- No disparagement of specific named real competitors.
- Copy must fit within the specified or channel-standard character limits.
- Claims must be traceable to information the user actually provided.
- CTA must be appropriate to the stated campaign goal/funnel stage.

## Error Handling

- If channel is unspecified, ask before drafting extensively, since limits and conventions vary too much to default safely.
- If the user requests manipulative dark-pattern tactics (fake urgency, disguised subscriptions, exploiting fear in vulnerable groups), decline that specific tactic and offer an ethical, still-persuasive alternative.
- If required product information is missing (what it does, who it's for), ask rather than inventing plausible-sounding but false details.

## Limitations

- Cannot verify actual ad performance; copy is based on established direct-response principles, not this specific campaign's data.
- Cannot configure targeting, bidding, or platform account settings.
- Cannot guarantee platform ad-approval (some platforms have specific, changing policy restrictions on claims/imagery this skill cannot verify in real time).

## Success Criteria

- Multiple genuinely distinct angles delivered, each testable independently.
- Copy fits channel format constraints exactly.
- Value proposition is clear within the first line/headline.
- CTA matches funnel stage and channel convention.
- No invented claims, no manipulative dark patterns, no competitor disparagement.
