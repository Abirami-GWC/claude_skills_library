# Budget Model Template

**Purpose of this file**: A fill-in-the-blank template for building a channel-level GTM budget allocation model. Copy this template and replace all bracketed placeholders with actual figures. See `references/budget_planning.md` for methodology guidance on choosing top-down, bottom-up, or zero-based approach.

---

## 1. Planning Parameters

| Field | Value |
|---|---|
| Planning horizon | [PLANNING_PERIOD, e.g., Q3 2026 / FY2027] |
| Total available budget | [TOTAL_QUARTERLY_BUDGET] |
| Currency | [CURRENCY] |
| Planning approach | [TOP_DOWN / BOTTOM_UP / ZERO_BASED / BLENDED] |
| Revenue target for period | [REVENUE_TARGET] |
| Customer/new-logo target for period | [CUSTOMER_TARGET] |
| Reserve / contingency held back | [RESERVE_AMOUNT] ([RESERVE_PERCENT]% of total) |

## 2. Channel Allocation Table

*Instruction: list every channel under consideration, including channels not currently funded, per zero-based discipline. Add rows as needed.*

| Channel Name | Prior Period Spend | Prior Period CAC | Prior Period ROI/ROAS | Proposed Spend | % of Total Budget | Rationale |
|---|---|---|---|---|---|---|
| [CHANNEL_NAME_1] | [PRIOR_SPEND_1] | [HISTORICAL_CAC_1] | [PRIOR_ROI_1] | [PROPOSED_SPEND_1] | [PCT_1]% | [RATIONALE_1] |
| [CHANNEL_NAME_2] | [PRIOR_SPEND_2] | [HISTORICAL_CAC_2] | [PRIOR_ROI_2] | [PROPOSED_SPEND_2] | [PCT_2]% | [RATIONALE_2] |
| [CHANNEL_NAME_3] | [PRIOR_SPEND_3] | [HISTORICAL_CAC_3] | [PRIOR_ROI_3] | [PROPOSED_SPEND_3] | [PCT_3]% | [RATIONALE_3] |
| [CHANNEL_NAME_N] | [PRIOR_SPEND_N] | [HISTORICAL_CAC_N] | [PRIOR_ROI_N] | [PROPOSED_SPEND_N] | [PCT_N]% | [RATIONALE_N] |
| **Total** | [SUM_PRIOR_SPEND] | — | — | [SUM_PROPOSED_SPEND] | 100% | — |

*Validation: [SUM_PROPOSED_SPEND] + [RESERVE_AMOUNT] must equal [TOTAL_QUARTERLY_BUDGET].*

## 3. Fixed / Non-Channel Costs

*Instruction: list committed costs not tied to a specific acquisition channel (tooling, salaries not allocated above, contracts).*

| Cost Item | Amount | Notes |
|---|---|---|
| [FIXED_COST_ITEM_1] | [FIXED_COST_AMOUNT_1] | [NOTES_1] |
| [FIXED_COST_ITEM_2] | [FIXED_COST_AMOUNT_2] | [NOTES_2] |

## 4. Payback / Tier Classification

*Instruction: classify each channel into a payback tier per `references/channel_strategy.md`.*

| Channel Name | Tier (Fast / Medium / Slow Payback) | Expected Payback Window |
|---|---|---|
| [CHANNEL_NAME_1] | [TIER_1] | [PAYBACK_WINDOW_1] |
| [CHANNEL_NAME_2] | [TIER_2] | [PAYBACK_WINDOW_2] |

## 5. Assumptions & Data Gaps

*Instruction: list every assumption made and every data point that was estimated rather than sourced from actuals.*

- [ASSUMPTION_1]
- [ASSUMPTION_2]
- [DATA_GAP_1] — estimated using [BENCHMARK_SOURCE_OR_METHOD]

## 6. Sign-Off

| Role | Name | Date |
|---|---|---|
| Prepared by | [PREPARER_NAME] | [DATE] |
| Reviewed by | [REVIEWER_NAME] | [DATE] |
| Approved by | [APPROVER_NAME] | [DATE] |
