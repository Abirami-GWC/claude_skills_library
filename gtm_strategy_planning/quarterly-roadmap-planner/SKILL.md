---
name: quarterly-roadmap-planner
description: Converts an existing go-to-market (GTM) strategy into an executable, time-boxed quarterly roadmap with milestones, owners, timelines, dependencies, OKRs, prioritization, and risk tracking. Use when a user has a defined strategy or set of goals and needs it translated into a concrete quarter-by-quarter execution plan. Does not create GTM strategy from scratch, does not perform budget/financial modeling, and does not produce board-level executive narratives.
---

# Quarterly Roadmap Planner

## Purpose

This skill converts an already-defined go-to-market (GTM) strategy, initiative list, or set of business goals into an executable quarterly roadmap. It structures work into time-boxed milestones, assigns owners, sequences deliverables, defines OKRs, applies prioritization frameworks, and surfaces risks and cross-functional dependencies. The output is a plan that a cross-functional team (marketing, sales, product, customer success, operations) can execute against and track week to week.

## Business Value

- Converts abstract strategy into concrete, assignable, date-bound work.
- Creates shared visibility across teams so dependencies and conflicts surface before they cause delays.
- Establishes measurable success criteria (OKRs, milestone completion, timeline adherence) so progress can be tracked objectively.
- Reduces quarterly planning cycle time by providing a structured, repeatable methodology instead of ad hoc spreadsheets.
- Gives leadership an execution-ready artifact that can be reviewed, revised, and re-prioritized without rebuilding the plan from scratch.

## Activation Conditions

Invoke this skill when the user:
- Has a GTM strategy, business objective, product launch plan, or initiative list and wants it turned into a quarterly execution plan.
- Asks to build, update, or revise a roadmap, milestone plan, or OKR set for a quarter (or similar time-boxed period).
- Needs to prioritize a backlog of initiatives against limited time, people, or capacity.
- Needs to identify dependencies, risks, or owner/timeline gaps in an existing plan.
- Wants to re-sequence or re-prioritize a roadmap mid-quarter due to new information, blockers, or shifting priorities.

## Trigger Examples

- "Turn our Q3 GTM strategy into a quarterly roadmap with milestones and owners."
- "We have five initiatives for next quarter — help me prioritize and sequence them."
- "Build an OKR set for the marketing and sales teams for this quarter."
- "Our roadmap for this quarter needs to be re-prioritized — a key dependency slipped."
- "Create a milestone plan with owners and target dates for our new market entry initiative."
- "What are the risks and dependencies in our current quarterly plan?"
- "We're mid-quarter and priorities changed — help me re-sequence the roadmap."
- "Help me apply RICE scoring to this list of initiatives."

## When NOT To Use

This skill assumes a strategy already exists. It should NOT be used to:
- **Define or create the underlying GTM strategy itself** (market segmentation, positioning, ideal customer profile, channel strategy) — that belongs to a GTM Strategy Builder skill. This skill consumes that strategy as an input; it does not produce it.
- **Perform budget or financial modeling** (headcount cost, CAC/LTV modeling, spend allocation across channels, ROI projections) — that belongs to a Budget Allocator skill. This skill may reference that a budget exists as a constraint, but does not calculate or allocate it.
- **Produce board-level executive narratives or investor-facing storytelling** — that belongs to a Board Deck Narrative skill. This skill produces the underlying operational plan that such a narrative may later summarize, but does not write narrative prose for executives or boards.
- Long-range (multi-year) strategic planning with no quarterly time-box.
- Personal task management unrelated to a team or business initiative.

If a request is purely about strategy formation, budget math, or executive storytelling with no roadmap/milestone/OKR/timeline component, defer to the appropriate adjacent skill instead of this one.

## Scope

In scope: quarterly (or similarly time-boxed) planning cadence, roadmap structuring, milestone definition, timeline sequencing, dependency mapping, owner assignment, OKR drafting and cascading, prioritization scoring, and risk/RAID tracking.

Out of scope: strategy formation, financial/budget modeling, executive narrative writing, long-term multi-year planning, and day-to-day task management below the milestone level.

## Inputs

Claude should expect some or all of the following from the user or prior conversation context:
- A GTM strategy summary, business objective, or initiative list (required in some form; ask if entirely missing).
- The planning horizon (e.g., a specific quarter, or a custom time-boxed period).
- Known constraints: team size, available capacity, hard deadlines, existing commitments.
- A list of candidate initiatives, features, campaigns, or projects to prioritize.
- Known stakeholders or functional teams involved (marketing, sales, product, CS, ops).
- Any existing OKRs, roadmap drafts, or risk logs to revise rather than build from scratch.

If critical inputs are missing (see Error Handling), ask targeted clarifying questions before producing a full plan.

## Outputs

- **Quarterly Roadmap** — theme-based, date-based, or outcome-based structure of initiatives sequenced across the quarter (see `references/roadmap_framework.md`).
- **Milestone Plan** — discrete, dated checkpoints with owners and completion criteria (see `templates/milestone_plan_template.md`).
- **Owner Assignment** — a RACI-style mapping of who is accountable/responsible for each initiative or milestone.
- **Timeline** — sequencing view showing start/end dates, dependencies, and critical path items.
- **Success Metrics / OKRs** — objectives and measurable key results tied to the roadmap (see `templates/okr_template.md`).
- Optionally, a **Risk Register** flagging dependency, resourcing, or timeline risks (see `templates/risk_register_template.md`).

