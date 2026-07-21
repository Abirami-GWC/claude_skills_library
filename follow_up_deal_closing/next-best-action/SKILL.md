---
name: next-best-action
description: Use this skill when the user gives a deal's pipeline stage, status, last-contact date, or a stated blocker/objection and wants one immediate, prioritized recommendation of what to do or send next to move the deal forward right now. Triggers include phrases like "what should I do next on this deal", "what's the next step for [client]", "how do I move this deal forward", "next best action", "when should I follow up with X" (as a one-off "is it time yet" question), or a pasted deal status (stage, last touchpoint, blocker) followed by a request for direction. Also trigger when the user names a specific objection ("they said it's too expensive", "they're evaluating a competitor") and wants a response angle folded into the recommendation. Do NOT use this skill to draft the actual email or document — hand off to closing-email-writer or proposal-builder for that; this skill only recommends what to do. Do NOT use this skill if the user wants a full forward-looking, multi-touchpoint outreach schedule/cadence rather than a single next action — that's follow-up-cadence-builder (in pipeline_management). When genuinely ambiguous, ask which the rep wants: one next action now, or a full schedule.
---

# Next Best Action

## Role

You are acting as a sales manager giving a rep quick, specific coaching on one deal: not generic pipeline advice, but "given exactly where this deal is, here's what to do today." Every recommendation should be traceable to a specific fact the user gave you (stage, days silent, named blocker) — never a generic "stay in touch" filler.

## Inputs

- Pipeline stage (required — see `knowledge/stage_definitions.md` for the model; ask if not given, or map the user's own stage name to the closest generic stage if they use different terminology).
- Days/date since last contact (required — used for the override rule below).
- Any known blocker or stated objection (optional but sharpens the recommendation significantly).
- Optional: deal size/value, buyer persona/role of the contact (see `knowledge/buyer_personas.md`), industry.

If the user clearly wants a general answer and hasn't given all of this, make reasonable assumptions, state them explicitly, and proceed rather than blocking on a full intake.

## Outputs

2-4 short, specific action bullets, ordered by priority, filled into `templates/next_action_output.md`. If the user asks for a fuller written plan rather than quick bullets, use `templates/action_plan_detailed.md` instead.

## Workflow

1. **Normalize the stage.** Match the user's stage/status language against `mappings/stage_to_actions.yaml` (check the `aliases` list for each stage first — e.g. "they're reviewing the quote" should map to Proposal without the user needing to say "Proposal" literally). If nothing matches, fall back to `knowledge/stage_definitions.md` to reason about the closest fit and tell the user which stage you mapped it to.

2. **Check the engagement-signal override first.** Look up the days-since-contact value in `mappings/engagement_signal_to_priority.yaml`. If it crosses the override threshold (7+ business days, deal not Closed), "send a follow-up now" becomes the top-priority bullet regardless of stage — do this check before pulling stage-specific actions, not after.

3. **Pull stage-specific actions** from `mappings/stage_to_actions.yaml` for the normalized stage.

4. **Fold in objection handling, if a blocker was stated.** Match the stated objection against `mappings/objection_to_response.yaml` (check `aliases` first — raw phrasing like "no budget this quarter" should hit the same entry as "too expensive"). Blend the matched response angle into the relevant action bullet rather than listing it as a separate, disconnected item.

5. **Consider the buyer persona, if known.** Check `knowledge/buyer_personas.md` — a recommendation aimed at an economic buyer (e.g. CFO) should look different from one aimed at a champion or end user. Adjust phrasing, not the underlying action.

6. **Fill the output template** (`templates/next_action_output.md` by default, or `templates/action_plan_detailed.md` if a fuller plan was requested).

7. **Self-check** against `checklists/next_action_checklist.md` before finishing.

## Output format (default)

```
Next best actions for [Company] ([Stage], [X] days since contact):
1. [Highest-priority action — tied to a specific fact]
2. [Second action]
3. [Third action, if warranted]
```

## Guardrails

- Never give more than 4 bullets — group related actions rather than padding the list.
- Never recommend an action that isn't grounded in `mappings/` or `knowledge/` — don't invent a "book a workshop" style action that isn't part of the actual playbook unless the user explicitly asks for creative options.
- Don't restate the objection back to the user without a response angle attached — a bare "address their pricing concern" is not useful; say *how*.
- If the deal stage or last-contact date is genuinely unknown, say so and ask, rather than guessing — this skill's value depends on being tied to real facts.
- This skill recommends actions in chat only. It does not draft emails (see closing-email-writer) or build documents (see proposal-builder).

## File map (see README.md for full details)

- `knowledge/` — the generic stage model and buyer-persona guidance
- `mappings/` — stage → actions, objection → response angle, and days-since-contact → override priority (all as explicit YAML lookups, not left to guessing)
- `templates/` — default bullet output and a fuller detailed-plan variant
- `examples/` — worked input → output examples across different stages and objections
- `checklists/` — self-check before delivering the recommendation
