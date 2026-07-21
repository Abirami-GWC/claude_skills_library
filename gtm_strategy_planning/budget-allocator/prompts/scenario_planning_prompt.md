# Scenario Planning Prompt

**Purpose of this file**: Documents the reusable internal Claude prompt used to build best/base/worst-case scenarios and sensitivity analysis for a GTM budget plan.

## Purpose

This prompt guides Claude through stress-testing a budget plan using `references/scenario_planning.md` and `references/forecasting_models.md`, producing scenario outputs that can be layered onto `templates/forecast_template.md` and `templates/budget_model_template.md`.

## Inputs

- The base-case budget allocation and/or forecast to be stress-tested
- Key drivers to vary (typically CAC, conversion rate, channel cost inflation, market demand)
- Any known constraint (e.g., a mandated budget cut percentage, a hard revenue floor)

## Instructions

```
You are producing a scenario analysis for a GTM budget plan. Follow this process:

1. Identify the 3-5 key drivers most likely to affect the outcome (e.g., CAC,
   conversion rate, channel cost inflation, market demand growth). Do not vary
   more than this in a single scenario set, per references/scenario_planning.md.

2. Build a base case using the stated or most likely assumption for each driver.

3. Build a best case by moving each driver to a favorable-but-plausible value
   (state the specific movement, e.g., "CAC improves 15%").

4. Build a worst case by moving each driver to an unfavorable-but-plausible
   value (state the specific movement).

5. If a budget cut is involved, do not model only a uniform percentage cut.
   Also model an efficiency-ranked cut (defund lowest ROI/CAC-payback channels
   first) and, if strategic priorities are stated, a strategic-protection cut.
   Present the resulting outcome of each option side by side.

6. Run a simple sensitivity check: vary each key driver independently (holding
   others constant) and rank drivers by the size of their effect on the
   headline outcome (e.g., customers acquired, revenue). Report this ranking.

7. State the outcome range (best to worst) for the headline metrics (pipeline,
   revenue, customers acquired, CAC) rather than a single point estimate.

8. Recommend what should be pre-planned as a response if the worst case
   begins to materialize (e.g., which channels would be cut first).
```

## Expected Output

A best/base/worst case comparison table for headline metrics, a sensitivity ranking of key drivers, and — where relevant — a side-by-side comparison of uniform vs. efficiency-ranked vs. strategic-protection budget-cut options.

## Validation Checklist

- [ ] No more than 3-5 key drivers varied per scenario set
- [ ] Best and worst cases are plausible, not extreme/unrealistic bounds
- [ ] Budget-cut scenarios include an efficiency-ranked alternative to a uniform cut
- [ ] Sensitivity ranking identifies which drivers matter most
- [ ] Outcome is presented as a range, not a single point estimate
