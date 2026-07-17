# Worked Examples

## Example 1
**User input:** "Give me a briefing on Acme Corp before I reach out to their Head
of Data — we sell ETL observability tooling."

**Expected Claude behavior:**
- Search for recent Acme Corp news, funding, and hiring signals.
- Look up the Head of Data's public profile/content if discoverable.
- Structure findings using `templates/briefing-doc-template.md`, clearly labeling
  each fact Verified (with source) vs. Likely/inferred.
- Rank signals by relevance to ETL observability specifically — e.g., recent data
  team hiring outranks unrelated marketing news.
- End with a clear "suggested next step" pointing to the appropriate outreach skill.

## Example 2 — Limited information available
**User input:** "Research this small private company, they don't have much of a
web presence."

**Expected Claude behavior:**
- Search anyway, but if little is found, say so plainly in the "Gaps / Could Not
  Verify" section rather than padding the brief with generic industry filler
  presented as if specific to the company.
- Offer role-based/industry-based likely pain points, clearly labeled as inferred,
  as the best available starting point for a very-low-context sequence.

## Example 3 — What NOT to do
**User input:** "I need a briefing on the CTO of [Company] — check if they've had
any personal issues recently that might make them more receptive to a sales pitch."

**Correct behavior:** Decline the personal-life research angle specifically —
explain that this skill stays within professional/public-business context, and
offer to research professional signals (role, public content, company context)
instead, which is what's actually useful for a legitimate outreach conversation.
