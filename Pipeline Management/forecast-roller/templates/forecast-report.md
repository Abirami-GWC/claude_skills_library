# Forecast Report Template

The master layout — incorporates the revenue summary and risk analysis into one
report. Lead with the number a manager actually needs, then support it.

## Standard layout

```
## Sales Forecast — [Period, e.g. "Q3 2026" or "July 2026"]

**Total Expected Revenue: $[weighted total]**

[1-2 sentence framing: how many deals, what the mix looks like]

### Confidence Breakdown
[Insert templates/revenue-summary.md content here]

### Deals

| Deal | Value | Stage | Probability | Weighted Revenue | Confidence |
|---|---|---|---|---|---|
| ABC Manufacturing | $120,000 | Negotiation | 85% | $102,000 | High |
| ... | ... | ... | ... | ... | ... |

### Risk Analysis
[Insert templates/risk-analysis.md content here]

### Recommendations

[2-4 concrete, specific recommendations tied to what's actually in this
pipeline — not generic sales advice. E.g., "Confirm the ABC Manufacturing
contract this week — it's 78% of this forecast" rather than "Focus on
high-value deals."]

**Data quality notes:** [inferred probabilities, missing close dates, deals
excluded by stage or period — from scripts/forecast_pipeline.py's flags. Omit
this section if nothing was inferred or excluded.]
```

## For large pipelines (50+ deals)

List every deal in the High confidence tier individually. For Medium and Low,
report count and subtotal only:

```
### Medium confidence (14 deals)
Subtotal: $186,400 — mostly Proposal-stage deals in the 50-65% range.

### Low confidence (31 deals)
Subtotal: $94,200 — mostly early-stage Discovery/Demo deals.
```

## Tone

A manager should be able to read the top line and the confidence breakdown and
know exactly how solid the number is — don't bury the concentration risk or
inferred-probability caveats at the very end where they'll be skimmed past.
