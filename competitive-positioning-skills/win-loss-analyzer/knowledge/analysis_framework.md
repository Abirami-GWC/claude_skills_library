# Win/Loss Analysis Framework

## The four-step approach: Categorize → Quantify → Qualify → Recommend

### 1. Categorize
Every deal record gets coded against `knowledge/loss_reason_taxonomy.json`.
Consistency here is what makes aggregation meaningful — resist inventing a new
one-off category per deal; nuance belongs in the `detail` field.

### 2. Quantify
Compute, at minimum:
- Overall win rate, and win rate specifically against each named competitor
- Reason-code distribution per competitor
- Trend over time, if the date range allows
- **Multi-dimension cuts**: by industry, customer size/segment, region, and
  product line — but only report a cut if its sample size clears the bar in
  `references/statistical_significance_notes.md`. Cuts compound quickly (e.g.
  "Competitor X × Healthcare × EMEA × Enterprise" can shrink to n=1–2 even in
  a dataset of hundreds) — always check the specific cut's n, not just the
  overall dataset's n.

### 3. Qualify
Layer in qualitative color from interview notes or transcripts — 1–3
representative paraphrased points per major reason-code cluster. Note where
qualitative color contradicts or adds nuance to the quantitative pattern.

### 4. Recommend
Translate patterns into specific, owned recommendations, each tied to the
finding that motivated it, with a likely owner (Product / Marketing / Sales /
Pricing / Sales Enablement). Distinguish quick fixes from structural findings.

## Common analytical pitfalls

- **Cherry-picking losses to explain a narrative** — always report the full distribution.
- **Treating small samples as trends**, especially after cutting by
  industry/region/size simultaneously.
- **Conflating correlation with causation** — "deals lost to Competitor X skew
  toward industry Y" doesn't necessarily mean X is stronger in that industry;
  could reflect deal sourcing, rep assignment, etc. Flag alternative explanations.
- **Ignoring wins** — include win-side reason distribution, not just losses.
- **Over-slicing for leadership** — a report with 15 different segment cuts is
  harder to act on than 3 well-chosen, well-supported ones. Prioritize the
  cuts most relevant to the stated business question.
