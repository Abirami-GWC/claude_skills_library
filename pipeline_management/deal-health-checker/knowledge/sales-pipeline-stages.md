# Sales Pipeline Stages (Health Context)

Same 8-stage taxonomy used by `forecast-roller` — keep this consistent with
that skill so a deal's stage carries the same meaning in both places.

**Note on `pipeline-prioritizer` and `follow-up-cadence-builder`:** those two
skills deliberately use a *different*, coarser 3-bucket taxonomy
(`early`/`mid`/`late` — see their own `knowledge/sales-stages.md` and
`knowledge/deal-stages.md`) suited to ranking and cadence-timing, where this
skill's and `forecast-roller`'s finer 8-stage model suits health-diagnosis and
probability-weighted forecasting. The two taxonomies are not interchangeable —
don't assume a stage-derived score or probability from one skill carries over
to the other; each skill's own knowledge file is the source of truth for its
own stage handling.

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
