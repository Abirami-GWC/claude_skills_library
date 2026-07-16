# narrative-deck-builder

Turns a demo plan (or raw customer/problem/product info) into a story-driven
customer presentation outline — problem, challenge, solution, proof, business
value, next steps — instead of a feature-listing product brochure.

## Folder structure

```
narrative-deck-builder/
│
├── SKILL.md                          # Main instructions: role, workflow, rules
├── README.md                          # This file
│
├── templates/
│   └── presentation_template.md       # Slide-by-slide output structure
│
├── frameworks/
│   └── storytelling_framework.md      # THE core file — the 8-beat story flow
│
├── knowledge/
│   └── knowledge.md                    # Product benefits, success stories, migration facts
│
└── examples/
    └── examples.md                      # Worked examples incl. the ABC Retail case
```

## How it works

1. Understand the business context (industry, current vendor, problems,
   recommended product) — from raw input or an existing demo plan.
2. Apply `frameworks/storytelling_framework.md` — the required narrative beats,
   which don't change regardless of input order.
3. Pull facts from `knowledge/knowledge.md` — product benefits, a matching
   success story, migration data. Never invent facts not found here.
4. Fill `templates/presentation_template.md`.
5. Use `examples/examples.md` for style/slide-count consistency.

## What makes this skill different from the other two

| Skill | Purpose | Output |
|---|---|---|
| pain-based-demo-builder | Solve stated pain points | Lean, sequenced demo agenda |
| discovery-to-demo-mapper | Organize a full discovery call | Complete demo plan |
| narrative-deck-builder | Turn a demo plan into a business story | Story-driven presentation outline |

This skill leans on narrative logic (`frameworks/`) rather than lookup tables
(`mappings/`) — there's no `mappings.yaml` here by design, since sequencing is
governed by the fixed story flow, not a pain→feature lookup.

## Placeholder content notice

`knowledge/knowledge.md` contains generic/illustrative WatchGuard-style
content (Firebox, ThreatSync, sample success stories, sample migration
timelines). Replace these with verified product facts and marketing-approved
customer success stories before using this for real customer presentations —
the skill explicitly refuses to invent a success story or statistic that isn't
in this file.
