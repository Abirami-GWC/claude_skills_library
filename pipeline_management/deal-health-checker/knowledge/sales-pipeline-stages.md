# Sales Pipeline Stages (Health Context)

Same 8-stage taxonomy used across the Pipeline Management skills — keep this
consistent with `pipeline-prioritizer` and `forecast-roller` so a deal's stage
means the same thing everywhere.

| Stage | Evaluated for health? | Notes |
|---|---|---|
| Lead | Yes | Very early — some risk indicators (e.g., no decision maker yet) are expected here and shouldn't be over-weighted |
| Qualified | Yes | |
| Discovery | Yes | |
| Demo | Yes | |
| Proposal | Yes | Deals often stall here — proposal-pending risk is most relevant at this stage |
| Negotiation | Yes | Highest-value stage to catch a stall in — closest to revenue |
| Closed Won | No | Already closed — not part of an open-pipeline health check |
| Closed Lost | No | Already closed — not part of an open-pipeline health check |

If a deal's CRM stage name doesn't match one of these exactly, map it by meaning
to the closest bucket above rather than asking the user to rename it.
