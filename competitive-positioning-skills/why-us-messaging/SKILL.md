---
name: why-us-messaging
description: >
  Builds persuasive "Why Us vs. Competitor" messaging explaining why a customer
  should choose this product over a named competitor — focused on business
  outcomes, not a feature dump, tailored to a buyer persona (CEO, CTO, PM, IT
  Manager, etc.). Produces copy for websites, decks, sales calls, and emails,
  grounded in verified info, never negative or misleading. Use when asked to
  write or refine differentiation messaging, a positioning statement, a "why us
  vs [Competitor]" narrative, or persona-specific competitive messaging.
  Trigger on "why should a CTO pick us over Competitor X", "website copy on why
  we beat Competitor Y", "persona-based messaging vs Competitor Z for our
  deck", or "email about our advantage over X for procurement." Not for
  comparison tables (feature-comparison-builder), rep cheat sheets
  (battlecard-generator), or win/loss analysis (win-loss-analyzer) — this is
  persuasive, persona-tailored business messaging.
---

# Why-Us Messaging

## Overview

"Why us" messaging is fundamentally about business value and outcomes, not
features — and it changes depending on who's reading it. A CTO cares about
different things than a CFO or a Product Manager, even when the underlying
product facts are identical. This skill builds that persona-aware narrative
layer, distinct from a battlecard (rep quick-reference) or a comparison table
(structured feature grid).

## Purpose

- Produce a clear point of view on why the company wins against one named
  competitor, translated into the language and priorities of a specific buyer persona.
- Keep messaging outcome-focused ("what changes for you") rather than
  feature-focused ("what the product has").
- Stay strictly evidence-based and fair to the competitor — no unverified or
  misleading claims, ever.
- Adapt tone, length, and structure to the delivery channel (website copy,
  slide, sales call talk track, email).

## When to use this Skill

- Website "vs. [Competitor]" landing page copy
- Deck slide narrative / speaker notes for a competitive section
- Persona-specific email campaign copy ("why CTOs choose us over X")
- Sales call talk tracks for a specific buyer role
- Refining/tightening existing differentiation messaging

## When NOT to use this Skill

- A compact rep-facing cheat sheet with landmines/objections/quick facts →
  `battlecard-generator`
- A structured, multi-dimension side-by-side feature/pricing table →
  `feature-comparison-builder`
- Retrospective analysis of why deals were actually won/lost →
  `win-loss-analyzer`
- Generic product messaging with no named competitor — that's standard product marketing

## Required Inputs

Before drafting, confirm (ask if missing — never fabricate):

1. **Competitor name** (and product line/tier if relevant)
2. **Buyer persona**: which role is this for? See
   `knowledge/persona_priorities.json` for the standard persona set and what
   each typically cares about — confirm or select the closest match.
3. **At least 2–3 real, sourced differentiators** — features, economics,
   architecture, outcomes, customer proof points. If none are ready, ask
   rather than inventing plausible ones.
4. **Channel/format**: website copy, deck notes, email, or talk track.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Confirm competitor, persona, channel, and available evidence.
2. Map available differentiators to what this persona actually cares about
   (`knowledge/persona_priorities.json`) — select 2–4, not a kitchen sink.
3. Draft using the acknowledge-then-pivot pattern and the matching template.
4. Run the validation checklist in `instructions/validation_rules.md`.
5. Present the draft, flagging any claim still needing a source.

## Best Practices

- **Outcomes over features.** Translate every feature into "what changes for
  this persona" — e.g., not "supports SSO" but "your security team stops
  fielding manual access requests."
- **One narrative, one persona.** Don't try to serve every buyer role in a
  single piece of messaging — build separate versions per persona, using
  `knowledge/persona_priorities.json` as the map.
- **Acknowledge, then pivot.** Concede something genuine about the competitor
  before pivoting to the differentiator — this reads as more credible than pure
  attack. See `knowledge/messaging_principles.md`.
- **Match tone to channel.** Website copy is punchier/shorter; a talk track is
  spoken-sentence length; a deck needs headline + speaker-note pairing; email
  stays under ~120 words.

## Rules and Limitations

- Never invent a competitor's pricing, features, customer names, or quotes —
  ask for sourcing or mark `[NEEDS SOURCE]`.
- Never attribute a claim to a named real individual at the competitor without
  a genuine public source.
- No disparaging, mocking, or misleading language about the competitor —
  persuasive and fair, never derisive. This is a hard constraint, not a style preference.
- Do not reproduce a competitor's copyrighted marketing copy verbatim; paraphrase.
- Do not blend multiple personas into one piece of copy — if the user wants
  coverage of several buyer roles, produce separate labeled versions.

## References

- `knowledge/messaging_principles.md` — narrative structure and tone theory
- `knowledge/persona_priorities.json` — standard buyer-persona priority map
- `instructions/workflow.md` — step-by-step elicitation and drafting process
- `instructions/validation_rules.md` — pre-delivery checklist
- `examples/example_1.md` — worked example (CTO persona)
- `examples/example_2.md` — worked example (CFO/procurement persona)
- `templates/why_us_messaging.yaml` — structured config template for reusable persona/channel combos
- `templates/why_us_one_pager.md`, `templates/talk_track.md`, `templates/email_snippet.md`
- `references/objection_handling.md` — patterns for handling buyer pushback
