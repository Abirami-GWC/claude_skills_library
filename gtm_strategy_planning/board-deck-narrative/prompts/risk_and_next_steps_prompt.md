# Risk and Next Steps Drafting Prompt

**Purpose of this file:** Provide the drafting prompt used to produce the risk framing and next-steps/ask sections common to all board outputs, ensuring consistent risk-adjusted framing and decision-ready asks.

## Purpose

Use this prompt as a focused pass — either standalone (e.g., "just help me frame the risks for the board" or "help me write the next steps and ask") or as a component embedded within a fuller executive summary, board memo, or decision brief. It applies the decision-framework guidance for risk-adjusted asks and next-step framing.

## Inputs

- Known risks, obstacles, or open issues from the source material
- Any planned mitigations or contingency plans
- The specific ask, if any (budget, approval, resourcing, timeline extension)
- Alternatives already considered, if any
- Any deadline or timing constraint driving urgency

## Instructions

```
You are drafting the risk framing and/or next-steps/ask section of a board narrative.

For risks:
1. List the risks most relevant to the current narrative or decision — typically no more than 3. Do not include an exhaustive operational risk register.
2. For each risk, state: what the risk is, its business impact if it materializes (in plain business terms, not technical/process terms), and the mitigation or contingency plan if one exists.
3. If a risk has no known mitigation yet, say so explicitly rather than implying one exists.
4. If risks conflict with the overall positive tone of the narrative (e.g., strong results but a real emerging risk), name the tension directly rather than downplaying it.

For next steps / the ask:
5. If this is a pure information update, state next steps as concrete actions with owners and target dates where known.
6. If there is an explicit ask (approval, budget, pivot sign-off), structure it per references/decision_frameworks.md:
   - State the recommendation clearly and first.
   - Present at least one genuine alternative and the status-quo/do-nothing option.
   - State the rationale for the recommendation relative to the alternatives.
   - State the risk if approved (impact and mitigation) and the cost of inaction if not approved.
7. State explicitly what decision or action is being requested of the audience, and by when if there is a deadline.
8. Note any missing information needed to finalize the ask (e.g., a cost figure not yet available) rather than estimating it.
```

## Expected Output

A risk section and/or next-steps/ask section, ready to insert into any of the templates in `templates/`, including:
- Up to 3 risks, each with business impact and mitigation (or an explicit note that mitigation is not yet defined)
- A clearly stated next-steps list (owner/date) for informational updates, or
- A fully structured ask (recommendation, alternatives, rationale, risk-adjusted framing, cost of inaction) for decision requests

## Validation Checklist

- [ ] No more than 3 risks listed, each with business impact stated in plain terms
- [ ] Mitigation stated where known; explicitly marked as undefined where not
- [ ] Conflicting signals (good news vs. emerging risk) named directly, not smoothed over
- [ ] Next steps include owner and date where informational
- [ ] Any ask includes recommendation, at least one alternative, status quo, rationale, and cost of inaction
- [ ] The specific decision or action requested is stated explicitly, with a deadline if applicable
- [ ] Missing information is flagged rather than estimated
