---
name: email-sequence-writer
description: Generate complete, strategically-sequenced email marketing sequences (welcome series, lead nurture, onboarding, re-engagement, drip campaigns, promotional/launch sequences) including subject lines, preview text, body copy, and CTA progression. Use this skill whenever the user asks for an email sequence, email series, email flow, email campaign, drip campaign, welcome emails, nurture emails, onboarding emails, win-back/re-engagement emails, cart-abandonment emails, or a multi-email strategy — even if they only ask for "a few emails" or "an email flow" rather than explicitly saying "sequence." Also use it for improving, expanding, or diagnosing an existing email sequence's structure, subject lines, or CTA logic. Do not use this skill for a single one-off transactional email, for brand voice/tone rewrites of already-written copy (use brand-voice-writer), for paid ad copy (use ad-copy-generator), or for landing page copy (use landing-page-copywriter).
---

# Email Sequence Writer

## Purpose

Produce complete, multi-email marketing sequences that move a recipient from one psychological/behavioral state to another (stranger → subscriber → customer → advocate, or dormant → re-engaged). Each sequence is built as a system of emails with a shared strategic arc, not a batch of disconnected messages.

## Business Value

- Turns one-off "write an email" requests into a coherent revenue- or retention-driving system
- Encodes proven sequence architectures (welcome, nurture, onboarding, win-back, launch, cart-abandon) so strategy doesn't have to be reinvented each time
- Increases open/click/conversion rates through tested subject-line and CTA frameworks
- Produces sequences that are ready to load into any ESP (email service provider) with minimal editing

## Activation Conditions

Use this skill when the user's request involves:
- Multiple emails that build on each other over time
- A named sequence type: welcome, nurture, onboarding, drip, re-engagement/win-back, cart abandonment, post-purchase, launch/promotional
- A funnel stage description ("emails to convert trial users," "emails after someone downloads my lead magnet")
- Subject line + body + CTA generation across more than one email
- Diagnosing or improving an existing multi-email flow

### Trigger Examples
- "Write a 5-email welcome sequence for new subscribers to my newsletter."
- "I need a cart abandonment flow for my Shopify store."
- "Create an onboarding email series for new SaaS trial users."
- "Give me a win-back campaign for customers who haven't purchased in 6 months."
- "Draft a 7-day product launch email sequence."
- "My nurture sequence isn't converting — can you review and rewrite it?"

### When NOT To Use
- A single standalone transactional or announcement email → handle directly, no skill needed
- Pure tone/voice rewriting of existing copy with no sequencing involved → brand-voice-writer
- Paid social/search ad copy → ad-copy-generator
- Website or landing page copy → landing-page-copywriter
- General marketing strategy unrelated to email → handle directly

## Scope

In scope: sequence architecture, subject lines, preview text, body copy, CTA progression, send-timing recommendations, segmentation notes.
Out of scope: ESP-specific technical implementation (Zapier/HTML/merge-tag syntax beyond standard `{{first_name}}`-style placeholders), deliverability/spam-compliance auditing, A/B test statistical analysis.

## Inputs

Required (ask only if truly missing and blocking):
- Sequence type/goal (e.g., welcome, nurture, win-back)
- Audience/persona
- Product or offer being promoted (if any)
- Number of emails or desired sequence length (default to the standard length for that sequence type if unspecified — see `references/email_sequence_frameworks.md`)

Helpful but optional:
- Brand voice/tone reference
- Existing subject line or open-rate data
- Sending cadence constraints
- CTA/destination (signup, purchase, book a call, etc.)

## Outputs

- A complete sequence: for each email, subject line (+1-2 alternates), preview text, body copy, single clear CTA
- A one-line note per email on its strategic role in the arc (e.g., "Email 2: build trust with social proof")
- Recommended send-timing/cadence
- Optional: subject line A/B variants for the most critical emails (first email, final conversion email)

## Workflow

1. **Identify sequence type** from the request; if ambiguous, ask one clarifying question or infer the most likely type and state the assumption.
2. **Select the architecture** from `references/email_sequence_frameworks.md` matching that sequence type (number of emails, purpose of each step, typical cadence).
3. **Gather inputs**: audience, offer, tone, any constraints. Use `templates/templates.md` (Email Sequence Brief) as the mental checklist.
4. **Draft the arc** — one sentence per email describing its job in the sequence before writing full copy, so each email has a distinct, non-redundant purpose.
5. **Write each email**: subject line (use `references/subject_line_playbook.md`), preview text, body (use `references/email_copywriting_frameworks.md` for structure — AIDA/PAS/StoryBrand as fits), single CTA (use `references/cta_best_practices.md`).
6. **Sanity-check the whole sequence** against `checklists/checklists.md` — no duplicate CTAs doing the same job, no redundant subject lines, logical narrative progression, cadence makes sense.
7. **Deliver** the full sequence with per-email strategic notes and cadence recommendation.

## Reasoning Guidelines

- Every email must earn its place: if two emails could be merged without losing a distinct psychological beat, merge them.
- Escalate commitment gradually — don't ask for the sale in email 1 of a cold nurture sequence.
- Subject lines should feel like they're from a person, not a brand — avoid ALL CAPS, excessive punctuation, and generic marketing language.
- Preview text should extend the subject line's curiosity, never repeat it.
- One CTA per email. Multiple competing CTAs measurably reduce conversion.
- Match urgency/scarcity language to genuine constraints; avoid manufactured urgency for evergreen sequences.

## Best Practices

- Default to the shortest sequence length that can accomplish the stated goal; longer isn't automatically better.
- Personalize the opening line beyond `{{first_name}}` where possible — reference the specific trigger event (signup, cart abandon, trial start).
- Vary email length: not every email should be long-form; skimmable short emails often outperform in the middle of a sequence.
- Write mobile-first: front-load the value in the first two lines since most email is read on mobile.

## Validation Rules

Before delivering, confirm:
- [ ] Sequence length matches the stated or inferred goal
- [ ] Each email has exactly one CTA
- [ ] No two subject lines are near-duplicates
- [ ] The arc shows clear progression (not repetition) of the core message
- [ ] Tone is consistent across all emails in the sequence

## Error Handling

- If sequence type is unclear, infer the closest standard type from `references/email_sequence_frameworks.md` and state the assumption rather than blocking on a clarifying question.
- If no product/offer is given for a promotional sequence, ask once for the offer since copy cannot be written without it.
- If brand voice isn't specified, default to a warm, direct, conversational B2C or professional-but-human B2B tone based on context clues, and note the assumption.

## Limitations

- Does not send or schedule emails — output is copy only.
- Does not guarantee deliverability or inbox placement; that depends on ESP configuration and sender reputation.
- Cannot verify real open/click data; recommendations are based on established copywriting and lifecycle-marketing principles, not the user's live analytics unless supplied.

## Success Criteria

A successful output is a complete, ready-to-send sequence where each email has a distinct strategic role, subject lines earn opens without being clickbait, CTAs are singular and clear, and the sequence as a whole moves the recipient logically toward the stated goal.
