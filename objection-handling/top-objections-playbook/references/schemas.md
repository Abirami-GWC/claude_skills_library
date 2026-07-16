# Schemas

Data shapes and integration reference shared across all four handlers. Load this only when you
need the precise schema — the handler files cover day-to-day usage.

## Table of contents
- Objection taxonomy (JSON schema)
- Response format spec
- CRM logging (Salesforce field mapping)
- Classifier contract

## Objection taxonomy

Every objection instance, whether logged or generated in roleplay, follows this shape:

```json
{
  "objection_id": "string, e.g. obj_2026_07_16_001",
  "raw_text": "string, what the prospect actually said",
  "category": "playbook | pricing | competitor",
  "subcategory": "string, e.g. 'existing_vendor', 'budget_freeze', 'fortinet'",
  "confidence": "high | medium | low",
  "matched_entry": "string, the handler-file row/id this was matched to, or null if unmatched",
  "opportunity_id": "string or null, Salesforce Opportunity Id if in a logged context",
  "rep_id": "string or null",
  "timestamp": "ISO 8601"
}
```

`confidence: low` means the classifier or Claude wasn't sure which bucket this belongs to — in
that case, present the best-guess response but flag the uncertainty rather than stating it with
false confidence.

## Response format spec

All three lookup handlers (playbook, pricing, competitor) return responses in this shape so
downstream UI/logging stays consistent:

```json
{
  "objection_category": "playbook | pricing | competitor",
  "response_summary": "1-2 sentence talking point, what the rep should say",
  "supporting_points": ["short bullet", "short bullet"],
  "follow_up_question": "optional, a question the rep can ask back",
  "confidence_level": "high | medium | low",
  "needs_verification": "boolean — true if any competitor claim or pricing figure needs a fact-check before use"
}
```

Keep `response_summary` short enough to read in one glance mid-call.

## CRM logging (Salesforce field mapping)

If a Salesforce connector is available and the user confirms logging, map fields like this. This
is illustrative — confirm actual field API names against the org's schema before writing.

| Objection taxonomy field | Salesforce field (typical) | Object |
|---|---|---|
| `raw_text` | `Objection_Text__c` | Opportunity or a related custom object (e.g. `Objection__c`) |
| `category` | `Objection_Category__c` | same |
| `subcategory` | `Objection_Subcategory__c` | same |
| `matched_entry` | `Playbook_Entry__c` | same |
| `opportunity_id` | `Opportunity__c` (lookup) | same |
| `rep_id` | `OwnerId` | same |
| `timestamp` | `CreatedDate` (system-set) | same |

Always confirm the target object exists in the org (`getObjectSchema` before writing) rather than
assuming a custom object is present — fall back to a plain Opportunity note/task, or ask the user
how they want it logged, if it doesn't.

## Classifier contract

`scripts/classify_objection.py` is a lightweight keyword/rule-based router — not a model call —
meant as a fast first pass before Claude reasons over ambiguous cases.

**Input:** raw objection string via stdin or `--text` arg.

**Output (JSON to stdout):**
```json
{
  "category": "playbook | pricing | competitor",
  "matched_competitor": "string or null",
  "confidence": "high | medium | low"
}
```

**Rules, in priority order:**
1. Known competitor name appears (case-insensitive) → `competitor`, `confidence: high`.
2. Else pricing keywords appear (price, cost, budget, expensive, discount, afford) → `pricing`,
   `confidence: high`.
3. Else matches a top-objection keyword set → `playbook`, `confidence: medium`.
4. Else → `playbook`, `confidence: low` (default bucket; Claude should re-classify by reasoning
   rather than trusting a low-confidence script output blindly).

The competitor list and keyword sets live at the top of the script as plain Python lists/dicts —
edit those in place whenever `handlers/competitor-objection-handler.md` or
`handlers/pricing-objection-handler.md` content changes, so they stay in sync.
