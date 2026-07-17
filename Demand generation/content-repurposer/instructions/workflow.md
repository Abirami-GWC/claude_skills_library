# Workflow: Repurposing Long-Form Content

## Step 1 — Ingest the full source

Read the complete source asset — not a summary of it. If the user only
supplied a link or a brief description, ask for the full text/transcript or
fetch the link, since repurposing from a vague summary risks drifting from
what the source actually says.

Optionally run `scripts/extract_key_points.py` against the source text to
surface candidate quotes, statistics, and section headers as a starting point
— treat its output as a draft shortlist to review, not a final selection.

## Step 2 — Confirm target formats

Ask which formats/channels are needed, or propose a sensible default set
(e.g., one LinkedIn post, a 3-post thread, one email snippet) and confirm.
Check each requested format against `references/platform_specs.md` for its
constraints before drafting.

## Step 3 — Select the core idea per piece

For each output piece, choose ONE strong idea from the source — not a summary
of everything. If producing multiple pieces for the same platform, ensure
each one surfaces a different point (see Best Practices in SKILL.md on
varying the angle) rather than restating the same headline five ways.

## Step 4 — Draft using the format conversion guide

Follow `knowledge/format_conversion_guide.md`'s structural guidance for each
format — genuinely restructure for the platform, don't truncate a paragraph.
Use `templates/social_post_template.md` / `templates/email_snippet_template.md`
as drafting scaffolds.

## Step 5 — Validate

Run every item in `instructions/validation_rules.md` — fidelity to source,
copyright limits, and format constraints (character counts, etc.).

## Step 6 — Deliver

Present all pieces together, each clearly labeled by channel/format, in the
order the user's campaign would likely use them (or as requested). If the
user also wants a source-section-to-output mapping (useful for larger
repurposing jobs), fill `templates/repurposing_plan.csv`.

## Common mistakes to avoid

- **Copy-paste-and-trim**: producing outputs that are just shortened versions
  of the same paragraph. Prevention: Step 4's explicit "genuinely restructure"
  requirement, checked against the format conversion guide.
- **Drifting from the source's actual claims**: adding emphasis, statistics,
  or framing not present in the original. Prevention: Step 5 fidelity check.
- **Repeating the same angle across multiple pieces for one platform**.
  Prevention: Step 3's explicit angle-variation requirement.
- **Exceeding platform length limits**: prevention — Step 2's constraint
  lookup before drafting, and Step 5's explicit length check before delivery.
- **Over-quoting the source**: reproducing more than a short quote per piece.
  Prevention: Step 5 copyright check — one short quote max per piece, paraphrase the rest.
