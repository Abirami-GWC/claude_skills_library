---
name: campaign-calendar-builder
description: >
  Builds a launch timeline across channels with explicit task dependencies,
  owners, and dates — turning a channel plan or list of content pieces into
  a schedulable calendar, flagging conflicts (e.g. a post scheduled before
  the asset it promotes is ready). Use when the user has campaign
  activities/channels/pieces needing sequencing, or asks for a "campaign
  calendar", "launch timeline", or "content calendar with dependencies."
  Trigger on "build a launch calendar for this campaign", "sequence these
  pieces across the next 3 weeks", "what order should these go out in", or
  "check if our timeline has scheduling conflicts." Not for defining channel
  strategy (campaign-multiplier), producing content pieces
  (content-repurposer), or drafting gated offers (lead-magnet-builder) —
  this takes defined activities and turns them into a sequenced,
  conflict-checked timeline.
---

# Campaign Calendar Builder

## Overview

A campaign with great content still fails if the sequencing is wrong — a
social post promoting a guide that isn't live yet, an email announcing a
webinar with three days' notice, a paid campaign whose creative isn't
approved until after the launch date. This skill turns a list of campaign
activities into an actual timeline, makes dependencies explicit, and
programmatically checks for scheduling conflicts before they become a live problem.

## Purpose

- Convert a set of campaign activities (from a `campaign-multiplier` brief, a
  set of repurposed content pieces, or a fresh list) into a sequenced calendar
  with dates, owners, and explicit dependencies.
- Catch dependency conflicts automatically — an activity scheduled before a
  prerequisite it depends on — rather than relying on manual review to catch them.
- Produce both a human-readable calendar view and a visual timeline (Gantt-style chart).

## When to use this Skill

- Turning a campaign brief's channel list into an actual dated schedule
- Sequencing a set of already-drafted content pieces across a launch window
- Auditing an existing timeline for dependency or date conflicts
- Producing a visual timeline/Gantt chart for stakeholder review

## When NOT to use this Skill

- Deciding which channels/angles the campaign should use → `campaign-multiplier`
- Writing the actual content pieces being scheduled → `content-repurposer`
- Building the gated offer being promoted → `lead-magnet-builder`

## Required Inputs

1. **List of activities**: each with a name, channel/type, and (if known) a
   target date or relative timing ("2 days after launch")
2. **Dependencies**: which activities must happen before others (e.g., "asset
   must be published before the email announcing it can send")
3. **Owners**, if relevant for the deliverable
4. **Launch/anchor date** or window the calendar is built around
5. **Constraints**: blackout dates, lead-time requirements for specific
   channels (e.g., paid social needs creative approval N days ahead — see
   `knowledge/timeline_planning_principles.md`)

If dependencies aren't explicitly stated, infer obvious ones (e.g., a social
post promoting an asset depends on that asset's publish date) but flag
inferred dependencies as such rather than treating them as user-confirmed.

## Workflow (summary — see instructions/workflow.md for full detail)

1. Gather activities, dependencies, owners, and the anchor date/window.
2. Populate `knowledge/calendar_schema.json`, marking inferred vs. confirmed dependencies.
3. Run `scripts/validate_calendar.py` to catch date/dependency conflicts
   (an activity scheduled before something it depends on, owner
   double-booking if that data is available, missing lead time for
   lead-time-sensitive channels).
4. Resolve or flag every conflict found — do not deliver a calendar with
   unresolved conflicts without calling them out explicitly.
5. Render the calendar as a table (`templates/campaign_calendar.csv`) and a
   visual timeline via `scripts/build_gantt_chart.py`.

## Best Practices

- **Make dependencies explicit, not implicit.** If activity B needs activity
  A done first, say so in the data model — don't just order them visually and
  hope the sequencing holds if dates shift.
- **Respect channel lead times.** Paid social, webinars, and PR each have
  their own minimum lead time (see `knowledge/timeline_planning_principles.md`)
  — check the calendar against these, don't just space activities evenly.
- **Flag conflicts, don't silently resolve them.** If two activities can't
  both hit their stated dates given a dependency, surface the conflict and
  let the user decide the tradeoff rather than picking one silently.
- **Keep the calendar legible.** A timeline with 40 unlabeled entries is
  harder to act on than one grouped by week/phase with clear owners.

## Rules and Limitations

- Never invent an owner, date, or dependency not supplied or clearly
  inferable from the activities themselves — mark unknowns as "TBD."
- Do not silently drop or reorder an activity to resolve a conflict — flag
  the conflict and the available resolution options, let the user decide.
- Do not assume a channel's lead-time requirement without checking
  `knowledge/timeline_planning_principles.md` or asking, if the user's
  organization has different constraints (e.g., faster internal approval process).
- Keep inferred dependencies clearly distinguished from user-confirmed ones
  in the output.

## References

- `knowledge/timeline_planning_principles.md` — lead-time norms and sequencing logic
- `knowledge/calendar_schema.json` — structured data model for the calendar
- `instructions/workflow.md` — full step-by-step process
- `instructions/validation_rules.md` — pre-delivery checklist
- `examples/example_1.md` — worked example (product launch, dependency conflict caught)
- `templates/campaign_calendar.csv` — the calendar's tabular structure
- `templates/calendar_template.md` — narrative/human-readable calendar view
- `scripts/validate_calendar.py` — checks the populated calendar for date/dependency conflicts
- `scripts/build_gantt_chart.py` — generates a visual Gantt-style timeline image
- `references/dependency_mapping_guide.md` — how to identify dependencies between activities
