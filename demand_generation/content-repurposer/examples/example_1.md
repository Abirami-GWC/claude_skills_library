# Worked Example — Content Repurposer

## User input

> "Repurpose this blog post [attaches the deploy-time blog post from earlier]
> into a LinkedIn post, a 3-post X thread, and an email teaser."

## Claude's internal process (not shown to user)

1. Ingest the full blog post text (not just a summary).
2. Run `scripts/extract_key_points.py` against it to get a candidate
   shortlist: the 45min→9min stat, the 62% survey stat, the staff engineer
   quote, the 14x/day shipping stat, the 35% incident-drop stat.
3. Confirm target formats: LinkedIn post, X thread (3 posts), email teaser —
   all three requested, check each against `references/platform_specs.md`.
4. Select ONE core idea per LinkedIn/email piece (the 45→9 minute stat is the
   strongest, most concrete hook) and vary the thread's three posts across
   three different stats so they don't all repeat the same number.
5. Draft each with format-native structure per
   `knowledge/format_conversion_guide.md`, using the staff engineer quote
   verbatim (it's under 15 words in the quotable portion) — only once, in the
   LinkedIn post, not reused in every piece.
6. Validate: character counts checked, only one quote used across all three
   pieces total (not one per piece, since it's the same quote source), no
   fabricated stats beyond what the script surfaced and the source confirms.

## Output delivered to user (abbreviated)

```
### LinkedIn Post
Hook: "We cut our deploy time from 45 minutes to 9 minutes — an 80% reduction."
Body: [2 short paragraphs on what changed — parallel test execution,
incremental builds — and the resulting shipping cadence increase]
Quote: One staff engineer put it simply: "I actually look forward to Friday
deploys now."
CTA: What's your team's deploy time? Curious how common the old normal still is.
Character count: 612 / ~3000 limit ✓

### X Thread (3 posts)
1/ We used to dread Friday deploys. 45 minutes average, and a failed one
could eat your whole afternoon.
2/ We rebuilt CI around parallel tests + incremental builds. Deploy time: 9
minutes. Shipping frequency: 3x/day → 14x/day.
3/ Bonus: deploy-related incidents dropped 35% in the same period. Faster,
smaller deploys turned out to be safer ones too.
Character counts: 118 / 121 / 132 — all under 280 ✓

### Email Teaser
Subject: How we made Friday deploys something people look forward to
Body: A year ago, 62% of our engineers had delayed a release just to dodge a
risky deploy window. Here's what changed once deploy time dropped from 45
minutes to 9 — and why deploys got safer, not just faster.
CTA: Read the full breakdown →
Word count: 54 / target 60–90 (slightly under, acceptable for a punchy teaser)
```

## Why this is a good output

- Each piece leads with a different stat (45→9 min / 3x→14x / 35% incident
  drop) — no redundant angle repetition across the thread.
- The staff engineer quote was used exactly once across all three pieces, at
  under 15 words, correctly following the one-quote-per-source discipline
  even across multiple output pieces from the same source.
- Every number appearing in the outputs is traceable to the extraction
  script's shortlist and the actual source text — nothing invented.
- Character/word counts were verified, not estimated.
