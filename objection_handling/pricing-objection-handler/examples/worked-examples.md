# Worked examples — pricing objections

Full input-to-output example for `handlers/pricing-objection-handler.md`, including an optional
CRM log entry, matching the shapes in `references/schemas.md`.

## Example 1 — Pricing objection

**Raw text:** "This is way more than we're paying for our current setup."

**Classification:** `{"category": "pricing", "confidence": "high"}`

**Generated response:**
```json
{
  "objection_category": "pricing",
  "response_summary": "Makes sense to compare — can I walk through what's included beyond license cost, like incident response time and the staff hours it typically saves?",
  "supporting_points": [
    "Reframes to total cost of ownership rather than sticker price",
    "Does not disparage the current setup's price"
  ],
  "follow_up_question": "What does your team currently spend handling incidents manually?",
  "confidence_level": "high",
  "needs_verification": false
}
```

**Why this matches the handler:** follows the hard rule in `handlers/pricing-objection-handler.md`
— no discount is stated, and the reframe goes to TCO per the "more expensive than what we pay now"
row.

## Example 2 — CRM log entry (Salesforce), following on from Example 1

If the user confirms logging:

```json
{
  "raw_text": "This is way more than we're paying for our current setup.",
  "category": "pricing",
  "subcategory": "more_expensive_than_current",
  "matched_entry": "pricing_scenario_1",
  "opportunity_id": "0061a00000ExampleId",
  "rep_id": "0051a00000RepIdHere",
  "timestamp": "2026-07-16T14:32:00Z"
}
```

Mapped per `references/schemas.md` § CRM logging — always confirm the target object/fields exist
in the org before writing.

*(All conversation text above is illustrative placeholder content for a network-security sales
scenario, matching the rest of this skill.)*
