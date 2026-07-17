# renewal-expansion-planner

A Claude skill that builds a renewal/expansion touchpoint timeline for an existing account, timed against the real contract end date and framed by usage signal.

## Why this exists

A generic "reach out 60 days before renewal" reminder misses two things this skill fixes: it should skip milestones already in the past, and it should change its framing entirely depending on whether the account is thriving, flat, or at risk — pitching an upsell to an at-risk account is a sequencing mistake this skill is designed to prevent.

## Folder structure

```
renewal-expansion-planner/
├── SKILL.md
├── README.md
├── knowledge/
│   ├── usage_signal_definitions.md   # How to classify growing/flat/at-risk from notes
│   └── expansion_playbook.md         # Which upsell path fits which situation
├── mappings/
│   └── signal_to_framing.yaml        # Usage signal -> framing + touchpoint sequencing
├── templates/
│   ├── renewal_timeline_template.md  # Default: short table/checklist
│   └── qbr_agenda_template.md        # Fuller QBR-style write-up
├── examples/
│   └── examples.md                   # Growing / flat / at-risk worked examples
└── checklists/
    └── renewal_checklist.md
```

## Design principle: separation of concerns

- **SKILL.md** — the sequencing logic (classify → calculate → build → frame). Rarely changes.
- **mappings/** — the actual business rule connecting usage signal to framing and timing. Edit this as your renewal playbook evolves — most frequently updated folder.
- **knowledge/** — supporting definitions and the expansion playbook.
- **templates/** — output shape.
- **examples/** — few-shot calibration across the three usage-signal cases.
- **checklists/** — safety net, especially for the at-risk sequencing rule.

## Placeholder content notice

`mappings/signal_to_framing.yaml` and `knowledge/expansion_playbook.md` use a generic touchpoint cadence (90/60/30/14 days) and the running example scenario (Alderbrook Health Network). Adjust the cadence and upsell paths to match your actual customer success process before relying on this for real accounts.
