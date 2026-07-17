# Worked Example 2 — Interactive Calculator Lead Magnet

## User input

> "Build us a support cost savings calculator. Inputs: tickets per month,
> current cost per ticket, and expected reduction percentage from switching
> to us. Formula: tickets_per_month × cost_per_ticket × (reduction_pct/100) ×
> 12 for annual savings. Output: estimated annual savings in dollars."

## Claude's internal process (not shown to user)

1. Format: calculator (user-specified). This is the highest-risk lead-magnet
   type per SKILL.md, so Step 3a applies: the user has explicitly supplied
   the exact formula and inputs — good, this satisfies the confirmation gate.
   No need to ask further, since the formula, inputs, and output are all
   already fully specified.
2. Build the spec JSON matching `scripts/build_calculator_html.py`'s expected format.
3. Run the script — it validates the formula only uses declared input ids and
   arithmetic operators (passes).
4. Test with the default sample inputs (500 tickets, $12/ticket, 30%
   reduction) and confirm the computed result (500 × 12 × 0.30 × 12 =
   $21,600) matches manual calculation before delivering.
5. Draft accompanying landing page copy per
   `references/gating_and_conversion_best_practices.md`'s calculator-specific
   note: since this is a simple 3-input calculator, recommend showing the
   result ungated and gating only a "get the detailed breakdown emailed to
   you" follow-up, rather than gating the whole tool — flagged as a
   recommendation, not assumed.

## Output delivered to user

- A working `support-savings-calculator.html` file (see
  `scripts/build_calculator_html.py`), verified to compute $21,600 for the
  default inputs, matching the user's formula exactly
- Landing page copy:

```
Headline: See what switching could save your support team this year
Subheadline: Enter your current ticket volume and cost — get your estimated
annual savings in seconds.

[Calculator embedded here, results shown immediately on the page]

Optional follow-up: "Want the full breakdown emailed to you, plus a
implementation timeline? Enter your email below."
Form: Work email (1 field, matches the stated ungated-first flow)
Button: Email me the breakdown
```

## Why this is a good output

- The formula was fully supplied by the user, satisfying the mandatory
  confirmation gate before any calculator gets built — no business logic was invented.
- The generated tool was actually tested against a manual calculation of the
  same formula, not just assumed to be correct because the code "looks right."
- Recommended (rather than assumed) an ungated-calculator-first flow per the
  conversion best practices reference, leaving the final call to the user.
