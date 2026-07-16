# Worked Example 2 — CFO / Procurement Persona (same competitor as Example 1)

## User input

> "Same comparison, Flowly — but now write a short email for a procurement lead
> who's mostly focused on cost predictability. Keep it under 120 words."

## Claude's internal process (not shown to user)

1. Persona = CFO/Procurement → per persona map, prioritize economic
   differentiator type; avoid leading with architecture detail (on the "avoid" list for this persona).
2. From the same evidence base as Example 1, the rate-limit differentiator has
   an economic angle worth surfacing (avoiding forced upgrades = cost
   predictability) — reframe it accordingly rather than reusing the CTO framing verbatim.
3. Channel = email → `templates/email_snippet.md`, 80–120 word target.
4. Note: this is a clearly separate, labeled piece of copy from Example 1, per
   the "don't blend personas" rule — same underlying facts, different framing entirely.

## Output delivered to user

```
Subject: Keeping integration costs predictable as you scale

Hi [Name],

As you're comparing platforms, one thing worth flagging: Flowly's lower API
rate limits mean teams often hit a forced tier upgrade sooner than expected
once usage grows — ours ships with 10x the headroom on the standard tier, so
you're less likely to get an unplanned pricing conversation mid-contract.

Happy to send over a side-by-side on total cost at your expected usage volume
whenever useful — no pressure either way.

[Sign-off]
```

(103 words)

## Why this is a good output

- Same underlying fact (10x rate limits) as Example 1, but reframed entirely
  around cost predictability rather than architecture — correct persona adaptation.
- Did not lead with the SOC 2 or webhook differentiators here, since they're
  lower priority for this persona — selective, not exhaustive.
- Under the 120-word email target.
