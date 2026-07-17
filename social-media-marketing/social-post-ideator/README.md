# Social Post Ideator

Generates platform-specific social media post ideas and hooks from a single topic, product update, blog post, or raw idea.

## What it does
Takes one input (a topic, announcement, or piece of content) and produces 5-8 post concepts per requested platform, each with a ready-to-use hook, angle description, and suggested format — matched to the user's brand voice instead of generic AI-sounding suggestions.

## When it triggers
- "Give me post ideas for..."
- "What should I post about [topic]?"
- "I have this blog post/update, turn it into social ideas"
- "Hooks for LinkedIn/Instagram/X/TikTok about..."

## Folder contents
- `SKILL.md` — the skill definition and workflow Claude follows
- `knowledge/platform-content-norms.md` — format/length/tone expectations per platform
- `knowledge/hook-formulas.md` — library of hook patterns to draw from
- `mappings/topic-to-angle-mapping.md` — which content angle suits which topic type
- `templates/idea-batch-template.md` — output structure
- `examples/example-run.md` — a full worked example (input → output)

## Related skills
- `post-structurer` — once an idea is picked, write it out as a full post
- `engagement-cta-writer` — sharpen or vary the closing CTA
- `social-content-calendar` — plan which ideas go where across the week/month
