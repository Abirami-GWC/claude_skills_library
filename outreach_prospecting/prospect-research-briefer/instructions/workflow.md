# Workflow: Building a Prospect Research Brief

## Step 1 — Scope the request
Confirm:
- Company name (required)
- Contact name/role (optional — can research company-only if no specific contact yet)
- What's being sold, so relevance framing is possible
- Any research already available from the user (documents, notes) — use these
  first before searching, since they may contain private/first-party context not
  publicly available.

## Step 2 — Company research
Use `sub-skills/company-research/SKILL.md`. Gather: what the company does, size,
stage, recent news, and structural signals (hiring, tech stack if discoverable).

## Step 3 — Contact research
Use `sub-skills/contact-research/SKILL.md`, if a specific contact was given.
Gather: role, tenure, relevant public content, likely priorities based on title.

## Step 4 — Signal detection
Use `sub-skills/buying-signal-detection/SKILL.md` to identify which pieces of
research constitute genuine trigger events / buying signals versus interesting-but-
irrelevant trivia. Rank by relevance to the offer.

## Step 5 — Structure and label
Assemble into `templates/briefing-doc-template.md`. For every factual line:
- If sourced from search/research tool or user-provided document → label as
  **Verified** with source noted.
- If inferred from role/industry pattern-matching with no direct source → label
  as **Likely / inferred** and explain the reasoning briefly.
- If searched for but not found → state plainly ("Could not find recent news on
  X") rather than omitting silently, so the user knows it was checked.

## Step 6 — Deliver
Default to a clean in-chat structured summary. Only produce a downloadable
document (via `scripts/generate_brief_docx.py` and the docx skill conventions) if
the user asks for a file to save/share — do not default to file creation for a
quick research request.

## Handoff
If the user's next ask is outreach copy, pass this brief's structured output
directly as input to `personalized-sequence-writer`, `cold-open-generator`, or
`linkedin-outreach-writer` rather than re-researching from scratch.
