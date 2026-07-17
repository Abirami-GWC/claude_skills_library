# New pricing scenario template

Use when adding a row to `handlers/pricing-objection-handler.md`'s scenario table, or a row to
`playbooks/renewal-and-upsell-objections.md`.

## Template

```
| Scenario | Talk track direction | Do not say |
|---|---|---|
| [Objection as the prospect would phrase it] | [Direction to respond in — reframe to value/TCO, ask a clarifying question, or route to an owner. Not exact wording.] | [Anything that would commit to a number or imply unauthorized flexibility] |
```

## Checklist before adding

- [ ] The talk track direction never states a specific discount percentage or dollar figure —
      per the hard rule in `handlers/pricing-objection-handler.md`.
- [ ] If the scenario involves a competitor's quote, note that it should route to
      `../competitor-objection-handler/` for the comparison, and keep this row focused on the
      pricing angle only.
- [ ] The "do not say" column is specific enough that a rep can self-check before responding, not
      a generic "don't overpromise."
- [ ] If adding to `scripts/classify_objection.py`'s `PRICING_KEYWORDS`, confirm the new keywords
      won't false-positive-match unrelated objections (e.g. "cost" appearing in an unrelated
      sentence).

## Example filled in

```
| "We'd need a multi-year discount to make this work" | Ask what timeline they're planning around, then route the actual discount question to the approved pricing owner rather than answering with a number. | Don't imply a specific multi-year discount rate is available. |
```
