# Testing Guide

**Purpose of this file:** Define positive, negative, boundary, and edge test cases for validating this skill's behavior, along with expected outputs and evaluation criteria, to support quality assurance and regression testing of the skill.

## Introduction

This guide is used to verify that the Board Deck Narrative skill activates correctly, stays within scope, applies its frameworks consistently, and handles imperfect real-world input gracefully. Each test case below can be run manually or scripted against the skill's expected behavior as defined in `SKILL.md` and the supporting `references/`, `templates/`, and `prompts/` files.

## Positive Test Cases

These confirm the skill activates and produces correct output when the request is squarely in scope.

1. **Basic executive summary request.** Input: a short GTM plan plus 3-4 metrics; request a one-page board summary. Expected: BLUF-first one-pager using `templates/executive_summary_template.md`, metrics with trend/comparison, priorities compressed to 5 or fewer.
2. **Investment ask.** Input: a budget increase request with rationale. Expected: options analysis with status quo, recommendation, risk-adjusted framing, and cost of inaction per `references/decision_frameworks.md`.
3. **Underperformance report.** Input: a missed target and known cause. Expected: honest naming of the miss in the BLUF, cause stated plainly, corrective plan with timeframe — no softening.
4. **Pivot narrative.** Input: prior strategy, evidence of a ceiling, and new direction. Expected: context-conflict-resolution arc applied correctly, explicit ask for approval structured with alternatives.
5. **Presentation outline request.** Input: full strategy and metrics; request an 8-12 slide outline. Expected: `templates/presentation_outline_template.md` populated with one core message per slide, no unfilled placeholders.
6. **Roadmap compression.** Input: a long list (20+) of initiatives; request 3-5 strategic priorities. Expected: initiatives grouped by outcome/theme, capped at 5, each an outcome statement.
7. **Multi-format request.** Input: request both a memo and a slide outline from the same source material. Expected: consistent narrative and metrics across both outputs, each using its correct template.

## Negative Test Cases (Out-of-Scope Requests)

These confirm the skill correctly declines or redirects requests outside its stated scope.

1. **"Build my full GTM strategy."** Expected: skill declines to originate strategy, states this is the role of a GTM Strategy Builder skill, and offers to proceed with narrative condensation once strategy content exists.
2. **"Model our marketing budget by channel and calculate ROI."** Expected: skill declines to build a budget model, states this belongs to a Budget Allocator skill, and offers to narrate a budget ask once conclusions exist.
3. **"Build our detailed Q3 roadmap with owners and dates."** Expected: skill declines to construct a detailed roadmap, states this belongs to a Quarterly Roadmap Planner skill, and offers to compress an existing roadmap's priorities once supplied.
4. **"Research our competitive landscape and size the market."** Expected: skill declines to perform net-new market research, states this is out of scope, and asks the user to supply findings if they want them included in the narrative.
5. **Compound request: "Build the strategy and then turn it into a board deck."** Expected: skill separates the two parts, declines the strategy-origination portion, and proceeds only with the narrative-condensation portion once strategy content is supplied.

## Boundary Cases

These test behavior at the edges of usable input.

1. **Extremely sparse input** (e.g., "We had an okay quarter, write the board summary"). Expected: skill does not fabricate metrics or priorities; it requests minimum viable input (at least one metric, the meeting's purpose, and top priorities) or delivers a clearly labeled skeleton with placeholders.
2. **Extremely long source material** (e.g., a 40+ page strategy document or a 40-initiative roadmap). Expected: skill reads and compresses fully, capping metrics at 5-7 and priorities at 5, grouping by theme, and noting that detail was omitted for length.
3. **No stated length/format constraint.** Expected: skill defaults to board-standard brevity (1-2 pages or 8-12 slides) rather than producing an unbounded document.
4. **No stated audience or ask.** Expected: skill asks a clarifying question about audience and purpose before drafting, since this materially changes structure (informational vs. decision-request framing).
5. **Extremely tight constraint** (e.g., "3 sentences only"). Expected: skill compresses to the BLUF and, if space allows, the single most important supporting point, honoring the constraint even at the cost of dropping secondary detail.

## Edge Cases

1. **Conflicting data** (e.g., two different totals for the same metric in the source material). Expected: skill surfaces the conflict to the user rather than silently choosing one figure.
2. **Request to obscure or omit bad news.** Expected: skill maintains honest framing of material risks and misses, declining to omit them, while still presenting them constructively with a forward plan.
3. **Sensitive/confidential figures with wide distribution.** Expected: skill frames figures at appropriate precision (e.g., ranges or trend direction) rather than exact sensitive values, while still disclosing material risk.
4. **Board wants unusually high operational detail.** Expected: skill can accommodate if explicitly requested, but defaults to higher altitude and flags that the level of detail is atypical for board material.
5. **Mixed informational and decision content in one request with no labeling provided by the user.** Expected: skill classifies each piece of content as For Information, For Decision, or For Discussion itself and labels the output accordingly.
6. **User asks for output in a format not covered by the four templates.** Expected: skill adapts the closest matching template and notes the adaptation, rather than declining entirely.

## Expected Outputs (Summary Reference)

| Test Category | Expected Output Shape |
|---|---|
| Positive cases | Fully populated template, BLUF-first, within scope, respecting all validation rules |
| Negative cases | Clear decline/redirect statement naming the correct upstream skill, no fabricated strategy/budget/roadmap content |
| Boundary cases | Either a compressed, capped output or a clarifying request for minimum viable input — never fabrication |
| Edge cases | Conflicts and sensitivities surfaced explicitly; honest framing preserved; graceful adaptation when format doesn't match a template exactly |

## Evaluation Criteria

- **Scope fidelity:** Did the skill correctly distinguish narrative condensation from strategy/budget/roadmap origination in every test case?
- **BLUF and altitude discipline:** Does every output lead with the bottom line and stay at board-appropriate altitude throughout?
- **Compression discipline:** Are metrics capped at 5-7 and priorities capped at 5 in every applicable case?
- **Honesty under compression:** Is bad news, risk, and conflicting data preserved and named clearly rather than smoothed over or omitted?
- **Gap handling:** Are missing data and assumptions explicitly flagged rather than fabricated, in both sparse-input and long-source-material cases?
- **Decision structuring:** Does every ask include alternatives, a clear recommendation, rationale, and risk-adjusted framing (including cost of inaction)?
- **Template fidelity:** Is the correct template used and fully populated, with no leftover bracketed placeholders in final output?
- **Reusability:** Does the output remain industry-agnostic and free of any fabricated company/brand references beyond what the user themselves supplied?
