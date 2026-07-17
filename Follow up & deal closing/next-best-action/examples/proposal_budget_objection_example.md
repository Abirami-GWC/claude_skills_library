# Example: Proposal stage, budget objection, override triggered

## Scenario

GWC Data proposed its Insight Suite platform to Alderbrook Health Network. Proposal sent June 20 ($85K/year, 2-year term). It's now July 2 — 12 days silence. Blocker: the VP of Data (Priya Anand) said budget approval is pending with their CFO.

## Input

> "Deal is with Alderbrook Health Network, stage is Proposal, proposal was sent June 20, no response since, it's now July 2. Blocker: budget approval pending with their CFO. What should I do next?"

## Output

```
Next best actions for Alderbrook Health Network (Proposal, 12 days since contact):

1. Send a follow-up now — 12 days exceeds the 7-day override threshold, so this comes before anything else.
2. Address the budget objection directly with ROI framing (cost of current manual reporting vs. Insight Suite) rather than jumping straight to a discount.
3. Offer to join a call with their CFO directly, or send a forwardable one-page ROI summary Priya can share internally.
```

## Why this is correct

The override rule (12 days > 7-day threshold) took priority over the default Proposal-stage action. The budget objection was matched to the `budget_or_price` entry in `objection_to_response.yaml` and folded into action #2 rather than listed separately. Action #3 reflects that Priya is a champion, not the economic buyer — per `knowledge/buyer_personas.md`, the move is to equip her, not just tell her to "follow up with your CFO."
