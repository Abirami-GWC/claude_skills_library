# Worked examples — competitor objections

Full input-to-output example for `handlers/competitor-objection-handler.md`, matching the
response shape in `references/schemas.md`.

## Example 1 — Competitor objection

**Raw text:** "We're also talking to Palo Alto and they seem to have a lot more going on feature-wise."

**Classification:** `{"category": "competitor", "matched_competitor": "palo alto", "confidence": "high"}`

**Generated response:**
```json
{
  "objection_category": "competitor",
  "response_summary": "Palo Alto has a strong enterprise feature set, no argument there. Where we tend to win is time-to-value and lower day-to-day overhead, especially for teams your size.",
  "supporting_points": [
    "Concedes their genuine strength first rather than disputing it",
    "Differentiates on time-to-value and operational overhead, not a feature-count argument"
  ],
  "follow_up_question": "How long did your last policy rollout take end to end?",
  "confidence_level": "high",
  "needs_verification": false
}
```

**Why this matches the handler:** follows `handlers/competitor-objection-handler.md`'s structure
— their strength, then differentiation, then a question — and only uses the verified battlecard
row for Palo Alto Networks.

*(All conversation text above is illustrative placeholder content for a network-security sales
scenario, matching the rest of this skill.)*
