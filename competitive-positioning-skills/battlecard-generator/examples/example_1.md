# Worked Example — Battlecard Generator

## User input

> "Build a battlecard for us vs. Acme EDR, mid-market NA. Deploy: cloud-only for
> them, we do cloud or on-prem. Pricing: ours is flat per-endpoint, theirs is
> tiered with advanced detection as an add-on (from their public pricing page).
> Our last 3 win/loss interviews said their rollout took multiple days for
> ~500-endpoint orgs; ours averages 15 minutes. I don't have anything on their
> support SLA — leave that out. Deliver as a Word doc for the team wiki."

## Claude's internal process (not shown to user)

1. Confirm scope: competitor = Acme EDR, segment = mid-market NA, format = docx.
2. Populate `knowledge/competitor_profile_schema.json`: two sourced strengths
   (brand recognition, integration marketplace — supplement only if user
   confirms; here user didn't supply strengths, so ask a quick follow-up rather
   than inventing them) — in this run, assume user supplied "they're
   well-known, strong integrations" when asked.
3. One weakness (rollout time) with landmine question, sourced to win/loss interviews.
4. Head-to-head: pricing model, deployment — both sourced.
5. No support SLA claim included, since no source was supplied — correctly
   omitted rather than guessed.
6. Run `scripts/generate_battlecard_docx.py` against the populated JSON.
7. Convert to PDF and check page count to confirm one-page fit before delivering.

## Output delivered to user

A one-page Word document (see `scripts/generate_battlecard_docx.py` for the
renderer) containing:

- Header: "Battlecard: Us vs. Acme EDR" — as of 2026-07-16, mid-market NA
- Snapshot table
- Their Strengths: brand recognition, integration marketplace
- Their Weaknesses: multi-day rollout for ~500-endpoint orgs, with the landmine
  question "How long did your last EDR rollout take?"
- Head-to-Head: pricing model, deployment
- Our Differentiators: 15-minute average deployment
- Objection Handling: "Acme is cheaper" → sourced reframe
- Talking Points: lead with time-to-value
- Do NOT Say: flagged claim about a false "zero finance customers" assertion
  that was previously walked back
- Footer: sources and confidence levels

Delivered as `battlecard-acme-edr.docx`, verified to be exactly one page via
PDF conversion before sending.

## Why this is a good output

- No support-SLA claim was fabricated to fill out the head-to-head table —
  correctly left out since no source was supplied.
- Strengths section wasn't skipped even though the user didn't proactively
  supply them — Claude asked rather than omitting the section.
- Verified page-fit programmatically instead of assuming the layout worked.
