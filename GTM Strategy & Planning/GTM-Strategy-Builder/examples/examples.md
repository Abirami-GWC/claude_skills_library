# Examples

**Purpose of this document:** Illustrate how the GTM Strategy Builder skill activates and behaves across a range of industries and request types, proving reusability across domains. All companies, products, and brands referenced below are generic/hypothetical ("Company A," "a mid-market provider," etc.) — none are real.

---

## Example 1 — B2B SaaS: Full Quarterly GTM Plan

**User Request:** "We sell a project-collaboration SaaS tool to mid-market teams. Help us build our Q3 GTM plan — we want to grow expansion revenue this quarter."

**Why the Skill Activates:** The request asks for a full quarterly GTM plan with a stated business goal — a direct, textbook activation of this skill's core capability.

**Workflow:** Gather context (product, current customers, goal = expansion revenue) → segment/ICP review focused on existing accounts with expansion potential → positioning refresh check → persona review for economic buyer (department head) and user/champion (team lead) → messaging pillars emphasizing expansion use cases → motion/channel selection favoring in-product prompts and customer success outreach over new-logo channels → assemble Quarterly GTM Plan.

**Expected Output:** A completed Quarterly GTM Plan (`templates/quarterly_gtm_plan_template.md`) prioritizing expansion-focused segments, messaging, and channels.

**Final Response (condensed):** "Q3 goal: expansion revenue. Priority segment: existing mid-market accounts nearing usage-tier thresholds. ICP for expansion: accounts with 3+ active teams and rising seat usage. Motion: product-led expansion prompts + customer-success-assisted upsell for Tier 1 accounts. Channels: in-product messaging, customer success outreach, quarterly business reviews. Goals: X% expansion revenue growth, Y% upsell conversion on flagged accounts."

**Alternative Response:** If usage data isn't available, propose a proxy trigger set (seat count, login frequency) as an assumption and flag it for validation.

**Edge Cases:** If the user has no existing customer base yet (pre-launch), redirect to new-logo acquisition planning instead of expansion, since expansion GTM cannot be built without an installed base.

---

## Example 2 — Healthcare: ICP Definition Only

**User Request:** "We have compliance documentation software for hospitals. We need to nail down our ICP before our next sales push."

**Why the Skill Activates:** Direct request for ICP definition, a named skill output.

**Workflow:** Gather product/context → apply `references/icp_framework.md` → define firmographic (multi-site outpatient/hospital systems), technographic (existing EHR/compliance tooling), behavioral (manual audit-prep process), trigger (upcoming accreditation cycle) → define anti-ICP (single-location practices without dedicated administrative staff) → build weighted scoring model.

**Expected Output:** Completed `templates/icp_template.md`.

**Final Response (condensed):** "Primary ICP: multi-site outpatient groups (10+ locations) with a named compliance officer, currently using manual/paper-based audit prep, entering an accreditation cycle within 6 months. Anti-ICP: single-location independent practices with no dedicated administrative role. Tier 1 score threshold: 4/5 criteria met including the trigger criterion."

**Alternative Response:** If the user has both hospital-system and independent-practice customers today, present both as separate ICP tiers with different motions rather than forcing one ICP.

**Edge Cases:** If no accreditation-cycle data is available, mark the trigger criterion as a hypothesis pending sales validation rather than asserting it as confirmed.

---

## Example 3 — Fintech: Positioning Refresh After Moving Upmarket

**User Request:** "We used to sell to small business owners, now we're moving upmarket to mid-size finance teams. Our positioning still talks about being 'simple' — can we refresh it?"

**Why the Skill Activates:** Direct positioning refresh request tied to a segment shift.

**Workflow:** Identify the segment shift (SMB owner → mid-size finance team) → re-run competitive-alternative mapping for the new segment (finance teams likely compare against ERP modules and manual reconciliation, not just "simple" consumer-style tools) → identify new unique attributes relevant to finance teams (audit trail, multi-entity support) → choose category frame (leader/challenger within "financial operations software" rather than generic "simple tool") → draft new positioning statement, explicitly noting the "simple" framing is now a liability, not an asset, at this buyer level.

**Expected Output:** Completed `templates/positioning_canvas_template.md` with an explicit note on what changed and why.

