# Internal Prompt: Positioning Statement Generation

**Purpose of this document:** Document the reusable internal prompt pattern Claude should adapt when asked specifically to create or refresh positioning (not a full quarterly plan). This is an internal reasoning aid, not a user-facing template.

## Purpose

Guide Claude through the competitive-alternative-first method in `references/positioning_framework.md` to produce a defensible, differentiated positioning statement rather than a generic tagline.

## Inputs

- `product_description`: what the product/service does
- `target_customer`: the segment/ICP this positioning targets (from `icp_template.md` if available)
- `known_alternatives`: named competitors and/or status quo behavior, if known
- `existing_positioning`: prior positioning statement, if this is a refresh
- `evidence_available`: any win/loss data, customer interviews, or capability documentation available to ground claims

## Instructions

```
1. List every competitive alternative the target customer would actually consider, in three
   tiers: direct competitors, indirect/adjacent alternatives, and status quo/non-consumption
   (manual process, spreadsheet, in-house build, or doing nothing). Do not skip status quo.
2. List the unique attributes/capabilities this product/company has that those alternatives lack.
   If evidence_available includes win/loss data, prioritize attributes confirmed by that data
   over internally-assumed ones.
3. Translate each unique attribute into a customer-facing outcome/value statement.
4. Confirm which target customer segment values that outcome most (cross-check against
   references/icp_framework.md and references/market_segmentation.md if available).
5. Choose a market category (frame of reference) deliberately: compete in an existing category,
   position as leader/challenger within it, or reframe/create a category. State the tradeoff
   for the choice made (comprehension speed vs. differentiation upside).
6. Assemble the positioning statement:
   "For [target customer] who [need], [product] is the [category] that [differentiator],
   because [reason to believe] — unlike [primary alternative], which [limitation]."
7. Write a shorter customer-facing value proposition derived from the statement.
8. Explicitly flag any differentiator claim that lacks a proof point as unvalidated, and
   suggest the validation step needed (e.g., win/loss interview, capability audit).
9. If existing_positioning was provided, note specifically what changed and why (segment shift,
   competitive shift, or new evidence) rather than silently replacing it.
```

## Expected Output

A completed `templates/positioning_canvas_template.md`, including the full 10-step canvas and the final positioning statement and value proposition, with any unvalidated claims clearly flagged.

## Validation Checklist

- [ ] Status quo/non-consumption alternative included, not just named competitors
- [ ] Positioning statement contains all five components (target, category, differentiator, reason to believe, value)
- [ ] Category choice is stated deliberately with rationale, not defaulted without comment
- [ ] Every differentiator claim is either backed by a proof point or explicitly flagged as unvalidated
- [ ] If refreshing existing positioning, the delta and its rationale is stated explicitly
