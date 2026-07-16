# ROI Analysis Prompt

**Purpose of this file**: Documents the reusable internal Claude prompt used to calculate and interpret ROI, ROAS, and LTV:CAC by channel, and to produce reallocation recommendations grounded in marginal return.

## Purpose

This prompt guides Claude through a rigorous ROI/ROAS/LTV:CAC analysis using `references/roi_framework.md` and `references/cac_calculation.md`, outputting into `templates/roi_calculator_template.md`.

## Inputs

- Channel-level spend and attributed revenue/margin for a stated time window
- Gross margin percentage (overall or by channel/segment)
- Customer lifespan / retention data, if LTV:CAC is requested
- Any available data on incremental/marginal spend-response (e.g., results at different historical spend levels)

## Instructions

```
You are producing an ROI/ROAS/LTV:CAC analysis for GTM channels. Follow this process:

1. Confirm the value basis being used for each channel (revenue vs. gross
   margin dollars vs. pipeline-weighted value) and state it explicitly.
   Do not silently mix bases across channels in the same comparison.

2. Calculate ROI (%) = (Value Generated - Cost) / Cost x 100 for each channel,
   using margin-based value where the data supports it, per
   references/roi_framework.md.

3. Calculate ROAS = Attributed Revenue / Spend for channels where revenue
   attribution is direct (e.g., paid channels).

4. If lifespan/retention data is available, calculate LTV = Avg Revenue per
   Period x Gross Margin % x Avg Lifespan, then LTV:CAC = LTV / CAC.
   State the benchmark context (e.g., ~3:1 often considered healthy for
   recurring-revenue models) without asserting it as a universal rule.

5. Distinguish average return from marginal return: if historical data at
   multiple spend levels exists, estimate whether the channel shows signs
   of saturation (declining marginal return) before recommending an increase.

6. Match the measurement window to each channel's natural sales cycle
   (short window for fast-attribution paid channels, longer window for
   events/ABM/enterprise field) rather than applying one universal window.

7. Populate templates/roi_calculator_template.md with the results.

8. Flag any input inconsistencies (e.g., conflicting CAC or margin figures
   for the same channel) rather than silently resolving them.
```

## Expected Output

A completed ROI/ROAS/LTV:CAC table by channel (using `templates/roi_calculator_template.md`), a marginal-return assessment for any channel being considered for a spend increase, and explicit statements of value basis, attribution method, and measurement window used.

## Validation Checklist

- [ ] Value basis (revenue/margin/pipeline-weighted) stated for every figure
- [ ] ROI, ROAS, and LTV:CAC (where applicable) are not mixed or compared inconsistently
- [ ] Marginal return is assessed, not just average return, for any proposed spend increase
- [ ] Measurement window matches each channel's natural sales cycle
- [ ] Any conflicting or missing inputs are flagged, not silently resolved
