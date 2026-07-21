# Board Deck Narrative — Worked Examples

**Purpose of this file:** Provide realistic worked examples showing when this skill activates, how it processes a request, and what a good (and alternative) output looks like, across different industries, company stages, and board asks. All examples use generic, illustrative content only — no real company, product, or brand names.

---

## Example 1: Early-Stage Software — Requesting a Budget Increase

**User Request:** "We have our board meeting in two weeks. I need a one-pager that makes the case for a 25% increase in our demand generation budget, based on the pipeline data and plan I'm pasting in."

**Why the Skill Activates:** The user has existing pipeline data and a plan, and wants it condensed into a board-ready ask — a classic investment-justification scenario, squarely within the skill's narrative-condensation scope.

**Workflow:** Inventory source material → identify north star and 2-3 supporting metrics → select "investment ask" narrative arc → apply decision framework (recommendation, alternatives, status quo, risk-adjusted framing) → populate the executive summary template.

**Expected Output:** A one-page executive summary with a BLUF stating the ask, 5-7 metrics showing pipeline efficiency trend, 3 options (increase, status quo, larger increase) with the recommended option highlighted, and a risk-adjusted framing noting payback risk and the cost of not investing.

**Final Response:** Delivered one-pager per `templates/executive_summary_template.md`, with the ask stated in the first sentence and options analysis embedded in the "Ask / Next Steps" section.

**Alternative Response:** If the user only supplies the ask with no supporting metrics, the draft proceeds but explicitly flags "[METRIC NOT PROVIDED]" for pipeline efficiency and asks the user to supply at least a directional figure before the board meeting.

**Edge Cases:** If the user's pasted data contradicts itself (e.g., two different pipeline totals), the skill surfaces the conflict rather than picking one number silently.

---

## Example 2: Mature B2B Services Firm — Reporting on Underperformance

**User Request:** "Our renewal rate missed target this quarter. Help me write the board update explaining why and what we're doing about it."

**Why the Skill Activates:** This is a narrative-framing task for an existing, known outcome (a miss) — not strategy origination. The skill compresses the situation into an honest, board-appropriate underperformance narrative.

**Workflow:** Identify situation type as "underperformance" → apply context-conflict-resolution arc (target → miss and cause → corrective plan) → select metrics showing the miss and any leading indicators → draft risk and next-steps section.

**Expected Output:** A board memo section (or one-pager) that states the miss plainly in the BLUF, explains the primary driver, and lays out the corrective plan and expected recovery timeframe, without softening or burying the bad news.

**Final Response:** Draft delivered using `templates/board_memo_template.md`, "For Information" section, with the miss named in the first line and a dated corrective plan.

**Alternative Response:** If the user wants the miss framed alongside a request for additional resources to fix it, the output shifts to include a "For Decision" section structured per `references/decision_frameworks.md`.

**Edge Cases:** If the user asks to "make it sound better than it is," the skill maintains honest framing per its reasoning guidelines rather than complying with a request to obscure bad news, while still presenting the situation constructively and pairing it with the forward plan.

---

## Example 3: Consumer Products Company — Presenting a Strategic Pivot

**User Request:** "We're changing our go-to-market approach from broad retail distribution to a direct-to-consumer focus. I need the board narrative and slide outline explaining why and asking for approval."

**Why the Skill Activates:** The user already has a defined new direction (the pivot itself was decided/developed elsewhere); the request is to narrate and package it for board approval, not to develop the pivot strategy itself.

**Workflow:** Confirm the pivot rationale and evidence are supplied (if not, ask for them) → select "pivot" narrative arc → structure the ask (recommendation, alternatives considered, rationale, risk-adjusted framing) → populate both memo and presentation outline templates.

**Expected Output:** A board memo and a 9-10 slide presentation outline: context (why the prior approach made sense), conflict (evidence of a ceiling), resolution (the pivot and the specific approval requested).

**Final Response:** Delivered both `templates/board_memo_template.md` and `templates/presentation_outline_template.md`, cross-referenced so the memo serves as pre-read and the outline as the live deck structure.

**Alternative Response:** If slide count must be under 8, the skill combines the context and market-opportunity slides per the outline template's guidance note.

**Edge Cases:** If the user has not yet actually decided the new direction and is really asking "should we pivot," the skill flags that this is a strategy-formulation question outside its scope and recommends resolving that with a GTM strategy skill first.

---

## Example 4: Healthcare Services Provider — Steady Progress Update

**User Request:** "Nothing dramatic happened this quarter — just need a clean summary of steady progress against our GTM plan for the board."

**Why the Skill Activates:** Routine board-cycle narrative condensation of an existing plan's results — a core, low-friction use case.

**Workflow:** Select "steady progress" arc → identify the specific challenge that was managed even amid overall on-track performance (avoiding a "nothing happened" narrative) → select north star and supporting metrics → compress priorities.

