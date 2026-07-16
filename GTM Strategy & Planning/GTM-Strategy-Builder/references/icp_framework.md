# Ideal Customer Profile (ICP) Framework

**Purpose of this document:** Equip Claude with a rigorous, standard method for defining and scoring an Ideal Customer Profile that is specific enough to drive targeting decisions, independent of industry.

## Introduction

An Ideal Customer Profile (ICP) describes the type of account (company/organization) most likely to buy, succeed with, and expand usage of a product — the target that yields the best combination of win rate, deal size, time-to-close, retention, and lifetime value. ICP is an account-level construct (the organization), distinct from buyer personas, which describe individual roles within that account (see `buyer_persona_guide.md`). A precise ICP is the foundation for segmentation, messaging relevance, and channel selection.

## Detailed Explanation

### ICP Dimensions
A complete ICP is defined across four dimension categories:
1. **Firmographic** — company size (employees/revenue), industry/vertical, geography, growth stage, ownership structure (public/private/PE-backed).
2. **Technographic** — existing technology stack, tools already in use, integration requirements, technical maturity.
3. **Behavioral/operational** — how the organization currently solves the problem (status quo process), buying process maturity, budget cycle, team structure relevant to the purchase.
4. **Situational/trigger** — events that increase propensity to buy now (e.g., recent funding, leadership change, compliance deadline, rapid headcount growth, expansion into a new market).

### Fit vs. Propensity
ICP definition should separate two related but distinct questions:
- **Fit:** Would this account succeed with and get value from the product if they adopted it? (structural/firmographic/technographic match)
- **Propensity/intent:** Is this account likely to be actively evaluating or ready to buy right now? (behavioral/trigger signals)
High-fit, high-propensity accounts are the priority target; high-fit/low-propensity accounts are nurture candidates; low-fit accounts should generally be deprioritized regardless of apparent interest, since they tend to churn or extract disproportionate support cost even if they buy.

### ICP Scoring Model
A practical ICP scoring approach assigns weighted criteria across the dimensions above and produces a tiered output:
- Define 5-8 scoring criteria drawn from firmographic/technographic/behavioral/trigger dimensions.
- Weight criteria by demonstrated correlation with successful outcomes (win rate, retention, expansion) where historical data exists; where data does not exist, weight by logical proximity to the value proposition (criteria closest to the core problem solved should weigh most).
- Score accounts (or account types) against the criteria to produce tiers, e.g., Tier 1 ("Best-fit," proactively targeted), Tier 2 ("Good-fit," served but not proactively prioritized), Tier 3 ("Poor-fit," deprioritized or redirected to self-serve/low-touch).
- Revisit and re-weight the model periodically using actual win/loss and retention data as it accumulates (see `competitive_analysis.md` for win/loss method) — an ICP model should get sharper over time, not stay static.

### Anti-ICP (Negative Criteria)
An often-overlooked but critical component: explicitly define the *anti-ICP* — account characteristics that reliably predict poor fit, churn, or excessive service cost (e.g., "single-location businesses under a certain size," "organizations without a named technical owner," "accounts requiring capabilities structurally outside the product's design"). Naming the anti-ICP prevents sales and marketing from spending resources on unwinnable or unprofitable accounts and sharpens targeting more than positive criteria alone.

### One ICP or Several?
Most companies benefit from a primary ICP with 1-2 clearly bounded secondary ICPs (e.g., by vertical or by company-size tier), rather than either a single overly-broad ICP or an unbounded list of many ICPs that dilutes focus. Each additional ICP should only be added if it justifies distinct messaging, channel, or motion decisions — otherwise it belongs inside the primary ICP as a segment variation (see `market_segmentation.md`).

## Professional Guidance

Always ground ICP criteria in evidence where available: existing customer data (best accounts by retention/expansion/NPS), win/loss interviews, and sales team pattern-recognition. Where no such data exists (new product/company), construct a hypothesis-driven ICP explicitly labeled as a hypothesis to be validated with the first cohort of customers, rather than presenting it with false confidence as data-backed. Always produce both positive (best-fit) and negative (anti-ICP) criteria.

## Examples

- *B2B SaaS:* Primary ICP — mid-market companies (200-2,000 employees), operations or IT department buyer, existing use of at least one adjacent workflow tool, recent headcount growth signaling scaling pain. Anti-ICP — sole proprietors and companies under 20 employees lacking a dedicated technical owner.
- *Healthcare:* Primary ICP — multi-site outpatient clinic groups (10+ locations) with a compliance officer role, currently using manual/paper-based audit processes. Anti-ICP — single-location independent practices without dedicated administrative staff.
- *Industrial/manufacturing:* Primary ICP — mid-size manufacturers (100-1,000 employees) running continuous-process equipment, with a named plant operations or reliability engineering lead, currently relying on manual inspection rounds. Anti-ICP — job-shop/one-off manufacturers with no continuous-process equipment.

## Common Mistakes

- Defining ICP purely by firmographics (size/industry) while ignoring behavioral and trigger signals that actually predict propensity to buy.
- Treating "anyone who could technically use the product" as the ICP instead of the subset that gets the most value fastest.
- Skipping the anti-ICP, leading sales to chase low-fit accounts that inflate pipeline but rarely close well or retain.
- Never revisiting ICP after launch, even as real customer data accumulates that should sharpen or correct the original hypothesis.
- Confusing ICP (account-level) with buyer persona (individual-level) and blending the two into one unfocused document.

## Best Practices

- Separate fit criteria from propensity/trigger criteria explicitly.
- Always include an anti-ICP alongside the positive ICP.
- Use a simple weighted scoring model with tiers (best-fit / good-fit / poor-fit) rather than a binary yes/no definition.
- Ground criteria in real customer data when available; clearly label hypothesis-based criteria when it is not.
- Limit to one primary ICP plus at most 1-2 clearly justified secondary ICPs.
- Revisit ICP each quarter or whenever new win/loss or retention data materially updates the hypothesis.

## Summary

The ICP defines which accounts are worth targeting, expressed across firmographic, technographic, behavioral, and trigger dimensions, and separated into fit (would they succeed) versus propensity (are they ready now). A weighted, tiered scoring model — paired with an explicit anti-ICP — produces a sharper, more actionable target than a broad or purely firmographic definition. ICP should be evidence-based where data exists, clearly labeled as hypothesis where it does not, and refreshed periodically as real outcomes accumulate.
