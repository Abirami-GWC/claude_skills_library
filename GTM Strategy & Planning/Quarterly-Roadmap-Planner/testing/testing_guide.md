# Testing Guide

> **Purpose:** Provide positive, negative, boundary, and edge test cases for validating this skill's behavior, along with expected outputs and evaluation criteria.

## How to Use This Guide

Each test case describes an input scenario, what the skill is expected to do, and how to judge whether the output is correct. Use `checklists/roadmap_checklist.md` and `checklists/quality_checklist.md` alongside these cases for detailed scoring.

---

## Positive Test Cases

### P1: Full roadmap from a complete strategy input
**Input:** A GTM strategy summary, a stated quarter, a list of 6 initiatives, known team capacity, and known stakeholders.
**Expected Behavior:** Full workflow runs end-to-end (Steps 1-11); all deliverables produced (roadmap, milestone plan, owner assignment, timeline, OKRs, risk register).
**Evaluation Criteria:** Passes `roadmap_checklist.md` and `quality_checklist.md` in full; no clarifying questions needed since all critical inputs were provided.

### P2: Prioritization-only request
**Input:** A list of 8 initiatives with reach/effort estimates and a request to "just prioritize these."
**Expected Behavior:** Claude selects RICE (sizeable backlog with estimable reach/effort), applies it transparently, and returns a ranked list without necessarily producing a full roadmap unless asked.
**Evaluation Criteria:** Framework choice is justified; scoring inputs are shown; ranking is internally consistent with the stated formula.

### P3: OKR drafting from existing roadmap themes
**Input:** An existing roadmap with 3 named themes and a request to draft OKRs.
**Expected Behavior:** Claude cascades 2-4 objectives per contributing team per theme, each with 2-4 measurable key results.
**Evaluation Criteria:** No key result is vague or activity-based; every key result has a measurement method and data source; objectives contain no embedded numeric targets.

### P4: Mid-quarter re-prioritization due to a slipped dependency
**Input:** An existing roadmap, six weeks into the quarter, with a stated delayed dependency.
**Expected Behavior:** Only the affected initiatives/milestones are re-prioritized and re-sequenced; unaffected items are explicitly confirmed unchanged; risk register is updated to reflect the issue.
**Evaluation Criteria:** Revision log entry present; critical path re-evaluated; no unnecessary changes to unaffected workstreams.

### P5: Risk register build for an existing roadmap with no prior risk tracking
**Input:** An existing roadmap/milestone plan with no RAID log.
**Expected Behavior:** Claude proposes likely risks, assumptions, issues, and dependencies based on the roadmap content, each with an owner, for user confirmation.
**Evaluation Criteria:** Every proposed item has a single accountable owner; critical path is identified; proposed items are flagged as inferred/for confirmation rather than presented as established fact.

---

## Negative Test Cases (Out-of-Scope Requests)

### N1: Request to build the underlying GTM strategy
**Input:** "We don't have a strategy yet — can you create our market segmentation and positioning for us?"
**Expected Behavior:** Claude declines this specific request as out of scope, states that strategy formation belongs to a GTM Strategy Builder skill, and offers to proceed with roadmap planning once a strategy exists.
**Evaluation Criteria:** No attempt to fabricate a market segmentation or positioning strategy under this skill's identity.

### N2: Request for budget/financial modeling
**Input:** "Calculate our CAC, LTV, and total ad spend needed for this roadmap."
**Expected Behavior:** Claude declines the financial modeling portion, identifies the Budget Allocator skill as the correct tool, and (if applicable) still completes any in-scope roadmap portions of a mixed request.
**Evaluation Criteria:** No numeric financial model (CAC, LTV, spend totals) is fabricated or presented as a real calculation.

### N3: Request for a board/investor narrative
**Input:** "Write the board deck story for why this roadmap matters to investors."
**Expected Behavior:** Claude declines to produce persuasive executive narrative content, identifies the Board Deck Narrative skill as the correct tool, and offers the roadmap as a structured input to that process.
**Evaluation Criteria:** No narrative/persuasive prose framed for a board or investor audience is produced under this skill.

### N4: Multi-year strategic planning request
**Input:** "Build us a 3-year roadmap with milestones."
**Expected Behavior:** Claude notes this skill is designed for quarterly or similarly time-boxed periods, and either asks the user to scope it down to a specific quarter/period or explicitly caveats that a multi-year plan is outside the skill's intended granularity.
**Evaluation Criteria:** Claude does not silently produce a 3-year plan using quarterly-planning assumptions without flagging the scope mismatch.

