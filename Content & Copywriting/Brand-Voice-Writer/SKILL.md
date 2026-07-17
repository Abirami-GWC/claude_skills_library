---
name: brand-voice-writer
description: Rewrites or generates content so it consistently matches a defined brand voice, tone, messaging framework, and writing style. Use whenever the user needs copy checked against, adapted to, or produced from a brand voice/style guide — including tone adjustments, terminology/voice consistency edits, and messaging alignment across any channel or industry. Do not use for channel-specific persuasion copy (ads, emails, landing pages) that has no brand-voice-matching component — route those to Ad Copy Generator, Email Sequence Writer, or Landing Page Copywriter instead.
---

# Brand Voice Writer

## Purpose

Brand Voice Writer takes any piece of content — a paragraph, a page, a full document, or a blank brief — and produces copy that consistently reflects a defined brand voice: its tone, personality, vocabulary, sentence rhythm, and messaging pillars. It is the "consistency layer" that sits underneath channel-specific copywriting skills, ensuring that whatever is written sounds like it came from one coherent brand rather than a generic AI.

This skill is deliberately industry-agnostic and company-agnostic. It works from whatever brand voice inputs the user supplies (a style guide, brand adjectives, example copy, or a described personality) — it does not assume or hardcode any specific company's voice.

## Business Value

- Protects brand equity by preventing tonal drift across writers, teams, agencies, and AI-generated content.
- Cuts brand review/editing cycles by producing on-voice drafts the first time.
- Lets organizations scale content production (blogs, support copy, social captions, internal comms, product copy) without diluting their identity.
- Turns an informal or incomplete brand voice ("we want to sound more like X") into a usable, referenceable framework.

## Activation Conditions

Claude should activate this skill when the user:
- Asks to rewrite, edit, or "voice-match" existing content to a brand's tone or style.
- Provides a style guide, brand voice document, or set of example copy and asks for new content in that voice.
- Asks whether a piece of copy "sounds on-brand," is "too formal/casual," or is "consistent" with other material.
- Asks to define, document, or formalize a brand voice, tone of voice, or messaging framework.
- Asks for terminology standardization (preferred terms, banned words, capitalization rules) across content.
- Asks to adapt one piece of on-brand content into a different format while preserving voice (e.g., "turn this blog post into a voice-consistent internal memo").

## Trigger Examples

- "Rewrite this paragraph so it sounds more like our brand voice — here's our style guide."
- "Does this product description match the tone in these three example posts?"
- "We're playful and irreverent, but this draft reads corporate. Fix it."
- "Create a one-page brand voice guide from these five sample pieces of our content."
- "Standardize terminology across these support articles — we use both 'sign in' and 'log in' inconsistently."
- "Take this formal press release and rewrite it in our friendly, plain-English voice."

## When NOT To Use

- The request is purely about persuasive structure or conversion mechanics with no voice-matching component (e.g., "write me a Facebook ad" with no brand voice reference) — use **Ad Copy Generator**.
- The request is for a full email nurture sequence or drip campaign strategy — use **Email Sequence Writer** (this skill can still be invoked afterward, or alongside, to voice-check the output).
- The request is for full landing page copy/structure (hero, FAQ, objection handling) — use **Landing Page Copywriter**.
- The request has nothing to do with brand tone/voice/messaging at all (e.g., pure grammar fix with no stylistic dimension, unrelated coding or data tasks).
- The user asks Claude to impersonate or write as a specific real, named public figure or real company it has no legitimate connection to — decline per standard persuasive-content and impersonation guidelines regardless of "brand voice" framing.

## Scope

In scope: tone calibration, brand personality expression, vocabulary/terminology consistency, sentence-level style, messaging pillar alignment, style guide creation and application, cross-format voice adaptation, before/after tone edits.

Out of scope: channel-specific conversion frameworks (AIDA ad structures, email drip sequencing, landing page layout) — those live in their respective skills. Legal/compliance review, translation/localization, and SEO keyword strategy are out of scope (flag to the user if relevant).

## Inputs

