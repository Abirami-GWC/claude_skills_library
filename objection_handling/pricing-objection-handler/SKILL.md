---
name: pricing-objection-handler
description: "Classify and respond to price/budget sales pushback, renewals, and upsell objections. Use for pricing objections, discount requests, or budget pushback."
---

# Pricing Objection Handler

Classifies and responds to price and budget objections in real time, and supports building
objection handling into a sales agent (e.g. a CRM-connected digital coworker).

**This is a general-purpose framework, not tied to any specific company, product, or Claude
Project.** Once installed as an account-level skill (see Installation below), it's available in
any conversation — this chat, a different project, Claude Code, or the API — not just the
context it was built in. The bundled tables are illustrative sample content (written for a
network-security sales scenario) — swap them for the real team's pricing rules. Nothing in
`SKILL.md` or `references/schemas.md` is industry-specific; only the handler tables need
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
- `competitor-objection-handler` — responses when a competitor is name-dropped
- `objection-roleplay-simulator` — practice mode simulating live pushback

If the pushback is really about a named competitor rather than price, defer to
`competitor-objection-handler` — "Fortinet is cheaper" routes there, not here.

## Structure

```
pricing-objection-handler/
├── SKILL.md
├── examples/worked-examples.md
├── handlers/pricing-objection-handler.md
├── knowledge/pricing-psychology.md
├── playbooks/renewal-and-upsell-objections.md
├── references/schemas.md
├── scripts/classify_objection.py
└── templates/
    ├── follow-up-email-template.md
    └── new-pricing-scenario-template.md
```

- **`handlers/pricing-objection-handler.md`** — the core lookup file: the response table. This is
  almost always the first and often only file that needs reading. It never states a specific
  discount.
- **`playbooks/renewal-and-upsell-objections.md`** — broader, situation-based guidance that doesn't
  fit a single-objection lookup (renewals, upsell pushback, late-stage stalls). Use when the
  question is about a deal stage or account situation, not one objection sentence.
- **`knowledge/pricing-psychology.md`** — background on *why* the pricing response frame works. Use
  when an objection doesn't match any handler row closely, or when asked to explain the reasoning
  rather than just produce a response.
- **`examples/worked-examples.md`** — worked, concrete input-to-output samples. Use as a few-shot
  reference when unsure how closely a generated response should match the schema.
- **`templates/`** — fill-in-the-blank artifacts for extending this skill (a new pricing scenario)
  or following up after a call (an email template).
- **`references/schemas.md`** — the shared taxonomy, response format, and CRM field mapping.
- **`scripts/classify_objection.py`** — rule-based classifier that routes objection text to
  `playbook`, `pricing`, or `competitor`.

## Workflow

1. **Classify.** Run the objection text through `scripts/classify_objection.py` (or reason through
   it directly if the script isn't runnable in the current environment). Competitor mentions take
   priority even when price is also raised — if the result is `competitor`, hand off to
   `competitor-objection-handler` instead of continuing here. If it's `playbook`, hand off to
   `top-objections-playbook`.
2. **Read `handlers/pricing-objection-handler.md`** and follow its response frame — don't
   improvise a different structure per answer, and always check the "do not say" column before
   responding. Pricing objections need more care than general pushback because a wrong answer can
   commit the company to something a rep isn't authorized to offer.
3. **Generate the response** using the format in `references/schemas.md` § Response format spec.
   Keep it short enough for a rep to glance at mid-call.
4. **If prepping for a renewal or upsell conversation rather than reacting to one objection**,
   read `playbooks/renewal-and-upsell-objections.md` instead of the handler.
5. **If the objection doesn't match any handler row closely**, or the user asks *why* a response
   works, read `knowledge/pricing-psychology.md` before answering.
6. **If the user wants a post-call follow-up message**, use `templates/follow-up-email-template.md`.
7. **If unsure how a generated response should look**, check `examples/worked-examples.md` for a
   reference before answering.
8. **If the user wants to add/edit content** (a new pricing scenario), open
   `templates/new-pricing-scenario-template.md` to shape the new row, then add it to
   `handlers/pricing-objection-handler.md` or `playbooks/renewal-and-upsell-objections.md`.
9. **If a CRM connector is available, offer to log the exchange** using the mapping in
   `references/schemas.md` § CRM logging. Always confirm before writing; never log silently.

## Testing this skill

1. **Local check (no upload needed):** run `scripts/classify_objection.py` with a few sample
   objections and confirm it returns the expected category — see the script's docstring for
   usage. Also read through `handlers/pricing-objection-handler.md` to confirm the table renders
   and the response frame makes sense standalone.
2. **Trigger check (after uploading):** enable the skill in Customize > Skills, then try prompts
   that should trigger it (e.g. "the prospect says our price is too high, how do I respond") and
   ones that shouldn't (e.g. "write a cold outreach email") to confirm it fires only when
   relevant. Check Claude's visible thinking/response to confirm the skill was loaded.
3. **Content check:** run one real or realistic pricing objection through it and check the
   response follows the handler format and hard rules (never states a discount number).
4. **Iterate on the description field** if the skill under- or over-triggers — it's the only thing
   Claude sees before deciding whether to load the rest of the skill, and Claude.ai caps it at 200
   characters, so keep it tight and trigger-focused rather than exhaustive.

## Building or extending this skill

Placeholder pricing scenarios and renewal/upsell content are illustrative sample data for a
network-security sales scenario — replace with the real team's data before production use:
1. Confirm real discount authority before writing pricing guardrails — never let a talk track
   imply flexibility a rep isn't approved to offer. This applies in full, including
   `playbooks/renewal-and-upsell-objections.md`.
2. When adding a new pricing scenario, start from `templates/new-pricing-scenario-template.md` so
   the rationale stays grounded in a real underlying concern, not a guess — see
   `knowledge/pricing-psychology.md` for what that means.
3. After adding real content, replace the corresponding placeholder entries in
   `examples/worked-examples.md` so the few-shot reference matches the team's actual objections
   rather than the network-security sample data.

### Keeping in sync with the sibling skills

`references/schemas.md` and `scripts/classify_objection.py` are intentionally duplicated
identically across all four sibling skills so each one is fully self-contained (shareable or
usable on its own, without needing the others). Treat `top-objections-playbook/`'s copies as the
canonical source, since that's the default/entry skill — if the response-format schema, CRM field
mapping, or classifier keyword lists change, update this folder's copies too and diff against
`top-objections-playbook/` when in doubt about which is current.
