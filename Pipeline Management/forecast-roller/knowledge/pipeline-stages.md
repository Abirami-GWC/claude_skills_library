# Pipeline Stages

The full stage taxonomy, and which stages count toward an active forecast.

| Stage | Included in forecast? | Notes |
|---|---|---|
| Lead | No | Too early/unqualified — informational only, not weighted into the forecast |
| Qualified | Yes | Earliest stage counted in the active forecast |
| Discovery | Yes | |
| Demo | Yes | |
| Proposal | Yes | |
| Negotiation | Yes | Latest open stage — highest confidence |
| Closed Won | Tracked separately | Already-recognized revenue — report alongside the forecast, but don't add it into the *forecasted* total, since it's not a prediction anymore |
| Closed Lost | No | Excluded entirely |

If a deal's CRM stage name doesn't match one of these exactly (e.g., "Contract
Sent" instead of "Negotiation"), map it by meaning to the closest bucket above —
don't ask the user to rename their stages.
