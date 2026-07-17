# Health Report Template

The per-deal report. Lead with the status so it's scannable, then support it with
specifics — never a generic risk factor that doesn't come from this deal's actual
data.

## Standard layout

```
## Deal Health Report — [Deal Name]

**Health Status:** 🔴 At Risk _(or 🟡 Warning / 🟢 Healthy)_
**Priority:** High _(or Medium / Low)_

**Positive Indicators**
- [Only list what's actually confirmed positive for this deal]

**Risk Factors**
- [Only list what's actually flagged for this deal — from scripts/deal_health.py's output]

**Missing Information**
- [Only list fields that were genuinely not provided — omit this section entirely
  if nothing was missing]

**Recommended Actions**
1. [Specific action tied to an actual risk factor above — e.g., "Identify the
   economic buyer" only if decision maker is actually unidentified for this deal]
2. ...
```

## When a deal is fully Healthy

Still produce the report — don't skip it or pad it with invented caveats:

```
**Health Status:** 🟢 Healthy
**Priority:** Low

**Positive Indicators**
- Recent contact, next meeting scheduled, decision maker identified, customer responsive

No risk factors identified. No action needed beyond the next scheduled meeting.
```
