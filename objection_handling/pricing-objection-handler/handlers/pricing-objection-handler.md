# Pricing objection handler

Talk tracks for price and budget pushback. Use when `scripts/classify_objection.py` (or
reasoning) returns `category: pricing`.

## How to use this file

Pricing objections need more care than the general playbook because a wrong answer can commit
the company to something a rep isn't authorized to offer. Match the scenario, follow the talk
track direction, and always check the "do not say" column before responding.

## Pricing scenarios

| Scenario | Talk track direction | Do not say |
|---|---|---|
| "It's more expensive than what we pay now" | Reframe to total cost of ownership — incident response cost, downtime cost, staff time saved — not just license price. | Don't disparage the incumbent's price as "cheap for a reason" without evidence. |
| "We don't have budget this cycle" | Ask if this is a hard budget freeze or a prioritization question; offer a smaller starting scope if one exists. | Don't offer a discount rate — flag to sales ops for approved ranges. |
| "Competitor X quoted us less" | Ask what's included in that quote — support tier, contract length, add-ons — before comparing. | Don't assume the competitor quote is apples-to-apples; verify first. |
| "Can you do a discount?" | Acknowledge, then route to the actual approved discount process/owner rather than answering in the moment. | Never commit to a specific percentage in the handler's output. |

## Hard rule

This handler never states a specific discount percentage or dollar figure. If the prospect
pushes for a number, the response should route them to the approved pricing/discount owner, not
generate one.

*(Placeholder scenarios — confirm actual discount authority and approved ranges with sales ops
before using this in production.)*
