# Risk Summary Template

The pipeline-level rollup, used when checking more than one deal at once. Give the
manager the shape of the whole pipeline before the per-deal detail.

## Layout

```
## Pipeline Risk Summary

| Status | Count | Deals |
|---|---|---|
| 🟢 Healthy | [count] | [names, or "see below" if long] |
| 🟡 Warning | [count] | [names] |
| 🔴 At Risk | [count] | [names] |

**Overall Pipeline Health:** [1-2 sentence read on the whole pipeline — e.g., "1 of
3 open deals is at risk, driven mainly by stalled communication rather than a
structural pipeline problem" — don't just restate the counts, interpret them]
```

## For large pipelines (50+ deals)

Give full per-deal detail only for At Risk deals. For Healthy and Warning, list
names grouped under their tier without individual risk-factor write-ups, unless
asked for detail on a specific one.
