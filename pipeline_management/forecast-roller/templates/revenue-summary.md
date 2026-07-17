# Revenue Summary Template

The confidence-tier breakdown, inserted into `forecast-report.md`. Always show all
three tiers, even if one is zero — a manager should see the full shape of the
pipeline, not just the parts with revenue in them.

## Layout

```
| Confidence | Revenue | Deals |
|---|---|---|
| High (≥70%) | $[high total] | [count] |
| Medium (40-69%) | $[medium total] | [count] |
| Low (<40%) | $[low total] | [count] |
| **Total Expected Revenue** | **$[total]** | **[total count]** |
```

If any deals were already Closed Won (tracked separately, not part of this total)
or fall in a later period, add a line noting the amount excluded and why —
directly under the table, not buried in prose elsewhere:

```
*Already won this period (not included above): $[amount] — [deal names]*
*Excluded (closing after this period): $[amount] — [deal names]*
```
