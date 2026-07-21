# closing-email-writer

A Claude skill that drafts ready-to-send follow-up emails for stalled or progressing deals — nudges, contract chases, re-engagement, and recaps.

## Why this exists

Reps lose momentum rewriting the same four kinds of emails from scratch every time. This skill keeps a skeleton per goal and fills it with the real deal facts, so drafts are fast without sounding like a mail-merge.

## Folder structure

```
closing-email-writer/
├── SKILL.md
├── README.md
├── knowledge/
│   ├── email_guidelines.md          # Tone, length, structure, signature rules
│   └── voice_and_style_notes.md     # How personal voice interacts with structure
├── mappings/
│   └── goal_to_template.yaml        # Request -> goal classification (with aliases)
├── templates/
│   ├── proposal_nudge_email.md
│   ├── contract_chase_email.md
│   ├── reengagement_email.md
│   └── recap_email.md
├── examples/
│   └── examples.md                  # Worked input -> output per goal
└── checklists/
    └── email_checklist.md
```

## Design principle: separation of concerns

- **SKILL.md** — the workflow logic. Rarely changes.
- **templates/** — the skeleton per goal. Edit when your standard email structure changes.
- **knowledge/** — writing rules (length, tone). Edit when company email standards change.
- **mappings/** — classification logic for ambiguous requests. Most frequently updated as you notice new phrasings.
- **examples/** — few-shot calibration for tone and level of detail.
- **checklists/** — safety net before sending.

## Placeholder content notice

Templates and examples use a generic tone and the running example scenario (GWC Data / Alderbrook Health Network). Swap in your actual company voice, signature block, and any real legal/compliance disclaimer language before using this for real customer-facing email.
