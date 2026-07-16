# Priority Rules

These are the policy decisions behind the ranking — the "what to do when" rules that
sit above the raw scoring math (see `scoring-guidelines.md` for the formula itself).

## Default weighting

| Factor | Default weight |
|---|---|
| Deal Value | 25% |
| Probability to Close | 20% |
| Urgency (time to close date) | 20% |
| Engagement Recency | 20% |
| Stage Weight | 15% |

## When to override the default weights

If the user states a different priority in conversation (e.g., "ignore deal size,
I only care what closes this quarter", or "weight engagement higher, I want to know
who's going cold"), use their stated priority instead of the default — pass it to
`scripts/score_deals.py --weights` and say plainly in the output that custom
weighting was used and why.

Don't silently keep defaults if the user has expressed a preference, and don't
apply a one-off preference to future requests unless they say to make it standard.

## Tie-breaking

1. Nearer expected close date wins.
2. If still tied, higher deal value wins.
3. If still tied, report the deals as effectively tied rather than forcing an
   arbitrary order — don't invent a false distinction.

## Edge cases

- **Only one deal given**: still score it, but say plainly there's nothing to rank
  it against — report the score and what it implies, not a "#1 of 1" table.
- **All deals missing close dates**: note that urgency scoring is degraded across
  the whole batch — don't quietly treat them as either urgent or safe.
- **Very large batches (50+ deals)**: rank all of them, but only give full
  per-deal explanations for the top ~10-15. Group the remainder into High/Medium/Low
  tiers with one shared reason per tier (see `templates/priority-report.md`).
- **Mixed currencies in one batch**: ask the user once how to handle it rather than
  guessing an exchange rate.
