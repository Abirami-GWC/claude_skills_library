# Sales Stages & Input Fields

## Stage taxonomy

Every deal's CRM stage must normalize into one of three buckets:

| Bucket | Typical CRM stage names |
|---|---|
| `early` | Discovery, Qualification, Prospecting, New |
| `mid` | Proposal, Negotiation, Solution Review |
| `late` | Verbal Commit, Contract Sent, Legal Review, Closing |

CRM stage names vary a lot between companies — map whatever the user's export uses
onto these three buckets by meaning, not exact string match.

## Expected fields

| Field | CSV column (for scripts/score_deals.py) | Required? | Common aliases | Notes |
|---|---|---|---|---|
| Deal name / account | `deal_name` | Yes | Opportunity Name, Account, Company | Used to label rows in output |
| Deal value | `value` | Yes | Amount, ACV, Deal Size | Assume the currency stated by the user; if mixed currencies appear, ask once rather than guessing an FX rate |
| Sales stage | `stage` | Yes | Stage, Pipeline Stage | Normalize per the taxonomy above |
| Deal probability (%) | `probability` | No | Win %, Confidence | If blank, inferred from stage — see `priority-rules.md` |
| Expected close date | `close_date` | No | Close Date, Target Close | Format YYYY-MM-DD. If blank, urgency is treated as unknown, not safe |
| Last customer interaction date | `last_activity_date` | No | Last Activity, Last Touch | Format YYYY-MM-DD. If blank, engagement recency is treated as unknown |
| Customer engagement notes | `engagement_notes` | No | Notes, Sentiment | Free text; used only in the written explanation, not the numeric score |

## Handling missing data

- Never block the ranking on a missing optional field — apply the documented
  default (see `priority-rules.md` and `scoring-guidelines.md`) and flag it.
- Do not silently invent a specific number in prose (e.g., a made-up close date).
- If a *required* field (deal name, value, stage) is missing, ask the user for just
  that gap rather than guessing.
