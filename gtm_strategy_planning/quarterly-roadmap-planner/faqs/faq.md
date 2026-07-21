# Frequently Asked Questions

> **Purpose:** Answer common questions about this skill's scope, methodology choices, handling of missing information, mid-quarter revisions, and how it interoperates with adjacent skills (GTM Strategy Builder, Budget Allocator, Board Deck Narrative) without duplicating their content.

---

**1. Does this skill create our GTM strategy for us?**
No. This skill assumes a GTM strategy, business objective, or initiative list already exists and converts it into an executable quarterly roadmap. Strategy formation (market segmentation, positioning, ideal customer profile, channel strategy) is handled by a separate GTM Strategy Builder skill. If you don't yet have a strategy, that skill (or a conversation to define one) should come first.

**2. Can this skill calculate our budget or headcount cost for the quarter?**
No. Budget and financial modeling (spend allocation, CAC/LTV, ROI projections, headcount cost) is handled by a separate Budget Allocator skill. This skill may reference a stated budget or capacity as a constraint on the roadmap, but it does not calculate or allocate financial figures.

**3. Can this skill write our board deck or investor narrative?**
No. Executive and board-facing narrative writing is handled by a separate Board Deck Narrative skill. This skill produces the underlying operational plan (roadmap, milestones, OKRs, risks) that a narrative skill can later summarize for that audience.

**4. How does this skill's output feed into the Board Deck Narrative skill?**
The roadmap, OKRs, and success metrics this skill produces are structured, factual inputs that a narrative-focused skill can draw on to tell a story for leadership or investors. This skill does not attempt persuasive framing itself — it hands off a clean, structured plan.

**5. How does this skill consume output from the GTM Strategy Builder skill?**
It treats the strategy's stated goals, target segments, and priorities as the starting input for initiative inventory and prioritization (Workflow Steps 1-2). It does not re-derive or second-guess the strategy itself — if the strategy seems incomplete for planning purposes, it asks clarifying questions rather than inventing strategic direction.

**6. How does this skill consume output from a Budget Allocator skill?**
If a budget or resourcing constraint has already been determined by a budget/financial modeling process, this skill treats that as a capacity constraint when checking for overcommitment (see Validation Rules in `SKILL.md`). It does not recalculate the budget itself.

**7. Why would I use RICE instead of MoSCoW for prioritization?**
RICE is best when you have a sizeable backlog (5+ initiatives) and want a defensible numeric ranking based on reach, impact, confidence, and effort. MoSCoW is best when you have a fixed deadline and need to negotiate scope into explicit Must/Should/Could/Won't categories. See `references/prioritization_frameworks.md` for the full comparison.

**8. Why would I use Weighted Scoring instead of RICE?**
Weighted Scoring is better when multiple stakeholders have legitimately different priorities (e.g., sales wants revenue impact weighted heavily, product wants technical risk weighted heavily) that need to be reconciled transparently through agreed criteria weights. RICE is a single-formula approach that doesn't natively incorporate multiple stakeholder-weighted criteria.

