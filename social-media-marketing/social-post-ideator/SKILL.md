---
name: social-post-ideator
description: Generate platform-specific social media post ideas and hooks from a topic, product, announcement, or content pillar. Use this skill whenever the user asks for "post ideas," "content ideas," "hooks," "what should I post," "give me ideas for social media/LinkedIn/Instagram/X/TikTok," or wants a batch of on-brand post concepts. Also trigger when the user pastes a blog post, product update, or raw idea and wants it turned into multiple social post angles. Produces ideas tuned to platform norms and the user's brand voice rather than generic AI-sounding suggestions.
---

# Social Post Ideator

Turns one topic, product update, or raw idea into a batch of platform-native post ideas with ready-to-use hooks — not generic "10 tips" filler.

## Workflow

1. **Clarify inputs** (ask only what's missing, default sensibly otherwise):
   - Topic / raw material (a product update, blog post, announcement, personal story, data point, etc.)
   - Target platform(s) — LinkedIn, Instagram, X/Twitter, TikTok, Facebook. Default to LinkedIn + Instagram if unspecified for B2B; LinkedIn + X for a personal brand.
   - Brand voice cues — if the user has shared examples of their past posts or a style guide, use it. If not, ask for 2-3 sample posts or a few adjectives (e.g. "witty and blunt" vs "warm and educational").
   - Goal — awareness, engagement, leads, thought leadership. This changes which angle to lean on.

2. **Read `knowledge/platform-content-norms.md`** to understand what "good" looks like on each requested platform (length, tone, format expectations) before generating ideas.

3. **Read `knowledge/hook-formulas.md`** and select 3-5 formulas that fit the topic and goal. Don't force every formula onto every topic — pick what's genuinely a fit.

4. **Check `mappings/topic-to-angle-mapping.md`** to decide which angles (contrarian take, behind-the-scenes, data-led, story-led, how-to, etc.) suit the topic type.

5. **Generate 5-8 post ideas per platform**, each with:
   - A ready-to-use hook (first line, verbatim, not a placeholder)
   - A one-line description of the angle/body direction
   - Suggested format (carousel, single image, text-only, video/reel, thread)

   Use `templates/idea-batch-template.md` for output structure.

6. **Avoid generic AI voice**: no "In today's fast-paced world," no listicle titles like "5 Things You Need to Know," no em-dash-heavy corporate tone unless that's the user's actual voice. Write hooks as if a sharp human in that niche wrote them.

7. If the user gives sample posts, mirror their sentence length, punctuation habits, and vocabulary — don't just extract "tone" adjectives, actually pattern-match the writing.

## Output

Present ideas grouped by platform, using `templates/idea-batch-template.md`. Do not pad with commentary between ideas — the ideas themselves are the deliverable.

## Reference files
- `knowledge/platform-content-norms.md` — format/length/tone expectations per platform
- `knowledge/hook-formulas.md` — hook pattern library
- `mappings/topic-to-angle-mapping.md` — which angle fits which topic type
- `templates/idea-batch-template.md` — output structure
- `examples/example-run.md` — a full worked example
