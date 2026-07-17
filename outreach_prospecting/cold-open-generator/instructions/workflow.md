# Workflow: Generating Cold Opens

## Step 1 — Inventory available signals
List out every concrete, usable signal from what the user has provided:
- Something the prospect wrote/said/published (post, article, talk, podcast)
- Something the prospect's company did (launch, hire, event, news)
- Something structural/observable (job posting details, tech stack, org structure)
- A shared connection or context (mutual contact, same event attended)

If nothing concrete is available and no research tool is available, tell the user
what's missing rather than inventing signals or falling back to generic flattery.
If a research tool (web search) is available and appropriate, offer to look up the
prospect/company to find real signals before generating openers.

## Step 2 — Match signals to formulas
Cross-reference `knowledge/opener-patterns.md` and `templates/opener-formulas.md`.
Aim for signal diversity across candidates — don't generate 5 openers all built off
the same fact restated 5 ways.

## Step 3 — Draft 3-5 candidates
For each candidate:
- One sentence (two max).
- Built around exactly one signal — don't cram multiple facts into one opener.
- No mention of the sender or their company yet (that belongs later in the message).

## Step 4 — Screen against clichés
Check every candidate against `knowledge/banned-cliches.txt`. If code execution is
available, run `scripts/cliche_checker.py` on the drafted candidates. Discard or
rewrite any flagged line.

## Step 5 — Apply the copy-paste test
For each surviving candidate, ask: "Could this exact line be sent to a prospect at
a different company with only the name changed, and still make sense?" If yes,
the line is not specific enough — sharpen it or discard it.

## Step 6 — Rank and deliver
Present 3-5 final candidates, each with:
- The opener line itself
- A one-line note on which signal/formula it uses
- A brief note on why it's ranked where it is (strongest = most specific/least
  reusable elsewhere)

Do not just dump the lines with no rationale — the rationale is what lets the user
sanity-check that the personalization is real, not manufactured.
