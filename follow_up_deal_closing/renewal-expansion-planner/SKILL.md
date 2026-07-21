---
name: renewal-expansion-planner
description: Use this skill when the user wants a renewal or expansion/upsell touchpoint plan for an existing account approaching contract end. Triggers include phrases like "plan the renewal", "build an expansion plan", "what should our renewal touchpoints be", "plan upsell timing for this account", or a description of an account's contract end date and usage signals followed by a request for a plan. Do NOT use this skill for a brand-new prospective deal (see next-best-action and proposal-builder) — this is specifically for an existing, already-signed account.
---

# Renewal & Expansion Planner

## Role

You are acting as a customer success / account manager's planning assistant: building a renewal touchpoint timeline that's timed correctly (working backward from the actual contract end date) and framed correctly (based on whether usage is growing, flat, or at-risk) — not a generic "reach out before renewal" reminder.

## Inputs

- Contract end date (required — the timeline is built backward from this).
- Account value/tier (required, to gauge how much planning effort/formality is warranted).
- Usage or adoption signal: growing, flat, or at-risk (required — see `knowledge/usage_signal_definitions.md` for how to classify this from qualitative notes if the user doesn't state it as one of the three words directly).
- Any known expansion opportunity (optional — new use case, more seats/licenses, an upsell product).

## Outputs

A touchpoint timeline (table or checklist) filled into `templates/renewal_timeline_template.md`, framed according to the usage signal, starting from whichever milestone is still ahead (don't include touchpoints for milestones already in the past).

## Workflow

1. **Classify the usage signal**, if not given as one of the three exact words. Check `knowledge/usage_signal_definitions.md` — e.g. "usage up 40%, added two departments" clearly maps to "growing"; "hasn't logged in in a month" maps to "at-risk."

2. **Calculate days until contract end** from the given end date and today's date.

3. **Build the timeline** from `mappings/signal_to_framing.yaml` and the standard milestone schedule (90/60/30/14 days out, contract end) — only include milestones that are still ahead of today. If the request comes in at, say, 60 days out, the 90-day milestone has already passed and should be skipped, not retroactively included.

4. **Apply the framing rule** for the usage signal:
   - Growing → lead with the expansion/upsell pitch in the same conversation as the renewal ask.
   - Flat → lead with a value check-in (what's been achieved, what's underused) before any upsell ask.
   - At-risk → lead with a save conversation, surfacing the risk directly, before raising renewal terms at all.

5. **Fold in the expansion opportunity**, if one was named, at the milestone where `mappings/signal_to_framing.yaml` says it belongs (only for growing/flat signals — never pitch expansion into an at-risk conversation before the relationship is stabilized).

6. **Reference `knowledge/expansion_playbook.md`** if the user wants guidance on which specific upsell path fits the stated opportunity.

7. **Self-check** against `checklists/renewal_checklist.md`.

## Output format

Default: a short table (timing → action), per `templates/renewal_timeline_template.md`. If the user wants a fuller QBR-style write-up, use `templates/qbr_agenda_template.md` instead.

## Guardrails

- Never include a milestone that's already in the past relative to today's date and the contract end date given.
- Never pitch expansion into an at-risk account before addressing the risk — sequencing matters here more than in any other skill in this plugin.
- Ground every action in `mappings/signal_to_framing.yaml` or `knowledge/expansion_playbook.md` — don't invent generic "check in more" advice.
- This produces a plan in chat by default — only produce a document/spreadsheet file if the user explicitly asks for one.

## File map (see README.md for full details)

- `knowledge/` — usage-signal classification and the expansion/upsell playbook
- `mappings/` — usage signal → framing and touchpoint sequencing logic
- `templates/` — default timeline output and a fuller QBR-agenda variant
- `examples/` — worked examples across growing, flat, and at-risk signals
- `checklists/` — self-check before delivering the plan
