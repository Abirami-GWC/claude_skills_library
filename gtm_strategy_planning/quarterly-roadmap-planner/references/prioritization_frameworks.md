# Prioritization Frameworks: RICE, MoSCoW, Value vs. Effort, and Weighted Scoring

> **Purpose:** Explain four prioritization frameworks used to rank initiatives for a quarterly roadmap and provide guidance on when to use each.

## Introduction

Before initiatives can be sequenced into a roadmap, they must be prioritized against limited time, people, and budget. Different decision contexts call for different frameworks: some situations need a quick numeric ranking of a long backlog, others need a binary scope-negotiation tool against a fixed deadline, and others need a way to reconcile multiple stakeholders' differing priorities. This reference covers four widely used frameworks — RICE, MoSCoW, Value vs. Effort, and Weighted Scoring — and how to choose among them.

## Detailed Explanation

### RICE (Reach, Impact, Confidence, Effort)

RICE produces a numeric score for each initiative: `RICE Score = (Reach × Impact × Confidence) / Effort`.
- **Reach:** how many customers, accounts, or users the initiative affects in a given period.
- **Impact:** the magnitude of effect on the target outcome, typically scored on a scale (e.g., 3 = high, 2 = medium, 1 = low, 0.5 = minimal).
- **Confidence:** how confident the team is in the reach and impact estimates, expressed as a percentage (e.g., 100%, 80%, 50%).
- **Effort:** the estimated person-time required, typically in person-months or person-weeks.

RICE is best suited to ranking a sizeable backlog of initiatives (5 or more) where reach and effort can be reasonably estimated, and where the team wants a defensible, numeric ranking rather than a subjective one.

### MoSCoW (Must, Should, Could, Won't)

MoSCoW sorts initiatives into four categories against a fixed scope or deadline:
- **Must have:** non-negotiable; the plan fails without it.
- **Should have:** important but not fatal to omit this quarter.
- **Could have:** desirable if capacity allows, first to be cut under pressure.
- **Won't have (this time):** explicitly out of scope for this period, to manage expectations.

MoSCoW is best suited to scope negotiation under a fixed deadline or fixed capacity — for example, finalizing what goes into a specific launch date — because it forces an explicit, stakeholder-visible line between commitment and exclusion.

### Value vs. Effort

This is a simple two-axis visual framework plotting each initiative's business value against its implementation effort, typically producing four quadrants: high value/low effort ("quick wins," do first), high value/high effort ("major projects," plan deliberately), low value/low effort ("fill-ins," do if slack exists), and low value/high effort ("thankless tasks," deprioritize or reject). It is best suited to fast triage of a moderate-size list when precise numeric estimation is not necessary or not yet possible, and when a visual, easy-to-communicate artifact is needed for a broad stakeholder audience.

### Weighted Scoring

Weighted Scoring assigns multiple criteria (e.g., strategic alignment, revenue potential, customer request volume, risk reduction, effort) each a stakeholder-agreed weight, scores every initiative against each criterion, and sums the weighted scores to produce a ranked list. It is best suited when multiple stakeholders have legitimately different priorities that need to be reconciled transparently (e.g., balancing a sales-driven criterion against a product-quality criterion) and a single-dimension framework like RICE would understate factors stakeholders care about, such as strategic alignment or risk.

### Choosing a Framework

| Situation | Recommended Framework |
|---|---|
| Long backlog, need defensible numeric ranking | RICE |
| Fixed deadline, need explicit scope negotiation | MoSCoW |
| Need a fast, visual, broadly understandable triage | Value vs. Effort |
| Multiple stakeholders with different weighted priorities | Weighted Scoring |

Frameworks can be combined: for example, use Weighted Scoring or RICE to produce an initial ranked list, then apply MoSCoW to finalize what fits within a hard deadline.

## Professional Guidance

- Always state which framework is being used and why; silently defaulting to one framework regardless of context reduces stakeholder trust in the outcome.
- Keep scoring inputs (reach, impact, effort, criteria weights) visible in the output so the ranking is auditable, not a black box.
- Recalibrate confidence and effort estimates when new information arrives — a RICE score from six weeks ago may no longer reflect reality.
- When using Weighted Scoring, agree on criteria and weights with stakeholders before scoring individual initiatives, not after, to avoid the appearance of reverse-engineering a preferred outcome.
- MoSCoW categories should be revisited, not fixed forever — a "Could have" item may become a "Must have" if circumstances change (see mid-quarter re-prioritization guidance in `examples/examples.md`).

## Examples

*Illustrative and generic — no real company implied.*

- A backlog of ten candidate initiatives for a quarter is scored with RICE; an initiative reaching a large customer segment with high estimated impact and modest effort rises to the top of the ranked list.
- A product launch with a fixed external date uses MoSCoW to separate "Must have" launch-blocking features from "Could have" enhancements that are explicitly deferred to the following quarter.
- A cross-functional planning session uses a Value vs. Effort quadrant chart to quickly agree which of fifteen proposed initiatives are "quick wins" worth doing immediately.
- A leadership team facing competing priorities from sales, product, and customer success uses Weighted Scoring with agreed criteria (strategic alignment 30%, revenue potential 30%, customer risk reduction 20%, effort 20%) to produce a ranked list all three functions accept as fair.

## Common Mistakes

- Using RICE on a very short list (2–3 items) where the scoring overhead exceeds its value; a simpler comparison would suffice.
- Using MoSCoW without a genuinely fixed deadline, which removes the forcing function that makes the framework useful.
- Treating Value vs. Effort quadrant placement as precise scoring rather than an approximate visual triage tool.
- Setting Weighted Scoring criteria weights without stakeholder agreement, leading to disputed rankings.
- Never revisiting prioritization after initial scoring, even when new information invalidates original estimates.

## Best Practices

- Match the framework to the decision context rather than defaulting to a single familiar tool.
- Keep all scoring inputs transparent and auditable in the output.
- Revisit prioritization at defined checkpoints (e.g., the mid-quarter review) rather than only at the start of the quarter.
- Combine frameworks when useful — for example, RICE to rank, then MoSCoW to finalize scope against a deadline.
- Document the rationale for the chosen framework briefly alongside the ranked output.

## Summary

RICE, MoSCoW, Value vs. Effort, and Weighted Scoring each solve a different prioritization problem: RICE ranks a sizeable backlog numerically, MoSCoW negotiates scope against a fixed deadline, Value vs. Effort provides fast visual triage, and Weighted Scoring reconciles multiple stakeholders' differing priorities transparently. Selecting the right tool — and being explicit about why it was chosen — is what makes a quarterly roadmap's prioritization defensible rather than arbitrary.
