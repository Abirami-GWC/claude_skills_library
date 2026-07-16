---
name: dm-sequence-writer
description: >
  Sub-skill of linkedin-outreach-writer. Writes the post-connection DM sequence
  (typically 2-4 messages) once a LinkedIn connection has been accepted. Use
  internally at Step 3 of the parent workflow. Not intended to be triggered
  directly by end users.
---

# DM Sequence Writer

## Purpose
Once connected, the goal shifts from "earn the accept" to "build enough context
and trust to get a reply/meeting" — but LinkedIn DMs stay shorter and more
conversational than email touches even as the sequence progresses.

## Sequence pattern (2-4 messages)
1. **Acknowledge + continue thread** — sent right after accept. References the
   connection note's reason, doesn't pitch yet.
2. **Value/insight message** — shares something useful or asks a genuine follow-up
   question tied to their situation. Still light-touch.
3. **Soft ask** — this is where the actual reason for reaching out can surface,
   framed as a question/offer rather than a hard pitch.
4. *(Optional)* **Light breakup** — shorter than the email breakup pattern; a
   single line is often enough on this platform.

## Length guidance
Keep each DM under ~500 characters / ~80-100 words — see
`../../knowledge/linkedin-character-limits.json` for the full limit reference.
Longer messages read as an email pasted into the wrong app.

## Common mistakes prevented
- Pitching in DM 1 immediately after connecting, before any relationship context.
- Writing DMs at email length/formality instead of matching platform norms.
- Skipping the breakup message, leaving the thread to trail off unresolved.
