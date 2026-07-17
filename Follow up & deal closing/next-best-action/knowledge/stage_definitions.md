# Generic B2B Pipeline Stage Definitions

Use this model as the default. If the user's organization uses different stage names, map their terms to the closest stage below (or ask), and remember their naming for the rest of the conversation.

| Stage | Definition | Typical duration |
|---|---|---|
| Prospecting | No meeting booked yet, or an initial outreach/intro has been sent but not yet answered with interest | Days to a few weeks |
| Discovery | A discovery call has happened; the buyer's needs and pains are still being scoped | 1-2 weeks |
| Demo/Evaluation | A demo has been delivered; the buyer is actively evaluating fit, possibly running a trial/POC | 2-4 weeks |
| Proposal | A formal proposal or quote has been sent; awaiting a decision | 1-3 weeks |
| Negotiation | Commercial or legal terms are actively being discussed (redlines, pricing, contract language) | 1-4 weeks |
| Closed Won | Contract signed | — |
| Closed Lost | Deal explicitly lost or gone permanently cold | — |

## Signals that indicate a stage, even if not stated explicitly

- "They asked for pricing" → Demo/Evaluation transitioning to Proposal.
- "Legal is reviewing" or "redlines" → Negotiation.
- "Went quiet after the demo" → still Demo/Evaluation, but flag as at-risk (see the engagement-signal override).
- "They said no" or "went with someone else" → Closed Lost.
- "They signed" / "PO issued" → Closed Won.

## What "moving forward" means at each stage

- Prospecting → Discovery: securing a first qualified conversation.
- Discovery → Demo/Evaluation: getting a demo booked that's scoped to the stated needs.
- Demo/Evaluation → Proposal: getting to "yes, send us pricing."
- Proposal → Negotiation: getting a substantive response (not silence) to the proposal.
- Negotiation → Closed Won: getting to signature.