**Final Response (condensed):** "For finance teams at mid-size companies who need multi-entity reconciliation without a full ERP rollout, [product] is the financial operations platform that delivers audit-ready reconciliation in days, not months — unlike ERP modules, which require lengthy implementation, and unlike manual spreadsheets, which don't scale past a few entities. Note: previous 'simple for small business' framing should be retired for this segment — mid-size finance buyers read 'simple' as 'lacks controls.'"

**Alternative Response:** If the user wants to keep serving both SMB and mid-size segments, recommend two segment-specific positioning variants rather than one blended statement.

**Edge Cases:** If no evidence yet confirms the new differentiator resonates with finance-team buyers, flag it as unvalidated and recommend win/loss interviews in the new segment before finalizing.

---

## Example 4 — Industrial/Manufacturing: Messaging Framework

**User Request:** "We make condition-monitoring sensors for factory equipment. We need a messaging framework — right now everyone on the sales team says something different."

**Why the Skill Activates:** Direct messaging-framework request, and the stated symptom (sales inconsistency) matches this skill's stated business value.

**Workflow:** Gather positioning (or draft one first if missing) → gather personas (reliability engineer, plant financial owner) → derive 3 pillars from differentiator (early failure detection) mapped to persona pains (unplanned downtime, false alarms) → attach proof points → build persona-specific variants → define message hierarchy.

**Expected Output:** Completed `templates/messaging_framework_template.md`.

**Final Response (condensed):** "Pillar 1: Catch failures before downtime (proof: detects failure signatures ahead of stoppage in pilot deployments) — engineer variant emphasizes alert accuracy; financial-owner variant emphasizes avoided downtime cost. Pillar 2: Install without disrupting production (proof: non-invasive sensor mounting, no process shutdown required). Pillar 3: See it in your existing systems (proof: integrates with common plant historian software). Primary message for cold outreach: Pillar 1; supporting messages: Pillars 2-3 for later-stage conversations."

**Alternative Response:** If no proof points exist yet (pre-launch), mark Pillar 1 as aspirational and recommend a pilot-customer proof point be collected before broad sales rollout.

**Edge Cases:** If personas were never formally defined, first produce a lightweight persona pass using `references/buyer_persona_guide.md` directly before drafting messaging, since messaging without persona grounding will be generic.

---

## Example 5 — Consumer (D2C): Market Segmentation for New Product Line

**User Request:** "We're launching a new product line in our direct-to-consumer wellness brand. Who should we target first?"

**Why the Skill Activates:** Segmentation and targeting question, a core skill output, tied to new-market/product entry.

**Workflow:** Apply `references/market_segmentation.md` — layer needs-based segmentation (e.g., "proactive optimizers" vs. "acute problem-solvers") over behavioral/purchase-channel data → size candidate segments (rough TAM/SAM/SOM) → score on reachability, willingness-to-pay, competitive intensity, time-to-proof → recommend a beachhead segment.

**Expected Output:** A segmentation summary with a recommended beachhead segment and rationale (embedded in `icp_template.md` and referenced in a Quarterly GTM Plan if requested).

**Final Response (condensed):** "Recommended beachhead: 'acute problem-solvers' segment — smaller than 'proactive optimizers' but faster to reach via existing acute-need search/content channels and faster time-to-proof (word-of-mouth referral cycle is shorter). Recommend sequencing 'proactive optimizers' as the second wave once initial reviews/proof points exist."

**Alternative Response:** If the brand has budget for only one influencer-channel push, recommend concentrating entirely on the beachhead segment's primary channel rather than splitting spend across both segments simultaneously.

**Edge Cases:** If the user insists on targeting "everyone interested in wellness," push back with the specific reachability/dilution tradeoff and request a narrower prioritization before proceeding.

---

## Example 6 — Professional Services: Buyer Personas for a Consulting Offering

**User Request:** "We're a consulting firm rolling out a new advisory service. We need buyer personas."

**Why the Skill Activates:** Direct persona-definition request.

**Workflow:** Confirm linked ICP (client organizational maturity segment) → apply `references/buyer_persona_guide.md` → define economic buyer (COO/functional VP) and influencer (internal process owner) personas with JTBD, pains, objections, decision criteria, trusted channels.

**Expected Output:** Completed `templates/buyer_persona_template.md` per persona.

**Final Response (condensed):** "Persona: Functional VP (economic buyer). Functional job: close a capability gap before a board-visible deadline. Emotional job: avoid being seen as reactive. Decision criteria: consultant's relevant case pattern experience, speed to first recommendation, cost predictability. Trusted channels: peer referral, industry conference talks — not paid search."

