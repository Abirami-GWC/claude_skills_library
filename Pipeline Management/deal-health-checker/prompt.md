# Deal Health Checker — Process

Evaluates every open opportunity and classifies it as Healthy, Warning, or At Risk,
explaining exactly why, so a rep or manager can see trouble before a deal is lost —
not after.

## Step 1 — Get the deal data

Ask for or read in each deal's current stage, last customer contact date, whether
a next meeting is scheduled, whether a decision maker is identified, and how the
customer has been responding. This may arrive as a pasted description, a CRM
export, or a few sentences per deal.

Read `knowledge/sales-pipeline-stages.md` for the stage taxonomy — Closed Won and
Closed Lost deals aren't evaluated for health, since they're no longer open.

If a critical field (last contact date, decision maker status, meeting status,
customer response) is missing, do not assume it's fine. Per
`knowledge/deal-health-rules.md`, missing information is itself treated as a
caution signal, not silently skipped — and it must be listed explicitly in the
"Missing Information" section of the output, never invented.

See `examples/input-example-1.md` for what realistic, unstructured deal
descriptions look like.

## Step 2 — Score and classify each deal

Read `knowledge/risk-indicators.md` for the full list of risk indicators and their
weights, and `knowledge/deal-health-rules.md` for how those weights combine into a
Healthy / Warning / At Risk classification and a priority level.

Compute the actual classification by running `scripts/deal_health.py` on the deal
data rather than tallying indicators by hand — this guarantees the same deal
facts always produce the same health status. Run
`python3 scripts/deal_health.py --help` for the expected CSV columns. If data
arrived as a pasted description rather than a file, write it to a temporary CSV
first, then run the script.

## Step 3 — Build the report

For a single deal, use `templates/health-report.md` as the exact layout — status,
positive indicators, risk factors, missing information, and recommended actions.

For multiple deals, also produce a pipeline-level rollup using
`templates/risk-summary.md` (counts per tier, overall pipeline health), and use
`templates/action-plan.md` to lay out the concrete next actions for every Warning
and At Risk deal — don't just describe the problem, give the rep something to do
about it.

`examples/output-example-1.md` shows a complete worked example — a small pipeline
with one deal in each tier — matched to `examples/input-example-1.md`. Use it to
check tone, scoring, and format before replying.

## Step 4 — Recommend, don't just diagnose

Every At Risk or Warning deal must get specific, practical recommended actions
tied to its actual risk factors (e.g., "identify the decision maker" only if that's
actually missing for this deal) — not generic advice repeated across every deal.

## Edge cases

Full edge-case handling (deals with almost no data at all, Closed Won/Lost deals
mixed into the input, very large pipelines, deals with only positive indicators
and nothing to flag) is documented in `knowledge/deal-health-rules.md` — read it
rather than improvising when one of these comes up.
