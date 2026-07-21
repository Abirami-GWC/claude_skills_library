# Workflow: Building a Lead Magnet

## Step 1 — Confirm topic, persona, and specific value

Ask (if not already known):
1. Topic/problem the offer addresses
2. Target persona
3. The specific, concrete value delivered — "what will the reader be able to
   do after this that they couldn't before?" A topic alone ("a guide about
   onboarding") is not enough to start drafting; push for the specific angle
   ("a checklist to cut new-hire ramp time from 6 weeks to 3").

## Step 2 — Select the format

If the user hasn't specified, use `knowledge/lead_magnet_types.md`'s
selection table to propose the best-fit format for the stated value, and confirm.

## Step 3 — Draft the offer content

- **Guide**: use `templates/guide_template.md`. Scope sections to only what's
  needed for the stated promise — cut anything that doesn't serve it.
- **Checklist**: use `templates/checklist_template.md`. Every item must be a
  concrete, checkable action, not a restated goal.
- **Calculator**: do NOT start drafting until the exact formula/inputs/outputs
  are confirmed with the user (Step 3a below) — never invent business logic.
- **Template/Worksheet**: use `templates/worksheet_template.md`. Structure
  fields around the specific methodology/framework being taught, not a
  generic blank document.
- **Quiz/Assessment**: use `templates/quiz_assessment_template.md`. Every
  result must be genuinely differentiated per answer pattern, not a single
  generic result regardless of input.

### Step 3a — For calculators specifically

Confirm explicitly:
- What inputs does the user provide? (e.g., "number of employees," "current
  monthly spend")
- What is the exact formula/logic connecting inputs to output? Get this from
  the user directly — do not assume a standard industry formula unless the
  user confirms it's the one they want.
- What should the output look like (a single number, a range, a
  breakdown table)?

Then build using `scripts/build_calculator_html.py`. Test the generated
calculator with at least one sample input set to confirm the math actually
matches the confirmed formula before delivering.

## Step 4 — Draft landing page copy

Use `templates/landing_page_copy_template.md` and
`references/gating_and_conversion_best_practices.md`. The copy should sell
the specific outcome (Step 1's value statement), not just describe the format.

## Step 5 — Validate

Run every item in `instructions/validation_rules.md`.

## Step 6 — Deliver

Present the offer content and landing page copy together. For calculators,
deliver the working HTML tool plus the landing page copy that would surround it.

## Common mistakes to avoid

- **Padding for length**: adding filler sections to make a guide look more
  substantial. Prevention: Step 3's explicit "cut anything that doesn't serve
  the promise" rule.
- **Vague checklist items**: restating goals instead of actions. Prevention:
  Step 3's concrete-action requirement, checked again in validation.
- **Fabricated calculator logic**: guessing at a formula instead of
  confirming it. Prevention: Step 3a is a hard gate — no calculator build
  starts without confirmed formula/inputs/outputs.
- **Landing copy that oversells**: promising guaranteed results or
  exaggerated claims. Prevention: Step 4's reference to conversion best
  practices, which explicitly flags this.
- **Over-asking on the form**: requesting more fields than the offer
  justifies. Prevention: `references/gating_and_conversion_best_practices.md`
  explicit field-count guidance.