**Alternative Response:** If the firm serves both large enterprise and mid-size clients with different buying committees, produce two persona sets rather than blending them.

**Edge Cases:** If the user provides only job titles with no other detail, build a hypothesis-based persona explicitly labeled as such and recommend 3-5 client interviews to validate JTBD and objections.

---

## Example 7 — B2B SaaS: Competitive Positioning Against a Named Competitor

**User Request:** "Prospects keep comparing us to [Competitor X] and we don't have a good answer. Help us sharpen our competitive positioning."

**Why the Skill Activates:** Competitive positioning request tied to messaging/positioning, in scope for this skill (tactical battlecard scripting is not, and should be flagged as adjacent).

**Workflow:** Apply `references/competitive_analysis.md` — map direct/indirect/status-quo alternatives including the named competitor → identify capability and outcome-level differentiators, prioritizing any confirmed by win/loss data → update positioning statement's "unlike [alternative]" clause → note that full tactical battlecard scripting (specific objection-handling talk tracks) is a distinct, more tactical artifact outside this skill's scope, though the strategic differentiation produced here is the direct input to it.

**Expected Output:** Updated positioning statement plus a concise competitive differentiation summary.

**Final Response (condensed):** "Unlike [Competitor X], which requires a dedicated implementation team and multi-month rollout, [product] delivers working integration within the first week, validated across recent onboarding data. Recommend this becomes the lead proof point in the 'unlike' clause of positioning going forward. Note: turning this into a full sales battlecard with objection-handling scripts is a tactical sales-enablement exercise outside this skill's scope."

**Alternative Response:** If no win/loss data exists yet on this specific competitor, recommend a targeted win/loss interview round before finalizing the claim.

**Edge Cases:** If the "differentiator" the user wants to claim is not actually true (competitor already matches it), surface this directly rather than drafting a false claim.

---

## Example 8 — Industrial: New-Market Entry GTM Motion Selection

**User Request:** "We're expanding from our current market into a new international region. What GTM motion should we use?"

**Why the Skill Activates:** GTM motion selection request, a core in-scope output.

**Workflow:** Apply `references/gtm_frameworks.md` decision factors — deal complexity, buyer autonomy (regulatory/procurement involvement in the new region), time-to-value, market maturity, and trust/channel norms in the new region → recommend motion (likely partner-led given regional trust/distribution norms in unfamiliar markets) → note this decision should be revisited once local reference customers exist.

**Expected Output:** A GTM motion recommendation with explicit rationale, embedded in a Quarterly GTM Plan if one is being built.

**Final Response (condensed):** "Recommend a partner-led motion for initial regional entry: local systems-integrator partners provide the trust and distribution reach a direct sales team cannot replicate in an unfamiliar market. Revisit toward a direct or hybrid sales-led motion once 3-5 referenceable local accounts exist."

**Alternative Response:** If the company has strong brand recognition already in the new region (e.g., through existing global customers with local offices), a direct sales-led motion leveraging those referenceable relationships may be recommended instead.

**Edge Cases:** If the request also asks "how much budget should we allocate to partner incentives," complete the motion recommendation and explicitly hand off the budget question to the Budget Allocator skill.

---

## Example 9 — B2B SaaS: Request That Should Be Redirected (Budget Allocation)

**User Request:** "Build our Q3 GTM plan and tell us exactly how much to spend on each channel."

**Why the Skill Activates (Partially):** The GTM-plan portion (segments, positioning, messaging, motion, channel selection) is in scope; the specific dollar-budget-allocation portion is not.

**Workflow:** Produce the full Quarterly GTM Plan as normal, selecting and prioritizing channels strategically → explicitly state that channel selection/prioritization is complete but dollar-amount budget allocation across those channels is handled by the Budget Allocator skill, and hand off the channel list as its input.

**Expected Output:** Complete Quarterly GTM Plan with channels prioritized (not budgeted), plus an explicit handoff note.

**Final Response (condensed):** "GTM plan complete with channel priorities (in-product, outbound sales, industry events). Specific dollar allocation across these channels is a budgeting exercise — hand this channel list to the Budget Allocator skill to determine spend split."

**Alternative Response:** If the user insists on a rough directional split (e.g., "just tell me roughly, not exact"), it is reasonable to give a qualitative emphasis order (primary/secondary/tertiary channel) without precise dollar figures, while still noting precise allocation belongs to the companion skill.

