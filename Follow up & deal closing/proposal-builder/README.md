# proposal-builder

A Claude skill that generates a client-ready proposal or quote document from deal scope, pricing, and terms — built together with the `docx` skill.

## Why this exists

Proposals need to be consistent (same structure every time) but accurate (real numbers, real terms) and specific (tied to the client's actual need, not boilerplate). This skill separates the reusable structure (`templates/`) from the real business numbers (`assets/`), so the output is both fast and correct.

## Folder structure

```
proposal-builder/
├── SKILL.md
├── README.md
├── knowledge/
│   ├── proposal_structure_guidelines.md
│   └── case_studies.md
├── assets/
│   ├── pricing_rate_card_template.md      # Fillable rate card — source of truth for pricing
│   └── terms_and_conditions_template.md   # Fillable standard terms
├── templates/
│   ├── standard_proposal_template.md      # Full multi-section proposal
│   └── quote_only_template.md             # Lightweight pricing-only quote
├── examples/
│   └── examples.md
└── checklists/
    └── proposal_checklist.md
```

## Design principle: separation of concerns

- **SKILL.md** — the workflow (gather → price → structure → build). Rarely changes.
- **assets/** — the actual business numbers (rate card, terms). This is the most important folder to keep accurate — the skill treats it as ground truth and never invents beyond it.
- **templates/** — the document shape. Edit when your proposal format changes.
- **knowledge/** — supporting facts (case studies, structural best practices).
- **examples/** — few-shot calibration for tone and completeness.
- **checklists/** — final safety net before the file goes out.

## Placeholder content notice

`assets/pricing_rate_card_template.md` and `assets/terms_and_conditions_template.md` contain **bracketed placeholders**, not real prices — replace every bracket with your actual products, rates, discounts, and standard terms before using this for real client-facing proposals. `knowledge/case_studies.md` similarly uses placeholder company names; replace with real, verified case studies before use. The skill will not invent numbers beyond what's in these files, so it's only as accurate as what you put in them.
