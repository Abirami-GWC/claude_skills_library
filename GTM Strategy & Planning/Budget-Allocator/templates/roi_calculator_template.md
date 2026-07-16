# ROI Calculator Template

**Purpose of this file**: A fill-in-the-blank template for calculating ROI, ROAS, and LTV:CAC by channel. Copy this template and replace bracketed placeholders. See `references/roi_framework.md` for full methodology.

---

## 1. Inputs by Channel

*Instruction: complete one row per channel. All monetary figures should be in the same currency and time window.*

| Channel Name | Spend | Value Generated (Revenue) | Value Generated (Margin $) | Gross Margin % |
|---|---|---|---|---|
| [CHANNEL_NAME_1] | [SPEND_1] | [REVENUE_1] | [MARGIN_DOLLARS_1] | [MARGIN_PCT_1]% |
| [CHANNEL_NAME_2] | [SPEND_2] | [REVENUE_2] | [MARGIN_DOLLARS_2] | [MARGIN_PCT_2]% |

## 2. ROI Calculation

Formula: ROI (%) = (Value Generated − Cost) / Cost × 100

| Channel Name | Value Basis (Revenue/Margin) | ROI % |
|---|---|---|
| [CHANNEL_NAME_1] | [VALUE_BASIS_1] | [ROI_PCT_1]% |
| [CHANNEL_NAME_2] | [VALUE_BASIS_2] | [ROI_PCT_2]% |

## 3. ROAS Calculation

Formula: ROAS = Revenue Attributable to Spend / Spend

| Channel Name | Revenue Attributed | Spend | ROAS (x) |
|---|---|---|---|
| [CHANNEL_NAME_1] | [ATTRIBUTED_REVENUE_1] | [SPEND_1] | [ROAS_1]x |
| [CHANNEL_NAME_2] | [ATTRIBUTED_REVENUE_2] | [SPEND_2] | [ROAS_2]x |

## 4. LTV:CAC Calculation

Formula: LTV = Avg Revenue per Customer per Period × Gross Margin % × Avg Lifespan (periods)
Formula: LTV:CAC = LTV / CAC

| Channel Name | Avg Revenue/Period | Margin % | Avg Lifespan (periods) | LTV | CAC | LTV:CAC Ratio |
|---|---|---|---|---|---|---|
| [CHANNEL_NAME_1] | [AVG_REVENUE_PERIOD_1] | [MARGIN_PCT_1]% | [AVG_LIFESPAN_1] | [LTV_1] | [CAC_1] | [LTV_CAC_RATIO_1] |
| [CHANNEL_NAME_2] | [AVG_REVENUE_PERIOD_2] | [MARGIN_PCT_2]% | [AVG_LIFESPAN_2] | [LTV_2] | [CAC_2] | [LTV_CAC_RATIO_2] |

## 5. Marginal Return Check

*Instruction: for channels being considered for a spend increase, estimate the incremental return of the next spend tranche, not just the average.*

| Channel Name | Current Spend | Current Avg ROAS | Proposed Increase | Estimated Marginal ROAS | Recommendation |
|---|---|---|---|---|---|
| [CHANNEL_NAME_1] | [CURRENT_SPEND_1] | [AVG_ROAS_1]x | [PROPOSED_INCREASE_1] | [MARGINAL_ROAS_1]x | [RECOMMENDATION_1] |

## 6. Time Horizon & Notes

- Measurement window used: [MEASUREMENT_WINDOW]
- Value definition used (revenue vs. margin vs. pipeline-weighted): [VALUE_DEFINITION]
- Attribution method used (last-touch/first-touch/multi-touch): [ATTRIBUTION_METHOD]
- Notes / caveats: [NOTES]
