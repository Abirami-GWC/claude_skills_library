# CAC Analysis Prompt

**Purpose of this file**: Documents the reusable internal Claude prompt used to calculate fully-loaded CAC by channel, trend, and payback period.

## Purpose

This prompt guides Claude through building a consistent, fully-loaded CAC analysis using `references/cac_calculation.md`, outputting into `templates/cac_analysis_template.md`.

## Inputs

- Channel-level cost components (media, creative, tooling, salaries/commissions, agency fees, events, partner fees)
- New customers acquired per channel over a stated time window
- Average monthly revenue per customer and gross margin %, if payback period is requested
- Historical CAC by period, if a trend view is requested

## Instructions

```
You are producing a CAC analysis for GTM channels. Follow this process:

1. For each channel, gather every available cost component (media, creative,
   tooling allocation, salary/commission allocation, agency fees, event costs,
   partner fees). If a component is unavailable, state it as excluded rather
   than assuming zero.

2. Calculate fully-loaded CAC = Total Fully-Loaded Cost / New Customers
   Acquired, per references/cac_calculation.md. If only media spend is
   available, calculate and clearly label a "media-only CAC" and state that
   it understates true acquisition cost.

3. State the attribution method used (last-touch, first-touch, multi-touch,
   or channel-level cohort approximation) and apply it consistently across
   all channels being compared.

4. If historical data across multiple periods is available, show the CAC
   trend (rising/falling/stable) per channel, not just a single-period value.

5. If revenue-per-customer and margin data are available, calculate CAC
   Payback Period = CAC / (Avg Monthly Revenue per Customer x Gross Margin %).

6. Segment CAC by customer segment (e.g., SMB vs. Enterprise) if the sales
   motion differs materially and segment-level data is available.

7. Populate templates/cac_analysis_template.md with the results.

8. Flag any channel where CAC cannot be calculated due to missing data, and
   state what data would be needed to complete the analysis.
```

## Expected Output

A completed CAC analysis (using `templates/cac_analysis_template.md`) including fully-loaded CAC by channel, trend direction where data allows, payback period, and explicit notes on excluded cost components or data gaps.

## Validation Checklist

- [ ] Cost components included in each CAC figure are explicitly stated
- [ ] Attribution method is stated and applied consistently across channels
- [ ] Trend direction is shown when multi-period data is available
- [ ] Payback period calculation states the margin assumption used
- [ ] Data gaps are flagged rather than silently filled with unstated assumptions
