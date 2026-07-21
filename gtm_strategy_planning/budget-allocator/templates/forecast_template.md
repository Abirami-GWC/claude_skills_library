# Forecast Template

**Purpose of this file**: A fill-in-the-blank template for projecting pipeline, revenue, and customer outcomes from a proposed budget, using one or more forecasting models. See `references/forecasting_models.md` for methodology guidance.

---

## 1. Forecast Parameters

| Field | Value |
|---|---|
| Forecast period | [FORECAST_PERIOD] |
| Forecasting model(s) used | [MODEL_TYPE: LINEAR_TREND / COHORT_BASED / PIPELINE_COVERAGE / BLENDED] |
| Number of historical periods used | [NUM_HISTORICAL_PERIODS] |
| Confidence level | [HIGH / MEDIUM / LOW] — [CONFIDENCE_RATIONALE] |

## 2. Linear / Trend-Based Inputs (if used)

| Period | Spend | Output (Leads/Pipeline/Revenue) |
|---|---|---|
| [PERIOD_1] | [SPEND_PERIOD_1] | [OUTPUT_PERIOD_1] |
| [PERIOD_2] | [SPEND_PERIOD_2] | [OUTPUT_PERIOD_2] |
| [PERIOD_3] | [SPEND_PERIOD_3] | [OUTPUT_PERIOD_3] |

Projected output at proposed spend of [PROPOSED_SPEND]: [PROJECTED_OUTPUT]

## 3. Cohort-Based Inputs (if used)

| Cohort | Size | Conversion Rate | Avg Revenue/Period | Retention (Month N) |
|---|---|---|---|---|
| [COHORT_1] | [COHORT_SIZE_1] | [CONVERSION_RATE_1]% | [AVG_REVENUE_1] | [RETENTION_1]% |
| [COHORT_2] | [COHORT_SIZE_2] | [CONVERSION_RATE_2]% | [AVG_REVENUE_2] | [RETENTION_2]% |

Projected new cohort size implied by proposed budget: [PROJECTED_COHORT_SIZE]
Projected revenue from new cohort at Month [MONTH_N]: [PROJECTED_COHORT_REVENUE]

## 4. Pipeline-Coverage Inputs (if used)

| Field | Value |
|---|---|
| Revenue target | [REVENUE_TARGET] |
| Historical pipeline coverage ratio | [COVERAGE_RATIO]x |
| Required pipeline | [REQUIRED_PIPELINE] |
| Historical pipeline per $1 of spend (blended or by channel) | [PIPELINE_PER_DOLLAR] |
| Required spend | [REQUIRED_SPEND] |

## 5. Forecast Output Summary

| Metric | Base Case | Notes |
|---|---|---|
| Projected leads/opportunities | [PROJECTED_LEADS] | [NOTES_LEADS] |
| Projected pipeline | [PROJECTED_PIPELINE] | [NOTES_PIPELINE] |
| Projected new customers | [PROJECTED_CUSTOMERS] | [NOTES_CUSTOMERS] |
| Projected revenue | [PROJECTED_REVENUE] | [NOTES_REVENUE] |
| Projected CAC trend | [PROJECTED_CAC_TREND] | [NOTES_CAC] |

## 6. Assumptions & Caveats

- [ASSUMPTION_1]
- [ASSUMPTION_2]
- Cross-check against alternative model: [CROSS_CHECK_RESULT_OR_NA]