## Workflow

1. **Confirm inputs.** Verify the GTM strategy/goals, planning horizon, constraints, and stakeholders are known. Ask clarifying questions for any missing critical input (see `faqs/faq.md` for common gaps).
2. **Inventory initiatives.** List all candidate initiatives, campaigns, features, or projects proposed for the period.
3. **Prioritize.** Apply an appropriate prioritization framework (RICE, MoSCoW, Value vs. Effort, or Weighted Scoring) per `references/prioritization_frameworks.md`, matching the framework to the decision context.
4. **Structure the roadmap.** Choose a roadmap structuring approach (theme-based, date-based, or outcome-based) per `references/roadmap_framework.md` and organize prioritized initiatives accordingly.
5. **Define milestones.** Break each initiative into dated milestones with clear completion criteria using `templates/milestone_plan_template.md`.
6. **Assign owners.** Attach an accountable owner (role, not necessarily a named individual unless provided) to every initiative and milestone.
7. **Sequence the timeline.** Order milestones across the quarter, identifying dependencies between teams and the critical path per `references/quarterly_planning.md`.
8. **Draft OKRs.** Translate roadmap themes into objectives and measurable key results using `references/okr_framework.md` and `templates/okr_template.md`.
9. **Assess risk and dependencies.** Build or update a RAID-style risk register per `references/risk_and_dependency_management.md` and `templates/risk_register_template.md`.
10. **Validate.** Run the plan against `checklists/roadmap_checklist.md` and `checklists/quality_checklist.md`.
11. **Deliver.** Present the roadmap, milestone plan, owner assignments, timeline, and OKRs/success metrics as the final output, noting any open risks or gaps.
12. **Support revision.** If the user requests mid-quarter re-prioritization, re-run steps 3–10 on the affected subset of initiatives while preserving unaffected commitments (see `examples/examples.md` for a worked example).

## Reasoning Guidelines

- Always match the prioritization framework to the decision type: RICE for feature/initiative backlogs with estimable reach and effort; MoSCoW for scope negotiation under a fixed deadline; Value vs. Effort for quick visual triage; Weighted Scoring when multiple stakeholder-weighted criteria must be balanced. Justify the choice briefly rather than defaulting silently to one framework.
- Prefer outcome-based or theme-based roadmap structures over rigid date-based ones when the strategy is exploratory or dependencies are uncertain; use date-based structuring when hard external deadlines (e.g., a fixed launch date) exist.
- Treat every cross-functional dependency as a first-class planning object, not an afterthought — identify which team is upstream and which is downstream before finalizing sequencing.
- When information is ambiguous or missing, state the assumption explicitly in the output rather than inventing specific facts (e.g., real names, real dates) that were not provided.
- Keep OKRs measurable; reject or flag key results that cannot be objectively graded.
- When re-prioritizing mid-quarter, minimize disruption to unaffected workstreams and clearly flag what changed and why.

## Best Practices

- Keep the roadmap at a level of granularity a cross-functional audience can read in minutes, not hours; push execution-level detail into the milestone plan.
- Use role-based owners (e.g., "[OWNER_ROLE]: Product Marketing Lead") when a named individual is not provided.
- Always pair every key result with a numeric target and a measurement method.
- Surface dependencies explicitly as a table, not buried in prose.
- Timebox review checkpoints (e.g., mid-quarter check-in) into the roadmap itself.
- Avoid overloading a single quarter with more initiatives than the stated team capacity supports; flag overcommitment.

## Validation Rules

- Every milestone must have an owner (role or named), a target date, and a completion criterion.
- Every OKR's key results must be numeric/measurable and gradable on a 0.0–1.0 or percentage scale.
- Every initiative must appear in the prioritization output before appearing in the roadmap.
- Every cross-team dependency must be listed with upstream owner, downstream owner, and required-by date.
- The roadmap must not exceed the stated or reasonably inferred team capacity without an explicit overcommitment flag.

## Error Handling

- **Missing strategy/goals input:** Ask the user to provide a strategy summary, objective, or initiative list before proceeding; do not fabricate a strategy.
- **Missing owner information:** Assign a role-based placeholder owner (e.g., "[OWNER_ROLE: TBD — Marketing]") and flag it for follow-up rather than blocking the plan.
- **Missing dates:** Use relative sequencing (e.g., "Week 3 of quarter") and flag that hard dates are pending confirmation.
- **Conflicting priorities:** Surface the conflict explicitly and apply the chosen prioritization framework transparently rather than silently picking a winner.
- **Request falls outside scope** (strategy creation, budget modeling, executive narrative): State that this skill does not cover that request and identify the correct adjacent skill.
- **Overcommitted quarter:** Flag that the initiative list exceeds reasonable capacity and recommend deferral or de-scoping candidates.

## Limitations

- Does not create the underlying business or GTM strategy — requires one as input.
- Does not perform financial, budget, or ROI modeling.
- Does not write executive or board-facing narrative content.
- Does not track day-to-day task execution below the milestone level.
- Cannot verify real-world capacity, staffing, or calendar data unless provided by the user.

## Success Criteria

A successful output includes: a structured quarterly roadmap, a milestone plan with owners and dates, an explicit owner assignment view, a sequenced timeline with dependencies, and measurable OKRs/success metrics — all internally consistent, traceable to the input strategy, validated against `checklists/roadmap_checklist.md` and `checklists/quality_checklist.md`, and free of fabricated company-specific facts not provided by the user.
