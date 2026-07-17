# Engagement CTA Writer

Writes calls-to-action for social posts that are tuned to a specific engagement goal — comments, shares, saves, follows, or clicks — instead of generic filler.

## What it does
Given a post's content and a stated (or inferred) goal, produces 3-5 labeled CTA options, each matched to a CTA mechanic that's actually known to drive that goal, with a recommendation on which to use.

## When it triggers
- "Give me CTA ideas for this post"
- "How should I end this post?"
- "Call to action for social media"
- A finished post/caption that's missing a closing line or has a weak one

## Folder contents
- `SKILL.md` — the skill definition and workflow Claude follows
- `knowledge/cta-types.md` — CTA mechanics broken down by goal (comments, shares, saves, follows, clicks)
- `mappings/goal-to-cta-mapping.md` — which CTA type fits which stated goal and platform
- `templates/cta-options-template.md` — output format
- `examples/example-run.md` — a full worked example (post + goal → CTA options)

## Related skills
- `post-structurer` — write the full post first if it doesn't exist yet
- `social-post-ideator` — generate the underlying idea if starting from scratch
