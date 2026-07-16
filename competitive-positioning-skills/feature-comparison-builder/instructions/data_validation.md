# Data Validation Checklist — Feature Comparison Builder

Run before rendering any output.

## Sourcing checks

- [ ] Every non-"us" cell has a `source_note` or `source_url`, OR is explicitly `Unknown`.
- [ ] No cell was inferred from general assumptions about "companies like this."
- [ ] Pricing rows follow `references/pricing_comparison_guidelines.md`.
- [ ] AI Capabilities rows follow `references/ai_capability_comparison_notes.md`
      (GA/beta/roadmap status explicitly checked, not assumed).

## Consistency checks

- [ ] The same support-level scale (`knowledge/scoring_legend.md`) is used for
      every cell — no mixed symbol sets, no free-text ratings.
- [ ] Every vendor has a value (even if `Unknown`) for every dimension — no blank cells.
- [ ] Dimension labels are neutral/outcome-based, not phrased to favor one vendor.
- [ ] Dimension wording matches the RFP's exact requirement text, if applicable.
- [ ] For 3+ vendor comparisons, every dimension row has a cell for every vendor
      (no silently-dropped vendor in a subset of rows).

## Accuracy risk checks

- [ ] No competitor cell is marked `Unsupported` (❌) without a clear source.
- [ ] Nuanced cases (add-on, partial, beta) are reflected precisely, not
      flattened to a binary yes/no.
- [ ] `as_of_date` is present and accurate to when the source data was gathered.

## Copyright/legal checks

- [ ] No verbatim reproduction of competitor marketing copy or datasheet text.
- [ ] No fabricated competitor pricing numbers.

## Final gate

If any sourcing or accuracy-risk box fails, do not render the table with that
cell stated as fact. Either resolve it with the user or mark it `Unknown` and
flag it in the delivery notes.
