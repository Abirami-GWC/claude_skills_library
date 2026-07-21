---
name: linkedin-outreach-writer
description: >
  Writes LinkedIn connection request notes and follow-up DM sequences for
  prospecting outreach, respecting LinkedIn's character limits and platform norms
  (which differ meaningfully from email — shorter, more casual, no subject line,
  higher scrutiny for anything that reads as a sales pitch). Use this skill when
  the user asks to write a "connection request," "LinkedIn message," "InMail,"
  "LinkedIn DM," or "LinkedIn outreach," or wants to adapt an email sequence for
  LinkedIn. Also trigger when a mixed-channel sequence built by
  personalized-sequence-writer calls for a LinkedIn touch. Do NOT use this skill
  for email copy (use personalized-sequence-writer or cold-open-generator), or for
  LinkedIn content marketing/thought-leadership posts (that is content creation,
  not outbound prospecting).
---

# LinkedIn Outreach Writer

## Overview
LinkedIn outreach has different constraints than email: a 300-character limit on
connection request notes, no subject line, an inherently more casual/social
register, and a platform culture where an overtly salesy first message gets
ignored or reported. This skill produces LinkedIn-native copy respecting those
constraints, split into two natural stages handled by its sub-skills: the
connection request note, and the DM sequence that follows after connection.

## Purpose
- Draft connection request notes under the character limit that earn an accept.
- Draft a short DM follow-up sequence (typically 2-4 messages) once connected.
- Keep tone platform-appropriate: shorter, more conversational, less "email voice."
- Coordinate with `personalized-sequence-writer` when LinkedIn is one channel in a
  larger mixed-channel cadence, without duplicating that skill's cadence logic.

## When to use this Skill
- Direct requests for LinkedIn connection notes, DMs, or InMail copy.
- A mixed-channel sequence (built via `personalized-sequence-writer`) specifies a
  LinkedIn touch — this skill supplies that touch's actual copy.
- User wants to adapt existing email copy "for LinkedIn."

## When not to use this Skill
- Email copy → `personalized-sequence-writer` / `cold-open-generator`.
- LinkedIn thought-leadership or content posts (not 1:1 outreach) → out of scope.
- Cadence/timing decisions for a multi-channel sequence → handled by
  `personalized-sequence-writer/sub-skills/cadence-strategy/reference.md`; this skill only
  writes the LinkedIn-specific copy once timing is decided.

## Workflow
See `instructions/workflow.md`. Summary:
1. Confirm whether this is a cold connection request, a warm one (mutual
   connection, shared group, engaged with content), or a post-connection DM.
2. If a connection request: draft the note using
   `sub-skills/connection-request-writer/reference.md`, respecting the 300-character limit.
3. If a DM sequence: draft 2-4 messages using `sub-skills/dm-sequence-writer/reference.md`,
   each shorter and more conversational than email equivalents.
4. Validate character limits and platform-appropriateness using
   `knowledge/platform-etiquette.md` and, if available, `scripts/char_limit_check.py`.

## Best Practices
- Connection request notes: 150-300 characters, one sentence, one specific reason
  for connecting — never pitch in the connection note itself.
- First DM after connecting should NOT immediately pitch — acknowledge the
  connection and continue the specific thread from the connection note.
- Keep sentences short; LinkedIn messages read more like texts than emails.
- No formal salutations ("Dear," "Best regards") — use a natural, direct register.
- Emoji: use sparingly if at all, only if it matches the user's stated brand voice.

## Rules and Limitations
- Hard limit: connection request notes must fit LinkedIn's character limit — see
  `knowledge/linkedin-character-limits.json` for current known limits and always
  flag to the user that platform limits can change and are worth double-checking.
- Never draft a connection request that pitches a product/service directly — this
  reads as spam and hurts accept rates and account standing.
- Do not encourage or draft mass, unpersonalized connection requests at volumes
  that would violate LinkedIn's platform terms (e.g., explicit automation/scraping
  requests) — this skill writes copy for individual, human-sent outreach.

## References
- `instructions/workflow.md`
- `knowledge/linkedin-character-limits.json` — platform character limits by message type
- `knowledge/platform-etiquette.md` — tone/etiquette norms specific to LinkedIn
- `templates/dm-sequence-template.md`
- `examples/examples.md`
- `scripts/char_limit_check.py`
- `sub-skills/connection-request-writer/reference.md` — connection note copywriting
- `sub-skills/dm-sequence-writer/reference.md` — post-connect DM sequence copywriting

## Common Mistakes This Skill Prevents
- Connection requests that exceed the character limit and get truncated or rejected by the form.
- Pitching in the connection request note itself.
- Using email-register formality ("Dear Sir/Madam") on a platform where it reads as odd.
- Immediately pitching in the first DM instead of continuing the relationship naturally.
