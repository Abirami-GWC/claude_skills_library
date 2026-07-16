# Worked Examples

## Example 1
**User input:** "Write a 5-touch email sequence for VP of Engineering at Series B
SaaS companies. We sell an ETL observability tool. I don't have specific target
accounts yet, just the persona."

**Expected Claude behavior:**
- Recognize there is no per-account signal available, so touch 1 cannot cite a
  specific company fact. Instead, personalize to the *persona and stage* (Series
  B eng team, likely scaling data infra, likely feeling pipeline reliability pain)
  rather than inventing a fake company detail.
- Clearly note in the response that this is persona-level personalization, and
  that per-account signals (from `prospect-research-briefer`) would sharpen touch 1
  further once real accounts are selected.
- Deliver 5 touches following the standard cadence (Day 0/3/7/12/18), each with a
  distinct angle: pipeline-failure pain (touch 1), reliability cost-of-downtime
  stat placeholder marked [VERIFY] (touch 2), a give-touch sharing an ETL
  reliability checklist (touch 3), a peer-example placeholder (touch 4), breakup (touch 5).

## Example 2
**User input:** "Here's our research doc on Acme Corp — they just raised a $40M
Series C and are hiring 8 data engineers. Write a sequence targeting their Head of
Data, who published a blog post last month about migration pain from legacy ETL."

**Expected Claude behavior:**
- Use the two concrete signals (funding + hiring, and the blog post) as the spine
  of touch 1 — e.g., referencing the blog post directly as the hook, since it is
  the sharpest, most specific signal.
- Distribute the funding/hiring signal to touch 2 rather than cramming everything
  into touch 1 (avoids an overloaded, listy opener).
- Since these facts came from the user's own research doc, they don't need
  `[VERIFY:]` placeholders — treat them as confirmed.
- Include a rationale line per touch pointing back to which signal it uses.

## Example 3 — What NOT to do
**User input:** "Write a quick follow-up sequence, keep it generic since I have 200
accounts to send this to."

**Anti-pattern to avoid:** Writing a single generic template and calling it
"personalized" via `{{first_name}}` and `{{company}}` merge tags alone.

**Correct behavior:** Deliver a template with clearly marked, structured
personalization slots (e.g., `[PERSONALIZATION: 1-sentence account-specific hook]`)
and explicitly tell the user that true personalization at this scale requires either
(a) per-account research inputs for each of the 200 accounts, or (b) accepting a
lighter, role-based personalization approach — and ask which they want rather than
silently defaulting to fully generic copy.
