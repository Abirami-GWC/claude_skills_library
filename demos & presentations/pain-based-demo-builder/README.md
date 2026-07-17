# pain-based-demo-builder

A Claude skill that turns a customer's stated pain points into a sequenced,
customer-focused demo agenda or script — instead of a generic feature walkthrough.

## Why this exists

Salespeople default to walking through Feature 1, Feature 2, Feature 3... Customers
disengage because they have to do the mental work of connecting features to their
own problems. This skill does that mapping and sequencing automatically.

## Folder structure

```
pain-based-demo-builder/
│
├── SKILL.md                # Main instructions Claude follows (role, workflow, rules)
├── README.md                # This file — human-facing documentation
│
├── templates/                # Output structure per audience
│   ├── demo_agenda.md        # Default: agenda-only output
│   ├── executive_demo.md     # Business-value framed, for leadership audiences
│   ├── technical_demo.md     # Deeper technical detail, for engineers/architects
│   └── poc_demo.md           # Proof-of-concept structure with success criteria
│
├── playbooks/                 # "If pain X, demo flow Y" per category
│   ├── security_playbook.md
│   ├── networking_playbook.md
│   ├── cloud_playbook.md
│   ├── compliance_playbook.md
│   └── industries/            # Industry lens: how to weight/frame category playbooks
│       ├── README.md
│       └── manufacturing_playbook.md
│
├── examples/                  # Few-shot worked examples (input -> output)
│   ├── vpn_example.md
│   ├── firewall_example.md
│   ├── endpoint_example.md
│   ├── sase_example.md
│   └── manufacturing_abc_example.md
│
├── mappings/                  # Explicit business logic, not left to guessing
│   ├── pain_to_feature.yaml   # Pain -> relevant product capabilities (with aliases)
│   ├── pain_to_demo.yaml      # Pain -> demo elements to show (with aliases)
│   └── objection_mapping.yaml # Common objection + competitive-vendor angles
│
├── knowledge/                 # Company/product facts Claude should treat as ground truth
│   ├── product_features.md
│   ├── case_studies.md
│   ├── customer_personas.md
│   ├── success_metrics.md
│   └── sizing_guidance.md     # Company size / site count -> tier suggestion
│
└── checklists/                 # Self-check before finishing
    ├── demo_checklist.md
    └── discovery_checklist.md
```

## Design principle: separation of concerns

- **SKILL.md** defines *how Claude should think* (role, workflow, rules). It should
  rarely need to change.
- **templates/** define *what the output looks like*. Edit these when your demo
  format changes.
- **mappings/** and **knowledge/** define *business facts* (which feature solves
  which pain, what case studies exist). Edit these when your product or proof
  points change — this is the most frequently updated folder.
- **playbooks/** capture *expert methodology* — the recommended flow and framing
  for a category of pain. Edit these as your sales methodology evolves.
- **examples/** exist purely to keep output style consistent via few-shot
  learning. Add a new example any time you see the output style drift.
- **checklists/** are a safety net, not the primary logic — they catch omissions,
  they don't drive the reasoning.

If a product feature changes: update `knowledge/` or `mappings/`, not `SKILL.md`.
If the demo structure changes: update `templates/`, not the reasoning logic.

## Placeholder content notice

The `mappings/`, `knowledge/`, `playbooks/`, and `examples/` files in this starter
kit are filled with **generic, illustrative product/feature names** (e.g. "SD-WAN",
"XDR", "Unified Dashboard") as placeholders. Before using this skill for real
customer-facing demos, replace these with your actual product names, real case
studies, and verified metrics — the skill explicitly avoids inventing facts not
found in these files, so it's only as accurate as what you put in them.
