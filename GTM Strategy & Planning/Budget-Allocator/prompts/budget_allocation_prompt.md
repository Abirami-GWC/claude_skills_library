# Budget Allocation Prompt

**Purpose of this file**: Documents the reusable internal Claude prompt used to build a channel-level GTM budget allocation model from user-supplied data and constraints.

## Purpose

This prompt guides Claude through producing a defensible, methodology-grounded budget allocation across GTM channels, using `references/budget_planning.md`, `references/cac_calculation.md`, `references/roi_framework.md`, and `references/channel_strategy.md`, and outputting into `templates/budget_model_template.md`.

## Inputs

- Total available budget and planning horizon
- Historical channel-level spend, CAC, ROI/ROAS (as available)
- Growth targets (revenue, customers, pipeline) for the period
- Known constraints (minimum commitments, contractual spend, headcount-linked costs)
- Preferred planning approach, if the user has one (top-down / bottom-up / zero-based)

## Instructions

```
You are producing a GTM budget allocation model. Follow this process:

1. Confirm you have: total budget, planning horizon, and at least directional
   historical performance data for each channel under consideration. If any
   of these are missing, state the assumption you will use instead of asking
   a blocking question, unless the missing input would materially change the
   recommendation — in that case, ask.

2. Select a planning approach (top-down, bottom-up, zero-based, or a blend)
   based on data maturity and the user's context, per references/budget_planning.md.
   State which approach you are using and why.

3. For each channel (including any channel the user is considering but not
   currently funding), summarize: prior-period spend, fully-loaded CAC (or
   media-only CAC clearly labeled as such if that is all the data supports),
   and ROI/ROAS if available, per references/cac_calculation.md and
   references/roi_framework.md.

4. Classify each channel into a payback tier (fast/medium/slow) per
   references/channel_strategy.md, and consider concentration risk if any
   channel would exceed roughly 50-60% of total budget.

5. Propose a spend allocation across channels that:
   - Sums exactly to the stated total budget (net of any reserve held back)
   - Favors channels with strong marginal (not just average) return
   - Preserves a reasonable tier balance (fast/medium/slow payback) unless
     the user has stated a reason to concentrate
   - Flags any channel recommended for a cut or increase with the specific
     metric justifying the change

6. Populate templates/budget_model_template.md with the resulting model.

7. State all assumptions and data gaps explicitly in a dedicated section.

8. Do not produce messaging/positioning copy, roadmap timelines, or board
   narrative content even if asked in the same request — note that these
   belong to separate skills.
```

## Expected Output

A completed Budget Allocation Model (using `templates/budget_model_template.md`) including: total budget reconciliation, channel-by-channel spend recommendation with rationale, payback tier classification, and an explicit assumptions/data-gaps section.

## Validation Checklist

- [ ] Total proposed spend across channels plus reserve equals the stated total budget
- [ ] Every channel recommendation is tied to a specific metric (CAC, ROI, payback, or marginal return)
- [ ] Payback tier classification is present for every channel
- [ ] Concentration risk is flagged if any channel exceeds ~50-60% of budget
- [ ] Assumptions and data gaps are explicitly listed
- [ ] No positioning, roadmap, or narrative content included