**9. What if I don't know which prioritization framework to use?**
Tell Claude your situation (backlog size, whether there's a fixed deadline, whether multiple stakeholders disagree) and it will recommend and justify a framework per `references/prioritization_frameworks.md` rather than defaulting silently to one.

**10. What happens if I don't provide an owner for a milestone?**
Claude assigns a role-based placeholder owner (e.g., "TBD - Marketing Lead") and flags it as an open item requiring follow-up. It will not block the entire plan on a missing owner, but it will not silently omit ownership either.

**11. What happens if I don't provide target dates?**
Claude uses relative sequencing (e.g., "Week 4 of quarter") instead of absolute dates and flags that firm dates are pending confirmation. The plan still gets built; the date precision is simply lower until confirmed.

**12. Can I revise a roadmap mid-quarter?**
Yes — this is an explicit, supported workflow step (Step 12). Claude re-runs prioritization and structuring only on the affected subset of initiatives, preserving unaffected commitments, and logs what changed and why in the roadmap's revision log.

**13. Does a mid-quarter revision rebuild the entire roadmap from scratch?**
No. Only the initiatives and milestones affected by the new information (a slipped dependency, a new priority, a capacity change) are re-prioritized and re-sequenced. Unaffected workstreams are left untouched to minimize disruption.

**14. How do I know if my quarter is overcommitted?**
Claude checks the total estimated effort of prioritized initiatives against your stated (or reasonably inferred) team capacity, including any reserved buffer. If the total exceeds capacity, it flags this explicitly and recommends deferring or de-scoping specific candidates rather than silently fitting everything in.

**15. What if I have zero reserved buffer capacity?**
Claude will note this as a risk in the risk register — a 100%-allocated quarter has no slack to absorb the first unplanned issue. It will proceed with your plan as stated but will flag the risk rather than silently building in buffer against your wishes.

**16. What if my team is just one person?**
The skill still produces a full roadmap, milestone plan, and OKRs, but flags that all critical-path risk is concentrated in a single individual, since there is no one else to absorb a delay or an unplanned absence.

**17. Should every initiative have OKRs, or just the roadmap as a whole?**
OKRs typically cascade from roadmap themes to the contributing teams, not from every individual initiative. A theme's objective may be supported by several initiatives; drafting a separate OKR per initiative usually produces too many objectives and dilutes focus.

**18. What's the difference between a milestone and a key result?**
A milestone is a dated checkpoint confirming a deliverable was completed (an activity-level tracking unit). A key result is a measurable outcome indicating whether the underlying objective was achieved, and may not move in lockstep with milestone completion — a milestone can finish on time while its associated key result still misses target.

**19. Can this skill grade our OKRs at the end of the quarter?**
Yes, if you provide the actual achieved values for each key result, Claude will grade them (typically on a 0.0-1.0 scale) with evidence-based notes, using `templates/okr_template.md`'s grading section, and can help capture lessons learned as input for the next quarter's planning.

**20. What roadmap structure should I use — theme-based, date-based, or outcome-based?**
It depends on scope certainty, presence of hard external deadlines, and audience. See `references/roadmap_framework.md`. Most quarters benefit from a hybrid: themes at the top level, outcome accountability underneath, and dates at the milestone level wherever real external deadlines exist.

**21. Can this skill handle a planning cycle that isn't exactly a quarter (e.g., 6 weeks or a trimester)?**
Yes. The methodology scales to any time-boxed period; the cadence (pre-period planning, kickoff, mid-period review, close-out) is simply compressed or extended proportionally.

**22. How does this skill handle conflicting priorities between two teams?**
It surfaces the conflict explicitly rather than silently picking a winner, applies the chosen prioritization framework transparently to both competing initiatives, and proposes a sequencing or trade-off option — flagging it for an explicit decision-maker if the conflict cannot be resolved by prioritization alone. See `examples/examples.md`, Example 5.

**23. What if a cross-team dependency has no confirmed required-by date?**
Claude will flag this explicitly as an open item in the dependency table and risk register rather than proceeding as if the dependency has an implicit deadline. A dependency without a required-by date cannot be reliably sequenced.

**24. Does this skill track day-to-day tasks below the milestone level?**
No. Task-level execution tracking (e.g., a detailed sprint backlog or daily to-do list) is below this skill's intended granularity. The milestone plan is the most granular artifact this skill produces.

**25. Can this skill be used for a non-software industry?**
Yes. It is intentionally industry-agnostic. Initiative types, milestone content, and dependency patterns will differ by industry (e.g., services, retail, manufacturing GTM), but the underlying methodology — prioritization, roadmap structuring, milestone planning, OKRs, and risk/dependency management — applies unchanged.

**26. What happens if I ask for something entirely out of scope, like a competitive analysis?**
Claude states plainly that competitive analysis is not something this skill produces and, if relevant, indicates that this falls to a different skill or a general research approach — it will not attempt to fabricate a competitive analysis under this skill's umbrella.

**27. Will this skill invent company names, real dates, or real people if I don't provide them?**
No. Per the skill's design, missing specifics are handled with bracketed placeholders and explicit flags for follow-up, never with fabricated real-sounding names, dates, or facts.

**28. How often should the risk register be updated?**
At minimum, at every planning checkpoint: kickoff, mid-quarter review, and close-out — and additionally whenever a new risk, assumption, issue, or dependency is identified during the quarter, per `references/risk_and_dependency_management.md`.

**29. What if the roadmap I already have doesn't have any risk tracking at all?**
Claude can build a RAID log from scratch for an existing roadmap by reviewing its milestones and dependencies and proposing likely risks, assumptions, and dependencies for your confirmation, using `templates/risk_register_template.md`.

**30. Can I use this skill just for the prioritization step, without building a full roadmap?**
Yes. Each workflow step (prioritization, milestone planning, OKR drafting, risk assessment) can be invoked independently using the corresponding file in `prompts/`, without necessarily running the full end-to-end workflow.
