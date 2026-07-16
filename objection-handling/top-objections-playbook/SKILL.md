---
name: top-objections-playbook
description: "Classify and respond to general sales pushback (the recurring top-10 weekly objections). Use for objection handling or general sales call prep that isn't specifically about pricing or a named competitor."
---

# Top Objections Playbook

Classifies and responds to general, recurring sales objections in real time, and supports
building objection handling into a sales agent (e.g. a CRM-connected digital coworker).

**This is a general-purpose framework, not tied to any specific company, product, or Claude
Project.** Once installed as an account-level skill (see Installation below), it's available in
any conversation — this chat, a different project, Claude Code, or the API — not just the
context it was built in. The bundled table is illustrative sample content (written for a
network-security sales scenario) — swap it for the real team's top objections. Nothing in
`SKILL.md` or `references/schemas.md` is industry-specific; only the handler table needs
replacing per deployment.

## Installation (makes it available everywhere, not just this chat)

Claude.ai skills live at the account level, not inside a single Project or conversation:
1. Upload the `.skill` file (or this folder, zipped with the folder as the zip's root) at
   **Customize > Skills** → the **+** button → **Create skill** → **Upload a skill**.
2. Toggle it on. It now applies across every conversation and every Project on the account —
   Claude decides whether to load it per-conversation based on the `description` field above, the
   same way in a Project as outside one.
3. On Team/Enterprise plans, use **Share** (org-wide or specific people) or org provisioning to
   make it available to teammates too.

## Related skills

This folder is one of four sibling objection-handling skills, each self-contained and
independently installable:
- `pricing-objection-handler` — price/budget pushback
- `competitor-objection-handler` — responses when a competitor is name-dropped
- `objection-roleplay-simulator` — practice mode simulating live pushback

If price or a competitor comes up instead of a general objection, defer to the matching sibling
skill rather than handling it here.

## Structure

```
top-objections-playbook/
├── SKILL.md
├── examples/worked-examples.md
├── handlers/top-objections-playbook.md
├── knowledge/objection-psychology.md
├── playbooks/discovery-to-close-playbook.md
├── references/schemas.md
├── scripts/classify_objection.py
└── templates/
    ├── follow-up-email-template.md
    └── new-playbook-entry-template.md
```

- **`handlers/top-objections-playbook.md`** — the core lookup file: the response table. This is
  almost always the first and often only file that needs reading.
- **`playbooks/discovery-to-close-playbook.md`** — broader, situation-based guidance that doesn't
  fit a single-objection lookup (call-stage prep, discovery-to-close dynamics). Use when the
  question is about a deal stage, not one objection sentence.
- **`knowledge/objection-psychology.md`** — background on *why* the response frame works. Use when
  an objection doesn't match any handler row closely, or when asked to explain the reasoning
  rather than just produce a response.
- **`examples/worked-examples.md`** — worked, concrete input-to-output samples. Use as a few-shot
  reference when unsure how closely a generated response should match the schema.
- **`templates/`** — fill-in-the-blank artifacts for extending this skill (a new table row) or
  following up after a call (an email template).
- **`references/schemas.md`** — the shared taxonomy, response format, and CRM field mapping.
- **`scripts/classify_objection.py`** — rule-based classifier that routes objection text to
  `playbook`, `pricing`, or `competitor`.

## Workflow

1. **Classify.** Run the objection text through `scripts/classify_objection.py` (or reason through
   it directly if the script isn't runnable in the current environment). Competitor mentions take
   priority even when price is also raised — "Fortinet is cheaper" routes to
   `competitor-objection-handler`, not `pricing-objection-handler`. If the result is `pricing` or
   `competitor`, hand off to that sibling skill instead of continuing here.
2. **Read `handlers/top-objections-playbook.md`** and follow its response frame — don't improvise
   a different structure per answer.
3. **Generate the response** using the format in `references/schemas.md` § Response format spec.
   Keep it short enough for a rep to glance at mid-call.
4. **If prepping for a call or a deal stage rather than reacting to one objection**, read
   `playbooks/discovery-to-close-playbook.md` instead of the handler.
5. **If the objection doesn't match any handler row closely**, or the user asks *why* a response
   works, read `knowledge/objection-psychology.md` before answering.
6. **If the user wants a post-call follow-up message**, use `templates/follow-up-email-template.md`.
7. **If unsure how a generated response should look**, check `examples/worked-examples.md` for a
   reference before answering.
8. **If the user wants to add/edit content** (a new objection), open
   `templates/new-playbook-entry-template.md` to shape the new row, then add it to
   `handlers/top-objections-playbook.md`.
9. **If a CRM connector is available, offer to log the exchange** using the mapping in
   `references/schemas.md` § CRM logging. Always confirm before writing; never log silently.

## Testing this skill

1. **Local check (no upload needed):** run `scripts/classify_objection.py` with a few sample
   objections and confirm it returns the expected category — see the script's docstring for
   usage. Also read through `handlers/top-objections-playbook.md` to confirm the table renders and
   the response frame makes sense standalone.
2. **Trigger check (after uploading):** enable the skill in Customize > Skills, then try prompts
   that should trigger it (e.g. "a prospect just said it's not a priority right now, how do I
   respond") and ones that shouldn't (e.g. "write a cold outreach email") to confirm it fires only
   when relevant. Check Claude's visible thinking/response to confirm the skill was loaded.
3. **Content check:** run one real or realistic general objection through it and check the
   response follows the handler format and hard rules.
4. **Iterate on the description field** if the skill under- or over-triggers — it's the only thing
   Claude sees before deciding whether to load the rest of the skill, and Claude.ai caps it at 200
   characters, so keep it tight and trigger-focused rather than exhaustive.

## Building or extending this skill

Placeholder content (10 objections, plus the discovery-to-close playbook and worked examples) is
illustrative sample data for a network-security sales scenario — replace with the real team's data
before production use:
1. Get the actual top 10 weekly objections (win/loss data, call notes, or rep interviews).
2. When adding a new objection row, start from `templates/new-playbook-entry-template.md` so the
   rationale stays grounded in a real underlying concern, not a guess — see
   `knowledge/objection-psychology.md` for what that means.
3. After adding real content, replace the corresponding placeholder entries in
   `examples/worked-examples.md` so the few-shot reference matches the team's actual objections
   rather than the network-security sample data.

### Keeping in sync with the sibling skills

`references/schemas.md` and `scripts/classify_objection.py` are intentionally duplicated
identically across all four sibling skills so each one is fully self-contained (shareable or
usable on its own, without needing the others). This copy is treated as the canonical source —
if the response-format schema, CRM field mapping, or classifier keyword lists change here, update
the matching files in `pricing-objection-handler/`, `competitor-objection-handler/`, and
`objection-roleplay-simulator/` too, and diff their copies against this one when in doubt about
which is current.
