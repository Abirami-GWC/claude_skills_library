---
name: cadence-strategy
description: >
  Sub-skill of personalized-sequence-writer. Determines touch count, spacing
  (day offsets), and channel mix for an outbound sequence based on deal size,
  persona seniority, and warm/cold status. Use internally at Step 2 of the
  parent workflow before any copy is drafted. Not intended to be triggered
  directly by end users.
---

# Cadence Strategy

## Purpose
Prevent two common failure modes: (1) using the same 5-touch/12-day cadence for
every deal size and persona regardless of fit, and (2) drafting copy before
timing/channel decisions are made, which forces awkward retrofitting later.

## Inputs needed
- Approximate deal size / ACV (ask if unknown; a rough band is enough)
- Persona seniority (IC, manager, director, VP, C-level)
- Warm or cold (any existing signal: content download, intro, event, or fully cold)
- Whether multi-channel (LinkedIn, call) is in scope

## Decision logic
1. Look up deal-size band in `knowledge/timing-rules.md`.
2. Adjust touch count down by 1-2 if persona is VP/C-level.
3. Adjust touch count up by 1 if warm signal exists (justifies extra touches since
   engagement likelihood is higher).
4. If multi-channel requested, insert LinkedIn/call touches per the mixed-cadence
   pattern in the parent skill's `references/channel-cadence-guide.md` — do not
   invent a new pattern here.
5. Output: a simple day-offset list (e.g., "Day 0, 3, 7, 12, 18") and per-touch
   channel tag, handed to the parent workflow before drafting begins.

## Common mistakes prevented
- Using an SMB cadence (fast, high-touch) on an enterprise deal, which reads as
  pushy to senior buyers.
- Cramming a C-level sequence into too many touches, burning goodwill.
- Deciding channel mix mid-draft instead of upfront, causing inconsistent pacing.
