# demo-recap-writer

Turns raw post-demo meeting notes (customer, attendees, topics, questions,
requested documents, next meeting) into a professional, company-standard
follow-up email.

## Folder structure

```
demo-recap-writer/
│
├── SKILL.md                    # Main instructions: role, workflow, rules
├── README.md                    # This file
│
├── templates/
│   └── followup_email.md        # Standard email structure Claude fills in
│
├── knowledge/
│   └── email_guidelines.md       # Company communication/writing standards
│
└── examples/
    └── examples.md                # Worked examples: full notes, minimal notes, missing next-meeting date
```

## How it works

1. Extract discussion topics, questions, requested documents, next meeting
   details, and any other explicit action items from the pasted notes.
2. Apply `knowledge/email_guidelines.md` — tone, length (under 300 words),
   structure, and signature conventions.
3. Fill `templates/followup_email.md`.
4. Use `examples/examples.md` for consistency, especially on edge cases
   (missing name, missing next meeting, no questions asked).

## Where this fits in the flow

```
Discovery Call → Discovery-to-Demo Mapper → Pain-Based Demo Builder →
Narrative-Deck Builder → Customer Demo → 🟢 demo-recap-writer
```

This is the only skill in the set that runs **after** the customer meeting.
Its job is to document what happened and keep the sales process moving —
not to prepare content for a future meeting.

## Placeholder content notice

`templates/followup_email.md` uses `[Sales Representative Name]` as a
placeholder signature — either have the rep fill this in before sending, or
extend the skill to accept a rep name as an input field if you want it fully
automated.
