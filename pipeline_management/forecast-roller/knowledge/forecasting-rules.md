# Forecasting Rules

## Core principle

**Never simply total all open deal values.** A forecast weights each deal by its
probability of closing, so a $100,000 deal at 20% probability contributes far less
to the forecast than a $30,000 deal at 90%. This is the entire point of the skill —
a raw sum overstates revenue and misleads planning.

## Weighted revenue formula

`Weighted Revenue (per deal) = Deal Value × Probability`

Total Expected Revenue = sum of weighted revenue across all included deals (see
`pipeline-stages.md` for which stages are included).

## Confidence tiers

Based on the deal's probability (stated or inferred):

| Tier | Probability |
|---|---|
| High confidence | 70% and above |
| Medium confidence | 40-69% |
| Low confidence | Below 40% |

Report the Total Expected Revenue broken down by tier (see
`templates/revenue-summary.md`), not just as one aggregate number — a manager
needs to see how much of the forecast is solid versus speculative.

## Forecast period

If the user specifies a period (e.g., "this month", "Q3"), only include deals
whose expected close date falls within that period in the forecast total. Deals
closing after the period end still get analyzed, but are reported separately
(e.g., "next period") rather than folded into the current total — including them
would overstate what's realistically expected in the requested window.

If a deal has no close date at all, include it in the total but flag it — its
period assignment is genuinely unknown, which is itself worth surfacing to the
manager rather than silently guessing it falls inside the window.

## Missing probability

If a deal has no stated probability, infer it from
`knowledge/sales-probabilities.md`'s stage midpoint and flag the deal as using an
inferred value. Never leave a deal out of the forecast just because probability
is missing — infer conservatively and disclose it instead.

## Concentration risk

Flag it when a single deal contributes more than **30%** of the Total Expected
Revenue. A forecast that depends heavily on one deal closing is a real risk the
manager needs to see explicitly — not something to bury inside a generic "risks"
paragraph. Name the specific deal and its percentage of the total.

## Other risk signals worth surfacing

- A high-value or high-confidence deal with no recent activity (stale engagement)
  — the confidence tier may be optimistic if the deal has gone quiet.
- A pipeline with very few deals in Negotiation/Proposal relative to earlier
  stages — near-term revenue may be thinner than the total pipeline size suggests.
- Multiple deals converging on the same close date — a scheduling/capacity risk
  worth a mention, not a hard rule to compute.

## What to always disclose

- Every deal whose probability was inferred rather than stated.
- Every deal excluded from the total (wrong stage, outside the period) and why.
- The concentration risk check's result, even when nothing is flagged (a brief
  "no single deal dominates the forecast" is fine).
