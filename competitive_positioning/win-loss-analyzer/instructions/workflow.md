# Workflow: Win/Loss Analysis

## Step 1 — Confirm scope and ingest data

Ask (if not already given):
- Time range
- Segment scope (all deals, or filtered by region/industry/size/product line)
- Which competitor(s) are the focus, or "all competitors"
- Whether an executive summary + charts are needed (default: yes, for any
  report going to leadership/QBR)

Ingest the data the user supplies. If the shape doesn't match
`templates/deal_record_schema.csv`, map columns and confirm ambiguous mappings
with the user rather than guessing silently.

If the user references data that hasn't actually been provided or isn't
accessible via a connected tool, say so and ask for it — do not generate
illustrative/plausible numbers and present them as real data.

## Step 2 — Normalize and categorize

For each deal record, ensure outcome, competitor, industry, customer size,
region, product line, and a taxonomy-coded reason are present where available.
Flag any deal without enough information to code confidently as
`OTHER_UNKNOWN` rather than guessing a specific category.

## Step 3 — Compute quantitative patterns and multi-dimension cuts

Run `scripts/analyze_winloss.py` against the CSV rather than hand-computing.
The script computes overall win rate, per-competitor win rate, reason
distributions, and supports cutting by any combination of industry / size /
region / product line — always check the resulting n for each specific cut
against `references/statistical_significance_notes.md` before reporting it as
a pattern.

## Step 4 — Apply statistical caution

Label small-sample findings "directional" rather than "clear trend." This
matters most for multi-dimension cuts, which shrink fast.

## Step 5 — Extract qualitative themes (if interview notes/transcripts supplied)

Identify 1–3 recurring qualitative themes per major reason-code cluster.
Paraphrase; avoid long verbatim quoting.

## Step 6 — Generate charts

Run `scripts/generate_winloss_charts.py` against the CSV to produce supporting
chart images (win rate by competitor, reason-code distribution, trend over
time) for inclusion in the report or a slide deck.

## Step 7 — Draft the report

Use `templates/win_loss_report.md`. Lead with the executive summary — written
so it stands alone if that's all a leadership reader sees. Include the
quantitative section (with sample sizes), qualitative themes, charts, and
recommendations with owners.

## Step 8 — Self-review before delivering

- Does every stated pattern show its sample size, including multi-dimension cuts?
- Are uncomfortable findings included, not softened or omitted?
- Is every recommendation specific and owned?
- Are wins covered, not just losses?
- Does the executive summary stand alone as a complete, honest headline?

## Common mistakes to avoid

- **Simulating data the user hasn't actually provided.**
- **Silent miscategorization** when source data doesn't map cleanly to the taxonomy.
- **Overstating small-sample patterns**, especially compounded multi-dimension cuts.
- **Cherry-picking a flattering narrative.**
- **Over-slicing**: reporting every possible cut instead of the ones that
  actually answer the business question and clear the sample-size bar.
