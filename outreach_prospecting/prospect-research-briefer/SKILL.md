---
name: prospect-research-briefer
description: >
  Produces a structured pre-outreach research brief on a target company and/or
  contact — summarizing company context, recent events/signals, the contact's
  role and background, and likely relevant pain points — so a rep can personalize
  outreach or prep for a call. Use this skill when the user asks to "research this
  company/prospect," "give me a briefing on [company/person] before I reach out,"
  "prep me for a call with [company]," or provides a company/contact name and
  asks "what should I know before contacting them?" This skill produces research
  and a summary ONLY — it does not draft outreach copy. Route to
  `personalized-sequence-writer`, `cold-open-generator`, or
  `linkedin-outreach-writer` for the actual message copy, using this skill's
  output as their research input.
---

# Prospect Research Briefer

## Overview
Good personalized outreach depends on good research. This skill's job is to
gather and structure that research into a clean, scannable brief before any
copywriting happens — separating the research task (verifiable facts, "what do we
actually know") from the writing task (how to use those facts persuasively),
which keeps outreach copy grounded in real information rather than invented
plausible-sounding detail.

## Purpose
- Produce a structured brief covering company context, contact context, recent
  signals/trigger events, and likely relevant pain points.
- Clearly separate verified facts (with source) from inferred/likely context
  (role-based reasoning, industry pattern-matching).
- Hand off a clean, structured input that other outreach skills can use directly.

## When to use this Skill
- User asks for research/briefing/prep on a specific company or contact before outreach.
- User provides a company or contact and wants "what should I know before reaching out."
- Called internally by `personalized-sequence-writer` or `cold-open-generator` when
  they need real signals and none have been supplied yet.

## When not to use this Skill
- User wants outreach copy written, not research — route to the appropriate
  outreach skill (this skill can still be run first as an input step).
- User wants general company financial/investment research unrelated to
  prospecting outreach — that's a different research task with different
  standards of rigor (this skill is not built for investment-grade due diligence).
- Research would require accessing non-public, personal, or sensitive personal
  data about an individual — stay within professional/public-business information.

## Workflow
See `instructions/workflow.md`. Summary:
1. Confirm what's already known vs. what needs to be researched (company name,
   contact name/role, product/offer for relevance framing).
2. Gather company-level research using `sub-skills/company-research/reference.md`.
3. Gather contact-level research using `sub-skills/contact-research/reference.md`.
4. Identify buying/trigger signals using `sub-skills/buying-signal-detection/reference.md`.
5. Structure the output into `templates/briefing-doc-template.md`, clearly
   labeling verified vs. inferred information and citing sources for verified facts.

## Best Practices
- Every factual claim in the brief should be traceable to a source (a search
  result, a provided document, a stated date) — do not present inferred/likely
  information as verified fact.
- Keep the brief scannable: a rep should be able to read it in under 2 minutes
  before a call.
- Flag anything time-sensitive (e.g., "as of [date]") since company context
  changes quickly (headcount, funding stage, leadership).
- Prioritize signals with clear relevance to the offer over generic company trivia.

## Rules and Limitations
- Do not include personal information unrelated to the professional/business
  context (family, health, personal life, political/religious affiliation) even
  if technically discoverable.
- Do not present unverified information as fact; always label inference vs.
  verified fact and note the source for verified claims.
- Do not fabricate facts, sources, or citations if research tools are unavailable
  or return nothing — say plainly what could not be found.
- Respect that this brief is an input to a human decision process, not a
  surveillance dossier — keep scope limited to what's genuinely useful for a
  legitimate business outreach conversation.

## References
- `instructions/workflow.md`
- `knowledge/research-sources.md` — where to look and what each source is good for
- `knowledge/signal-taxonomy.json` — structured signal categories (shared concept
  with `personalized-sequence-writer` and `cold-open-generator`, this is the
  canonical/most detailed version)
- `templates/briefing-doc-template.md` — output structure
- `examples/examples.md`
- `scripts/generate_brief_docx.py` — optional: renders a brief into a Word
  document for sharing (uses the docx skill's conventions; only run this when the
  user wants a downloadable file, not for a normal chat response)
- `sub-skills/company-research/reference.md`
- `sub-skills/contact-research/reference.md`
- `sub-skills/buying-signal-detection/reference.md`

## Common Mistakes This Skill Prevents
- Producing outreach copy based on invented "research" that sounds plausible but isn't real.
- Mixing verified facts and inferred guesses without labeling which is which.
- Overly broad research (financial deep-dives, personal life details) that isn't
  relevant to a legitimate prospecting conversation and raises privacy concerns.
- Stale information presented without a date/timeframe caveat.