**Expected Output:** A one-pager stating results are on track, naming the one real challenge navigated this period, and previewing continued priorities for next period.

**Final Response:** Delivered via `templates/executive_summary_template.md`.

**Alternative Response:** If the user insists there truly was no notable challenge, the skill still asks a clarifying question about what required active management, since a narrative with zero tension often reads as thin to a board.

**Edge Cases:** Sparse input (a single line: "we're on track") triggers a request for at least directional metrics before drafting.

---

## Example 5: Manufacturing Firm — Market Opportunity Framing for New Segment Entry

**User Request:** "The board wants to understand the opportunity size for the new segment we're entering before they approve further investment. Can you draft that section?"

**Why the Skill Activates:** The user has (or will supply) opportunity sizing and wants it framed for board consumption — narrative and framing, not the underlying market research itself.

**Workflow:** Confirm sizing data or estimates are supplied → apply "so what" framing to translate raw figures into business implication → connect to the specific investment ask, if any, using the decision framework.

**Expected Output:** A concise market opportunity section (2-4 sentences) stating the sized opportunity and its implication for the investment decision at hand.

**Final Response:** Section drafted for insertion into the relevant template's "Market Opportunity" field.

**Alternative Response:** If no sizing data exists yet, the skill states plainly that market sizing/research is not something it performs and asks the user to supply figures, rather than fabricating a market size.

