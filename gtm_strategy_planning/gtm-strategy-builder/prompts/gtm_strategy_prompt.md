# Internal Prompt: Full Quarterly GTM Strategy Generation

**Purpose of this document:** Document the reusable internal prompt pattern Claude should adapt when asked to produce a full quarterly GTM plan (as opposed to a single sub-artifact like ICP or messaging alone). This is an internal reasoning aid, not a user-facing template.

## Purpose

Guide Claude through synthesizing segmentation, ICP, positioning, personas, messaging, and channel/motion decisions into one coherent Quarterly GTM Plan, in the correct dependency order, while explicitly flagging assumptions and out-of-scope adjacent work.

## Inputs

Claude needs (gathered from conversation or reasonably assumed and flagged):
- `product_description`: what the product/service is and its category
- `business_goal`: the primary goal for the quarter (growth, expansion, retention, new-market entry)
- `known_segments_or_customers`: any existing customer base or target description
- `known_competitors`: named competitors or alternatives, if any
- `existing_gtm_artifacts`: prior positioning/messaging/ICP if this is a refresh rather than a fresh build
- `constraints`: team size, resourcing, budget tier, existing sales motion
- `industry_context`: the industry/vertical, used only to keep examples and channel choices realistic — never to imply this skill is industry-specific

## Instructions

Use this reasoning sequence (adapt wording naturally; do not expose this as raw text to the user):

```
1. Restate the business goal for this quarter in one sentence, and identify what "success"
   looks like at the end of the quarter for that goal.
2. Using references/market_segmentation.md, identify 2-4 candidate market segments relevant
   to the stated goal. Score them on size, reachability, willingness-to-pay, competitive
   intensity, and time-to-proof. Select the priority segment(s) for this quarter.
3. Using references/icp_framework.md, define the ICP for the priority segment(s): firmographic,
   technographic, behavioral, and trigger criteria, plus an explicit anti-ICP.
4. Using references/positioning_framework.md, map competitive alternatives (direct, indirect,
   status quo) and unique attributes, choose a category/frame of reference, and draft the
   positioning statement.
5. Using references/buyer_persona_guide.md, define 2-4 personas within the priority ICP(s),
   each with JTBD, pains, gains, objections, and decision criteria.
6. Using references/messaging_framework.md, derive 3-4 messaging pillars from the positioning
   differentiator and persona pains/gains, each with a proof point and persona-specific variants.
7. Using references/gtm_frameworks.md, select the GTM motion (sales-led/product-led/
   marketing-led/partner-led/hybrid) matched to deal complexity and buyer autonomy, then select
   2-4 channels matched to where the priority personas actually research and buy.
8. Identify sales-alignment needs (handoff criteria, enablement assets, feedback cadence).
9. Set 2-4 measurable quarterly goals tied to the stated business goal.
10. Write 3-5 prioritized strategic recommendations, ordered by conviction and impact.
11. Explicitly list assumptions made due to missing information.
12. Explicitly list anything requested that belongs to a companion skill (Budget Allocator,
    Quarterly Roadmap Planner, Board Deck Narrative) rather than this one.
13. Assemble the full output using templates/quarterly_gtm_plan_template.md as the structure.
14. Validate against checklists/strategy_checklist.md, checklists/gtm_review_checklist.md, and
    checklists/quality_checklist.md before presenting.
```

## Expected Output

A complete Quarterly GTM Plan following `templates/quarterly_gtm_plan_template.md`, with every placeholder replaced by drafted content, assumptions clearly flagged in the Assumptions section, and any out-of-scope requests noted in the "Explicitly Out of Scope" section with a pointer to the correct companion skill.

## Validation Checklist

- [ ] Priority segment(s) and ICP are specific, not "everyone"
- [ ] Positioning statement includes target customer, category, differentiator, and reason to believe
- [ ] At least 2 personas defined and linked to messaging pillars
- [ ] Messaging pillars each have a proof point
- [ ] GTM motion and channel choices are justified by ICP/persona behavior, not asserted generically
- [ ] Quarterly goals are measurable and tied to the stated business goal
- [ ] Assumptions are explicitly listed, not silently embedded
- [ ] Any budget, roadmap-execution, or board-narrative content is flagged as out of scope with the correct companion skill named
