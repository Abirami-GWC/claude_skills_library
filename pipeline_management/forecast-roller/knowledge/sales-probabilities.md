# Sales Probabilities by Stage

Used to infer a deal's probability when none is stated. Always prefer a stated
probability over this inferred default — these ranges are a fallback, not a
correction.

| Stage | Typical probability range | Inferred default (midpoint) |
|---|---|---|
| Lead | 0-5% | Not applicable — excluded from forecast |
| Qualified | 5-15% | 10% |
| Discovery | 15-30% | 23% |
| Demo | 30-50% | 40% |
| Proposal | 50-80% | 65% |
| Negotiation | 80-95% | 88% |
| Closed Won | 100% | Not applicable — already recognized, not forecasted |
| Closed Lost | 0% | Not applicable — excluded from forecast |

If a stated probability falls well outside the typical range for its stage (e.g.,
a Proposal-stage deal at 45%, just under the 50-80% range), use the stated number
as given — a rep's specific knowledge of that deal outweighs the general range.
Don't "correct" a stated probability toward the stage average.
