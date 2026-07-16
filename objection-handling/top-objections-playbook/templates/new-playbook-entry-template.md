# New playbook entry template

Use when adding a row to `handlers/top-objections-playbook.md`, or when creating a new stage- or
segment-specific playbook under `playbooks/` modeled on the same shape.

## Template

```
| # | Objection (as prospect says it) | Response frame | Rationale |
|---|---|---|---|
| [n] | [Write it the way a real prospect would say it, not a formal paraphrase] | [Direction to respond in — a question or approach, not a script to read verbatim] | [Why this works — usually names the real underlying concern the surface objection is masking] |
```

## Checklist before adding

- [ ] The objection phrase sounds like something a real prospect would say, not a summary.
- [ ] The response frame is a *direction*, not exact wording — per every handler's "How to use
      this file" note, reps adapt it, they don't read it verbatim.
- [ ] The rationale names the underlying concern, consistent with the "objections are rarely the
      real concern" principle in `knowledge/objection-psychology.md`.
- [ ] If this objection could also be read as a pricing or competitor objection, confirm it
      belongs here and not in one of those handlers — check
      `scripts/classify_objection.py`'s priority order (competitor > pricing > playbook).
- [ ] If adding to `scripts/classify_objection.py`'s `PLAYBOOK_KEYWORDS`, keep the keyword set
      narrow enough not to false-positive-match unrelated objections.

## Example filled in

```
| 11 | "We're locked into a multi-year contract with our current vendor" | Ask when that contract renews and offer to circle back closer to that date with a no-obligation refresh of pricing/features. | Distinguishes a genuine contractual blocker from a soft no — worth a calendar follow-up rather than a hard close attempt now. |
```
