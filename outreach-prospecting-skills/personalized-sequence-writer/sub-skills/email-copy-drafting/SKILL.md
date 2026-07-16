---
name: email-copy-drafting
description: >
  Sub-skill of personalized-sequence-writer. Handles the actual copywriting of
  individual sequence touches (subject lines and bodies) once cadence and
  personalization signals are decided. Use internally at Steps 3-4 of the parent
  workflow. Not intended to be triggered directly by end users, though it can be
  reused any time short, plain-text B2B email copy needs to be drafted with a
  specific angle.
---

# Email Copy Drafting

## Purpose
Provide consistent copywriting patterns so touches read as human-written,
plain-text emails rather than marketing copy — this is what separates replies
from silent deletes in cold outbound.

## Subject line patterns
- Specific + lowercase-feeling: "the eng hiring push at acme"
- Question-form: "worth 10 minutes on your ETL setup?"
- Reference-based (for touch 2+): "re: [topic from touch 1]" — only use "re:" if
  genuinely continuing the same thread, never as a deceptive open-rate trick.
- Avoid: generic ("Quick question"), hypey ("Revolutionize your..."), or anything
  matching `resources/spam-trigger-words.txt` in the parent skill.

## Body patterns
See `templates/email-templates.md` for full structures. Core rules:
- Open with the prospect/their company, not "I hope this finds you well" or "My
  name is X and I work at Y."
- One idea per email. Resist the urge to list three value props.
- Write at a reading level and tone a busy person would actually text a colleague
  in — contractions are fine, sentence fragments are fine.
- End with one CTA, phrased as a question where possible ("Worth a look?" beats
  "Let me know if you'd like to schedule a call.").

## Worked pattern — see `examples/` for full samples
1. Hook (1 sentence, specific)
2. Bridge (1 sentence connecting hook to their likely problem)
3. Value (1 sentence on the offer, tied to outcome not features)
4. CTA (1 sentence, low-friction)

## Common mistakes prevented
- Emails that read as press releases about the sender's company instead of being
  about the prospect.
- Multiple CTAs in one email diluting the ask.
- Subject lines that trigger spam filters or look like mass-mail blasts.
- Overly long touch-1 emails that bury the hook under company background.
