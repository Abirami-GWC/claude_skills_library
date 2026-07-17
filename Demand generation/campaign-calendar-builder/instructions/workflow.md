# Workflow: Building a Campaign Calendar

## Step 1 — Gather activities and constraints

Confirm or ask:
1. The list of activities (name, channel/type, target/relative date if known)
2. Explicit dependencies between activities
3. Owners, if relevant
4. The anchor/launch date or overall window
5. Any blackout dates or organization-specific lead-time constraints

If the input comes from a `campaign-multiplier` brief or a
`content-repurposer` output set, map each channel entry/content piece to an
activity directly rather than re-eliciting from scratch.

## Step 2 — Infer missing dependencies, but mark them as inferred

Using `references/dependency_mapping_guide.md`, infer obvious dependencies
not explicitly stated (e.g., a promotional post depends on its asset being
live). Mark these `dependency_source: "inferred"` in the data model,
distinct from `"user-confirmed"` ones — never blend the two silently.

## Step 3 — Populate the calendar schema

Fill `knowledge/calendar_schema.json` for every activity: dates (explicit if
known, or work backward from the anchor date using
`knowledge/timeline_planning_principles.md`'s lead-time table for
activities with only relative timing), owner if known, and dependencies.

## Step 4 — Validate

Run `scripts/validate_calendar.py` against the populated data. This checks for:
- An activity scheduled before an activity it depends on
- Missing lead time relative to `knowledge/timeline_planning_principles.md`'s
  norms for that activity type
- Circular dependencies
- Owner double-booking on the same date, if owner data is present in enough
  detail to check

Do not proceed to rendering with unresolved conflicts — either adjust dates
with the user or clearly flag the conflict as unresolved in the delivered output.

## Step 5 — Render

- **Tabular**: `templates/campaign_calendar.csv` for spreadsheet use
- **Narrative**: `templates/calendar_template.md` for a human-readable view
  grouped by week/phase
- **Visual**: `scripts/build_gantt_chart.py` for a Gantt-style timeline image,
  useful for stakeholder review

## Step 6 — Deliver

Present the calendar with any flagged conflicts called out explicitly at the
top, not buried — a conflict a user has to notice themselves defeats the
purpose of this skill.

## Common mistakes to avoid

- **Silently resolving conflicts**: reordering or shifting dates without
  flagging that a conflict existed. Prevention: Step 4's explicit "flag, don't
  silently resolve" rule, reinforced in Step 6.
- **Treating inferred dependencies as confirmed**: prevention — Step 2's
  mandatory `dependency_source` tagging.
- **Ignoring channel-specific lead times**: scheduling paid creative or a
  webinar with same-day social-post-level lead time. Prevention: Step 3/4's
  explicit check against `timeline_planning_principles.md`.
- **Zero-buffer scheduling**: dependent activities scheduled immediately
  after their prerequisite with no slack. Prevention: validation script flags
  buffers under the recommended minimum.
