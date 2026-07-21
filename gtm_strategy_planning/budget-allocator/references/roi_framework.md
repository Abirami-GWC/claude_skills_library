# ROI Framework

## Purpose
This document provides standalone reference knowledge on ROI, ROAS, and LTV:CAC modeling for GTM spend, giving a consistent way to measure and compare the financial return of budget allocated to different channels and programs.

## Introduction
Return on Investment (ROI) answers the question "did this spend generate more value than it cost?" In GTM budget allocation, ROI is usually expressed through three related but distinct metrics: ROI itself, Return on Ad Spend (ROAS), and the ratio of customer Lifetime Value to Customer Acquisition Cost (LTV:CAC). Using the right metric for the right question — and understanding the assumptions behind each — is essential to avoid both over- and under-investing in a channel.

## Detailed Explanation

### ROI
ROI (%) = (Value Generated - Cost of Spend) / Cost of Spend x 100

"Value generated" should be defined precisely — closed revenue, gross margin dollars, or pipeline value weighted by expected close rate, depending on how conservative the analysis needs to be. Revenue-based ROI overstates return for low-margin businesses; margin-based ROI is more decision-useful for budget allocation because it reflects money the business actually keeps.

### ROAS
ROAS = Revenue Attributable to Spend / Spend

ROAS is a simpler, revenue-only ratio commonly used for paid media channels where attribution is relatively direct (e.g., paid search, paid social). A ROAS of 4x means $4 of attributed revenue for every $1 spent. ROAS does not account for margin, fixed costs, or the time value of the return, so it should be treated as a directional efficiency signal, not a full financial return measure.

### LTV:CAC
LTV:CAC = Customer Lifetime Value / Customer Acquisition Cost

Customer Lifetime Value (LTV) is typically estimated as:
LTV = Average Revenue per Customer per Period x Gross Margin % x Average Customer Lifespan (periods) x Retention adjustment

A commonly cited healthy benchmark is an LTV:CAC ratio of roughly 3:1 or higher for subscription/recurring-revenue businesses, though the "right" ratio depends on growth stage (early-stage, growth-focused businesses may intentionally accept a lower ratio to capture market share, while mature businesses often optimize for a higher ratio and better cash efficiency). A ratio below roughly 1:1 signals the business is losing money on every customer acquired before accounting for any other costs.

### Marginal vs. Average Return
The most common analytical error in ROI-based budget allocation is optimizing on **average** ROI/ROAS rather than **marginal** ROI/ROAS. A channel may show a strong average ROAS while its next incremental dollar of spend produces a much weaker return (diminishing marginal returns as a channel becomes saturated — e.g., bidding up an already-saturated paid search auction). Where data allows, model the marginal return curve (e.g., via spend-response testing or historical spend/output pairs at different budget levels) rather than assuming a flat return per dollar.

### Time Horizon
ROI/ROAS/LTV:CAC calculations must specify a time horizon. Short-cycle channels (paid search, paid social) can be measured on a rolling 30-90 day basis. Long-cycle channels (enterprise field sales, large partner deals, brand/awareness spend) require a longer measurement window (2-4+ quarters) before the return is fully realized; judging a long-cycle channel on a 30-day window will systematically undervalue it.

## Professional Guidance
- Always state which "value" definition is used (revenue, margin, or pipeline-weighted) alongside any ROI/ROAS figure.
- Use ROAS for fast-attribution paid channels; use ROI (margin-based) for cross-channel comparisons; use LTV:CAC for evaluating the durability of unit economics over the full customer relationship.
- When possible, model marginal return curves instead of relying solely on average return, especially before recommending a large increase in spend to an already-funded channel.
- Match the measurement window to the channel's natural sales cycle; do not apply a single universal window across channels with very different cycle lengths.

## Examples
**ROI example**: A campaign costs $50,000 and generates $180,000 in gross margin dollars attributable to it. ROI = ($180,000 - $50,000) / $50,000 x 100 = 260%.

**ROAS example**: Paid social spend of $30,000 generates $105,000 in attributed revenue. ROAS = $105,000 / $30,000 = 3.5x.

**LTV:CAC example**: Average customer generates $600/month revenue at 65% gross margin, with an average lifespan of 30 months. LTV = $600 x 0.65 x 30 = $11,700. If CAC = $3,000, LTV:CAC = 3.9:1, generally considered healthy.

**Marginal return example**: A channel currently spending $200,000/month shows average ROAS of 4x, but the last $50,000 increment (tested via a spend increase) only produced 1.2x incremental ROAS — signaling the channel is near saturation and further scaling should shift to a different channel instead.

## Common Mistakes
- Quoting ROI or ROAS without specifying whether it is revenue-based or margin-based.
- Assuming a channel's average return applies uniformly to the next incremental dollar (ignoring diminishing marginal returns).
- Judging long-sales-cycle channels (events, ABM, enterprise field) on a short measurement window that understates their true return.
- Treating LTV as a fixed number rather than updating it as retention/churn data matures.
- Comparing ROAS (revenue-only) directly against ROI (margin-based) as if they were the same metric.

## Best Practices
- Report ROI, ROAS, and LTV:CAC together for the most important channels rather than relying on a single metric.
- Model at least a simple marginal-return curve (e.g., three spend levels: current, +20%, -20%) before recommending large reallocations.
- Recompute LTV assumptions at least twice a year as retention and expansion data mature.
- Always pair a return metric with its time horizon and value definition when presenting to stakeholders.

## Summary
ROI, ROAS, and LTV:CAC each measure return from a different angle: ROI measures overall financial return net of cost, ROAS measures revenue efficiency of ad spend specifically, and LTV:CAC measures the durability of the customer relationship relative to acquisition cost. Effective budget allocation uses marginal — not average — return thinking and matches the measurement window to each channel's natural sales cycle.
