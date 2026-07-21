# Risk Indicators

Each indicator contributes points toward a deal's overall risk score (see
`deal-health-rules.md` for how the total maps to Healthy/Warning/At Risk). Points
reflect how strongly each factor predicts a deal stalling or being lost.

## Activity recency (based on days since last customer contact)

| Condition | Points | Rationale |
|---|---|---|
| Contact within 7 days | 0 | Recent — no concern |
| Contact 8-14 days ago | 1 | Minor inactivity — worth a nudge, not yet alarming |
| Contact more than 14 days ago | 2 | Significant inactivity — the single strongest predictor of a stalling deal |
| Last contact date not provided | 1.5 | Can't verify the deal is active — treated with real caution, not assumed fine |

## Next meeting scheduled

| Condition | Points | Rationale |
|---|---|---|
| Yes, scheduled | 0 | A scheduled next step is a strong positive signal |
| No | 1 | No forward motion planned — a deal with no next meeting has no forcing function to progress |
| Not stated | 0.5 | Unknown — can't confirm there's a next step |

## Decision maker identified

| Condition | Points | Rationale |
|---|---|---|
| Yes, named | 0 | |
| No / stated as unknown | 1 | Not knowing who ultimately decides is a real, not just administrative, risk — treat "unknown" here as equivalent to "not identified," since either way the rep can't confirm the deal can actually close |
| Not stated | 0.5 | Unknown status is treated more leniently than a confirmed "no," but still isn't scored as risk-free |

## Customer response

| Condition | Points | Rationale |
|---|---|---|
| Customer has responded | 0 | |
| No response | 1.5 | The strongest engagement signal — silence after outreach is a leading indicator of a dying deal |
| Not stated | 0.75 | Unknown response status is itself worth flagging |

## Optional supplementary indicators (only score if the data is provided — don't penalize a deal for a field simply not being tracked)

| Condition | Points | Rationale |
|---|---|---|
| Deal has sat in its current stage more than 30 days | +1 | A genuinely stalled deal, distinct from just "no recent contact" — the deal isn't progressing structurally |
| 2 or more missed/unanswered follow-up attempts logged | +1 | A pattern, not a one-off — worth weighting beyond the response-status indicator above |

## What is deliberately NOT scored numerically

Qualitative engagement signals (e.g., free-text notes like "champion seems less
enthusiastic" or "mentioned a budget freeze") are not converted into points —
they're too subjective to weight consistently. Use them to inform the narrative
explanation and recommended actions, not to move a deal between tiers on their
own. If a qualitative note meaningfully changes your read of a deal, say so
explicitly in the write-up rather than silently adjusting the score.
