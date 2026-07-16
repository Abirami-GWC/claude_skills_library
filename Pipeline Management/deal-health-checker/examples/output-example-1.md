# Output Example 1 — Matches input-example-1.md

Computed with `scripts/deal_health.py` (today = 2026-07-16). This is what the
final reply should look like, following `templates/risk-summary.md`,
`templates/health-report.md`, and `templates/action-plan.md`.

---

## Pipeline Risk Summary

| Status | Count | Deals |
|---|---|---|
| 🟢 Healthy | 1 | Beta Corp |
| 🟡 Warning | 1 | Gamma LLC |
| 🔴 At Risk | 1 | ABC Manufacturing |

**Overall Pipeline Health:** 1 of 3 open deals is at risk, and it's a genuine
concern — ABC Manufacturing has gone quiet on every front at once (contact,
meetings, decision maker, response). Gamma LLC's Warning status is mostly about
missing information rather than confirmed bad signals, and is easy to resolve.

---

## Deal Health Report — ABC Manufacturing

**Health Status:** 🔴 At Risk
**Priority:** High

**Risk Factors**
- No customer contact in 18 days
- No next meeting scheduled
- Decision maker not identified
- No customer response since the proposal was sent

**Recommended Actions**
1. Call the customer directly — 18 days of silence means email alone isn't working.
2. Identify the decision maker — right now there's no confirmation this deal can
   actually close.
3. Get a next meeting on the calendar, even a short check-in, to create forward
   motion.
4. Send a direct follow-up referencing the proposal specifically, not a generic
   check-in.

## Deal Health Report — Gamma LLC

**Health Status:** 🟡 Warning
**Priority:** Medium

**Positive Indicators**
- Next meeting scheduled

**Risk Factors**
- Minor inactivity — 10 days since last contact

**Missing Information**
- Decision maker status not provided
- Customer response status not provided

**Recommended Actions**
1. Confirm who the decision maker is before the next meeting.
2. Check whether the last email got a response — if not, follow up before the
   meeting rather than waiting.

## Deal Health Report — Beta Corp

**Health Status:** 🟢 Healthy
**Priority:** Low

**Positive Indicators**
- Recent contact (3 days ago)
- Next meeting scheduled
- Decision maker identified
- Customer has been responsive

No risk factors identified. No action needed beyond the next scheduled meeting.

---

## Action Plan

| Deal | Immediate Action | Reason | Priority | Expected Outcome |
|---|---|---|---|---|
| ABC Manufacturing | Call the customer directly | 18 days of silence — email alone hasn't worked | High | Re-establish contact and confirm the deal is still live |
| ABC Manufacturing | Identify the decision maker | Currently unknown — can't confirm this deal can close | High | A named economic buyer to engage directly |
| Gamma LLC | Confirm decision maker and response status before the next meeting | Both currently unstated — can't assess real risk without this | Medium | Clear read on whether this deal is genuinely on track |
