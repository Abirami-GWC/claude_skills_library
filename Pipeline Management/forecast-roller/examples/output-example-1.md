# Output Example 1 — Matches input-example-1.md

Computed with `scripts/forecast_pipeline.py` (period end = 2026-09-30, today =
2026-07-16). This is what the final reply to the manager should look like.

---

## Sales Forecast — Q3 2026

**Total Expected Revenue: $131,400**

Three open deals fall within Q3, weighted by stage-appropriate probability rather
than summed at face value (raw deal values total $200,000 — the forecast is
meaningfully lower once probability is applied).

### Confidence Breakdown

| Confidence | Revenue | Deals |
|---|---|---|
| High (≥70%) | $102,000 | 1 |
| Medium (40-69%) | $22,500 | 1 |
| Low (<40%) | $6,900 | 1 |
| **Total Expected Revenue** | **$131,400** | **3** |

### Deals

| Deal | Value | Stage | Probability | Weighted Revenue | Confidence |
|---|---|---|---|---|---|
| ABC Manufacturing | $120,000 | Negotiation | 85% | $102,000 | High |
| XYZ Retail | $50,000 | Proposal | 45% | $22,500 | Medium |
| Delta Software | $30,000 | Discovery | 23% (inferred) | $6,900 | Low |

### Risk Analysis

| Reason | Impact | Recommended Action |
|---|---|---|
| ABC Manufacturing is 77.6% of the total forecast | If this deal slips past Q3, the forecast drops by $102,000 — over three-quarters of the total | Prioritize confirming ABC this month; have a fallback plan in case it slips |
| Delta Software has no logged recent activity | Its Low-confidence rating may even be optimistic if it's gone cold | Confirm Delta is still active before counting on any of its $6,900 |

### Recommendations

1. Treat ABC Manufacturing as the deal that determines whether this forecast is
   hit — a single slipped signature changes the quarter's number materially.
2. Push for a firmer probability/close-date read on Delta Software; right now
   it's carrying an inferred, not stated, confidence level.
3. XYZ Retail at 45% is below the typical Proposal-stage range (50-80%) — worth
   understanding why before assuming it progresses on schedule.

**Data quality notes:** Delta Software's probability was inferred from its stage
(Discovery ≈ 23%) since none was stated, and it has no logged last-activity date,
so its engagement level is unknown.
