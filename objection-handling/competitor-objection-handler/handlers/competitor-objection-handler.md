# Competitor objection handler

Responses triggered when a competitor is name-dropped. Use when `scripts/classify_objection.py`
(or reasoning) returns `category: competitor`, and it also returns which competitor was matched.

## How to use this file

Look up the named competitor in the table below. Structure every response as: what they do well
→ how we differentiate → a question to ask back. Never state a competitor fact that isn't listed
here or otherwise verified — if the competitor isn't in the table, say the comparison needs
verification and offer to draft a new entry rather than guessing.

## Competitor battlecards

| Competitor | Their strength | Differentiation angle | Question to ask the prospect |
|---|---|---|---|
| Fortinet | Broad hardware/appliance portfolio, strong brand recognition | Emphasize unified management simplicity and total cost across the full stack, not just box price | "How much time does your team spend managing policies across appliances today?" |
| Palo Alto Networks | Deep enterprise feature set, strong analyst positioning | Emphasize faster time-to-value and lower operational overhead for mid-market teams | "How long did your last policy rollout take end to end?" |
| SonicWall | Price-competitive, familiar to SMB IT teams | Emphasize support responsiveness and update cadence | "How has support responsiveness been on your current contract?" |

## Hard rule

Only use verified, current facts about a competitor. If a claim can't be confirmed, flag it as
needing verification rather than including it in the response.

*(Placeholder set of three competitors — replace with the real competitor list and verified
current facts before production use.)*
