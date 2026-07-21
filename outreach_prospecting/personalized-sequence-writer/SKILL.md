---
name: personalized-sequence-writer
description: >
  Builds multi-touch outbound sales sequences (email, and optionally mixed-channel
  with LinkedIn/call touches) that are personalized per target account rather than
  templated. Use this skill whenever the user asks to write a "sequence," "cadence,"
  "outbound campaign," "drip campaign," "follow-up series," or "email flow" for
  prospecting/outbound sales — including requests like "write me a 5-touch sequence
  for VP Engineering personas," "build an outbound cadence for our Q3 ABM list,"
  "I need follow-up emails for prospects who didn't reply," or "draft a sequence for
  [company/persona]." Trigger this skill even if the user only supplies a single
  example prospect and asks for "an email" — if the underlying need is a
  multi-touch, spaced-out follow-up series (not a single one-off email), this is
  the right skill. Do NOT use this skill for a single standalone cold email with no
  follow-ups (write it directly), for LinkedIn-only sequences (use
  linkedin-outreach-writer), or for post-reply/deal-stage nurture emails to accounts
  already in active conversation (that is relationship management, not prospecting).
---

# Personalized Sequence Writer

## Overview
This skill produces multi-touch outbound sequences (typically 3-7 touches across
7-21 days) where each touch is written from real, per-account research rather than
a mail-merge template with `{{first_name}}` swapped in. The differentiator versus a
generic "write a cold email" request is twofold: (1) the sequence has a deliberate
**cadence** — timing, escalating specificity, and a graceful exit — and (2) each
touch demonstrably reflects something true and specific about *that* account.

## Purpose
Give Claude a repeatable, quality-controlled process for:
1. Extracting or requesting the account/persona signals needed for real personalization.
2. Selecting a cadence structure appropriate to deal size, ICP, and channel mix.
3. Drafting each touch with a distinct angle (not just a shorter version of touch 1).
4. Validating the sequence against deliverability, tone, and spam-trigger rules
   before handing it back.

## When to use this Skill
- User asks for a "sequence," "cadence," "outbound campaign," "drip," or "follow-up series."
- User provides a list of accounts/contacts and wants outbound copy for each.
- User wants A/B variants of a sequence for testing.
- User references SDR/BDR outbound motion, ABM (account-based marketing) campaigns,
  or "book a meeting" / "get a reply" as the goal.

## When NOT to use this Skill
- A single one-off cold email with no planned follow-up → write directly, no sequence needed.
- LinkedIn-only touches → route to `linkedin-outreach-writer`.
- Only the opening line/hook is needed → route to `cold-open-generator`, or use
  `sub-skills/email-copy-drafting/reference.md` directly if already inside a sequence build.
- The prospect has already replied or is mid-deal → this is account management /
  customer communication, not prospecting outreach; do not use this skill.
- User wants raw research on a company/contact with no copy attached →
  `prospect-research-briefer`.

## Workflow
Full step-by-step logic lives in `instructions/workflow.md`. Summary:

1. **Gather inputs.** Confirm: target persona(s), product/offer, proof points
   allowed to cite, number of touches wanted (default 5 if unspecified), channel
   mix (default: email-only unless mixed cadence requested), and any research
   already available (docs, call notes, prospect-research-briefer output).
   If personalization signals are missing, ask for them or, if research tools are
   available, gather them — do not fabricate specific facts about a real company.
2. **Choose a cadence.** Use `references/channel-cadence-guide.md` and
   `sub-skills/cadence-strategy/reference.md` to pick touch count, spacing, and escalation logic
   based on deal size and audience seniority.
3. **Draft touch 1 (the specific one).** This carries the heaviest personalization
   burden. See `sub-skills/email-copy-drafting/reference.md`.
4. **Draft touches 2-N with distinct angles**, not restatements — each touch should
   introduce a new reason to reply (proof point, resource, question, peer example).
   Never write "just following up" or "circling back" as the entire content of a touch.
5. **Draft the breakup/final touch** using `sub-skills/breakup-messaging/reference.md` — always
   include a graceful, low-pressure exit on the last touch.
6. **Validate.** Run the sequence against `instructions/validation-rules.md` and, if
   code execution is available, `scripts/validate_sequence.py` (checks length, spam
   trigger words, subject line duplication, and touch-to-touch repetition).
7. **Deliver** using the format in `templates/sequence-brief-template.yaml` (subject
   lines, body copy, send-day offsets, and a one-line "why this angle" note per touch
   so the user can sanity-check the personalization logic).

## Best Practices
- Personalization must be **load-bearing** — remove it and the email should no
  longer make sense for any other company. Generic flattery ("I saw you're growing
  fast!") is not personalization.
- Keep touch 1 body under ~120 words; brevity signals a human wrote it.
- Vary CTA weight across the sequence: soft curiosity question early, clearer ask
  mid-sequence, binary/easy-yes ask near the end.
- Never invent specific facts (funding amounts, exec names, product launches) about
  a real company — verify via research tools/user input, or keep the claim general.
- Write in the person's/brand's stated voice if known; default to plain, direct,
  non-hypey B2B tone otherwise.

## Rules and Limitations
- Do not generate sequences designed to evade spam filters through deceptive
  subject lines (e.g., fake "Re:" prefixes, fake meeting confirmations).
- Do not impersonate a real, named individual's writing voice without the user
  confirming they are that person or are authorized to write on their behalf.
- Do not fabricate case studies, customer names, or statistics — flag placeholders
  clearly (e.g., `[CUSTOMER NAME — confirm before sending]`) if the user hasn't
  supplied real proof points.
- Cap at 7 touches by default; more requires explicit user confirmation, since
  longer cadences risk diminishing reply quality and deliverability reputation.

## References
- `instructions/workflow.md` — detailed step-by-step build process
- `instructions/validation-rules.md` — pre-delivery QA checklist
- `references/channel-cadence-guide.md` — cadence timing by deal size/persona
- `knowledge/sequence-frameworks.md` — named frameworks (e.g., PAS, before/after/bridge) and when to use each
- `knowledge/personalization-tokens.json` — structured list of signal types to look for per account
- `knowledge/industry-benchmarks.csv` — reference reply-rate benchmarks by touch count/industry
- `templates/sequence-brief-template.yaml` — output format
- `templates/4-touch-email-sequence.md` — ready starting skeleton
- `scripts/validate_sequence.py` — automated QA checks
- `resources/spam-trigger-words.txt` — words/phrases to avoid in subject lines
- `sub-skills/cadence-strategy/reference.md` — timing and escalation logic
- `sub-skills/email-copy-drafting/reference.md` — per-touch copywriting patterns
- `sub-skills/breakup-messaging/reference.md` — final-touch/exit copy patterns

## Common Mistakes This Skill Prevents
- Writing 5 emails that are all the same email getting shorter (no new angle per touch).
- Treating "personalization" as name/company mail-merge only.
- Forgetting a breakup email, leaving the sequence to just fizzle out.
- Overloading touch 1 with the full pitch instead of one sharp reason to engage.
- Using spam-flagged subject line patterns that hurt inbox placement.
- Fabricating specific, checkable facts about a real prospect company.
