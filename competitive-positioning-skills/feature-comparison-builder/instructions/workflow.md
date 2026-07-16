# Workflow: Building a Feature Comparison Matrix

## Step 1 — Scope the comparison

Confirm or ask:
- Which vendor(s) to include (this company + one or more named competitors —
  this skill natively supports 3+ vendors in one matrix)
- Which dimensions matter — if unspecified, propose the standard categories
  from `knowledge/comparison_dimensions.md` and confirm
- Output format(s) needed: markdown, CSV, interactive HTML, and/or a
  presentation-ready Word/PDF export
- Purpose (RFP response, sales deck, website page) — affects tone/detail level

## Step 2 — Populate the data model

Fill in `knowledge/comparison_matrix_schema.json`'s structure for every
vendor × dimension cell: `support_level`, `detail` for nuance, and
`source_note`/`source_url` for every non-"us" cell (and for "us" cells if the
claim isn't obviously internal common knowledge).

Pull source data in priority order:
1. Documents/data the user has supplied in this conversation
2. Facts the user directly confirms in chat
3. Publicly available competitor documentation the user points to, or that has
   already been fetched in this session

Never fill a cell from general/trained knowledge about "how a company like
this probably works" — if there's no source, the cell is `Unknown`.

**AI Capabilities rows specifically**: verify release status (GA/beta/roadmap)
explicitly — do not assume a marketing claim means general availability. See
`references/ai_capability_comparison_notes.md`.

## Step 3 — Validate

Run every check in `instructions/data_validation.md`. Do not proceed to
rendering with unresolved validation failures.

## Step 4 — Render

- **Markdown**: `templates/comparison_table.md`, grouped by category with subheadings.
- **CSV**: `templates/comparison_table.csv` — one row per vendor×dimension, for
  spreadsheet/RFP tool import.
- **Interactive HTML**: `scripts/build_comparison_html.py` against the
  populated JSON — filterable/sortable widget for web pages or in-chat exploration.
- **Presentation-ready Word/PDF**: `scripts/build_comparison_docx.py` against
  the populated JSON — for decks or formal document export. Convert to PDF and
  visually check readability if the matrix has many vendors/dimensions (wide
  tables can overflow page width — consider landscape orientation or
  splitting by category if so).

## Step 5 — Deliver

- Include the `as_of_date` prominently.
- List sources in a footer/appendix, not embedded in every visible cell.
- Flag every `Unknown` cell as an open item with a suggested next step.

## Common mistakes to avoid

- **Guessing a competitor "No"**: highest-risk mistake. Always mark `Unknown`
  instead of inferring absence.
- **Inconsistent symbols/scale across rows**: always render from the single
  `scoring_legend.md` scale.
- **Stale pricing or AI-capability claims presented as current**: always
  include `as_of_date`; for AI rows specifically verify GA/beta/roadmap status
  rather than assuming.
- **Biased dimension naming**: dimension names must be neutral, outcome-based.
- **Overflowing table width in N-way (3+) comparisons**: for docx/PDF exports
  with many vendors, check landscape orientation or split into multiple
  category-scoped tables rather than shrinking text unreadably.
