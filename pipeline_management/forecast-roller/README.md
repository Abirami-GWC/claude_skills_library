# forecast-roller

Part of the **Pipeline Management** module (owner: Nithisri) in the Sales &
Marketing Claude Skills project.

## What it does

Analyzes the open pipeline and produces a realistic, weighted revenue forecast —
never a raw sum of deal values — with a High/Medium/Low confidence breakdown and
an explicit risk analysis (e.g., is the forecast overly dependent on one deal?).

## Folder guide

| Path | Purpose |
|---|---|
| `SKILL.md` | Triggering logic only (read by Claude automatically). Points to `prompt.md`. |
| `prompt.md` | The actual step-by-step process Claude follows once triggered. |
| `knowledge/pipeline-stages.md` | Full stage taxonomy + which stages count toward the forecast. |
| `knowledge/sales-probabilities.md` | Probability ranges/defaults per stage, used when probability isn't stated. |
| `knowledge/forecasting-rules.md` | The weighting formula, confidence tiers, period filtering, and concentration-risk rule. |
| `templates/forecast-report.md` | Master report layout. |
| `templates/revenue-summary.md` | Confidence-tier breakdown sub-template. |
| `templates/risk-analysis.md` | Risk table sub-template. |
| `examples/input-example-1.md` | A realistic, unstructured pipeline description. |
| `examples/output-example-1.md` | The correct forecast for that same input — real computed numbers. |
| `examples/sample-pipeline.json` | The same 3 deals in structured JSON, for reference/testing. |
| `scripts/forecast_pipeline.py` | Computes the actual weighted forecast, tiers, and concentration check — run this rather than doing the math by hand. |
| `assets/` | Reserved for a skill icon, if one is ever added — currently unused. |

## Why this needed a `scripts/` folder (unlike `follow-up-cadence-builder`)

This skill sums real dollar amounts across a whole pipeline and applies
period/stage filtering — the kind of multi-step aggregate math where a small
arithmetic slip compounds across every deal. Locking it into tested code means the
same pipeline always produces the same forecast, which is the entire basis for a
manager trusting the number.

## Key design decisions worth reviewing

- **Confidence tiers**: High ≥70%, Medium 40-69%, Low <40%. Verified against the
  original $124,500 example (ABC + XYZ only) before Delta Software was added.
- **Concentration risk threshold**: flags any single deal above 30% of the total
  forecast. Adjustable via `scripts/forecast_pipeline.py --concentration-threshold`.
- **Stage taxonomy**: reconciled into 8 stages (Lead through Closed Lost) with
  Lead and Closed Lost excluded from the forecast, and Closed Won tracked
  separately as already-recognized revenue rather than folded into the forecast.

## Testing it yourself

```bash
python3 scripts/forecast_pipeline.py examples/sample-pipeline.csv --period-end 2026-09-30 --today 2026-07-16
```

Compare against `examples/output-example-1.md` to sanity-check any changes to the
weighting or risk thresholds. `examples/sample-pipeline.json` holds the same three
deals in structured form for reference — the runnable input is `sample-pipeline.csv`.

## Related skills (same module)

- `pipeline-prioritizer` — ranks individual deals, doesn't aggregate revenue
- `deal-health-checker` — diagnoses one deal's risk status
- `follow-up-cadence-builder` — schedules outreach for one deal

Keep triggering descriptions in each skill's `SKILL.md` distinct so requests don't
collide between these four.
