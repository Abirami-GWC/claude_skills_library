# Internal Prompt: ICP Definition Generation

**Purpose of this document:** Document the reusable internal prompt pattern Claude should adapt when asked specifically to define or refresh an Ideal Customer Profile. This is an internal reasoning aid, not a user-facing template.

## Purpose

Guide Claude through the fit-versus-propensity method in `references/icp_framework.md` to produce a specific, scoreable ICP (plus anti-ICP) rather than a vague target description.

## Inputs

- `product_description`: what the product/service does and the core problem it solves
- `existing_customer_data`: any known best customers, retention/expansion patterns, or notable churn patterns
- `market_segmentation`: candidate segments already identified (from `market_segmentation.md`/`icp_template.md`), if available
- `industry_context`: relevant industry/vertical context, kept generic and not tied to any single named company
- `evidence_available`: win/loss interviews, sales pattern-recognition, or purely hypothesis-stage reasoning

## Instructions

```
1. Identify the priority segment(s) this ICP will describe (link to market_segmentation.md
   output if available; otherwise propose 1-2 plausible segments and state that as an
   assumption).
2. Define firmographic criteria: size, industry/vertical, geography, growth stage, ownership.
3. Define technographic criteria: expected existing stack, integration needs, technical maturity.
4. Define behavioral/operational criteria: current status-quo process, buying process maturity,
   team structure, budget cycle.
5. Define trigger/situational criteria: events that increase propensity to buy now.
6. Explicitly define the anti-ICP: characteristics predicting poor fit, churn, or high service
   cost, even if such accounts show apparent interest.
7. Build a lightweight weighted scoring model (5-8 criteria) and define tier thresholds
   (best-fit / good-fit / poor-fit).
8. State the evidence basis for each major criterion: grounded in real customer data, grounded
   in win/loss interviews, or hypothesis-only (and if hypothesis-only, propose a validation step).
9. Identify the persona(s) that exist within this ICP (link to buyer_persona_guide.md /
   buyer_persona_template.md) without fully building them out here unless requested.
10. Write a one-line ICP summary usable inside a Quarterly GTM Plan.
```

## Expected Output

A completed `templates/icp_template.md`, including firmographic/technographic/behavioral/trigger criteria, an explicit anti-ICP, a weighted scoring model with tiers, and a clearly labeled evidence basis.

## Validation Checklist

- [ ] ICP is specific enough to exclude a clear majority of the theoretical market (not "everyone")
- [ ] All four dimension categories (firmographic, technographic, behavioral, trigger) are addressed
- [ ] An explicit anti-ICP is included, not just positive criteria
- [ ] A scoring model with tiers is included, not a binary yes/no definition
- [ ] Evidence basis is stated per major criterion, with hypothesis-only criteria clearly flagged
- [ ] ICP is linked to at least one persona placeholder for downstream messaging work
