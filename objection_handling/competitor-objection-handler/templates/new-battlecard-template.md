# New battlecard entry template

Use when adding a competitor to `handlers/competitor-objection-handler.md`'s table. Fill in every
field before adding the row — an incomplete entry (especially an unverified "strength" or
"differentiation angle") risks the handler stating something inaccurate live on a call.

## Template

```
| Competitor | Their strength | Differentiation angle | Question to ask the prospect |
|---|---|---|---|
| [Name] | [One verified strength — cite the source, e.g. their own site, an analyst report, or confirmed rep feedback] | [What angle we win on — must be true and defensible, not just optimistic] | [One open question that surfaces information useful for the rest of the call] |
```

## Checklist before adding

- [ ] The "strength" is a real, current fact — not something outdated or assumed.
- [ ] The "differentiation angle" is something the team can actually back up if the prospect
      pushes back on it.
- [ ] The "question to ask" is open-ended, not a leading/loaded question.
- [ ] Source noted somewhere (even just in the PR/commit message or a comment) for where the
      "strength" fact came from, so it can be re-verified later if it goes stale.
- [ ] `scripts/classify_objection.py`'s `KNOWN_COMPETITORS` list is updated to include the new
      competitor's name (and common variants/misspellings) so the classifier catches it.

## Example filled in

```
| Cisco Secure Firewall | Deep existing footprint in large enterprise networking accounts | Emphasize faster deployment and simpler multi-site policy management for teams without a dedicated network team | "How is your team currently handling policy changes across multiple sites?" |
```
