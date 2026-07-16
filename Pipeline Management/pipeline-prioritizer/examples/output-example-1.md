# Output Example 1 — Matches input-example-1.md

Computed with `scripts/score_deals.py` (today = 2026-07-16). This is what the final
reply to the rep should look like, following `templates/priority-report.md` and
`templates/recommendation-template.md`.

---

## Pipeline Priority Ranking

| Rank | Deal | Value | Stage | Close Date | Why this rank |
|---|---|---|---|---|---|
| 1 | Acme Corp – Platform Upgrade | $85,000 | Late (contract sent) | Jul 22 | Largest deal in the batch, closing in a week, and you spoke yesterday — nothing else outranks this today. |
| 2 | Delta Co – Expansion | $60,000 | Late (verbal) | Jul 20 | Closing even sooner than Acme, but 10 days without contact for a deal this close to the line is worth a check-in before it closes. |
| 3 | Gamma LLC – Renewal | $45,000 | Mid (proposal) | Aug 15 | Solid probability (60%) and recent response, but mid-stage and closes a month out — steady, not urgent. |
| 4 | Beta Industries – New Deployment | $22,000 | Early (discovery) | Not set | Smallest deal, no close date, and 3 weeks of silence — lowest priority today, but the silence itself is a flag worth a follow-up nudge. |

**Data quality notes:** Probability wasn't given for any of these deals, so it was
inferred from stage (Late ≈ 80%, Mid stated at 60%, Early ≈ 20%). Beta Industries has
no close date, so its urgency was treated as unknown rather than assumed safe.

---

Note the explanations each cite specific facts from the input (dollar amounts, days
since contact, stated probability) rather than generic language — this is the bar
`recommendation-template.md` sets.
