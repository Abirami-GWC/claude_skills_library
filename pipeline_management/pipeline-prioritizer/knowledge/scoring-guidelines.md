# Scoring Guidelines

The exact per-factor math used by `scripts/score_deals.py`. This is implemented in
code rather than done by hand, so a rep gets the same score for the same deal every
time — trust in the ranking depends on that consistency.

## How each factor is scored (0-100 sub-score, before weighting)

**Deal Value** — normalized within the batch: the largest deal in the list scores
100, others scored proportionally. This is relative on purpose — a $50k deal is huge
in one rep's book and small in another's.

**Probability to Close** — uses the stated probability directly if given. If missing,
inferred from stage but *dampened halfway toward the neutral midpoint (50)* rather
than used at full strength: Early ~35, Mid ~50, Late ~65 (vs. the undamped
20/50/80 the stage itself would suggest). This is deliberate: Stage Weight (below)
is already a separate scored factor derived from the same stage value — if the
inferred Probability factor also used the raw stage-derived number at full
strength, one underlying fact (stage) would end up driving ~35% of the total
score (20% + 15%) instead of the documented 20%/15% split staying independent.
Dampening keeps the inference directionally correct (higher stage → higher
inferred probability) without letting it silently collapse into a second copy of
the Stage Weight factor. This only applies when probability is inferred — a
stated probability is always used as-is, undamped.

**Urgency** — based on days until expected close date:
- Within 7 days → 100
- 8–30 days → 75
- 31–90 days → 50
- 90+ days → 25
- No close date → 40 (neutral-low, flagged as unknown — not treated as either urgent
  or safe)

**Engagement Recency** — based on days since last interaction:
- Within 3 days → 100
- 4–14 days → 70
- 15–30 days → 40
- 30+ days → 15 (going cold — worth calling out explicitly in the explanation)
- Unknown → 50 (neutral, flagged as unknown)

**Stage Weight**:
- Late (verbal, contract sent, negotiation) → 100
- Mid (proposal) → 65
- Early (discovery, qualification) → 35

## Final formula

`Priority Score = (Value×0.25) + (Probability×0.20) + (Urgency×0.20) + (Engagement×0.20) + (Stage×0.15)`

(weights are the defaults from `priority-rules.md` — override via
`scripts/score_deals.py --weights` when the user asks for different priorities)

## Explaining the score (don't just report the number)

For each deal, name the 1-2 factors that most moved it up or down relative to the
rest of the batch — not all five every time. E.g.:
- "Ranked #2 — large deal and closing this week, despite being early-stage."
- "Ranked #8 — solid probability, but no contact in 3+ weeks is dragging it down."

The numeric score is a sorting mechanism for the script, not something to show the
rep broken down factor-by-factor unless they ask.
