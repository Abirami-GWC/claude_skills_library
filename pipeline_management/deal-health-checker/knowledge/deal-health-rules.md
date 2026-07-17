# Deal Health Rules

## Core principle

**Missing information is a caution signal, never a reason to assume health.** If a
deal is missing its last-contact date, decision-maker status, or response status,
that gap itself contributes points (see `risk-indicators.md`) and must be listed
explicitly in the report's "Missing Information" section — never silently treated
as "probably fine" or invented.

## Total score → classification

Sum the points from every applicable indicator in `risk-indicators.md`.

| Total score | Classification | Priority |
|---|---|---|
| 1.5 or below | 🟢 Healthy | Low |
| Above 1.5, up to 3.5 | 🟡 Warning | Medium |
| Above 3.5 | 🔴 At Risk | High |

These bands are calibrated so that a single strong negative signal (e.g., no
response at all, worth 1.5) doesn't alone tip a deal into At Risk, but two or more
real risk factors together do — a deal shouldn't need to look catastrophic on
every dimension to warrant a Warning.

## What "Healthy" requires

A deal only reaches Healthy when it has recent contact, a scheduled next meeting,
an identified decision maker, and a responsive customer — i.e., genuinely no open
question marks, not just "nothing catastrophic."

## Edge cases

- **Deal with almost no data provided**: score what you can, but the missing-info
  penalties alone will likely push it to at least Warning — this is correct
  behavior, not a bug. Say plainly that the classification is based on limited
  information.
- **Closed Won / Closed Lost deals mixed into the input**: exclude them from
  health evaluation entirely (see `sales-pipeline-stages.md`) — note that they
  were excluded rather than silently dropping them with no mention.
- **Very large pipelines (50+ deals)**: report full detail for every At Risk deal.
  For Healthy and Warning deals, list them by name under their tier in
  `templates/risk-summary.md` without a full risk-factor write-up for each one,
  unless the user asks for detail on a specific deal.
- **A deal with only positive indicators and literally nothing to flag**: still
  produce the report — a clean bill of health is a valid and useful output, not
  something to pad with invented caveats.
- **Early-stage deals (Lead/Qualified) missing a decision maker**: this is
  expected at that stage and shouldn't be weighted as heavily in the narrative
  even though it still contributes its points — mention that it's normal for the
  stage rather than treating it as alarming.
