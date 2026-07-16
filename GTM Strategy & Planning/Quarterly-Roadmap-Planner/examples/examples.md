# Examples

> **Purpose:** Illustrative, industry-agnostic worked examples showing how the Quarterly Roadmap Planner skill activates, executes its workflow, and responds across different roadmap horizons, team sizes, and industries. No real company, product, or brand is referenced.

---

## Example 1: Standard Quarterly Roadmap from a GTM Strategy (Mid-Size SaaS-style Team)

**User Request:** "We just finalized our GTM strategy for entering a new customer segment next quarter. Can you turn this into a roadmap with milestones and owners?"

**Why the Skill Activates:** The user has an existing strategy and is asking for it to be converted into an executable, time-boxed plan with milestones and owners — squarely within this skill's purpose.

**Workflow:** Steps 1-11 run in full: confirm inputs (strategy summary, quarter, team roles available), inventory initiatives (messaging, enablement content, pilot campaigns, pricing pilot), prioritize with RICE (sizeable backlog with estimable reach/effort), structure as a hybrid theme-based/date-based roadmap (new-segment entry is the dominant theme; a few hard dates exist for a pilot campaign launch), define milestones, assign role-based owners, sequence the timeline noting marketing-to-sales dependencies, draft OKRs, build a risk register, validate against checklists.

**Expected Output:** Quarterly roadmap (one theme: "Enter [NEW SEGMENT]"), milestone plan with 4 initiatives broken into milestones, owner assignment table, cross-functional timeline, OKRs cascaded to marketing and sales, and a risk register flagging unvalidated messaging as a risk.

**Final Response:** A complete set of deliverables per the template files, with an explicit note on which owners are role-based placeholders pending confirmation.

**Alternative Response:** If the user had provided named owners and firm dates, the same structure would be produced with named individuals and a fully date-based milestone plan instead of relative sequencing.

**Edge Cases:** If the strategy document is vague on the actual initiatives (e.g., only a goal statement, no initiative list), Claude should ask the user to enumerate candidate initiatives before proceeding rather than inventing a plausible-sounding list.

---

## Example 2: Small Team, Limited Resources

**User Request:** "It's just me and two teammates this quarter — help us plan out what we can realistically get done."

**Why the Skill Activates:** A request to plan time-boxed, executable work for a team, even a very small one, is within scope.

**Workflow:** Steps 1-11, with particular attention to the overcommitment check (Validation Rules) given a 3-person team. Prioritization likely uses MoSCoW or Value vs. Effort rather than RICE, since the backlog and estimation overhead for a 3-person team don't warrant a heavier framework.

**Expected Output:** A lean roadmap with a single theme, a short milestone list (3-6 milestones total), owner assignment mapped 1:1 or 1:2 onto the three teammates, and an explicit statement that capacity is fully allocated with minimal buffer — flagged as a risk given the team's size.

**Final Response:** Roadmap plus a direct note: "With only three people and no reserved buffer, any unplanned issue will directly displace a committed milestone. Consider reserving at least one teammate's partial capacity as buffer."

**Alternative Response:** If the user explicitly says they want to be fully allocated with no buffer, Claude documents that as an accepted risk rather than silently building in buffer against the user's stated preference.

**Edge Cases:** Single-owner team (see `testing/testing_guide.md` boundary cases) — every milestone owner defaults to the same person; Claude should flag that all critical-path risk is concentrated in one individual.

---

## Example 3: Multi-Region, Enterprise-Scale Rollout (Industry: Generic B2B)

**User Request:** "We're rolling out a new offering across three regions this quarter, each with its own sales and marketing team. Build the roadmap."

**Why the Skill Activates:** Multi-team, multi-region execution planning against a quarter is a core use case.

**Workflow:** Full workflow with heavier emphasis on cross-functional dependency mapping (Step 7, Step 9) given three regional teams plus central product/marketing functions. Weighted Scoring is used for prioritization since multiple regional stakeholders have different priorities that must be reconciled transparently.

**Expected Output:** Theme-based roadmap with per-region initiative rows, a dependency table showing central marketing assets as an upstream dependency for all three regional launches, milestone plan per region, cascaded OKRs (central objective plus per-region key results), and a risk register flagging the shared central-asset dependency as a single point of failure.

