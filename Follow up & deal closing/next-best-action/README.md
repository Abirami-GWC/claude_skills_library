# next-best-action

A Claude skill that turns a deal's stage, last-contact date, and any stated blocker into a short, specific list of what to do next — instead of generic "keep following up" advice.

## Why this exists

Reps often know a deal has stalled but not what to actually do about it. This skill encodes stage-by-stage playbook logic, an objection-response lookup, and a days-silent override rule, so the recommendation is always tied to a concrete fact about the deal.

## Folder structure

```
next-best-action/
├── SKILL.md                          # Instructions Claude follows
├── README.md                         # This file
├── knowledge/
│   ├── stage_definitions.md          # The generic B2B pipeline model
│   └── buyer_personas.md             # How to adjust recommendations by persona
├── mappings/
│   ├── stage_to_actions.yaml         # Stage -> recommended actions (with aliases)
│   ├── objection_to_response.yaml    # Objection -> response angle (with aliases)
│   └── engagement_signal_to_priority.yaml  # Days since contact -> override rule
├── templates/
│   ├── next_action_output.md         # Default: short bullet output
│   └── action_plan_detailed.md       # Fuller plan, if requested
├── examples/
│   ├── proposal_budget_objection_example.md
│   ├── discovery_stage_example.md
│   └── negotiation_stalled_example.md
└── checklists/
    └── next_action_checklist.md
```

## Design principle: separation of concerns

- **SKILL.md** — how Claude should think (workflow, rules). Rarely changes.
- **mappings/** — the actual business logic (which action for which stage/objection). This is the file to edit when your sales playbook changes — most frequently updated folder.
- **knowledge/** — ground-truth facts about your pipeline model and buyer types.
- **templates/** — output shape. Edit when you want the output formatted differently.
- **examples/** — few-shot calibration. Add a new one any time the output style drifts.
- **checklists/** — safety net, not the primary logic.

## Placeholder content notice

`mappings/`, `knowledge/`, and `examples/` currently use a **generic B2B pipeline model** (Prospecting → Discovery → Demo/Evaluation → Proposal → Negotiation → Closed Won/Lost) and a running example scenario (GWC Data selling Insight Suite to Alderbrook Health Network). Replace the stage names, actions, and objection responses in `mappings/` with your actual sales methodology and product before relying on this for real deals — the skill only recommends what's in these files, it doesn't invent playbook steps.
