---
name: post-structurer
description: Turn a topic, idea, or rough draft into a fully structured social media post with a hook, body, and CTA, formatted correctly for the target platform. Use this skill when the user asks to "structure this post," "turn this into a LinkedIn/Instagram/X post," "write out this idea as a post," has a topic or bullet points and wants a complete draft, or has a rough/rambling draft they want tightened into proper hook-body-CTA shape. Different from social-post-ideator, which generates many idea concepts — this skill takes one idea and writes the full post.
---

# Post Structurer

Takes one topic or rough draft and turns it into a complete, ready-to-publish post: hook, body, and CTA, correctly shaped for the target platform's format norms.

## Workflow

1. **Identify inputs**:
   - The core idea, topic, or rough draft text
   - Target platform (LinkedIn, Instagram, X, TikTok script, Facebook)
   - Goal of this specific post (engagement/comments, shares/saves, clicks, awareness)
   - Brand voice — use sample posts if given, otherwise ask for a couple of tone adjectives

2. **Read `knowledge/structure-frameworks.md`** and pick the framework that fits the goal and content type (not every post needs the same skeleton).

3. **Read `mappings/platform-format-mapping.md`** to know the correct length, paragraph/line-break style, and CTA placement for the chosen platform.

4. **Draft the post** using `templates/post-structure-template.md`:
   - **Hook** (line 1-2): must stand alone and create a reason to keep reading. If the user gave a rough draft, extract or rewrite its strongest idea into the hook — don't just use their first sentence if a better one is buried in paragraph 3.
   - **Body**: developed using the chosen framework (see below). Broken into short paragraphs/line breaks appropriate to the platform — no dense walls of text.
   - **CTA**: one clear ask, matched to the stated goal (see `engagement-cta-writer` skill if the user wants CTA variants specifically — this skill writes one CTA inline as part of the full post).

5. **Tighten**: cut throat-clearing openers, generic transitions ("In conclusion," "At the end of the day"), and any line that doesn't earn its place. Every sentence should either build the idea or move toward the CTA.

## Frameworks to choose from (detail in knowledge/structure-frameworks.md)
- Hook → Tension → Resolution → CTA (story-driven)
- Hook → Claim → Evidence → CTA (opinion/thought-leadership)
- Hook → Problem → Framework/Steps → CTA (educational/how-to)
- Hook → Before/After → Mechanism → CTA (transformation/case-study)

## Output
Present the finished post exactly as it should be pasted into the platform — correct line breaks, no markdown artifacts, ready to copy. If useful, briefly note which framework was used and why (one line, not a lecture).

## Reference files
- `knowledge/structure-frameworks.md` — the four core frameworks explained
- `mappings/platform-format-mapping.md` — length/line-break/CTA placement per platform
- `templates/post-structure-template.md` — internal drafting scaffold
- `examples/example-run.md` — worked example turning a rough idea into a finished post
