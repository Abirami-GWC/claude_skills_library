# Deal Stages (Cadence Context)

Same three-bucket taxonomy used across the Pipeline Management skills — keep this
consistent with `pipeline-prioritizer` so a deal's stage means the same thing
everywhere.

| Bucket | Typical CRM stage names | Cadence implication |
|---|---|---|
| `early` | Discovery, Qualification, Prospecting, New | Slower tempo — you're still earning attention, don't crowd the prospect |
| `mid` | Proposal, Negotiation, Solution Review | Moderate tempo — momentum matters, but so does patience while they evaluate |
| `late` | Verbal Commit, Contract Sent, Legal Review, Closing | Faster tempo — time-sensitive, administrative follow-through matters most |

## Fields needed for this skill

| Field | Required? | Notes |
|---|---|---|
| Deal/account name | Yes | For labeling the plan |
| Current stage | Yes | Normalize per the taxonomy above |
| Last contact date | Yes | If truly unknown, ask rather than assume "today" |
| Last contact channel | No | Email, call, LinkedIn, in-person — affects channel variety in the next touches |
| What happened at last contact | Yes | Drives message type — a positive call is different from an unanswered email |
| Number of consecutive unanswered touches | No | If unknown, ask or infer conservatively (assume 1 if unclear) — this number drives the stopping rule |
| Known stakeholders / decision makers | No | If a deal has multiple stakeholders and only one is engaged, note it — affects message content, see `followup-best-practices.md` |

If the deal's stage or last-contact date is missing, ask for it — don't guess a
contact history that wasn't given.