Claude should gather (ask only if genuinely missing and needed — see `references/glossary.md` for term definitions):
- The content to be written or rewritten (or a brief describing what's needed).
- Brand voice signal: a style guide, 3-5 adjectives describing the brand, example "on-voice" copy, or a completed Brand Messaging Guide (see `templates/`).
- Audience and context (who reads this, on what channel, why).
- Any hard constraints: banned words, required terminology, reading-level target, length limit, compliance language.

If no brand voice information is supplied at all, Claude should ask the user for at least one of: adjectives, example copy, or a style guide — rather than inventing a voice. A brief clarifying question is appropriate here since proceeding without it produces ungrounded work.

## Outputs

- Brand-aligned copy (rewritten or newly generated).
- A short "voice rationale" noting key choices (word swaps, tone shifts, structural changes) when the task is an edit of existing copy.
- Optionally: a reusable brand voice/style guide artifact if the user is trying to formalize their voice.
- Optionally: a terminology/consistency table when the task involves standardizing language across multiple pieces.

## Workflow

1. **Identify the voice signal.** Extract tone attributes, sentence patterns, vocabulary, and personality markers from whatever brand input is provided (see `references/brand_voice_framework.md`).
2. **Identify the gap** (for edits). Compare the draft against the target voice: where is it too formal, too generic, off in vocabulary, or structurally inconsistent?
3. **Apply the messaging framework**, if one exists, to make sure core value props/pillars are represented, not just tone (see `references/messaging_framework.md`).
4. **Draft or rewrite** the content, applying tone, vocabulary, sentence rhythm, and terminology rules (see `references/tone_of_voice_guide.md` and `references/editorial_standards.md`).
5. **Self-check** against the relevant checklist in `checklists/` before returning the result.
6. **Explain key changes** briefly if this was an edit, so the user can learn the pattern and apply it themselves next time.

## Reasoning Guidelines

- Voice is expressed through more than adjectives — attend to sentence length, contraction use, punctuation habits (em dashes vs. periods), address (you/we), humor, formality, and figurative language.
- When brand inputs conflict (e.g., style guide says "formal" but example copy is casual), prioritize the example copy — actual usage is a stronger signal than stated aspiration — and flag the conflict to the user.
- Don't over-correct: preserve the parts of a draft that already work; edit only what breaks voice.
- Never invent brand facts, claims, or specific product details not present in the source material.

## Best Practices

- Show, don't just tell: when defining a voice, use example sentences (do/don't pairs) rather than only abstract adjectives.
- Keep terminology consistent within a single deliverable and flag inconsistencies across a batch.
- Match register to channel even within one voice (a playful brand is still slightly more restrained in a legal disclaimer than in a tweet) — note this rather than flattening everything identically.
- Favor concrete, specific brand language over vague marketing-speak ("empowering synergistic solutions") even when asked to sound "professional."

## Validation Rules

- Every rewrite must preserve the factual content and claims of the source (no invented statistics, features, or promises).
- Terminology must be applied consistently within the deliverable.
- Tone must match the audience/channel constraints given, not just the abstract brand adjectives.
- Output must not silently drop required compliance/legal language if the user flagged any as mandatory.

## Error Handling

- If brand voice signal is absent or contradictory, ask one clarifying question or proceed with a clearly labeled default/neutral-professional voice and flag the assumption.
- If the source content contains claims Claude cannot verify (pricing, stats, legal claims), preserve them as-is but note they should be fact-checked by the user rather than altering their meaning.
- If a request would require impersonating a real named individual or unaffiliated real brand, decline and offer a fictional or generalized alternative.

## Limitations

- Cannot access a company's actual internal brand guidelines unless the user provides them.
- Cannot guarantee legal/regulatory compliance of resulting copy.
- Voice matching quality depends heavily on the quality and amount of example material provided.

## Success Criteria

- A reader familiar with the brand would find the output indistinguishable in voice from the brand's other material.
- Terminology and tone are consistent within the deliverable.
- No factual drift from source content.
- The user can articulate why each major edit was made from the rationale provided.
