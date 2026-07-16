# follow-up-cadence-builder

Part of the **Pipeline Management** module (owner: Nithisri) in the Sales &
Marketing Claude Skills project.

## What it does

Builds a personalized follow-up schedule for a single deal — when to reach out,
which channel, what type of message, and reminders — so a deal never goes quiet by
accident and a rep always has a concrete next action.

## Folder guide

| Path | Purpose |
|---|---|
| `SKILL.md` | Triggering logic only (read by Claude automatically). Points to `prompt.md`. |
| `prompt.md` | The actual step-by-step process Claude follows once triggered. |
| `knowledge/deal-stages.md` | Stage taxonomy (shared with `pipeline-prioritizer`) + fields needed for cadence. |
| `knowledge/followup-best-practices.md` | Cadence timing, channel selection, message types, and the stopping rule. |
| `knowledge/communication-guidelines.md` | Tone, length, and pacing rules for drafted messages. |
| `templates/followup-plan.md` | Exact output layout for the full cadence schedule. |
| `templates/email-template.md` | Message-type skeletons (check-in, proposal follow-up, urgency nudge, break-up). |
| `templates/reminder-template.md` | Short CRM/task-manager reminder line format, including the overdue marker. |
| `examples/input-example-1.md` | A realistic, unstructured deal description. |
| `examples/output-example-1.md` | The correct cadence plan for that same input, with real calculated dates. |
| `examples/sample-deal.json` | The same deal in structured JSON, for reference/testing. |
| `assets/` | Reserved for a skill icon, if one is ever added — currently unused. |

## Why there's no `scripts/` folder here

Unlike `pipeline-prioritizer`, this skill's date math (adding a documented interval
to a last-contact date) is simple enough that Claude computing it directly from
`followup-best-practices.md` is reliable — there's no multi-factor weighted formula
that benefits from being locked into code. If this skill later needs to
auto-calculate cadences across a rep's entire pipeline at once (not just one deal),
a `scripts/` folder computing all the dates in bulk would be worth adding then.

## Testing it yourself

Compare a new run's output against `examples/output-example-1.md` using
`examples/sample-deal.json` as the input — same stage, same silence streak, same
"today" — to sanity-check any changes to the cadence rules.

## Related skills (same module)

- `pipeline-prioritizer` — ranks deals against each other, doesn't schedule outreach
- `deal-health-checker` — diagnoses risk status; this skill hands a deal here once
  the stopping rule is hit
- `forecast-roller` — revenue rollup across the whole pipeline, manager-facing

Keep triggering descriptions in each skill's `SKILL.md` distinct so requests don't
collide between these four.
