# Worked Example — Win/Loss Analyzer (Multi-Dimension Cuts + Executive Report)

## User input

> "Here's our CRM export for Q1, 120 closed deals, includes competitor,
> industry, region, size, product line. Build an executive win/loss report
> with charts for the QBR — I especially want to know if we're weaker in any
> particular industry or region against Competitor A."

## Claude's internal process (not shown to user)

1. Scope: Q1 2026, all competitors with a focus on Competitor A, industry/region cuts requested.
2. Ingest CSV, confirm column mapping matches `templates/deal_record_schema.csv`.
3. Run `scripts/analyze_winloss.py deals.csv --cut competitor --cut industry`
   and `--cut competitor --cut region` — rather than hand-slicing 120 rows
   across two dimensions at once, which risks silent arithmetic errors.
4. Overall n=120 clears "clear pattern" for the aggregate view. But the
   competitor × industry × region cuts the user actually asked about shrink
   fast — e.g. "Competitor A × Healthcare × EMEA" comes back n=4, correctly
   flagged `[SKIP: n<5, not reportable]` by the script.
5. Report the two-dimension cuts that do clear the bar (e.g. "Competitor A ×
   Healthcare" at n=18) and explicitly note the three-dimension cut the user
   asked about is "insufficient data" rather than omitting it silently or
   reporting it anyway.
6. Run `scripts/generate_winloss_charts.py` for supporting visuals.
7. Draft using `templates/win_loss_report.md`, leading with an executive
   summary that stands alone.

## Output delivered to user (abbreviated)

```
# Win/Loss Report — Q1 2026, All Regions (n=120)

## Executive Summary
Overall win rate this quarter is 54% (65/120) — a clear pattern given the
sample size. Against Competitor A specifically, win rate is 41% (23/56),
noticeably below the overall average. The dominant loss driver vs. Competitor
A is FEATURE_GAP (48%, 16/33), concentrated in Healthcare deals (n=18,
emerging pattern) — Healthcare-specific compliance certification gaps appear
repeatedly in loss notes. The requested Healthcare × EMEA × Competitor A cut
has insufficient data (n=4) to report as a pattern this quarter; worth
revisiting next quarter once more deals close in that specific combination.

## Quantitative Findings
Win rate vs. Competitor A: 41% (23/56) — clear pattern
Win rate vs. Competitor A, Healthcare industry: 33% (6/18) — emerging pattern
Win rate vs. Competitor A, Healthcare x EMEA: insufficient data (n=4)

Loss reasons vs. Competitor A (n=33):
  FEATURE_GAP: 16 (48%)
  PRICE: 10 (30%)
  RELATIONSHIP: 4 (12%)
  OTHER_UNKNOWN: 3 (9%)

## Charts
[win_rate_by_competitor.png]
[loss_reason_distribution.png]

## Recommendations
1. [Product] Investigate the Healthcare-specific compliance gap behind the
   FEATURE_GAP losses to Competitor A — the largest single driver, concentrated
   in one industry.
2. [Sales Enablement] Update the Competitor A battlecard's Healthcare-specific
   objection handling.
3. [Sales Ops] Begin flagging region within the CRM close-reason workflow more
   consistently — the three-way cut the business question actually needed
   couldn't be answered this quarter due to sparse regional tagging.
```

## Why this is a good output

- Correctly refused to report the exact 3-dimension cut the user asked for
  once it fell below the significance threshold, rather than presenting a
  misleadingly confident n=4 finding.
- Surfaced a 2-dimension cut that did clear the bar as a useful substitute,
  clearly labeled with its own (lower) confidence level.
- Recommendation #3 turns a data-quality gap into an actionable fix rather
  than silently working around it.