### N5: Personal, non-business task management request
**Input:** "Help me plan my personal errands for the next three months."
**Expected Behavior:** Claude notes this skill is designed for team/business initiative planning, not personal task management, and declines or redirects.
**Evaluation Criteria:** No business-planning framework (OKRs, RAID logs) is force-fit onto a personal task list in a way that misrepresents the skill's purpose.

---

## Boundary Cases

### B1: Zero available resources / fully unstaffed initiative
**Input:** A roadmap request where one initiative has no assigned team or named owner at all, and no role is available to assign.
**Expected Behavior:** Claude flags the initiative as unstaffed, marks the owner field as "TBD — unassigned," and recommends either deferring the initiative or securing a resource before committing it to the roadmap.
**Evaluation Criteria:** The unstaffed initiative is not silently included in the committed roadmap as if it had normal owner coverage; overcommitment/capacity risk is flagged.

### B2: Single-owner team (all milestones owned by one person)
**Input:** A 1-person team requesting a full quarterly roadmap.
**Expected Behavior:** Claude builds the roadmap but explicitly flags that all critical-path risk is concentrated in one individual, and recommends minimal buffer/contingency planning appropriate to a single point of failure.
**Evaluation Criteria:** The concentration risk is explicitly called out in the risk register, not merely implied by the owner column.

### B3: Zero reserved buffer capacity
**Input:** A roadmap where 100% of stated capacity is allocated to initiatives with none held in reserve.
**Expected Behavior:** Claude proceeds with the plan as requested but flags the zero-buffer condition as a risk in the risk register.
**Evaluation Criteria:** The overcommitment/buffer check is performed and documented even when the user does not ask for it explicitly.

### B4: Single initiative, single theme quarter
**Input:** A roadmap request where the entire quarter is dedicated to exactly one initiative.
**Expected Behavior:** Claude still produces the full deliverable set (roadmap, milestones, owners, timeline, OKRs, risk register) scaled appropriately to one initiative rather than forcing multiple themes that don't exist.
**Evaluation Criteria:** No artificial themes or initiatives are invented to fill out a template structure.

### B5: Extremely short planning horizon (2 weeks)
**Input:** A request for a roadmap covering only a 2-week period.
**Expected Behavior:** Claude produces a milestone-focused plan and notes that a formal OKR cycle may not be well suited to such a short horizon, offering a simplified success-metrics view instead if appropriate.
**Evaluation Criteria:** Claude adapts cadence expectations (e.g., no mid-period review) rather than forcing a full 13-week cadence template onto a 2-week request.

---

## Edge Cases

### E1: Conflicting hard deadlines across teams sharing a dependency
**Input:** Two teams each have a hard deadline that depends on the same shared upstream resource, and the deadlines cannot both be met.
**Expected Behavior:** Claude surfaces the conflict explicitly, applies the chosen prioritization framework transparently, proposes a sequencing trade-off, and flags the need for an explicit decision-maker if it cannot be resolved by prioritization logic alone.
**Evaluation Criteria:** The conflict is never silently resolved without explanation; a trade-off rationale is given.

### E2: User provides contradictory information across the conversation
**Input:** The user states a team has 3 people early in the conversation, then later references a 5-person team without acknowledging the change.
**Expected Behavior:** Claude notes the discrepancy and asks for clarification rather than silently picking one number.
**Evaluation Criteria:** The discrepancy is surfaced, not silently resolved in either direction.

### E3: Request to fabricate specific real-world facts
**Input:** "Just make up a realistic-sounding company name and real launch date for the example."
**Expected Behavior:** Claude uses clearly generic, illustrative placeholders (as in `examples/examples.md`) rather than presenting invented specifics as if they were real, even if asked to "make it realistic."
**Evaluation Criteria:** Any illustrative content is clearly framed as generic/hypothetical, not stated as fact.

### E4: Mixed in-scope and out-of-scope request in one message
**Input:** "Build the roadmap, calculate the budget, and write the board narrative."
**Expected Behavior:** Claude completes the roadmap portion fully and explicitly declines/redirects the budget and board narrative portions in the same response.
**Evaluation Criteria:** The response clearly separates what was done from what was declined, with correct redirection for each out-of-scope portion.

---

## Evaluation Criteria Summary

For every test case, evaluate:
1. **Scope correctness** — did the skill stay within its defined boundaries (per `SKILL.md` "When NOT To Use" and "Scope")?
2. **Structural completeness** — does the output satisfy `checklists/roadmap_checklist.md`?
3. **Quality** — does the output satisfy `checklists/quality_checklist.md`?
4. **Transparency** — are framework choices, assumptions, and trade-offs explicitly stated rather than silently assumed?
5. **Non-fabrication** — is any missing information handled with flagged placeholders rather than invented specifics?
6. **Consistency** — are initiative names, owners, and dates consistent across all deliverables produced in the same session?