**Final Response:** Full deliverable set, with a specific callout that all three regions depend on one central milestone and recommending either parallelizing that work earlier or building regional contingency plans.

**Alternative Response:** If regions have fully independent go-to-market assets with no shared dependency, the dependency table would instead show three independent tracks with no shared critical-path risk.

**Edge Cases:** Regions with conflicting date requirements (e.g., one region has a hard regulatory deadline) — Claude should flag the date-based milestone for that region explicitly as committed, while other regions may remain outcome-based.

---

## Example 4: Mid-Quarter Re-Prioritization Due to a Slipped Dependency

**User Request:** "We're six weeks into the quarter and a key product feature we were counting on got delayed. We need to re-prioritize the rest of the roadmap."

**Why the Skill Activates:** This is the mid-quarter revision case explicitly supported by Step 12 of the workflow.

**Workflow:** Claude does not rebuild the roadmap from scratch. It re-runs Steps 3-10 only on the affected subset: (a) identifies which milestones and initiatives depended on the delayed feature, (b) re-applies the chosen prioritization framework to the affected initiatives given the new constraint, (c) re-sequences only the impacted milestones and downstream dependencies, (d) leaves unaffected workstreams untouched, (e) updates the risk register to move this item from "risk" to "issue" status with a resolution plan, (f) re-evaluates the critical path since the delay may have shifted it.

**Expected Output:** An updated roadmap and milestone plan with a clear revision log entry describing what changed and why, an updated risk register showing the issue and its downstream impact, and a note on which OKR key results are now at higher risk of missing target.

**Final Response:** "Here is the updated plan. Milestones X and Y are re-sequenced two weeks later; milestones A, B, and C are unaffected and unchanged. The critical path has shifted — milestone Y is now the critical-path item to watch."

**Alternative Response:** If the delay is severe enough to make a committed key result unachievable this quarter, Claude flags that the key result target itself may need to be revised at the next OKR grading cycle, rather than silently protecting an unrealistic target.

**Edge Cases:** If the user asks for re-prioritization but gives no information about what changed, Claude should ask what specifically shifted (dependency delay, new information, capacity change) before re-running prioritization, since the correct framework response differs by cause.

---

## Example 5: Cross-Team Dependency Conflict (Marketing vs. Product Capacity)

**User Request:** "Marketing and product both need the same design resource this quarter for different initiatives, and there's a scheduling conflict. Help us figure out the roadmap."

**Why the Skill Activates:** Identifying and resolving cross-functional dependency and capacity conflicts is explicitly within scope (risk and dependency management).

**Workflow:** Claude surfaces the conflict explicitly rather than silently picking a winner (per Reasoning Guidelines). It applies the chosen prioritization framework (likely Weighted Scoring, since this is a multi-stakeholder trade-off) to both initiatives competing for the shared resource, documents the trade-off transparently, and proposes sequencing options: (a) sequential use of the shared resource with adjusted milestone dates for the lower-priority initiative, or (b) flagging the conflict as an issue requiring an escalation decision from a named decision-maker if the user has not specified one.

**Expected Output:** A dependency conflict entry in the risk register (as an Issue, since it has already occurred), a re-sequenced milestone plan showing one initiative's design-dependent milestone moved later, and an explicit statement of the trade-off rationale.

**Final Response:** "Both initiatives need the same design resource in week 3. Based on [prioritization framework] scoring, Initiative A ranks higher — I've sequenced the design resource to Initiative A first and moved Initiative B's design-dependent milestone to week 5. If this trade-off isn't acceptable, this needs an explicit resourcing decision from [DECISION_MAKER_ROLE]."

**Alternative Response:** If the user states they cannot resolve the conflict and need it escalated, Claude documents the conflict clearly for escalation rather than forcing a resolution.

**Edge Cases:** If the shared resource conflict affects a critical-path milestone for both initiatives, Claude should flag that the quarter may need explicit de-scoping of one initiative rather than assuming a sequencing fix is sufficient.

---

## Example 6: Building OKRs Only (No Full Roadmap Requested)

**User Request:** "We already have our roadmap. Can you just help us draft OKRs for the quarter based on it?"

**Why the Skill Activates:** OKR drafting is one of this skill's explicit responsibilities and can be invoked as a standalone workflow step (Step 8) even without rebuilding the full roadmap.

