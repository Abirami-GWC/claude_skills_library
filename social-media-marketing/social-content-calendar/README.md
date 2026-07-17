# Social Content Calendar

Builds a weekly or monthly social media posting plan, organized by platform, content pillar, and cadence.

## What it does
Takes the user's platforms, content pillars, sustainable posting cadence, and any fixed dates (launches, events), then produces a calendar grid assigning a pillar + concrete topic + platform + format to each slot — sanity-checked against realistic posting benchmarks so it doesn't get abandoned.

## When it triggers
- "Build a content calendar for..."
- "Plan my posting schedule for the week/month"
- "What should I post on which day?"
- Any request to plan post topics in advance across platforms

## Folder contents
- `SKILL.md` — the skill definition and workflow Claude follows
- `knowledge/cadence-benchmarks.md` — realistic posting frequency ranges per platform
- `mappings/pillar-rotation-mapping.md` — how to rotate content pillars without overusing any one theme
- `templates/calendar-template.md` — output table structure
- `examples/example-run.md` — a full worked example (inputs → one-week calendar)

## Related skills
- `social-post-ideator` — generate ideas for each slot in the calendar
- `post-structurer` — write the full post once a slot's topic is picked
- `engagement-cta-writer` — sharpen the CTA on any post drafted from the calendar
