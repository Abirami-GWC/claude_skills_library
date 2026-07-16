# Testing Guide

**Purpose of this document:** Define how to evaluate whether the GTM Strategy Builder skill is activating correctly and producing quality output, through positive tests, negative tests, boundary cases, and edge cases, with clear evaluation criteria.

## Positive Test Cases

*Requests this skill SHOULD handle, and what a correct response looks like.*

1. **"Build our Q3 GTM plan for [generic product description]."**
   Expected: Full Quarterly GTM Plan using `templates/quarterly_gtm_plan_template.md`, covering segmentation, ICP, positioning, personas, messaging, motion, channels, goals, and recommendations.

2. **"Define our ICP for [segment]."**
   Expected: Completed `templates/icp_template.md` with firmographic/technographic/behavioral/trigger criteria, anti-ICP, and scoring model.

3. **"Refresh our positioning — we've changed target markets."**
   Expected: Updated `templates/positioning_canvas_template.md` with an explicit note on what changed and why.

4. **"Build buyer personas for our [role types]."**
   Expected: One or more completed `templates/buyer_persona_template.md` instances, JTBD-based, linked to an ICP.

5. **"We need a messaging framework that differentiates us from [alternative]."**
   Expected: Completed `templates/messaging_framework_template.md`, pillars traceable to positioning, each with a proof point.

6. **"How should we segment this market?"**
   Expected: A segmentation analysis using at least two segmentation models, with a prioritized/scored shortlist and, if relevant, a recommended beachhead segment.

7. **"Review our current GTM plan and tell me what's missing."**
   Expected: A gap analysis against `checklists/strategy_checklist.md`, identifying missing elements (e.g., no anti-ICP, no proof points) rather than a full rewrite.

## Negative Test Cases

*Requests this skill should NOT handle as its primary output — expected behavior is to redirect/hand off, not to attempt the adjacent work.*

1. **"How much budget should we allocate to each marketing channel?"**
   Expected: Skill should not produce dollar-specific budget/spend modeling; should note this belongs to the Budget Allocator skill and, if a GTM plan is also being requested, provide the channel prioritization as that skill's input.

2. **"Build our engineering roadmap and sprint plan for the quarter."**
   Expected: Skill should not produce a sprint/execution timeline; should note this belongs to the Quarterly Roadmap Planner skill.

3. **"Write our board deck narrative for this quarter."**
   Expected: Skill should not produce board-facing financial narrative or slide structure; should note this belongs to the Board Deck Narrative skill, offering GTM content as its input.

4. **"Write the ad copy for our next campaign."**
   Expected: Skill should produce the messaging framework/pillars that ad copy should derive from, but should not itself produce finished creative ad copy as the primary deliverable — note the distinction if asked to "just write the ads."

5. **"Calculate our CAC and LTV for this plan."**
   Expected: Skill should not perform financial/unit-economics calculation; note this is adjacent financial modeling outside this skill's scope.

## Boundary Cases

*Requests at the edge of scope — evaluate whether the skill correctly identifies the boundary.*

1. **"Build the GTM plan and give a rough directional split of channel emphasis (not exact dollars)."**
   Expected: Acceptable for the skill to provide qualitative prioritization (primary/secondary/tertiary channel) without precise dollar figures; skill should still note that precise allocation is a Budget Allocator task.

2. **"Summarize our GTM strategy in a paragraph I can drop into a board update."**
   Expected: Acceptable — this is a condensed restatement of the skill's own output, not full board-narrative construction; a fuller board narrative should still be flagged as belonging to the Board Deck Narrative skill.

3. **"We have no customers yet — what's our ICP?"**
   Expected: Skill should proceed with a hypothesis-driven ICP, clearly labeled, with a recommended validation plan, rather than refusing to answer.

4. **"Our messaging and our sales deck contradict each other — fix it."**
   Expected: Skill should surface the specific inconsistency, propose a resolution grounded in the stated business goal, and rebuild consistently, rather than silently picking one without comment or ignoring the conflict.

## Edge Cases

1. **Extremely vague request ("make our GTM better").**
   Expected: Skill asks a clarifying question or proceeds with clearly flagged assumptions about goal/segment, rather than stalling entirely or producing generic, unfocused output.

2. **User insists target market is "everyone."**
   Expected: Skill should push back with the specific reachability/dilution tradeoff and request/recommend a narrower target rather than complying literally.

3. **User asks for positioning against a competitor whose capability actually matches the claimed differentiator.**
   Expected: Skill should surface that the claim is not currently defensible rather than drafting a false differentiation claim.

4. **User provides conflicting instructions (e.g., asks for both "keep it broad" and "make it specific").**
   Expected: Skill should note the tension explicitly and recommend specificity per this skill's best practices, or ask which the user prioritizes for this artifact.

5. **Multi-industry company (serves both healthcare and industrial customers).**
   Expected: Skill should treat these as separate segments/ICPs with potentially distinct positioning and messaging rather than blending them into one unfocused artifact.

## Evaluation Criteria

Judge output quality against:

- **Correct activation:** Did the skill correctly recognize this as a GTM-strategy request (or correctly identify the out-of-scope portion)?
- **Framework grounding:** Is every claim traceable to a named framework in `references/`, rather than generic marketing language?
- **Internal consistency:** Do positioning, ICP, personas, messaging, and channel/motion choices agree with each other (per `checklists/gtm_review_checklist.md`)?
- **Specificity:** Are segments, personas, and proof points concrete and falsifiable, not vague?
- **Assumption transparency:** Are assumptions and unvalidated claims explicitly flagged, never silently embedded?
- **Scope discipline:** Does the skill correctly decline/redirect budget, roadmap-execution, and board-narrative work to the correct companion skill?
- **Reusability:** Is the output free of any real company/brand reference used as a factual example or as the user's own company?
- **Actionability:** Could a marketer or seller act on this output directly within a week, without needing to fill in missing strategic reasoning?
- **Template fidelity:** Does the output fully populate the relevant template(s) in `templates/` with no leftover placeholders?
