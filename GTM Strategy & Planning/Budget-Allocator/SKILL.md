---
name: Budget-Allocator
description: Models and optimizes go-to-market budget allocation across marketing and sales channels using historical performance metrics, CAC, ROI, and LTV:CAC data. Use when a user needs to build a budget allocation model, reallocate spend across channels, calculate or analyze customer acquisition cost (CAC), forecast return on marketing investment, run best/base/worst-case budget scenarios, or optimize spend distribution given a fixed or changing budget. Do not use for writing GTM positioning/messaging strategy, quarterly roadmap timelines, or board narrative decks — those are handled by separate skills.
---

# Budget-Allocator

## Purpose

The Budget Allocator skill models, evaluates, and optimizes go-to-market (GTM) budget allocation across marketing and sales channels. It applies financial and marketing-operations methodology — CAC calculation, ROI/ROAS modeling, LTV:CAC analysis, channel mix strategy, forecasting, and scenario planning — to turn historical performance data and business constraints into a defensible, quantified spend plan.

This skill is a financial modeling and optimization engine for GTM spend. It is industry-agnostic and works from whatever historical metrics, targets, and constraints the user supplies.

## Business Value

- Converts historical channel performance into a forward-looking, defensible budget plan.
- Identifies over- and under-invested channels using CAC, ROI, and marginal-return signals.
- Produces scenario-tested plans (best/base/worst case) so budget decisions survive demand or cost shocks.
- Gives finance and revenue leaders a shared, auditable model instead of ad-hoc spreadsheet guesses.
- Speeds up planning cycles (quarterly/annual budgeting, mid-cycle reallocation, budget-cut response).

## Activation Conditions

Invoke this skill when the user's request centers on **quantifying, allocating, reallocating, forecasting, or optimizing GTM/marketing spend or channel investment**, typically involving numbers such as budget totals, CAC, ROI/ROAS, LTV, conversion rates, or pipeline coverage.

## Trigger Examples

- "Help me allocate our $2M marketing budget across channels for next quarter."
- "Our CAC on paid social jumped 40% — should we shift budget to organic?"
- "Build a ROI forecast for a 15% increase in event marketing spend."
- "We need to cut the marketing budget by 20% — what should we cut first?"
- "Model best/base/worst case scenarios for next year's demand gen budget."
- "Calculate fully-loaded CAC by channel from this spend and pipeline data."
- "What's the optimal channel mix if we're launching in a new region with no history?"
- "Compare LTV:CAC ratios across our channels and recommend reallocation."
- "Forecast Q4 pipeline and revenue if we hold the current spend distribution."
- "Build a zero-based budget for a new product line's go-to-market spend."

## When NOT To Use

This skill does **not**:
- Write GTM positioning, messaging, or narrative strategy (use a GTM Strategy Builder skill).
- Build quarterly roadmap timelines, launch plans, or milestone sequencing (use a Quarterly Roadmap Planner skill).
- Produce board-ready narrative decks, executive storylines, or slide copy (use a Board Deck Narrative skill).
- Perform general financial accounting, tax, payroll, or non-GTM corporate budgeting.
- Generate creative assets, campaign copy, or channel-specific creative briefs.

If a request is purely about narrative, positioning, timelines, or slide storytelling with no budget/spend/ROI quantification, do not activate this skill — hand off to the relevant skill instead (see `FAQs/faq.md` for handoff patterns).

## Scope

In scope: budget planning frameworks, CAC calculation and analysis, ROI/ROAS/LTV modeling, channel strategy and mix optimization, forecasting, scenario and sensitivity planning, spend reallocation, and budget review/optimization outputs.

Out of scope: messaging/positioning, roadmap/timeline planning, board storytelling, non-GTM finance operations.

## Inputs

Typical inputs the user may supply (not all are required — see reference files for handling missing data):
- Total available budget (period, currency, constraints)
- Historical channel spend and results (leads, opportunities, pipeline, closed revenue, customers acquired)
- Current or target CAC, LTV, ROI/ROAS by channel
- Sales cycle length and conversion rates by stage
- Growth targets (revenue, customer count, pipeline) for the planning period
- Known constraints (minimum channel commitments, contractual spend, headcount-linked costs)
- Planning horizon (monthly, quarterly, annual) and scenario requirements

## Outputs

- **Budget Allocation Model** — recommended spend distribution across channels with rationale
- **Channel Recommendations** — which channels to grow, hold, or cut, and why
- **ROI Forecast** — projected return, ROAS, and payback by channel and in aggregate
- **CAC Analysis** — fully-loaded CAC by channel, trend, and payback period
- **Spend Distribution** — a table/breakdown of dollars (or % of budget) by channel and period

