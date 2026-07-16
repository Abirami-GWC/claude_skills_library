---
name: buying-signal-detection
description: >
  Sub-skill of prospect-research-briefer. Reviews gathered company and contact
  research to identify and rank genuine buying/trigger signals versus interesting
  but irrelevant trivia. Use internally at Step 4 of the parent workflow, after
  company-research and contact-research have gathered raw findings. Not intended
  to be triggered directly by end users.
---

# Buying Signal Detection

## Purpose
Raw research often turns up more facts than are useful. This sub-skill filters
and ranks findings so the brief highlights what actually matters for outreach
timing and framing, rather than listing every fact found.

## Ranking method
Score each candidate signal on:
1. **Specificity** — does it apply distinctly to this company/contact, or could
   it apply to almost any company in the industry?
2. **Recency** — see `knowledge/signal-taxonomy.json` in the parent skill for
   typical relevance windows by signal type (e.g., trigger events ~60 days,
   structural signals ~180 days).
3. **Offer relevance** — does this signal plausibly connect to the specific
   problem the offer solves, or is it generic company trivia?

Keep only signals that score reasonably on all three; a signal that's recent and
specific but has no offer relevance still doesn't belong as a primary hook (though
it may be worth a footnote).

## Output
A ranked list (strongest first) of 2-4 signals, each with a one-line note on why
it ranked where it did. This ranked list feeds directly into the brief's "Recent
Signals" section and, downstream, into `cold-open-generator`'s formula-matching step.

## Common mistakes prevented
- Listing every fact found with no prioritization, leaving the rep to guess which
  ones matter.
- Treating stale signals as current without a recency check.
- Elevating a generic industry-wide trend to "signal" status when it isn't
  specific to this company.
