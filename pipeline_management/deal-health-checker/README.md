# deal-health-checker

Part of the **Pipeline Management** module (owner: Nithisri) in the Sales &
Marketing Claude Skills project.

## What it does

Classifies every open deal as Healthy, Warning, or At Risk, explains exactly why
(risk factors, positive indicators, and missing information), and gives concrete
recommended actions — so a deal in trouble gets caught before it's lost, not after.

Unlike `pipeline-prioritizer` (which tells a rep what to work on first),
this skill answers: *which deals are in danger, why, and what should be done
about it?*

## Folder guide

| Path | Purpose |
|---|---|
| `SKILL.md` | Triggering logic only (read by Claude automatically). Points to `prompt.md`. |
| `prompt.md` | The actual step-by-step process Claude follows once triggered. |
| `knowledge/sales-pipeline-stages.md` | Stage taxonomy + which stages get evaluated (Closed Won/Lost don't). |
| `knowledge/risk-indicators.md` | Each risk indicator and its point weight, with rationale. |
| `knowledge/deal-health-rules.md` | How points sum into Healthy/Warning/At Risk + priority, and edge cases. |
| `templates/health-report.md` | Per-deal report layout. |
| `templates/risk-summary.md` | Pipeline-level rollup (counts per tier). |
| `templates/action-plan.md` | Concrete action table for Warning/At Risk deals. |
| `examples/input-example-1.md` | A realistic, unstructured 3-deal health check request. |
| `examples/output-example-1.md` | The correct classification and report for that input — real computed scores. |
| `examples/sample-deal.json` | The same 3 deals in structured JSON, for reference/testing. |
| `scripts/deal_health.py` | Computes the actual risk score and classification — run this rather than tallying indicators by hand. |
| `assets/` | Reserved for a skill icon, if one is ever added — currently unused. |

## Why this needed a `scripts/` folder

Classification here comes from summing several weighted indicators (activity
recency, meeting status, decision-maker status, response status, plus optional
stage-stall and missed-followup signals). Doing this by feel risks a rep getting a
different verdict on the same deal depending on the day — locking the arithmetic
into tested code means the same facts always produce the same status.

## Key design decisions worth reviewing

- **Missing information counts as partial risk, not zero risk.** A deal with no
  logged decision maker and no logged response status can't be called Healthy
  just because nothing was *confirmed* bad — this is deliberate, per the original
  spec's "do not make assumptions when information is missing."
- **Thresholds**: Healthy ≤1.5, Warning 1.5–3.5, At Risk >3.5 (see
  `deal-health-rules.md`). Verified against the original ABC Manufacturing example
  (18 days silent, no meeting, no decision maker, no response → score 5.5 → At
  Risk, matching the spec's expected output).
- **Qualitative signals aren't scored.** Free-text engagement notes inform the
  narrative and recommended actions, but never move a deal between tiers on their
  own — too subjective to weight consistently.

## Testing it yourself

```bash
python3 scripts/deal_health.py examples/sample-deal.json  # convert to CSV first
```

Compare against `examples/output-example-1.md` to sanity-check any changes to the
weights or thresholds.

## Related skills (same module)

- `pipeline-prioritizer` — ranks deals for work order, doesn't diagnose risk
- `forecast-roller` — revenue rollup, manager-facing
- `follow-up-cadence-builder` — schedules outreach once a deal is flagged here

Keep triggering descriptions in each skill's `SKILL.md` distinct so requests don't
collide between these four.
