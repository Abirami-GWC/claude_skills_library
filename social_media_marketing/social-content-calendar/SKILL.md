---
name: social-content-calendar
description: Build a weekly or monthly social media posting plan/calendar organized by platform, content pillar, and cadence. Use this skill when the user asks for a "content calendar," "posting schedule," "content plan for the month/week," wants to plan out post topics in advance, or needs to know what to post on which day across platforms. Distinct from social-post-ideator (single-topic idea generation) and post-structurer (writing one full post) — this skill produces the overall planning grid that those other skills feed into.
---

# Social Content Calendar

Builds a structured posting calendar — which pillar, which platform, which day — so the user isn't deciding what to post from scratch every day.

## Workflow

1. **Gather inputs**:
   - Time horizon: week or month
   - Platforms in scope
   - Content pillars/themes (e.g. product education, customer stories, industry commentary, behind-the-scenes, personal brand). If the user doesn't have pillars defined, propose 3-5 based on their business/goals and confirm.
   - Posting cadence per platform (how many posts/week they can realistically sustain) — don't assume; ask if unclear, since over-committing a cadence is the #1 reason calendars get abandoned.
   - Any fixed dates (launches, events, holidays) that need specific slots.

2. **Read `knowledge/cadence-benchmarks.md`** for realistic posting frequency benchmarks per platform, to sanity-check the user's stated cadence isn't wildly over- or under-shooting.

3. **Read `mappings/pillar-rotation-mapping.md`** to decide how pillars should rotate across the week/month so no single theme dominates and no pillar goes stale from overuse.

4. **Build the calendar** using `templates/calendar-template.md`:
   - Assign a pillar + rough topic + platform + format to each slot
   - Slot in any fixed dates first, then rotate remaining pillars around them
   - Flag slots that could use a post generated via the `social-post-ideator` skill for concrete ideas, and note where `post-structurer` would turn a slot into a full draft

5. **Sanity check before presenting**: no platform should have more posts scheduled than the user said they can sustain; no pillar should repeat two days in a row unless intentional (e.g. a themed week).

## Output
Present the calendar as a table (`templates/calendar-template.md`), grouped by day or week. Keep topic entries as short, concrete prompts (e.g. "Customer story — [specific account] onboarding win") rather than vague placeholders like "Engagement post."

## Reference files
- `knowledge/cadence-benchmarks.md` — realistic posting frequency per platform
- `mappings/pillar-rotation-mapping.md` — how to rotate pillars without overusing any one theme
- `templates/calendar-template.md` — output table structure
- `examples/example-run.md` — worked example of a one-week calendar
