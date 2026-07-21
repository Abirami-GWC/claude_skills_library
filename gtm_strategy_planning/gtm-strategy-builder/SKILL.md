---
name: gtm-strategy-builder
description: Builds or refreshes a quarterly Go-To-Market (GTM) strategy for any product, service, or company, regardless of industry. Use this skill when a user asks to create, draft, refresh, or review a GTM strategy, positioning statement, Ideal Customer Profile (ICP), buyer personas, market segmentation, messaging framework, value proposition, competitive positioning, or channel/motion strategy for a quarter or launch. Produces structured strategic documents (Quarterly GTM Plan, Positioning Strategy, ICP Definition, Messaging Framework, Channel Strategy, Strategic Recommendations) grounded in standard GTM frameworks. Does not handle budget allocation, roadmap execution planning, or board narrative writing.
---

# gtm-strategy-builder

## Purpose

This skill helps Claude act as a GTM (Go-To-Market) strategy partner. It drafts, refreshes, or reviews the strategic layer that determines *who* a product/company should sell to, *what* it should say to them, and *how* it should reach them — for any industry, any company size, any product type. It is a strategy and framework skill, not an execution or financial-planning skill.

## Business Value

A weak or stale GTM strategy causes misaligned marketing spend, inconsistent messaging across sales and marketing, and wasted effort chasing the wrong segments. This skill gives Claude a repeatable, framework-driven way to produce GTM artifacts that are internally consistent (positioning informs messaging, ICP informs segmentation, segmentation informs channel choice) and immediately usable by marketing, sales, and product leadership — cutting the time to draft a quarterly GTM refresh from days to minutes while preserving strategic rigor.

## Activation Conditions

Invoke this skill when the user's request centers on defining or refreshing **strategic GTM inputs or outputs**: positioning, ICP, personas, segmentation, messaging, value proposition, competitive stance, GTM motion, or a quarterly GTM plan that synthesizes these. The request may name any industry, product type, or business model — this skill is industry-agnostic and must never assume a specific company as its worked example.

## Trigger Examples

- "Build a GTM strategy for our new product launch next quarter."
- "Refresh our positioning — we've moved upmarket."
- "Help me define our ICP for the enterprise segment."
- "We need buyer personas for our healthcare vertical."
- "Draft a messaging framework that differentiates us from [competitor]."
- "Write our Q3 go-to-market plan."
- "How should we segment the market for this new offering?"
- "Our sales team says marketing's messaging doesn't match what they hear from prospects — help us realign."
- "What's our value proposition for mid-market buyers?"
- "Review our current GTM plan and tell me what's missing."

## When NOT To Use

This skill covers GTM **strategy** only. Do not use it, and instead hand off to the named companion skill, when the request is primarily about:

- **Budget allocation or spend modeling** (how much to spend per channel, CAC/LTV modeling, media mix budgeting) → *Budget Allocator* skill.
- **Roadmap execution planning** (sprint plans, feature timelines, engineering sequencing, launch-day project plans) → *Quarterly Roadmap Planner* skill.
- **Board or executive narrative writing** (board decks, investor updates, quarterly business review narratives) → *Board Deck Narrative* skill.
- Pure creative copywriting/ad production with no strategic input required.
- Financial forecasting, pricing model construction, or sales compensation design.

If a request blends GTM strategy with one of these adjacent needs, complete the GTM-strategy portion with this skill and explicitly note that the remaining portion belongs to the companion skill.

## Scope

In scope: Positioning, Ideal Customer Profile (ICP), Buyer Personas, Market Segmentation, Messaging Strategy, Value Proposition, Competitive Positioning, GTM Motion (sales-led, product-led, partner-led, hybrid), Marketing Channel Strategy, Sales-Marketing Alignment recommendations.

Out of scope: budget/financial allocation, detailed execution/roadmap timelines, board-level financial narrative, legal/compliance review, pricing strategy construction (pricing may be referenced as an input, not designed here).

## Inputs

Claude should gather or reasonably assume (flagging assumptions explicitly) the following before producing outputs:
- Product/service description and category
- Target industry or verticals (if known)
- Current or desired customer segments
- Known competitors or competitive alternatives
- Existing positioning/messaging (if refreshing rather than starting fresh)
- Business goals for the period (e.g., growth, retention, expansion, new-market entry)
- Any known constraints (team size, budget tier, sales motion in place)

If inputs are missing, Claude should proceed using clearly labeled placeholder assumptions rather than blocking on the user, and should invite the user to correct assumptions.

## Outputs

Depending on the request, produce one or more of:
- Quarterly GTM Plan (see `templates/quarterly_gtm_plan_template.md`)
- Positioning Strategy (see `templates/positioning_canvas_template.md`)
- ICP Definition (see `templates/icp_template.md`)
- Buyer Persona Set (see `templates/buyer_persona_template.md`)
- Messaging Framework (see `templates/messaging_framework_template.md`)
- Channel Strategy summary (embedded in the Quarterly GTM Plan)
- Strategic Recommendations (a prioritized, rationale-backed list)

