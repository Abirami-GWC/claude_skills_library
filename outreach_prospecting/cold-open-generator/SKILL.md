---
name: cold-open-generator
description: >
  Generates non-templated, specific opening lines (the first 1-2 sentences of a
  cold email, LinkedIn message, or call script) drawn directly from prospect
  research rather than generic flattery or mail-merge tokens. Use this skill when
  the user asks specifically for an "opener," "opening line," "hook," "icebreaker,"
  or says an existing draft's opening "sounds generic" / "sounds like a template" /
  "doesn't stand out." Also trigger when the user pastes prospect research (news,
  LinkedIn bio, company info) and asks "what should I open with?" or "how do I
  start this email?" This skill produces ONLY the opening hook, not a full
  email/message — use `personalized-sequence-writer` for a full sequence or
  `linkedin-outreach-writer` for full LinkedIn copy, and call this skill from
  within those workflows when just the hook needs sharpening.
---

# Cold Open Generator

## Overview
The opening line of a cold outreach message determines whether the rest gets
read. This skill's sole job is producing sharp, specific, non-cliché opening
lines by pattern-matching real research signals to proven opener formulas — and
explicitly rejecting generic flattery openers ("I saw you're doing great things
at X!", "Hope you're having a great week!") which read as templated regardless of
how personalized the rest of the message is.

## Purpose
- Turn raw prospect research into 3-5 candidate opening lines per request, ranked
  by specificity/strength.
- Enforce a hard rule against generic-flattery and banned-cliché openers.
- Work as a standalone tool (user pastes research, gets openers back) or as a
  sub-routine called by `personalized-sequence-writer` / `linkedin-outreach-writer`
  when their touch-1 hook needs strengthening.

## When to use this Skill
- User explicitly asks for opener/hook/icebreaker lines.
- User says a draft's opening feels generic, weak, or templated.
- User pastes research (news, bio, job posting, content) and asks how to start a message.
- Called internally by other outreach skills needing a stronger touch-1 opener.

## When not to use this Skill
- User wants a full email or sequence — use `personalized-sequence-writer`.
- User wants a full LinkedIn message — use `linkedin-outreach-writer`.
- User wants research gathered from scratch (no signals given at all and no
  research tool available) — first route to gathering research
  (`prospect-research-briefer`) since this skill needs real signals as input, not
  a blank slate.

## Workflow
See `instructions/workflow.md` for full detail. Summary:
1. Identify available signals from what the user provided (or gather via search
   tools if available and appropriate).
2. Match signals to opener formulas in `templates/opener-formulas.md`.
3. Draft 3-5 candidate openers, each using a different formula/angle.
4. Screen every candidate against `knowledge/banned-cliches.txt` and
   `scripts/cliche_checker.py`.
5. Rank candidates by specificity (a good test: could this line be sent to any
   other company unchanged? If yes, it's disqualified) and present with a
   one-line rationale each.

## Best Practices
- Every opener must fail the "copy-paste test": if it would make equal sense sent
  to a different company, it is not specific enough.
- Prefer openers that reference something the prospect did/said/published over
  openers that reference something about their company in the abstract (funding,
  headcount) — individual signals read as more genuinely researched.
- Keep openers to one sentence, two at most.
- Do not open with the sender's name/company/credentials — the opener is about
  the prospect, not the sender.

## Rules and Limitations
- Never fabricate a specific fact (an article they didn't write, an event they
  didn't attend) to manufacture a stronger opener — this is a trust-destroying
  failure if noticed.
- Never use flattery as the entire content of an opener ("Loved your LinkedIn
  post!" with no substance beyond that).
- Do not produce openers built on sensitive personal information not clearly
  public/professional in nature (health, family, personal life details even if
  technically discoverable) — stay within professional/business-relevant signals.

## References
- `instructions/workflow.md` — full step-by-step process
- `knowledge/opener-patterns.md` — formula catalog with when-to-use guidance
- `knowledge/banned-cliches.txt` — phrases to never produce
- `templates/opener-formulas.md` — fill-in-the-blank formula templates
- `examples/examples.md` — worked examples, good vs. bad
- `scripts/cliche_checker.py` — automated cliché/genericness screen
- `resources/research-signal-types.json` — structured signal taxonomy (shared
  concept with `personalized-sequence-writer/knowledge/personalization-tokens.json`,
  scoped here to opener-relevant signals only)

## Common Mistakes This Skill Prevents
- Producing generic-flattery openers dressed up as personalization.
- Reusing the same opener formula for every candidate instead of offering variety.
- Fabricating specific facts to force a stronger-sounding opener.
- Openers that are really about the sender ("I'm reaching out because we help...")
  rather than about the prospect.