## Workflow

1. **Clarify inputs**: Confirm total budget, planning horizon, available historical data, and any hard constraints. If data is missing, note assumptions explicitly (see `references/budget_planning.md`).
2. **Establish baseline**: Summarize current or most-recent channel performance (spend, CAC, ROI, conversion) using `references/cac_calculation.md` and `references/roi_framework.md`.
3. **Select planning approach**: Choose top-down, bottom-up, or zero-based methodology per `references/budget_planning.md`, based on data maturity and organizational context.
4. **Apply channel strategy**: Evaluate channel mix (paid, organic, partner, events, ABM, etc.) using `references/channel_strategy.md`.
5. **Build the forecast**: Project outcomes (pipeline, revenue, CAC trend) using an appropriate model from `references/forecasting_models.md`.
6. **Run scenarios**: Stress-test the plan with best/base/worst case and sensitivity analysis per `references/scenario_planning.md`, especially for budget cuts or high-uncertainty channels.
7. **Optimize allocation**: Reallocate toward channels with favorable marginal CAC/ROI/LTV:CAC, respecting constraints; flag over-concentration risk.
8. **Produce outputs**: Populate the relevant template(s) from `templates/` and present the Budget Allocation Model, Channel Recommendations, ROI Forecast, CAC Analysis, and Spend Distribution.
9. **Validate**: Apply `checklists/quality_checklist.md` and `checklists/budget_review_checklist.md` before finalizing.
10. **State assumptions and limitations**: Always disclose data gaps, confidence level, and sensitivity of key numbers.

## Reasoning Guidelines

- Prefer marginal-return thinking over average-return thinking when reallocating budget between channels.
- Treat CAC and ROI trends (direction over time) as more informative than single-period snapshots.
- When historical data is thin or a channel is new, use category benchmarks and clearly label figures as estimates, not facts.
- Always reconcile bottom-up channel plans against the top-down total budget constraint.
- Do not present a single-point forecast without at least a base case and one alternative scenario when uncertainty is material.
- Distinguish correlation (channel activity coincided with growth) from causation (channel activity caused growth) when historical data is sparse or attribution is weak.

## Best Practices

- Use fully-loaded CAC (including tooling, salaries, agency fees) not just media spend, whenever data allows.
- Express recommendations in ranges when confidence is low, not false-precision point estimates.
- Tie every reallocation recommendation to a specific metric movement (e.g., "CAC payback improved from 14 to 9 months").
- Keep the model reusable — no hardcoded industry assumptions unless the user specifies their industry/context.
- Surface concentration risk if any single channel exceeds roughly 50-60% of total budget without strong justification.

## Validation Rules

- Total allocated spend across channels must equal the stated total budget (no silent rounding drift beyond de minimis amounts).
- Every CAC, ROI, or LTV figure presented must have its calculation basis stated or referenced.
- Scenario outputs (best/base/worst) must use internally consistent assumptions across channels.
- Flag and do not silently resolve any contradictions between user-supplied figures (e.g., conflicting CAC values for the same channel).

## Error Handling

- **Missing historical data**: Proceed using industry-typical benchmark ranges, clearly labeled as assumptions, and recommend a data-collection plan.
- **Conflicting inputs**: Surface the conflict to the user rather than guessing; ask which figure is authoritative if it changes the recommendation materially.
- **Budget insufficient for stated targets**: State the gap explicitly and offer trade-off options (reduce targets, extend timeline, increase budget) rather than silently inflating projected ROI.
- **Out-of-scope request embedded in a budget conversation** (e.g., "also write our board narrative"): Complete the budget-related portion and note that the narrative/positioning/roadmap portion belongs to a different skill.

## Limitations

- Forecasts are only as reliable as the historical data and assumptions provided; this skill does not fabricate data.
- Attribution across channels is inherently imperfect (multi-touch effects); models here use simplifying assumptions that should be disclosed.
- This skill does not perform real-time data pulls from ad platforms, CRMs, or BI tools — it works from data supplied in the conversation.
- Not a substitute for formal financial/accounting sign-off on budget commitments.

## Success Criteria

- Recommended allocation sums correctly to the stated budget.
- Every output (Budget Allocation Model, Channel Recommendations, ROI Forecast, CAC Analysis, Spend Distribution) is present when requested.
- Assumptions and data gaps are explicitly disclosed.
- At least one alternative scenario is provided when uncertainty is material.
- Output is immediately usable by a marketing/finance stakeholder without further translation.
