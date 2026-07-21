# Forecasting Models

## Purpose
This document provides standalone reference knowledge on forecasting techniques used to project GTM outcomes (pipeline, revenue, CAC trend) from a proposed budget allocation, covering linear/trend-based regression, cohort-based forecasting, and pipeline-coverage modeling.

## Introduction
Forecasting translates a proposed budget allocation into an expected outcome — pipeline generated, revenue closed, customers acquired — so that stakeholders can evaluate whether a plan is likely to meet its targets before committing spend. No forecasting method is perfectly accurate; the goal is a reasonable, assumption-transparent projection with a clearly stated range of uncertainty, not a false-precision single number.

## Detailed Explanation

### Linear / Trend-Based Regression
Projects future output as a function of historical spend and output pairs, fitting a linear (or log-linear, to capture diminishing returns) relationship between spend and results.
- **Best for**: channels with a reasonably long, consistent history (6+ periods) and relatively stable market conditions.
- **Method**: plot historical spend vs. output (leads, pipeline, or revenue) for a channel, fit a trend line, and extrapolate to the proposed spend level. Log-linear or piecewise fits are preferred over simple linear fits once a channel shows signs of saturation (diminishing output per incremental dollar).
- **Limitation**: assumes the historical relationship continues to hold; breaks down for large step-changes in spend (extrapolating far beyond the observed data range is unreliable) and cannot anticipate structural changes (new competitor, platform policy change, market shift).

### Cohort-Based Forecasting
Tracks groups of customers or leads acquired in the same period (a "cohort") through their lifecycle (conversion, retention, expansion, churn) and uses observed cohort behavior to project future cohorts' performance.
- **Best for**: businesses with recurring revenue and enough historical cohorts (typically 4+ comparable cohorts) to identify a stable behavior pattern.
- **Method**: for each historical monthly/quarterly cohort, track conversion rate, average revenue, retention curve, and expansion. Apply the observed pattern (or a conservative blend of recent cohorts) to a new cohort implied by the proposed budget's expected lead/customer volume.
- **Limitation**: requires clean cohort-level data infrastructure; early cohorts may not yet show their full lifetime behavior (e.g., a 3-month-old cohort cannot yet show 12-month retention), so younger cohorts should be extrapolated carefully, not treated as complete.

### Pipeline-Coverage Modeling
Uses the ratio of pipeline generated to revenue closed (pipeline coverage ratio) to work backward from a revenue target to the pipeline — and therefore the spend — required to hit it.
Required Pipeline = Revenue Target x Pipeline Coverage Ratio
Required Spend = Required Pipeline / Historical Pipeline-per-Dollar-of-Spend (by channel)
- **Best for**: B2B/complex-sale businesses where a defined sales pipeline stage structure exists and historical stage-to-stage conversion rates are known.
- **Method**: establish the historical coverage ratio (commonly in the 3x-5x range, i.e., $3-5 of pipeline needed per $1 of closed revenue target, though this varies significantly by win rate and sales cycle), then translate the resulting pipeline requirement into a spend requirement using historical channel-level pipeline generation efficiency.
- **Limitation**: coverage ratios can shift when win rates, deal size, or sales cycle length change; using a stale coverage ratio will misstate the spend required.

### Choosing a Forecasting Model
- Use **linear/trend-based** for channels with ample consistent history and no anticipated structural change.
- Use **cohort-based** for recurring-revenue businesses where retention/expansion materially affects the return on acquisition spend.
- Use **pipeline-coverage** for complex B2B sales motions where the sales funnel stage structure is well understood.
- Blend methods when possible — e.g., use pipeline coverage to size the top-of-funnel requirement, then cohort-based projection to estimate downstream revenue and retention value.
- Always show a range (not a single point) when the underlying data has fewer than ~6 historical periods or when a channel is new.

## Professional Guidance
- State the model type and its core assumptions explicitly alongside every forecast number — a forecast without visible assumptions cannot be checked or updated later.
- Cross-check forecasts produced by different methods against each other when possible (e.g., does a cohort-based revenue projection roughly agree with a pipeline-coverage-based projection); a large discrepancy is a signal to investigate before trusting either number.
- Recompute forecasting inputs (spend/output ratios, coverage ratios, cohort curves) at least quarterly; these drift as market conditions, competition, and product-market fit evolve.
- Present forecasts with an explicit confidence qualifier (e.g., "high confidence — based on 8 stable historical periods" vs. "directional estimate — based on 2 periods of a new channel").

## Examples
**Linear/trend example**: Historical data shows paid search spend of $50k/$75k/$100k per month produced 200/280/340 leads respectively (a decelerating trend). A log-linear fit projects $125k in spend would produce approximately 385 leads — used instead of a naive linear extrapolation that would overstate the result.

**Cohort-based example**: The March cohort of 60 customers showed 92% month-3 retention and $450 average monthly revenue; applying this pattern to a projected 90-customer May cohort (implied by proposed spend) forecasts $37,000+ in month-3 recurring revenue from that cohort alone.

**Pipeline-coverage example**: Revenue target of $2M for the quarter, historical coverage ratio of 4x, implies $8M of pipeline required. If historical data shows $1 of spend generates $20 of pipeline (blended across channels), required spend ≈ $400,000.

## Common Mistakes
- Extrapolating a linear trend far beyond the range of observed historical spend levels.
- Using a single-cohort snapshot to project future cohort behavior instead of a blend of several recent cohorts.
- Applying a stale pipeline coverage ratio after win rates or deal size have shifted materially.
- Presenting a forecast as a single precise number without a range or confidence qualifier.
- Ignoring seasonality (e.g., typical slowdowns in certain periods) when extrapolating trend lines.

## Best Practices
- Always pair a point forecast with a range reflecting the underlying data's uncertainty.
- Reconcile forecasts from at least two methods when stakes are high (e.g., pipeline-coverage and cohort-based) before finalizing a plan.
- Refresh model inputs at least quarterly, and immediately after any material shift in win rate, deal size, or sales cycle length.
- Disclose the historical data window and number of periods used to build each forecasting model.

## Summary
Linear/trend-based, cohort-based, and pipeline-coverage forecasting each translate historical GTM data into a forward-looking projection, but each rests on different assumptions and data requirements. A production-grade budget forecast selects the model that matches the available data and sales motion, states its assumptions and confidence level explicitly, and cross-checks results across methods when the decision stakes are high.