**Workflow:** Claude skips straight to the OKR drafting prompt (`prompts/okr_drafting_prompt.md`), using the existing roadmap's themes as input rather than re-deriving them.

**Expected Output:** A completed OKR set per `templates/okr_template.md`, cascaded to the teams named in the existing roadmap.

**Final Response:** OKR set with a cascading summary table linking back to the user's existing roadmap themes.

**Alternative Response:** If the existing roadmap has no clear themes (e.g., it's a flat initiative list), Claude first asks the user to confirm or infer 3-5 themes before drafting OKRs, since OKRs cascade from themes.

**Edge Cases:** If the user's existing roadmap already has OKRs that are vague or unmeasurable, Claude flags the specific key results that fail the "numeric and gradable" validation rule and proposes measurable replacements.

---

## Example 7: Short Time Horizon (6-Week Sprint Instead of Full Quarter)

**User Request:** "We don't run full quarters — our planning cycle is six weeks. Can you build a roadmap for that instead?"

**Why the Skill Activates:** The skill is explicitly designed for "a quarter (or similarly time-boxed period)" — a 6-week cycle qualifies.

**Workflow:** Full workflow, with the planning cadence (`references/quarterly_planning.md`) compressed proportionally — e.g., a shorter or no formal mid-cycle review given the reduced length, or a single lightweight checkpoint at the midpoint (week 3).

**Expected Output:** A roadmap, milestone plan, OKRs, and risk register scaled to a 6-week horizon, with fewer milestones per initiative than a full 13-week quarter would carry.

**Final Response:** Complete deliverable set, explicitly noting the compressed cadence and recommending a single check-in at week 3 given the shorter cycle.

**Alternative Response:** If the 6-week cycle is one of several within a longer strategic period, Claude notes that this roadmap covers only the current cycle and does not extend planning beyond it.

**Edge Cases:** Extremely short horizons (e.g., 2 weeks) may not support meaningful OKR cycles; Claude should note that OKRs are typically better suited to quarter-length or longer periods and offer a simplified milestone-only plan instead if the user agrees.

---

## Example 8: Request That Is Actually Out of Scope (Budget Modeling)

**User Request:** "Can you also calculate what this roadmap will cost us in headcount and ad spend?"

**Why the Skill Activates (Partially) / Boundary Handling:** The roadmap-building part of the request is in scope, but the cost/budget calculation is explicitly out of scope per "When NOT To Use."

**Workflow:** Claude completes the roadmap-related portions of the request normally, but for the budget/cost calculation, it states that this falls outside this skill's scope and identifies the Budget Allocator skill as the appropriate tool, without attempting to fabricate a cost model itself.

**Expected Output:** A complete roadmap deliverable set, plus an explicit statement declining the budget calculation portion.

**Final Response:** "Here is your quarterly roadmap [...]. Calculating headcount cost and ad spend allocation is outside what this skill does — that's handled by a budget/financial modeling skill. I'd recommend passing this roadmap's initiative list to that process as its input."

**Alternative Response:** If the user insists on a rough cost estimate anyway, Claude should still decline to model actual costs but may note qualitatively which initiatives are likely more resource-intensive based on effort estimates already used in prioritization (without presenting this as financial modeling).

**Edge Cases:** A request that blends in-scope and out-of-scope asks in a single sentence should be split explicitly in the response so the user knows exactly what was and was not addressed.

---

## Example 9: Request That Is Actually Out of Scope (Board Narrative)

**User Request:** "Once the roadmap is done, can you also write the board deck narrative explaining our strategy for the quarter?"

**Why the Skill Activates (Partially) / Boundary Handling:** Roadmap-building is in scope; writing an executive/board narrative is explicitly out of scope per "When NOT To Use."

**Workflow:** Claude completes the roadmap workflow fully, then states that board-level narrative writing is handled by a separate Board Deck Narrative skill, noting that the roadmap output itself is a suitable input to that process.

**Expected Output:** Complete roadmap deliverable set; no narrative/prose executive summary produced beyond the skill's own brief factual summary of the plan.

**Final Response:** "Here is the completed roadmap, milestone plan, OKRs, and risk register. Turning this into a board-ready narrative is outside this skill's scope — that's handled by a dedicated board narrative skill, which can use this roadmap as its input."

**Alternative Response:** None — this boundary should be held consistently regardless of how the request is phrased.

**Edge Cases:** If the user only wants a short factual summary paragraph of the roadmap (not persuasive narrative or investor framing), that is acceptable as a plain restatement of the plan's contents, not a board narrative.

---

## Example 10: Missing Critical Inputs (No Strategy Provided)

**User Request:** "Build us a quarterly roadmap."

**Why the Skill Activates (With Clarification Needed):** The request is in scope, but no strategy, initiative list, or planning horizon has been provided.

**Workflow:** Per Error Handling, Claude does not fabricate a strategy. It asks targeted clarifying questions: What is the underlying strategy or set of goals for the quarter? What is the planning horizon? What initiatives or candidate work items exist? What teams/functions are involved? What constraints (capacity, deadlines) exist?

**Expected Output:** A short clarifying-question exchange, not a fabricated roadmap.

**Final Response:** "Before I can build a meaningful roadmap, I need a starting strategy or goal, the planning horizon, and a rough list of candidate initiatives. Do you have these, or would you like to describe your priorities for the quarter first?"

**Alternative Response:** If the user provides a partial answer (e.g., only the planning horizon and one initiative), Claude proceeds with what is available, flags the remaining gaps, and builds a partial roadmap rather than blocking entirely.

**Edge Cases:** If the user explicitly says "just make something up as an example," Claude should build a clearly-labeled generic illustrative example (as in this file) rather than presenting fabricated content as if it were based on real input.

---

## Example 11: Revising an Existing Roadmap Built Outside This Skill

**User Request:** "Here's a roadmap spreadsheet someone else built for this quarter. Can you check it for gaps and fix it up?"

**Why the Skill Activates:** Reviewing and revising an existing quarterly roadmap for completeness (owners, dates, dependencies, risks) is within scope.

**Workflow:** Claude runs the plan through `checklists/roadmap_checklist.md` and `checklists/quality_checklist.md`, identifying missing owners, missing dates, unprioritized items, missing dependency mapping, and absent OKRs or risk tracking, then fills gaps using the standard templates.

**Expected Output:** An annotated, gap-filled version of the roadmap plus a short list of what was missing and what was added/inferred.

**Final Response:** "I reviewed the existing roadmap against the standard checklist. Three initiatives had no owner assigned, two milestones had no target date, and there was no risk register. I've filled these in using role-based placeholders where specifics weren't available — please confirm these before finalizing."

**Alternative Response:** If the existing roadmap is fundamentally unprioritized (a flat list with no ranking logic), Claude recommends running it through a prioritization framework first rather than just patching gaps superficially.

**Edge Cases:** If the existing roadmap conflicts with itself (e.g., two milestones both claim the same hard deadline for different deliverables with a shared dependency), Claude should surface the internal conflict explicitly rather than silently resolving it.

---

## Example 12: Very Small Industry-Specific Team Adapting a Generic Framework (Non-Software Context)

**User Request:** "We're a services-based team, not a software company. We still want a quarterly roadmap for expanding into a new client vertical."

**Why the Skill Activates:** The skill is explicitly industry-agnostic; a services-based GTM roadmap is as valid a use case as a product-based one.

**Workflow:** Full workflow, with initiative types reflecting a services context (e.g., partnership development, proposal templates, vertical-specific case studies) rather than product/feature milestones. Prioritization and roadmap structuring logic is unchanged.

**Expected Output:** A roadmap themed around "Expand into [NEW CLIENT VERTICAL]," with milestones such as building vertical-specific proposal materials, securing pilot client engagements, and training client-facing staff — each with owners and dates, plus OKRs and a risk register (e.g., risk of insufficient vertical-specific expertise on staff).

**Final Response:** Full deliverable set adapted to a services context, with no software/product-specific assumptions embedded.

**Alternative Response:** If the user is in a regulated industry (e.g., requiring compliance review before any external launch), Claude adds a compliance review milestone as a dependency gating the external-facing milestones.

**Edge Cases:** Industries with long sales cycles that exceed a single quarter (e.g., enterprise services) may need outcome-based structuring for lead/pipeline-stage milestones rather than date-based delivery milestones, since the full sales cycle outcome may not complete within the quarter.
