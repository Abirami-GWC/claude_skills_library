# Validation Rules — Content Repurposer

Run before delivering any repurposed content set.

## Fidelity checks

- [ ] Every claim/stat in each output piece is actually present in the source
      — nothing added, no emphasis that changes the original's meaning.
- [ ] Qualifiers/caveats present in the source that materially affect a claim
      are preserved, not dropped for brevity.
- [ ] No quote is fabricated or altered from what the source actually says.

## Copyright checks

- [ ] No output piece contains more than one quote from the source, and that
      quote is under ~15 words.
- [ ] All other source material is paraphrased in the piece's own words, not
      lightly reworded from the original's sentence structure.
- [ ] If the source itself is third-party copyrighted material (not the
      user's own), outputs stay at summary/paraphrase level only.

## Format checks

- [ ] Each piece matches its platform's structural convention from
      `knowledge/format_conversion_guide.md` — genuinely adapted, not truncated.
- [ ] Each piece respects the character/length limits in
      `references/platform_specs.md` — verified by counting, not estimated.
- [ ] Multiple pieces for the same platform each surface a distinct angle —
      no two pieces restating the same point.

## Final gate

If any fidelity-check box fails, revise the piece rather than deliver it —
factual drift from the source is the single most damaging failure mode for
this skill, since repurposed content often reaches a wider audience than the original.
