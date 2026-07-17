---
name: engagement-cta-writer
description: Write calls-to-action for social media posts that are tuned to drive real engagement (comments, shares, saves) rather than generic asks like "thoughts?" or "like and share." Use this skill when the user asks for "CTA ideas," "how do I end this post," "call to action for social media," wants multiple CTA options for a post, or has a finished post/caption that's missing or has a weak closing line. Distinct from post-structurer (which writes the whole post) — this skill focuses specifically on the closing ask.
---

# Engagement CTA Writer

Writes calls-to-action matched to a specific engagement goal — comments, shares, saves, clicks, or follows — instead of generic filler like "thoughts?" or "like if you agree."

## Workflow

1. **Identify inputs**:
   - The post content or topic the CTA is for (need context to make the CTA specific, not generic)
   - The engagement goal: comments/discussion, shares, saves/bookmarks, profile follows, or link clicks
   - Platform (CTA style differs — see `mappings/goal-to-cta-mapping.md`)

2. **Read `knowledge/cta-types.md`** to understand which CTA mechanics actually drive each goal (they're not interchangeable — a save-driving CTA looks nothing like a comment-driving one).

3. **Read `mappings/goal-to-cta-mapping.md`** to select the right CTA type(s) for the stated goal and platform.

4. **Write 3-5 CTA options**, each:
   - Specific to the actual post content (never a generic template with the topic swapped in — reference something concrete from the post)
   - Matched to the CTA type selected
   - Short — a CTA that takes longer to read than the post's main point has failed

5. Use `templates/cta-options-template.md` for output, labeling each option by CTA type so the user understands why it might work.

## What to avoid
- "Thoughts?" / "Let me know what you think!" / "Like and share if you agree!" — these have effectively zero pull because they ask nothing specific.
- Asking two things at once ("comment below and share with a friend!") — pick one ask per post.
- CTAs that don't connect to anything in the actual post content.

## Output
Present 3-5 labeled CTA options via `templates/cta-options-template.md`. If the user wants just one, still generate a couple internally and hand over the strongest, noting briefly why.

## Reference files
- `knowledge/cta-types.md` — CTA mechanics by goal (comments, shares, saves, clicks, follows)
- `mappings/goal-to-cta-mapping.md` — which CTA type fits which goal + platform
- `templates/cta-options-template.md` — output format
- `examples/example-run.md` — worked example
