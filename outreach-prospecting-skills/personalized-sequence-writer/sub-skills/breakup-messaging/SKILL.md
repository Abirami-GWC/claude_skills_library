---
name: breakup-messaging
description: >
  Sub-skill of personalized-sequence-writer. Writes the final "breakup" or exit
  touch of an outbound sequence — the message that signals this is the last
  outreach attempt. Use internally at Step 5 of the parent workflow, always for
  the last touch of any multi-touch sequence. Not intended to be triggered
  directly by end users.
---

# Breakup Messaging

## Purpose
Every sequence needs a deliberate, low-pressure exit. Sequences that just stop
(or that escalate pressure on the final touch) both perform worse and reflect
poorly on the sender's brand. A good breakup email sometimes outperforms every
other touch in the sequence because it removes all pressure and triggers loss-aversion
naturally, without manufacturing false urgency.

## Rules
- Explicitly (but politely) signal this is the last message in this sequence.
- Do not manufacture scarcity or urgency that isn't real ("this offer expires
  Friday" when it doesn't).
- Do not guilt-trip ("I guess this isn't a priority for you") — this damages
  brand perception and reflects poorly on the sender.
- Leave a clear, easy way for the prospect to re-engage on their own timeline.
- Keep it short — breakup emails should be among the shortest in the sequence.

## Pattern
```
Hi [First Name],

[Acknowledge, without guilt, that you haven't connected — e.g. "Haven't heard
back, so I'll assume now isn't the right time."]

[Optional: one line leaving the door open — "If that changes, happy to pick this
back up whenever works."]

[Very low-friction reply option, e.g. "Feel free to just reply 'not now' and I'll
close this out — or reach out anytime if this becomes relevant."]

[Sender]
```

## Common mistakes prevented
- Sequences that trail off with no final message, leaving the prospect relationship
  ambiguous.
- Breakup emails that use manipulative urgency or guilt.
- Breakup emails that are longer than earlier touches (they should be the shortest).