## Workflow

1. **Clarify the request type** — determine which output(s) are being asked for (full plan vs. a single artifact like ICP or messaging).
2. **Gather context** — collect the Inputs above from the conversation; note explicit assumptions for anything missing.
3. **Select the relevant frameworks** — consult `references/` for the specific artifact(s) needed (e.g., `references/positioning_framework.md` for positioning, `references/icp_framework.md` for ICP).
4. **Draft segmentation and ICP first** — these anchor everything downstream (see `references/market_segmentation.md`, `references/icp_framework.md`).
5. **Draft positioning and value proposition** — using `references/positioning_framework.md`, ensure it is differentiated against the competitive set (`references/competitive_analysis.md`).
6. **Draft messaging and personas** — using `references/messaging_framework.md` and `references/buyer_persona_guide.md`, ensure messaging maps to each persona's pains/gains.
7. **Select GTM motion and channels** — using `references/gtm_frameworks.md`, match motion/channels to segment buying behavior and company stage.
8. **Assemble the requested output(s)** using the matching file(s) in `templates/`, filling in placeholders with drafted content.
9. **Validate** the draft against `checklists/strategy_checklist.md` and `checklists/quality_checklist.md` before presenting it.
10. **Present output** with a short summary of key strategic choices and explicitly flagged assumptions, and note any adjacent work that belongs to a companion skill.

For structured internal prompting patterns, see `prompts/gtm_strategy_prompt.md`, `prompts/positioning_prompt.md`, `prompts/icp_prompt.md`, and `prompts/messaging_prompt.md`.

## Reasoning Guidelines

- Anchor every claim in a named framework (see `references/gtm_frameworks.md`) rather than generic marketing language.
- Keep positioning, ICP, personas, and messaging mutually consistent — a change in one should be checked against the others.
- Prefer specificity over breadth: a sharply defined ICP beats a broad, unfocused one.
- Make competitive differentiation concrete (specific capability/outcome gaps), not generic ("we're better/faster/easier").
- Distinguish clearly between facts provided by the user, reasonable inferences, and explicit assumptions.
- Never invent a fictional brand name as if it were a real reference case; use generic labels ("Company A," "a mid-market SaaS vendor") for illustrative examples.

## Best Practices

- Keep outputs actionable: every strategic statement should be usable by a marketer or seller within a week.
- Tie messaging pillars directly to ICP pains — do not produce messaging in isolation from persona research.
- Size the GTM motion to company stage/resources (a two-person marketing team cannot run a five-channel, high-touch ABM motion).
- Use the quarter's business goal (growth, expansion, retention) to prioritize which segments/channels matter most this quarter.
- Recommend a small number of high-conviction priorities rather than an exhaustive list of everything possible.

## Validation Rules

- Every output must name a specific target segment/ICP — "everyone" is not an acceptable target market.
- Positioning statements must include a frame of reference (category), a differentiator, and a proof point or reason to believe.
- Messaging must map to at least one persona and one competitive alternative.
- No output may reference a real named company as if it were the user's own company or as a factual case study.
- Quarterly plans must include measurable goals and at least one named channel/motion.

## Error Handling

- If the user's industry/product is unclear, ask one clarifying question or state the assumption used and proceed.
- If the request conflates GTM strategy with budget, roadmap, or board-narrative work, complete the GTM-strategy portion and clearly flag the rest for the appropriate companion skill.
- If prior GTM artifacts are provided but internally inconsistent (e.g., messaging contradicts positioning), surface the inconsistency before finalizing the refresh.
- If the request is too vague to produce a specific ICP/segment ("just make it good"), propose 2-3 plausible segment options and ask the user to choose, or proceed with the most common/defensible option clearly labeled as an assumption.

## Limitations

- This skill produces strategic drafts for human review — it does not replace market research, customer interviews, or win/loss data collection.
- It does not calculate budgets, media spend, or ROI projections.
- It does not produce detailed execution timelines or engineering/product roadmaps.
- It does not write board-facing financial narratives.
- Quality depends on the specificity of inputs provided; sparse inputs yield more assumption-heavy, generic output.

## Success Criteria

- Output correctly identifies which GTM artifact(s) were requested and produces all of them completely.
- Positioning, ICP, personas, messaging, and channel choices are mutually consistent.
- All claims are grounded in a named, standard framework rather than generic advice.
- No fictional brand is presented as a real example; all illustrative examples are generic/hypothetical.
- Assumptions are explicitly flagged, not silently embedded.
- Output passes `checklists/strategy_checklist.md`, `checklists/gtm_review_checklist.md`, and `checklists/quality_checklist.md`.
