# Workflow: LinkedIn Outreach

## Step 1 — Classify the request
- **Cold connection request**: no prior relationship/context.
- **Warm connection request**: mutual connection, shared group, event, or the
  prospect engaged with the sender's/company's content.
- **Post-connection DM**: already connected, writing the message sequence.
- **Mixed-channel touch**: this is one touch within a larger sequence built by
  `personalized-sequence-writer` — check what day/position it falls at and match
  tone accordingly (e.g., don't repeat the exact hook already used in an email touch).

## Step 2 — Connection request (if applicable)
Hand off to `sub-skills/connection-request-writer/SKILL.md`. Key constraint:
150-300 characters, one sentence, no pitch.

## Step 3 — DM sequence (if applicable)
Hand off to `sub-skills/dm-sequence-writer/SKILL.md`. Typically 2-4 messages:
1. Post-connect acknowledgment + continue the thread from the connection note.
2. Value/insight message (similar spirit to the "give touch" in email sequences,
   but shorter and more conversational).
3. Soft ask.
4. Optional light breakup if no response.

## Step 4 — Validate
- Check character counts against `knowledge/linkedin-character-limits.json`.
- Cross-check tone against `knowledge/platform-etiquette.md` — flag anything that
  reads as too formal (email-register) or too salesy for a first message.
- If code execution is available, run `scripts/char_limit_check.py` on drafted copy.

## Step 5 — Deliver
Use `templates/dm-sequence-template.md` format. Always note character count next
to each connection request note so the user can see it fits the limit at a glance.
