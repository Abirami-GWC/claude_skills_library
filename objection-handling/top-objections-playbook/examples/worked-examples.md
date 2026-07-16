# Worked examples — playbook objections

Full input-to-output examples for `handlers/top-objections-playbook.md`, showing the whole flow:
raw objection → classification → handler lookup → generated response (in the
`references/schemas.md` § Response format spec shape). Use as a sanity check against a known-good
pattern, or as a few-shot reference when the wording of an incoming objection is unusual.

## Example 1 — Standard playbook objection

**Raw text:** "Honestly we already went with a vendor for this last quarter."

**Classification:** `{"category": "playbook", "subcategory": "existing_vendor", "confidence": "medium"}`

**Generated response:**
```json
{
  "objection_category": "playbook",
  "response_summary": "Totally fair — most teams we work with already had something in place too. What's got you taking this call now?",
  "supporting_points": [
    "Acknowledges the existing vendor without arguing against the choice",
    "Surfaces the real prompt for the conversation instead of assuming dissatisfaction"
  ],
  "follow_up_question": "What's prompting you to look at this now if you already have a vendor?",
  "confidence_level": "medium",
  "needs_verification": false
}
```

**Why this matches the handler:** follows `handlers/top-objections-playbook.md` row 1's frame —
acknowledge, then ask what's prompting the call, rather than arguing switching costs.

## Example 2 — Low-confidence / unmatched objection

**Raw text:** "I don't know, it just feels like a lot right now."

**Classification:** `{"category": "playbook", "confidence": "low"}`

**Generated response:**
```json
{
  "objection_category": "playbook",
  "response_summary": "That's a fair reaction — can you say more about what feels like the most, so I'm not guessing at what to address?",
  "supporting_points": [
    "Does not force a weak match to a specific playbook row",
    "Flags low confidence to the rep rather than presenting a guess as certain"
  ],
  "follow_up_question": "What specifically feels like the most right now — the change itself, the timing, or something else?",
  "confidence_level": "low",
  "needs_verification": false
}
```

**Why this matches the handler:** per this handler's "How to use this file" note, a weak match
should be flagged as needing a new entry rather than forced into a specific row.

*(All conversation text above is illustrative placeholder content for a network-security sales
scenario, matching the rest of this skill.)*
