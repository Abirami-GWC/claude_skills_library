# Pipeline Prioritizer — Process

Ranks a sales rep's open deals from highest to lowest priority, using a fixed
weighted-scoring model, and explains the reasoning behind each deal's position so the
rep trusts and can act on the ranking immediately.

## Step 1 — Get the deal data

Ask for or read in the rep's open deals. Data may arrive as a pasted table, an
uploaded CSV/Excel export, or a conversational description of a few deals.

Read `knowledge/sales-stages.md` for how to normalize whatever stage names the user's
CRM uses, and what fields are required vs optional. Do not block on missing optional
fields — apply the documented default and flag the gap in the output instead.

If the user has no data ready, offer `templates/deal-import-template.csv` — a
template with a header row and 2 filled-in example rows they can follow and
replace (or hand to someone else to fill in), rather than typing deals into chat
one at a time. See `examples/input-example-1.md` for what a filled-in,
realistic version of this looks like.

If the user has given no data at all and no file is attached, ask them to paste a
list, upload an export, or use the template — don't invent deals.

## Step 2 — Score each deal

Read `knowledge/priority-rules.md` first for the weighting rationale and any
edge-case rules (ties, missing dates, single-deal requests). Then read
`knowledge/scoring-guidelines.md` for the exact per-factor formula.

Compute the actual scores by running `scripts/score_deals.py` on the deal data rather
than doing the arithmetic by hand — this guarantees the same inputs always produce the
same score, which matters because reps will compare rankings across sessions. Run
`python3 scripts/score_deals.py --help` for the expected CSV columns (they mirror
`knowledge/sales-stages.md`). If data arrived as a pasted table rather than a file,
write it to a temporary CSV first, then run the script on that.

If the user has stated a different weighting preference in this conversation (e.g.,
"I only care about what closes this quarter"), pass that through via the script's
`--weights` override — see `knowledge/priority-rules.md` for how weight over
rides should be handled, and the script's `--help` for the exact syntax.

## Step 3 — Rank and explain

Take the script's sorted output and write each deal's explanation using
`templates/recommendation-template.md` as the pattern — name the 1-2 factors that
actually drove its position, not generic filler.

Assemble the full response using `templates/priority-report.md` as the exact layout.
`examples/output-example-1.md` shows a complete worked example end-to-end, matched to
`examples/input-example-1.md` — use it to sanity-check tone and format before
replying.

## Step 4 — Surface data quality issues once, at the end

The script flags which deals used inferred/default values (missing close date, missing
probability, etc.) in its `data_quality_flags` output column. Summarize those in one
short section after the ranking — don't repeat the caveat per deal.

## Edge cases

Full edge-case handling (single deal, ties, missing dates pipeline-wide, 50+ deal
batches) is documented in `knowledge/priority-rules.md` — read it rather than
improvising when one of these comes up.