**Edge Cases:** If the user actually wants the skill to research and size the market itself, this is redirected as out of scope (market research is not part of this skill's narrative-condensation responsibility).

---

## Example 6: SaaS Scale-up — Compressing a Long Roadmap into 3 Priorities

**User Request:** "Our roadmap doc has 40 initiatives across 6 teams. I need this down to 3 strategic priorities for the board deck."

**Why the Skill Activates:** Classic compression task — taking detailed roadmap content (built elsewhere) and reducing it to board-level strategic themes.

**Workflow:** Read all 40 initiatives → group by business outcome/theme rather than team → identify the 3 highest-impact themes → state each as an outcome, with 1-2 representative initiatives as illustration, not an exhaustive list → validate against the 5-priority maximum rule.

**Expected Output:** 3 strategic priority statements, each framed as a business outcome (e.g., "Expand net revenue retention through expansion motion," not "Ship features A, B, C"), each with a one-line rationale.

**Final Response:** Delivered as the "Strategic Priorities" section of `templates/executive_summary_template.md`.

**Alternative Response:** If the initiatives don't cleanly group into 3 themes, the skill uses up to 5 (the stated maximum) rather than forcing an artificial 3, and explains the grouping logic used.

**Edge Cases:** If the roadmap contains initiatives with no clear business outcome stated, the skill flags these as needing clarification from the user before they can be confidently grouped.

---

## Example 7: Nonprofit / Mission-Driven Organization — Investment Justification for a New Program

**User Request:** "We want to ask the board to fund a new outreach program. Give me the decision brief."

**Why the Skill Activates:** A defined ask (fund a new program) with supporting rationale to be condensed into a decision-ready brief — matches the decision-brief output type exactly.

**Workflow:** Confirm the program rationale, cost, and expected outcome are supplied → apply options analysis (fund now, fund partially, defer) → structure recommendation and risk-adjusted framing → populate the decision brief template.

**Expected Output:** A 1-2 page decision brief with the ask stated first, an options table, a recommendation with rationale, and risk-adjusted framing including cost of inaction (e.g., mission impact of delay).

**Final Response:** Delivered via `templates/decision_brief_template.md`.

**Alternative Response:** If cost figures are not yet finalized, the brief proceeds with ranges or "[COST NOT FINALIZED]" flagged, with a note that final board approval may require confirmed figures.

**Edge Cases:** If the user wants the skill to build the program's budget model itself, this is redirected to a budget-modeling skill; this skill only narrates the resulting ask.

---

## Example 8: Financial Services Firm — Investor Update Requiring High Confidentiality

**User Request:** "Draft the investor narrative on our Q2 results, but keep customer-level and churn detail generic since this will circulate beyond the board."

**Why the Skill Activates:** Narrative condensation for an executive/investor audience with an explicit distribution and confidentiality constraint — within scope, with the constraint applied to metric precision.

**Workflow:** Identify the confidentiality constraint up front → select metrics and phrase them at a level of precision appropriate for wider circulation (e.g., rounded ranges or trend direction instead of exact customer-level figures) → proceed with standard narrative arc.

**Expected Output:** A one-pager or memo with metrics presented as trend/range rather than precise sensitive figures, and a note confirming the confidentiality constraint was applied.

**Final Response:** Delivered with a footnote: "Figures presented at a level of precision appropriate for wider circulation per stated confidentiality constraint."

**Alternative Response:** If the user does not specify a confidentiality level, the skill asks whether the material will circulate beyond the immediate board before finalizing precision of sensitive figures.

**Edge Cases:** If the user asks to omit a materially relevant risk entirely because it's sensitive, the skill still recommends surfacing it (at appropriate altitude and precision) rather than omitting it, consistent with board-reporting norms around honest risk disclosure.

---

## Example 9: Multi-Region Retail Business — Board Wants Comparison Across Regions

**User Request:** "The board wants a single narrative comparing performance across our three regions this quarter, not three separate updates."

**Why the Skill Activates:** Compression and narrative unification across multiple sources of performance data into one board-consumable story — within the skill's remit.

**Workflow:** Inventory each region's data → identify a shared north star metric across regions → build one narrative arc that names the overall trend and highlights where regions diverge (the "conflict") → compress priorities to those relevant across regions or clearly flagged as region-specific.

**Expected Output:** A single one-pager or memo with one BLUF covering all regions, a shared metrics table with a region breakdown column, and priorities/risks tagged by region where they diverge.

**Final Response:** Delivered via `templates/executive_summary_template.md` with an added region column in the metrics table.

**Alternative Response:** If regions use inconsistent metrics definitions, the skill flags the inconsistency rather than presenting them as directly comparable.

**Edge Cases:** Extremely divergent regional performance (one region strongly outperforming, another missing badly) is named directly as the central tension rather than averaged into a misleadingly neutral overall statement.

---

## Example 10: Early-Stage Startup — Board Ask to Approve a Strategic Priority Sign-off (No Financial Ask)

**User Request:** "We just need the board to formally endorse our top 3 priorities for next year — no budget ask attached. Can you draft that?"

**Why the Skill Activates:** A non-financial decision ask (formal endorsement) still requires the same options-recommendation-rationale discipline and narrative compression — within scope even without a budget component.

**Workflow:** Compress underlying plan into 3 priorities → frame as a "For Decision" ask even though non-financial → apply lightweight options analysis (these 3 priorities vs. an alternative set or maintaining last year's priorities) → state rationale.

**Expected Output:** A brief decision brief or memo section stating the 3 priorities, why they were selected over alternatives, and the specific endorsement being requested.

**Final Response:** Delivered via `templates/decision_brief_template.md`, adapted to a non-financial ask (cost/resource fields marked not applicable).

**Alternative Response:** If the user wants this folded into a broader quarterly board update rather than a standalone brief, the same content is instead inserted as the "For Decision" section of `templates/board_memo_template.md`.

**Edge Cases:** If the "priorities" supplied are actually a detailed task list rather than strategic themes, the skill compresses/re-groups them into outcome-level priorities before presenting, per the priority-compression guidance in the workflow.

---

## Example 11: Edge Case — Request Is Actually Out of Scope

**User Request:** "Build our entire GTM strategy for next year and then turn it into a board deck."

**Why the Skill Activates (Partially):** The board-deck packaging portion is in scope; the strategy-origination portion is not.

**Workflow:** Recognize the compound request → separate the two parts → decline the strategy-origination portion explicitly, explaining this belongs to a GTM Strategy Builder skill → offer to proceed with the board-deck narrative once the strategy exists or is supplied.

**Expected Output:** A response that does not attempt to originate the strategy, clearly states the scope boundary, and asks the user to supply (or first develop via the appropriate skill) the underlying strategy before the narrative step can proceed.

**Final Response:** "I can turn a completed GTM strategy into a board-ready narrative, but building the strategy itself is outside what this skill does. Once you have the strategy (or key decisions) drafted, share it and I'll condense it into the board narrative."

**Alternative Response:** If the user has partial strategy content already (e.g., target segments and positioning decided, but not fully documented), the skill can proceed with the narrative using what exists, flagging any gaps.

**Edge Cases:** If the user pushes back and asks the skill to "just wing it," the skill still declines to fabricate strategic decisions, since doing so would misrepresent unvalidated content as board-ready fact.

---

## Example 12: Boundary Case — Extremely Sparse Input

**User Request:** "We had an okay quarter. Write the board summary."

**Why the Skill Activates:** Still a narrative-condensation request, but with insufficient source material to produce a credible, decision-ready output.

**Workflow:** Attempt to draft using only what's given → recognize the material is too sparse to support metrics, priorities, or a credible arc → request the minimum viable input (at least one directional metric, the stated ask or purpose of the meeting, and any known priority) before finalizing.

**Expected Output:** A short response identifying exactly what additional input is needed, plus an optional skeleton showing where that input would go, rather than a fabricated narrative with invented numbers.

**Final Response:** "To draft a credible board summary I'll need at least: one or two key metrics (even directional), the main purpose of this board interaction, and your top 2-3 priorities. Once you share those, I can turn them into a one-page summary."

**Alternative Response:** If the user insists on a draft immediately, the skill provides a structural skeleton with placeholders clearly marked, rather than inventing plausible-sounding but fabricated figures.

**Edge Cases:** None beyond the missing-data handling already described — this case exists specifically to test that the skill does not fabricate under pressure.
