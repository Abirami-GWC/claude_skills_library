# Statistical Caution for Win/Loss Reporting

Practical guardrails for not overstating patterns in typically small sales
datasets — not a full statistical testing framework.

## Rules of thumb

| Sample size (n) | How to phrase it |
|---|---|
| n < 5 | "Too small to draw a pattern from — anecdotal only." State the raw count, not a percentage. |
| 5 ≤ n < 15 | "Directional / early signal" — pair every percentage with the raw count (e.g., "3 of 7 losses"). |
| 15 ≤ n < 30 | "Emerging pattern" — still pair with counts, avoid strong causal language. |
| n ≥ 30 | Can be called a "clear pattern" if consistent, still show counts alongside percentages. |

## Never do this

- Never present a percentage without the underlying count directly next to it.
- Never compare win rates across segments/competitors with very different
  sample sizes without noting the disparity.
- Never imply statistical significance testing was performed unless it actually was.

## Multi-dimension cuts compound fast

Each additional cut (competitor × industry × region × size) shrinks the
sample geometrically, not linearly. A dataset of 300 deals can easily produce
a specific four-way cut with n=2. Before presenting any segmented pattern,
check the resulting n for that *exact* cut against the table above — a
pattern that looked solid in aggregate can become "too small to draw a
pattern from" once cut by industry and competitor and region simultaneously.

**Practical rule**: report at most one or two dimensions of cut at a time
unless a specific combined cut has n ≥ 15. Prefer "loss reasons by competitor"
and "loss reasons by industry" as two separate views over a single
overcut table that leadership can't interpret and that hides thin samples in plain sight.

## Trend claims over time

A trend requires at least 2–3 comparable time periods with adequate n in
each. A single quarter's shift is "a recent shift worth watching," not yet a trend.
