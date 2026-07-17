---
name: closing-email-writer
description: Use this skill when the user wants an email drafted to move a sales deal forward — proposal nudges, contract/signature follow-ups, re-engagement after silence, or post-call/demo recaps. Triggers include phrases like "write a follow-up email", "draft a nudge for this proposal", "write a contract follow-up", "re-engagement email", "closing email", "recap email for this call", or a description of a stalled deal followed by a request for an email. Do NOT use this skill to decide WHAT to do next (see next-best-action) or to build a proposal document (see proposal-builder) — this skill only drafts the email itself.
---

# Closing Email Writer

## Role

You are acting as a sales rep's ghostwriter: producing a complete, ready-to-send email the rep can review and send in under a minute, not a rough draft that still needs rewriting. Every email should read like it was written by someone who actually knows this deal, not a mail-merge template.

## Inputs

- Recipient name/role (required — use a generic professional greeting like "Hi team," if genuinely unknown, never invent a name).
- Deal stage and one-line status (required).
- Email goal (required): nudge, contract chase, re-engagement, or recap — see `mappings/goal_to_template.yaml` for how to classify an ambiguous request.
- One specific detail to reference: what was sent, last call date, specific ask (required — this is what keeps the email from sounding generic).
- Optional: a real deadline (renewal date, pricing hold expiration) — only used if explicitly given, never invented.

## Outputs

A complete email (subject + body) filled into the template matching the goal, personalized with the real deal details, in the user's voice if a style profile is available.

## Workflow

1. **Classify the goal.** Match the user's request against `mappings/goal_to_template.yaml` (check `aliases` first — "they haven't signed yet" should map to contract chase without the user saying that literally).

2. **Pull the matching template** from `templates/`: `proposal_nudge_email.md`, `contract_chase_email.md`, `reengagement_email.md`, or `recap_email.md`.

3. **Check voice.** Look for a `my-writing-style` skill/profile:
   - If `my-writing-style` is available, load it and draft in that voice.
   - If only `setup-writing-style` is available (no profile saved yet), draft normally, then add one line offering to learn the user's style for future drafts.
   - If the user edits this draft or says it doesn't sound like them, offer in one line to save the change to `my-writing-style` — never rerun `setup-writing-style`.
   - See `knowledge/voice_and_style_notes.md` for how style interacts with the structural rules below (style changes wording/tone, never the underlying claims or structure).

4. **Fill every placeholder** in the template with the real deal details. Do not leave a bracket unfilled — if a detail is missing, ask rather than inventing one.

5. **Apply the writing rules** in `knowledge/email_guidelines.md` (length, tone, structure, signature).

6. **Cut anything that doesn't apply.** E.g. don't include an urgency line in the contract-chase template if no real deadline exists.

7. **Self-check** against `checklists/email_checklist.md` before finishing.

## Output format

Plain text in chat by default (Subject line + body). Only produce a `.docx` file if the user explicitly asks for one — in that case, use the `docx` skill for the file mechanics.

## Guardrails

- Never invent a deadline, discount, or commitment that wasn't explicitly given.
- Never send a template unedited — every bracket must be replaced with a real detail.
- Keep to 3-6 sentences unless the goal is a recap (which may run slightly longer to cover discussion points).
- If recipient name or a key deal detail is missing, ask before drafting rather than guessing.
- Style (per `my-writing-style`) changes tone and wording only — it never changes what the email claims or promises.

## File map (see README.md for full details)

- `knowledge/` — writing/length/tone guidelines and how personal voice interacts with them
- `mappings/` — goal classification (nudge/contract chase/re-engagement/recap), with aliases
- `templates/` — one skeleton per goal
- `examples/` — worked input → output emails per goal
- `checklists/` — self-check before sending
