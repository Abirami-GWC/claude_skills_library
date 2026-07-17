# Forecast Roller — Process

Analyzes the current sales pipeline and produces a realistic, weighted revenue
forecast — never a simple sum of open deal values — along with a confidence
breakdown, risk analysis, and recommendations a sales manager can act on.

## Step 1 — Get the pipeline data

Ask for or read in the manager's open pipeline. Data may arrive as a pasted list,
an uploaded CSV/Excel export, or a conversational description of several deals.

Read `knowledge/pipeline-stages.md` for the full stage taxonomy and which stages
count toward an active forecast (Lead and Closed Lost do not; Closed Won is
tracked separately as already-recognized revenue, not forecasted). Read
`knowledge/sales-probabilities.md` for the probability ranges tied to each stage,
used when a deal has no stated probability.

If the user hasn't specified a forecast period (e.g., "this month", "Q3"), ask —
the period determines which deals with close dates should count. If the user has
no data ready at all, ask for it — don't invent a pipeline.

See `examples/input-example-1.md` for what realistic, unstructured pipeline input
looks like.

## Step 2 — Compute the weighted forecast

Read `knowledge/forecasting-rules.md` first — it explains why this is a weighted
estimate rather than a raw total, how missing probabilities are inferred, how the
forecast period filters deals, and how concentration risk is detected.

Then compute the actual numbers by running `scripts/forecast_pipeline.py` on the
deal data rather than doing the weighting by hand — this guarantees the same
pipeline always produces the same forecast. Run
`python3 scripts/forecast_pipeline.py --help` for the expected CSV columns and
options (period end date, concentration threshold). If data arrived as a pasted
list rather than a file, write it to a temporary CSV first, then run the script.

Do not simply total all deal values — every dollar figure in the final report
must come from the weighted calculation, not raw deal value.

## Step 3 — Build the report

Assemble the full response using `templates/forecast-report.md` as the master
layout, which incorporates:
- The confidence breakdown from `templates/revenue-summary.md`
- The risk analysis from `templates/risk-analysis.md`

`examples/output-example-1.md` shows a complete worked forecast end-to-end,
matched to `examples/input-example-1.md` — use it to check tone, math, and format
before replying.

## Step 4 — Explain assumptions and flag missing data, once

If any deal's probability was inferred from stage rather than stated, or its close
date was missing (so period assignment is uncertain), or it was excluded because it
falls outside the forecast period or in an excluded stage — summarize all of this
in one short section, not scattered per deal. The script's output flags each of
these per deal; you're consolidating them into a readable note.

## Edge cases

- **Deal missing both probability and stage-appropriate data**: infer per
  `knowledge/sales-probabilities.md` and flag it — never silently assume 100% or
  0%.
- **All deals in one stage**: still compute the forecast, but note in the risk
  section that the pipeline lacks stage diversity if that seems relevant.
- **A single deal dominates the forecast**: this is a concentration risk — see
  `knowledge/forecasting-rules.md` for the threshold and how to phrase it.
- **Very large pipelines (50+ deals)**: report the aggregate numbers in full, but
  only list individual deals for the high-confidence tier in detail; group
  medium/low confidence deals by count and subtotal rather than listing every row.
