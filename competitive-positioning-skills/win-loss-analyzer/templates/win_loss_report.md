# Win/Loss Report — [Scope, e.g. "Q1 2026, All Regions"]

_Data range: [start]–[end] &nbsp;|&nbsp; Records analyzed: n=[N] &nbsp;|&nbsp; Generated: [date]_

## Executive Summary

[3–5 sentences, written to stand alone: headline win rate, the single biggest
pattern, one notable uncomfortable finding if present, and the top
recommendation. A leadership reader should be able to stop here and know what
to do next.]

## Quantitative Findings

### Overall win rate

| Metric | Value | n |
|---|---|---|
| Overall win rate | [X]% | [N] |
| Win rate vs. [Competitor A] | [X]% | [N] |
| Win rate vs. [Competitor B] | [X]% | [N] |

_See `references/statistical_significance_notes.md` — any cell with n < 15 is
labeled directional, not a confirmed pattern._

### Loss reason distribution — vs. [Competitor A]

| Reason | Count | % of losses |
|---|---|---|
| PRICE | | |
| FEATURE_GAP | | |
| ... | | |

### Win reason distribution — vs. [Competitor A]

| Reason | Count | % of wins |
|---|---|---|

### Segment cuts (only where n clears the significance bar)

**By industry:** [finding, with n]
**By region:** [finding, with n]
**By customer size:** [finding, with n]
**By product line:** [finding, with n]

_Cuts without sufficient sample size are noted as "insufficient data" rather
than omitted silently — leadership should know the gap exists._

### Trend over time

[Chart reference / table by period. Note if trend claims aren't yet supportable.]

## Charts

![Win rate by competitor](charts/win_rate_by_competitor.png)
![Loss reason distribution](charts/loss_reason_distribution.png)

_(Generated via `scripts/generate_winloss_charts.py`.)_

## Qualitative Themes

**Theme 1: [name]** — [1–2 sentence description, paraphrased supporting evidence.]

**Theme 2: [name]** — ...

## Recommendations

| # | Recommendation | Tied to finding | Suggested owner |
|---|---|---|---|
| 1 | | | Product / Marketing / Sales / Pricing / Enablement |
| 2 | | | |

## Appendix

- Data source and date pulled
- Any excluded records and why
- Full reason-code taxonomy reference
