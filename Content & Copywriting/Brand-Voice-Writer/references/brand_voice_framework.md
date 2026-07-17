# Brand Voice Framework

## Purpose

This document gives Claude a structured way to identify, describe, and apply a brand voice from whatever inputs a user provides — a style guide, adjectives, example copy, or nothing more than a rough description. It is the foundational reference for the Brand Voice Writer skill.

## Introduction

"Brand voice" is often described only in adjectives ("friendly," "bold," "premium"), but adjectives alone are not enough to produce consistent copy — two writers given the word "friendly" will write very differently. A usable brand voice framework breaks voice into concrete, checkable dimensions.

## Detailed Explanation

### The Five Dimensions of Voice

1. **Personality** — the human character the brand would have if it were a person (e.g., "the encouraging coach," "the sharp-witted friend," "the calm expert"). This anchors every other dimension.
2. **Tone** — how personality flexes by context. The same brand personality sounds different in an error message than in a celebration email. Tone is personality adjusted for the emotional register of the moment (see `tone_of_voice_guide.md`).
3. **Language** — vocabulary choices: sentence length, contraction use, jargon tolerance, idiom use, reading-level target, use of humor or metaphor.
4. **Structure** — how the brand organizes information: short punchy paragraphs vs. long explanatory ones, heavy use of lists vs. prose, direct address ("you") vs. third person.
5. **Point of view** — what the brand believes and stands for; the messaging pillars and values that show up as recurring themes (see `messaging_framework.md`).

### Extracting Voice from Inputs

| Input type | What to extract |
|---|---|
| Style guide document | Explicit rules — use these as ground truth first |
| Example copy (3+ pieces) | Actual sentence patterns, vocabulary, punctuation habits — often more reliable than stated rules |
| Adjective list only | Personality direction — pair with 1-2 example sentences you draft and confirm with the user before large-scale use |
| Verbal description ("we're like X but for Y") | Personality analog — identify the specific traits of the reference, not just its category |

### Voice Spectrum Placement

For each dimension, voice can be placed on a spectrum. Useful spectrums to reason with:

- Formal ←→ Casual
- Serious ←→ Playful
- Reserved ←→ Enthusiastic
- Authoritative ←→ Approachable
- Traditional ←→ Innovative
- Matter-of-fact ←→ Poetic/figurative

A brand voice is rarely at the extreme of any spectrum — it typically sits at a specific point on 3-4 of these, and that specific combination is what makes it distinctive. "Playful but authoritative" (e.g., a brand that jokes but is never wrong) is a much more useful description than "fun."

## Professional Guidance

- When only adjectives are given, always translate each into a spectrum position and a concrete "do/don't" sentence pair before writing at scale. This prevents drift where "bold" quietly becomes "aggressive" over a long document.
- When example copy conflicts with a stated style guide, trust the example copy — people write what actually reflects the brand more often than they update the guide.
- Re-anchor to the voice framework every few paragraphs on long documents; voice tends to drift toward generic AI-neutral phrasing over length.
- Distinguish **brand voice** (constant) from **tone** (contextual). A brand's voice doesn't change between a product page and an apology email, but its tone does.

## Examples

**Adjectives given:** "innovative, approachable, no-nonsense"
**Translated:**
- Innovative → uses forward-looking language, avoids clichés like "cutting-edge," prefers specific descriptions of what's new over vague superlatives.
- Approachable → contractions used, second person ("you"), no unexplained jargon.
- No-nonsense → short sentences, leads with the point, minimal hedging language ("might potentially," "in some cases").

**Do:** "Set it up once. It just works."
**Don't:** "Our solution has been meticulously engineered to deliver a seamless, frictionless user experience."

## Common Mistakes

- Treating adjectives as the entire voice definition instead of a starting point.
- Applying the same tone regardless of context (a "playful" brand should still be direct and clear in an error message, not jokey).
- Letting voice drift toward generic corporate/AI-neutral phrasing over the course of a long piece.
- Confusing personality with formatting (using exclamation points is not the same as being "enthusiastic" in substance).

## Best Practices

- Always confirm voice direction with a short example before large-scale application if voice signal is thin.
- Keep a running mental (or written) "voice fingerprint": 3-5 dimension placements plus 2-3 do/don't sentence pairs.
- Prioritize actual example copy over stated rules when they conflict.
- Re-check voice consistency at intervals in long documents.

## Summary

Brand voice is a multi-dimensional, checkable construct — personality, tone, language, structure, and point of view — not a single adjective. Extract it from the most concrete signal available (examples over adjectives), translate abstractions into do/don't pairs, and re-anchor periodically to prevent drift toward generic phrasing.
