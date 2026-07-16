# Internal Prompt: Messaging Framework Generation

**Purpose of this document:** Document the reusable internal prompt pattern Claude should adapt when asked specifically to build or refresh a messaging framework. This is an internal reasoning aid, not a user-facing template.

## Purpose

Guide Claude through deriving a messaging house (pillars, proof points, persona variants) from existing positioning and persona inputs, per `references/messaging_framework.md`, rather than brainstorming messaging in isolation.

## Inputs

- `positioning_statement`: the current or drafted positioning statement (from `positioning_canvas_template.md`)
- `personas`: the persona set this messaging must address (from `buyer_persona_template.md`), including their pains, gains, and objections
- `competitive_proof_points`: any documented capability/outcome evidence available (from `references/competitive_analysis.md` findings, win/loss data, or product documentation)
- `existing_messaging`: prior messaging pillars, if this is a refresh
- `channel_context`: where this messaging will be used (website, sales narrative, campaign copy), which affects whether pillar/proof-point structure or narrative/story structure is more appropriate

## Instructions

```
1. Confirm the positioning statement's key differentiator(s) — messaging pillars must derive
   from these, not be invented independently.
2. For each persona provided, list their top 2-3 pains and top 1-2 gains.
3. Draft 3-4 messaging pillars, each: (a) tied to a positioning differentiator, (b) mapped to
   at least one named persona pain or gain, (c) paired with a specific proof point.
4. If a pillar has no available proof point, mark it explicitly as "aspirational / needs
   validation" rather than presenting it as market-ready.
5. For each pillar, write persona-specific variants: how the same pillar is phrased and
   prioritized differently for each persona (e.g., technical evaluator vs. economic buyer).
6. Define a message hierarchy: which single message leads (top-of-funnel/headline use) versus
   which are supporting (used in deeper content, FAQs, or later-stage sales conversations).
7. If channel_context calls for narrative content, draft an optional story framing (customer as
   hero, problem, guide's empathy/authority, plan, call to action, success outcome) built on top
   of the same pillar/proof-point foundation — do not let it introduce different claims.
8. If existing_messaging was provided, note explicitly what changed and why (new positioning,
   new evidence, new persona insight) rather than silently replacing it.
```

## Expected Output

A completed `templates/messaging_framework_template.md`, including the foundation, 3-4 pillars with proof points, a value-proposition-canvas mapping, persona-specific variants, and a stated message hierarchy.

## Validation Checklist

- [ ] Every pillar traces back to a stated positioning differentiator
- [ ] Every pillar maps to at least one named persona pain or gain
- [ ] Every pillar has a proof point, or is explicitly flagged as unvalidated
- [ ] No more than 4 pillars total
- [ ] Persona-specific variants are provided, not one generic message reused for every persona
- [ ] A message hierarchy (primary vs. supporting) is stated
