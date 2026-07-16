# Workflow: Building Persona-Aware Why-Us Messaging

## Step 1 — Elicit context

Confirm or ask:
1. Competitor name (and product line/tier if relevant)
2. Buyer persona — match against `knowledge/persona_priorities.json`; if the
   user's buyer doesn't fit cleanly, ask a short clarifying question rather
   than forcing the nearest label
3. Output channel: website copy | email | talk track | deck notes
4. Available differentiator evidence — accept a filled competitor profile,
   freeform facts, or uploaded documents

## Step 2 — Select and frame differentiators for this persona

From available evidence, choose 2–4 differentiators that:
- Match this persona's `preferred_differentiator_types`
  (capability/economic/operational) from the persona map
- Are translated into an **outcome statement** for this persona specifically,
  not left as a raw feature description
- Each carry a proof point where possible

Avoid the persona's `avoid` list (e.g., don't lead an end-user narrative with
pricing framing).

## Step 3 — Draft with acknowledge-then-pivot

For the lead differentiator especially, acknowledge a genuine competitor
strength before pivoting to the gap and how this product closes it, framed in
this persona's language.

## Step 4 — Assemble using the matching template

- Website copy / one-pager → `templates/why_us_one_pager.md`
- Talk track → `templates/talk_track.md`
- Email → `templates/email_snippet.md`
- For repeatable persona/channel combinations, offer to save the config using
  `templates/why_us_messaging.yaml` so future requests for the same
  persona+competitor can be regenerated quickly with updated facts.

## Step 5 — Validate

Run every item in `instructions/validation_rules.md` before delivering.

## Step 6 — Present

Deliver the narrative. If multiple personas were requested, produce clearly
labeled separate versions — never blend personas into one piece of copy.

## Common mistakes to avoid

- **One-size-fits-all messaging**: writing the same narrative regardless of
  persona. Prevention: Step 2 requires explicit persona-priority mapping.
- **Feature-dump framing**: stating capabilities without outcome translation.
  Prevention: Step 2's "outcome statement" requirement.
- **Fabricating competitor facts**: prevention — every claim must trace to
  Step 1 evidence; unresolved gaps get `[NEEDS SOURCE]`, never invented.
- **Blending personas in one document**: prevention — Step 6 explicit rule
  requiring separate labeled versions.
- **Wrong differentiator type for the persona** (e.g., leading a CFO narrative
  with a technical architecture deep-dive): prevention — Step 2's type-matching
  against the persona map.
