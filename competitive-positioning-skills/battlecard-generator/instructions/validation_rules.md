# Validation Rules — Battlecard Generator

Run before delivering any battlecard draft.

## Sourcing checks

- [ ] Every weakness/landmine claim has a source note or is marked `[UNVERIFIED]`.
- [ ] Every pricing claim is labeled `public`, `reported-by-prospect`, or
      `unverified` — never presented as flat fact without that context.
- [ ] No claim is attributed to a named real individual at the competitor
      without a genuine public source.
- [ ] The genuine strengths section is present and non-empty — a battlecard
      with zero acknowledged competitor strengths is a credibility risk.

## Structural / format checks

- [ ] All 11 sections from `knowledge/battlecard_structure.md` are present in
      the standard order (trim content within a section if space-constrained,
      never drop a whole section silently).
- [ ] The draft fits one page/screen at a glance in the requested format — if
      not, cut detail rather than shrink fonts.
- [ ] Every weakness has a paired landmine question, where the source material allows it.
- [ ] Objection responses are phrased as something a rep would actually say out
      loud (short, natural sentences), not marketing copy.
- [ ] `as_of_date` is present and accurate to when the source data was gathered.

## Fairness / legal checks

- [ ] No disparaging or mocking language about the competitor.
- [ ] No absolute claims ("never," "always," "the only") unless verifiably true.
- [ ] No claim on a supplied `do_not_say` list.
- [ ] No verbatim reproduction of competitor marketing copy, datasheets, or
      pricing-page text.

## Final gate

If any sourcing checkbox is unresolved, mark the specific claim
`[UNVERIFIED]` in the delivered draft and list open items needing user
confirmation — do not silently present a guess as a sourced fact.
