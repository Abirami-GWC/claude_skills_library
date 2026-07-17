---
name: objection-roleplay-simulator
description: "Run a live-practice roleplay where Claude plays a skeptical prospect raising objections, for sales reps to rehearse before a real call. Use for objection practice or mock sales calls."
---

# Objection Roleplay Simulator

Practice mode where Claude plays a skeptical prospect so a rep can rehearse handling objections
before a live call. This is a conversation, not a lookup — there's no content table here, only
instructions.

**This is a general-purpose framework, not tied to any specific company, product, or Claude
Project.** Once installed as an account-level skill (see Installation below), it's available in
any conversation — this chat, a different project, Claude Code, or the API — not just the
context it was built in. The bundled negotiation content is illustrative sample content (written
for a network-security sales scenario) — swap it for the real team's negotiation dynamics.
Nothing in `SKILL.md` or `references/schemas.md` is industry-specific.

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
- `competitor-objection-handler` — responses when a competitor is name-dropped

This skill draws realistic objections from the equivalent content in those three skills (bundled
copies live under `knowledge/` and referenced by name below) rather than inventing objections that
contradict the real playbooks.

## Structure

```
objection-roleplay-simulator/
├── SKILL.md
├── examples/roleplay-transcript-example.md
├── handlers/objection-roleplay-simulator.md
├── knowledge/deliberate-practice-and-qualification.md
├── playbooks/negotiation-endgame-playbook.md
├── references/schemas.md
├── scripts/classify_objection.py
└── templates/
    ├── follow-up-email-template.md
    └── new-roleplay-scenario-template.md
```

- **`handlers/objection-roleplay-simulator.md`** — the core instructions for running a practice
  session: which category to drill, how to stay in character, and how to close out the roleplay.
  This is almost always the first and often only file that needs reading.
- **`playbooks/negotiation-endgame-playbook.md`** — broader guidance for late-stage negotiation
  practice (final-offer dynamics, walk-away moments). Use when the practice session is about
  closing a negotiation rather than handling a single objection.
- **`knowledge/deliberate-practice-and-qualification.md`** — background on *why* the practice
  format is structured this way (deliberate-practice principles, how to qualify a rep's
  readiness). Use when asked to explain the reasoning behind the format, or to adapt it.
- **`examples/roleplay-transcript-example.md`** — a worked, concrete transcript sample. Use as a
  reference for expected tone and structure when unsure how a session should look.
- **`templates/new-roleplay-scenario-template.md`** — fill-in-the-blank artifact for adding a new
  practice scenario.
- **`templates/follow-up-email-template.md`** — for drafting a post-practice follow-up note.
- **`references/schemas.md`** — the shared taxonomy, response format, and CRM field mapping.
- **`scripts/classify_objection.py`** — the shared classifier, used here to keep the roleplay's
  objections consistent with how real objections would be categorized.

## Workflow

1. **Ask which category to drill** if the user hasn't said: general objections, pricing, or
   competitor pushback. One question, not a checklist.
2. **Read `handlers/objection-roleplay-simulator.md`** and follow its session instructions.
3. **Stay in character** as a mildly skeptical but reasonable prospect. Draw realistic objections
   consistent with the chosen category — don't invent objections that contradict the real
   playbook content in the sibling skills.
4. **If the practice is about a negotiation endgame** (final offer, walk-away moment) rather than
   a single objection, read `playbooks/negotiation-endgame-playbook.md` instead of the handler.
5. **If unsure how a session should look**, check `examples/roleplay-transcript-example.md` for a
   reference before starting.
6. **If asked why the format works this way**, read
   `knowledge/deliberate-practice-and-qualification.md` before answering.
7. **After the session, offer a follow-up note** using `templates/follow-up-email-template.md` if
   relevant.
8. **If the user wants to add a new practice scenario**, open
   `templates/new-roleplay-scenario-template.md` to shape it.
9. **If a CRM connector is available, offer to log the practice session** using the mapping in
   `references/schemas.md` § CRM logging. Always confirm before writing; never log silently.

## Testing this skill

1. **Local check (no upload needed):** read through `handlers/objection-roleplay-simulator.md` to
   confirm the session instructions make sense standalone, and run `scripts/classify_objection.py`
   with a few sample objections to confirm it still classifies correctly.
2. **Trigger check (after uploading):** enable the skill in Customize > Skills, then try prompts
   that should trigger it (e.g. "can you role-play a skeptical prospect so I can practice") and
   ones that shouldn't (e.g. "write a cold outreach email") to confirm it fires only when
   relevant. Check Claude's visible thinking/response to confirm the skill was loaded.
3. **Content check:** run one practice session per category (general, pricing, competitor) and
   check Claude stays in character and doesn't invent objections that contradict the real
   playbooks.
4. **Iterate on the description field** if the skill under- or over-triggers — it's the only thing
   Claude sees before deciding whether to load the rest of the skill, and Claude.ai caps it at 200
   characters, so keep it tight and trigger-focused rather than exhaustive.

## Building or extending this skill

Placeholder negotiation content and the example transcript are illustrative sample data for a
network-security sales scenario — replace with the real team's data before production use:
1. When adding a new practice scenario, start from `templates/new-roleplay-scenario-template.md`
   so it stays grounded in a real underlying concern, not a guess — see
   `knowledge/deliberate-practice-and-qualification.md` for what that means.
2. After adding real content, replace the placeholder transcript in
   `examples/roleplay-transcript-example.md` so it matches the team's actual objections rather
   than the network-security sample data.
3. Keep this skill's objections in sync with the real content in `top-objections-playbook`,
   `pricing-objection-handler`, and `competitor-objection-handler` as those are updated, so
   practice sessions don't drift from what reps actually hear.

### Keeping in sync with the sibling skills

`references/schemas.md` and `scripts/classify_objection.py` are intentionally duplicated
identically across all four sibling skills so each one is fully self-contained (shareable or
usable on its own, without needing the others). Treat `top-objections-playbook/`'s copies as the
canonical source, since that's the default/entry skill — if the response-format schema, CRM field
mapping, or classifier keyword lists change, update this folder's copies too and diff against
`top-objections-playbook/` when in doubt about which is current.
