# pipeline-prioritizer

Part of the **Pipeline Management** module (owner: Nithisri) in the Sales & Marketing
Claude Skills project.

## What it does

Ranks a rep's open deals from highest to lowest priority using a fixed, weighted
scoring model, and explains why each deal landed where it did. Point of this skill:
a rep should be able to ask "what should I work on today?" and get a defensible,
consistent order — not a different vibe-based answer every time.

## Folder guide

| Path | Purpose |
|---|---|
| `SKILL.md` | Triggering logic only (read by Claude automatically). Points to `prompt.md`. |
| `prompt.md` | The actual step-by-step process Claude follows once triggered. |
| `knowledge/sales-stages.md` | Stage taxonomy + expected input fields/aliases. |
| `knowledge/priority-rules.md` | Weighting policy, override rules, tie-breaking, edge cases. |
| `knowledge/scoring-guidelines.md` | The exact per-factor math (mirrors `scripts/score_deals.py`). |
| `templates/priority-report.md` | Exact output layout for the ranked table. |
| `templates/recommendation-template.md` | Pattern for the per-deal "why this rank" line. |
| `templates/deal-import-template.csv` | CSV template (header row + 2 filled-in example rows) a rep can follow and replace if they have no export. |
| `examples/input-example-1.md` | A realistic, unstructured pasted-in deal list. |
| `examples/output-example-1.md` | The correct ranked output for that same input (real computed scores). |
| `examples/sample-pipeline.json` | The same 4 deals in structured JSON, for reference/testing. |
| `scripts/score_deals.py` | Computes the actual 0-100 priority score — run this rather than doing the math by hand, so results are reproducible. |
| `assets/` | Reserved for a skill icon, if one is ever added — currently unused; no icon system consumes this file today. |

## Why the scoring is a script, not just prose

Claude *can* do this arithmetic in its head from the methodology docs alone, but
running the same numbers through code guarantees the exact same score for the exact
same deal every time it's asked — across different sessions, different reps, months
apart. That consistency is the whole point of a "priority ranking" a rep can trust.

## Testing it yourself

```bash
python3 scripts/score_deals.py templates/deal-import-template.csv --today 2026-07-16
```

Compare against `examples/output-example-1.md` using `examples/sample-pipeline.csv`
(same 4 deals as `sample-pipeline.json`, in runnable CSV form) to sanity-check any
changes to the scoring weights.

## Related skills (same module)

- `deal-health-checker` — diagnoses a single deal's risk status, doesn't rank across deals
- `forecast-roller` — revenue rollup across the whole pipeline, manager-facing
- `follow-up-cadence-builder` — generates the actual outreach schedule/reminders

Keep triggering descriptions in each skill's `SKILL.md` distinct so requests don't
collide between these four.
