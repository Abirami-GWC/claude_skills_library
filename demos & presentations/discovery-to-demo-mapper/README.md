# discovery-to-demo-mapper

Turns full discovery-call notes (company, industry, current vendor, pain
points, business goal, decision maker, timeline) into a structured,
customer-specific Demo Plan.

## Folder structure

```
discovery-to-demo-mapper/
│
├── SKILL.md              # Main instructions: role, workflow, output format, rules
├── README.md               # This file
│
├── templates/
│   └── demo_plan.md        # Standard output structure Claude fills in
│
├── mappings/
│   └── mappings.yaml        # current_vendor / decision_maker / industry -> focus areas
│
├── knowledge/
│   └── knowledge.md          # Product facts, migration paths, compliance coverage
│
└── examples/
    └── examples.md             # Worked examples: full notes, partial notes, unmapped vendor
```

## How it works

1. Discovery notes are parsed into fields (company, industry, vendor, pains,
   goal, decision maker, timeline).
2. `mappings.yaml` is checked three separate ways: what to show given the
   **current vendor**, what to emphasize given the **decision maker's role**,
   and what to weight given the **industry**.
3. `knowledge.md` supplies the actual facts (product benefits, migration
   timelines, compliance coverage) — this is the only source of truth for
   factual claims in the output.
4. `demo_plan.md` is filled in, skipping any section the discovery notes don't
   support (e.g. no Migration Strategy section if no current vendor was given).
5. `examples.md` keeps output style and edge-case handling consistent.

## Relationship to pain-based-demo-builder

- **pain-based-demo-builder**: short pain-point list → lean, sequenced agenda.
- **discovery-to-demo-mapper**: full discovery call → fuller demo plan with
  migration strategy and business benefits, tailored to the decision maker.

Use whichever matches how much context is actually available. If you use both
regularly, consider keeping `knowledge/knowledge.md` here and
`knowledge/product_features.md` + `case_studies.md` in the other skill in sync,
since they describe the same underlying products.

## Placeholder content notice

`mappings.yaml` and `knowledge.md` currently contain generic/illustrative
WatchGuard-style content (Firebox, ThreatSync, AuthPoint, sample migration
times, sample compliance coverage). Replace these with verified product facts,
real migration-time data, and confirmed compliance language before using this
for live customer-facing deals — the skill is designed to never state a fact
that isn't in these files, so it's only as accurate as what's in them.
