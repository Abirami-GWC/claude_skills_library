# Example: Negotiation stage, stalled on legal review

## Scenario

A third deal: Bristol Logistics is in contract negotiation for Insight Suite. Legal has had the redlined MSA for 9 business days with no update. No pricing objection — the holdup is purely legal review.

## Input

> "Bristol Logistics deal — we're in negotiation, their legal has had our redlined MSA for 9 business days, no word back. No pricing pushback, just stuck in legal."

## Output

```
Next best actions for Bristol Logistics (Negotiation, 9 days since contact):

1. Send a follow-up now — 9 days exceeds the 7-day override threshold.
2. Confirm the outstanding redlines in writing and ask specifically what's still open on their side.
3. Offer to loop in their procurement/legal contact directly, or propose a specific decision date to keep the review from drifting further.
```

## Why this is correct

Even though the deal is in Negotiation (not Proposal) and there's no stated pricing objection, the 9-day silence still triggers the override — the rule applies regardless of stage. Because the holdup is legal/procurement, not a value objection, the persona guidance for procurement/legal (contract terms and process, not value-selling) shapes actions #2 and #3.
