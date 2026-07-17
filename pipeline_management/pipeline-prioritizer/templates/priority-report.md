# Priority Report Template

Present results as a ranked table followed by a short data-quality note. Don't show
the raw 0-100 sub-scores unless the user asks for the math — lead with the ranking
and the plain-English reason.

## Standard layout

```
## Pipeline Priority Ranking

| Rank | Deal | Value | Stage | Close Date | Why this rank |
|---|---|---|---|---|---|
| 1 | Acme Corp – Platform Upgrade | $85,000 | Late (contract sent) | Jul 22 | Highest value in the batch, closing in a week, verbal already given |
| 2 | ... | ... | ... | ... | ... |

**Data quality notes:** [list any deals scored using inferred/default values, as
flagged by scripts/score_deals.py — e.g., "Beta Inc: no close date provided, urgency
treated as unknown" — omit this section entirely if nothing was inferred]
```

## For large batches (50+ deals)

Give full rows for roughly the top 10-15, then group the remainder:

```
### High priority (16-25)
[deal names], typically because: [shared reason, e.g., "mid-stage, closing within
the quarter, recently active"]

### Medium priority (26-40)
...

### Low priority (41+)
...
```

## Tone

Direct and scannable — a rep should be able to read the top 5 rows and know exactly
what to do next. Don't pad with generic sales encouragement ("Great pipeline!"). If a
deal's ranking implies a clear next action (e.g., "hasn't been touched in 3 weeks"),
it's fine to note that in the "why" column, but full next-action detail belongs to
`follow-up-cadence-builder`, not here — keep this skill focused on ordering.
