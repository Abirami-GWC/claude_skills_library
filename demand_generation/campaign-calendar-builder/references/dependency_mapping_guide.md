# Dependency Mapping Guide

How to identify dependencies between campaign activities — both the ones the
user states explicitly and the ones that need to be inferred.

## Common dependency patterns

| If activity B... | It almost always depends on... |
|---|---|
| Promotes, announces, or links to an asset | That asset being published/live |
| Requires legal/brand/compliance sign-off | The draft being complete |
| Is a "reminder" or "last chance" message | The original announcement having gone out first |
| Uses creative (images, video) in an ad | That creative being approved/finalized |
| Is a follow-up email in a sequence | The prior email in the sequence having sent |
| References data/results (e.g., "as seen in our report") | The report being published |

## Explicit vs. inferred dependencies

- **User-confirmed**: the user directly stated the relationship ("legal needs
  to review before it goes out," "send the reminder two days after the first email").
- **Inferred**: Claude derived the relationship from context because it's
  logically necessary (a post announcing an asset can't reasonably go out
  before that asset exists) but the user didn't say so explicitly.

Always tag which type each dependency is in `dependency_source`. Inferred
dependencies should be surfaced to the user for confirmation, especially if
resolving a conflict depends on whether the inferred relationship is correct
— see the worked example in `examples/example_1.md`, where an inferred
dependency between a LinkedIn post and a blog publish date was the actual
crux of the scheduling conflict.

## When NOT to infer a dependency

- Two activities on the same channel but unrelated content — don't assume
  sequencing dependency just because they're close in time.
- Activities across different campaigns or workstreams, unless the user
  says they're related.
- A "nice to have" ordering preference (e.g., "it'd be better if X came
  before Y") is not the same as a hard dependency — only encode it as a
  `depends_on` relationship if it's a true prerequisite, not a preference.
  Note soft preferences in the `notes` field instead.

## Common mistake this guide prevents

Treating every same-campaign activity as sequentially dependent on the one
before it, which turns a calendar into an artificially rigid chain and makes
the conflict-detection script report false positives. Only encode a real
prerequisite relationship, not simple chronological proximity.
