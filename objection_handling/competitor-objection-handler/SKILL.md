---
name: competitor-objection-handler
description: "Classify and respond to sales objections that name-drop a competitor. Use when a prospect mentions a specific competitor or asks for a comparison."
---

# Competitor Objection Handler

Classifies and responds to competitor-mention objections in real time, and supports building
objection handling into a sales agent (e.g. a CRM-connected digital coworker).

**This is a general-purpose framework, not tied to any specific company, product, or Claude
Project.** Once installed as an account-level skill (see Installation below), it's available in
any conversation — this chat, a different project, Claude Code, or the API — not just the
context it was built in. The bundled battlecards are illustrative sample content (written for a
network-security sales scenario) — swap them for the real team's competitors. Nothing in
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
- `top-objections-playbook` — general pushback (the 10 weekly objections)
- `pricing-objection-handler` — price/budget pushback
- `objection-roleplay-simulator` — practice mode simulating live pushback

Competitor mentions take priority even when price is also raised — "Fortinet is cheaper" is
handled here, not in `pricing-objection-handler`.

**Relationship to `competitive_positioning` (a different topic folder):** this skill's
`handlers/competitor-objection-handler.md` table is a live-call, named-competitor
lookup (Fortinet → strength → differentiation → question), not a duplicate of
`competitive_positioning/battlecard-generator`'s output. Battlecard Generator
produces the fuller, formal one-page battlecard document (which itself contains an
objection-handling section) — use that skill when building/refreshing the source
document a battlecard is generated from; use this skill when reacting in the
moment to a specific spoken objection. `competitive_positioning/why-us-messaging`
covers a third, distinct case: persuasive, persona-tailored "why us" narrative for
decks/emails/web copy, not a quick-reference for live objection handling.

## Structure

```
competitor-objection-handler/
├── SKILL.md
├── examples/worked-examples.md
├── handlers/competitor-objection-handler.md
├── knowledge/competitive-reframing.md
├── playbooks/competitive-evaluation-playbook.md
├── references/schemas.md
├── scripts/classify_objection.py
└── templates/
    ├── follow-up-email-template.md
    └── new-battlecard-template.md
```

- **`handlers/competitor-objection-handler.md`** — the core lookup file: the battlecard table.
  This is almost always the first and often only file that needs reading. It never states an
  unverified competitor claim.
- **`playbooks/competitive-evaluation-playbook.md`** — broader, situation-based guidance that
  doesn't fit a single-objection lookup (evaluation-stage dynamics, bake-offs). Use when the
  question is about a deal stage or account situation, not one objection sentence.
- **`knowledge/competitive-reframing.md`** — background on *why* the response frame works. Use
  when an objection doesn't match any handler row closely, or when asked to explain the reasoning
  rather than just produce a response.
- **`examples/worked-examples.md`** — worked, concrete input-to-output samples. Use as a few-shot
  reference when unsure how closely a generated response should match the schema.
- **`templates/`** — fill-in-the-blank artifacts for extending this skill (a new battlecard entry)
  or following up after a call (an email template).
- **`references/schemas.md`** — the shared taxonomy, response format, and CRM field mapping.
- **`scripts/classify_objection.py`** — rule-based classifier that routes objection text to
  `playbook`, `pricing`, or `competitor`, and identifies which competitor was matched.

## Workflow

1. **Classify.** Run the objection text through `scripts/classify_objection.py` (or reason through
   it directly if the script isn't runnable in the current environment) to confirm the category is
   `competitor` and get the matched competitor name. If the result is `playbook` or `pricing`,
   hand off to `top-objections-playbook` or `pricing-objection-handler` instead.
2. **Look up the named competitor** in `handlers/competitor-objection-handler.md`. Structure every
   response as: what they do well → how we differentiate → a question to ask back. Never state a
   competitor fact that isn't listed there or otherwise verified — if the competitor isn't in the
   table, say the comparison needs verification and offer to draft a new entry rather than
   guessing.
3. **Generate the response** using the format in `references/schemas.md` § Response format spec.
   Keep it short enough for a rep to glance at mid-call.
4. **If prepping for an evaluation or bake-off rather than reacting to one objection**, read
   `playbooks/competitive-evaluation-playbook.md` instead of the handler.
5. **If the objection doesn't match any handler row closely**, or the user asks *why* a response
   works, read `knowledge/competitive-reframing.md` before answering.
6. **If the user wants a post-call follow-up message**, use `templates/follow-up-email-template.md`.
7. **If unsure how a generated response should look**, check `examples/worked-examples.md` for a
   reference before answering.
8. **If the user wants to add/edit content** (a new competitor), open
   `templates/new-battlecard-template.md` to shape the new entry, then add it to
   `handlers/competitor-objection-handler.md`.
9. **If a CRM connector is available, offer to log the exchange** using the mapping in
   `references/schemas.md` § CRM logging. Always confirm before writing; never log silently.

## Testing this skill

1. **Local check (no upload needed):** run `scripts/classify_objection.py` with a few sample
   objections and confirm it returns the expected category and competitor — see the script's
   docstring for usage. Also read through `handlers/competitor-objection-handler.md` to confirm
   the battlecard table renders and the response frame makes sense standalone.
2. **Trigger check (after uploading):** enable the skill in Customize > Skills, then try prompts
   that should trigger it (e.g. "a prospect just said they're already using a competitor, how do I
   respond") and ones that shouldn't (e.g. "write a cold outreach email") to confirm it fires only
   when relevant. Check Claude's visible thinking/response to confirm the skill was loaded.
3. **Content check:** run one real or realistic competitor objection through it and check the
   response follows the handler format and hard rules (never states an unverified claim).
4. **Iterate on the description field** if the skill under- or over-triggers — it's the only thing
   Claude sees before deciding whether to load the rest of the skill, and Claude.ai caps it at 200
   characters, so keep it tight and trigger-focused rather than exhaustive.

## Building or extending this skill

Placeholder battlecards (3 competitors) and the evaluation playbook are illustrative sample data
for a network-security sales scenario — replace with the real team's data before production use:
1. Use only verified competitor facts in `handlers/competitor-objection-handler.md` — flag
   anything unconfirmed rather than guessing. Use `templates/new-battlecard-template.md`'s
   checklist when adding a competitor.
2. When adding a new battlecard entry, start from `templates/new-battlecard-template.md` so the
   rationale stays grounded in a real underlying concern, not a guess — see
   `knowledge/competitive-reframing.md` for what that means.
3. After adding real content, replace the corresponding placeholder entries in
   `examples/worked-examples.md` so the few-shot reference matches the team's actual objections
   rather than the network-security sample data.

### Keeping in sync with the sibling skills

`references/schemas.md` and `scripts/classify_objection.py` are intentionally duplicated
identically across all four sibling skills so each one is fully self-contained (shareable or
usable on its own, without needing the others). Treat `top-objections-playbook/`'s copies as the
canonical source, since that's the default/entry skill — if the response-format schema, CRM field
mapping, or classifier keyword lists (e.g. a new competitor name) change, update this folder's
copies too and diff against `top-objections-playbook/` when in doubt about which is current.