**Edge Cases:** If the user pushes back that they only have this one skill available, still avoid fabricating precise budget math — qualitative prioritization is the ceiling of this skill's scope.

---

## Example 10 — Healthcare: Request That Should Be Redirected (Board Narrative)

**User Request:** "Turn our GTM strategy into a board update slide narrative."

**Why the Skill Activates (Partially):** GTM strategy content itself is in scope; translating it into a board-facing narrative/slide structure is not.

**Workflow:** If a GTM strategy does not yet exist, build it first using the standard workflow. Then explicitly note that structuring it as a board narrative (executive framing, financial narrative conventions, slide sequencing) is the responsibility of the Board Deck Narrative skill, and offer the completed GTM plan as its direct input.

**Expected Output:** A complete GTM strategy artifact, with an explicit handoff note rather than an attempted board narrative.

**Final Response (condensed):** "Here is the completed Quarterly GTM Plan [summary]. Converting this into a board-ready narrative and slide structure is handled by the Board Deck Narrative skill — this GTM plan is the direct input it needs."

**Alternative Response:** If the user only wants a short plain-language summary paragraph (not a formal board narrative), that lightweight summary can be provided directly since it is just a condensed restatement of this skill's own output, not board-specific narrative construction.

**Edge Cases:** If it's ambiguous whether the user wants a full board narrative or just a summary, ask which, or provide the summary and note that a fuller board narrative is available via the companion skill.

---

## Example 11 — Fintech: Full GTM Refresh with Conflicting Prior Artifacts

**User Request:** "Refresh our GTM strategy — but heads up, our website messaging and our sales deck currently say different things about who we're for."

**Why the Skill Activates:** GTM refresh request; the stated inconsistency is directly relevant to this skill's consistency-checking responsibility.

**Workflow:** Gather both existing artifacts → identify the specific inconsistency (e.g., website targets SMB, sales deck targets mid-market) → surface this explicitly before proceeding → determine, based on stated business goal, which target is correct going forward → rebuild ICP, positioning, and messaging consistently around the resolved target → flag the inconsistency and its resolution explicitly in the output.

**Expected Output:** A refreshed, internally consistent set of GTM artifacts with an explicit note on the resolved inconsistency.

**Final Response (condensed):** "Found a conflict: website messaging targets SMB owners, sales deck targets mid-market finance teams. Given the stated Q3 goal (mid-market expansion), recommend resolving toward mid-market as the primary target, with website messaging updated to match. Refreshed positioning, ICP, and messaging below are built consistently around mid-market as primary."

**Alternative Response:** If the user says both segments must be kept, produce two clearly segmented, non-conflicting artifact sets instead of one blended, inconsistent one.

**Edge Cases:** If the user can't say which target is "correct," present the tradeoffs of each and recommend based on the stated quarterly business goal, flagging the choice as a recommendation pending leadership confirmation.

---

## Example 12 — Consumer: Insufficient Input, Skill Proceeds with Flagged Assumptions

**User Request:** "We sell an outdoor gear product. Write us a GTM strategy."

**Why the Skill Activates:** Direct GTM strategy request, though with minimal input provided.

**Workflow:** Note missing inputs (no stated business goal, no named segment, no competitive context) → proceed using the most defensible generic assumptions for an outdoor-gear consumer product (e.g., assume growth goal, assume a needs-based "outdoor enthusiast" beachhead segment) → clearly flag every assumption → produce a lighter-weight, assumption-heavy draft rather than blocking on the user.

**Expected Output:** A Quarterly GTM Plan clearly marked as assumption-heavy, with an explicit list of what should be confirmed or corrected.

**Final Response (condensed):** "Since no goal/segment was specified, this draft assumes a new-customer growth goal and a 'frequent outdoor enthusiast' beachhead segment (rather than casual/occasional users). Please confirm or correct these before treating this as final. [Plan follows.]"

**Alternative Response:** If the user's follow-up reveals the actual goal is retention, not growth, only the goal-dependent sections (motion, channel emphasis, quarterly metrics) need revision — segmentation/ICP/positioning can largely be retained.

**Edge Cases:** If the product category itself is ambiguous (e.g., could be positioned as sporting goods or as everyday consumer apparel), present both framing options briefly and ask which fits the company's intent, rather than silently picking one.
