# Brand Voice Writer — Internal Prompt Library

These are internal reasoning prompts Claude can use (mentally or as explicit self-instructions) when performing brand voice tasks. Each includes purpose, inputs, instructions, expected output, and a validation checklist.

---

## 1. Brand Voice Extraction Prompt

**Purpose:** Derive a usable voice fingerprint from whatever brand signal the user provides.

**Inputs:** Style guide text and/or 3+ example pieces of copy and/or a list of adjectives.

**Instructions:**
1. If example copy is provided, analyze sentence length, contraction use, punctuation habits, point of view, and figurative language across all samples.
2. If adjectives are provided, translate each into a spectrum placement and one do/don't sentence pair.
3. If both are provided and they conflict, prioritize example copy; note the conflict.
4. Produce a voice fingerprint: personality (2-3 words), 3-4 spectrum placements, 2-3 do/don't pairs.

**Expected Output:** A concise voice fingerprint (under 150 words) ready to apply to drafting.

**Validation Checklist:**
- [ ] Fingerprint is grounded in provided material, not invented
- [ ] Conflicts between sources are flagged, not silently resolved
- [ ] Do/don't pairs are concrete sentences, not abstract restatements of adjectives

---

## 2. Brand Voice Rewrite Prompt

**Purpose:** Rewrite existing content to match a defined voice while preserving meaning.

**Inputs:** Original content, voice fingerprint or style guide, any terminology/banned-word rules.

**Instructions:**
1. Read the full original for meaning and claims before editing.
2. Identify voice mismatches: formality level, sentence structure, vocabulary, point of view.
3. Rewrite sentence by sentence, preserving all factual claims exactly.
4. Apply terminology rules consistently.
5. Produce a short rationale of major changes.

**Expected Output:** Rewritten copy + 2-4 bullet rationale of key changes.

**Validation Checklist:**
- [ ] No factual claims added, removed, or altered
- [ ] Terminology consistent throughout
- [ ] Tone appropriate to context, not just to abstract brand adjectives
- [ ] Rationale is specific, not generic ("improved flow")

---

## 3. Tone Calibration Prompt

**Purpose:** Adjust tone for a specific situational context without changing underlying voice.

**Inputs:** Draft content, situation type (celebration/error/complaint/legal/etc.), brand voice fingerprint.

**Instructions:**
1. Map the situation to the tone matrix (see `references/tone_of_voice_guide.md`).
2. Identify the appropriate energy/formality level for this situation.
3. Adjust humor, exclamation, and enthusiasm markers up or down accordingly — never remove all brand personality.
4. Prioritize clarity and empathy in negative or high-stakes situations.

**Expected Output:** Tone-adjusted copy appropriate to the specific situation.

**Validation Checklist:**
- [ ] Tone matches the emotional stakes of the situation
- [ ] Some brand personality marker remains even at the most restrained end
- [ ] No humor at the reader's expense in negative-state content

---

## 4. Terminology Consistency Audit Prompt

**Purpose:** Identify and fix inconsistent terminology across one or multiple documents.

**Inputs:** One or more documents, any stated terminology preferences.

**Instructions:**
1. Scan for terms referring to the same concept used inconsistently (e.g., "sign in" vs. "log in").
2. Determine (from stated preference, frequency, or most recent usage) which term should be standard.
3. Flag every instance needing correction; correct if asked to edit directly.
4. Produce a terminology table of decisions made.

**Expected Output:** Corrected document(s) + terminology decision table.

**Validation Checklist:**
- [ ] Every inconsistency found and listed
- [ ] Chosen standard term is applied everywhere, not partially
- [ ] Decisions are explainable, not arbitrary

---

## 5. Brand Voice Guide Creation Prompt

**Purpose:** Formalize an implicit brand voice into a documented, reusable guide.

**Inputs:** Multiple example pieces of existing content (ideally 5+).

**Instructions:**
1. Extract recurring patterns across all samples: sentence structure, vocabulary, point of view, punctuation, recurring phrases.
2. Identify 3-5 adjectives that describe the resulting personality.
3. Place the voice on 3-4 spectrums.
4. Extract likely messaging pillars from recurring themes.
5. Fill out the Brand Messaging Guide template.
6. Flag any inferred elements as inferred, and invite user confirmation.

**Expected Output:** A completed Brand Messaging Guide (see `templates/templates.md`), with inferred elements marked.

**Validation Checklist:**
- [ ] Every element traces back to actual patterns in the samples
- [ ] Inferred (vs. explicit) elements are clearly marked
- [ ] Guide is usable directly for future drafting

---

## 6. Editing & Proofreading Prompt

**Purpose:** Apply baseline editorial standards independent of brand voice.

**Inputs:** Draft content.

**Instructions:**
1. Check grammar, tense, and point-of-view consistency.
2. Check sentence-level clarity: flag buried verbs, unnecessary passive voice, stacked prepositional phrases.
3. Check formatting consistency (heading case, list style).
4. Do not alter brand-voice-specific stylistic choices (e.g., don't "fix" intentional sentence fragments if they match a punchy voice).

**Expected Output:** Copyedited content with a brief list of corrections made.

**Validation Checklist:**
- [ ] No new grammar/mechanics errors introduced
- [ ] Voice-appropriate stylistic choices preserved, not "corrected" away
- [ ] Formatting is internally consistent

---

## 7. Voice Review / QA Prompt

**Purpose:** Assess whether a finished piece matches a defined voice, without rewriting it.

**Inputs:** Finished content, voice fingerprint or style guide.

**Instructions:**
1. Compare content against each dimension: personality, tone, language, structure, point of view.
2. Compare against messaging pillars if relevant.
3. Identify specific lines that are on-voice and off-voice, with reasons.
4. Give an overall verdict: on-voice / partially on-voice / off-voice, with specific fixes needed.

**Expected Output:** A structured review with specific line-level feedback, not just a general impression.

**Validation Checklist:**
- [ ] Feedback references specific lines, not vague impressions
- [ ] Both strengths and issues are noted
- [ ] Verdict is actionable (tells the user exactly what to change)

---

## 8. Cross-Format Voice Adaptation Prompt

**Purpose:** Take on-voice content in one format and adapt it to a different format while preserving voice.

**Inputs:** Original content, target format (e.g., blog post → internal memo, product page → social caption).

**Instructions:**
1. Identify what must change structurally for the new format (length, structure conventions, level of formality typically expected in that format).
2. Preserve the voice fingerprint and any core messaging pillars used.
3. Do not simply shorten/lengthen mechanically — restructure to fit the new format's natural conventions.

**Expected Output:** Adapted content appropriate to the new format, still recognizably on-voice.

**Validation Checklist:**
- [ ] Adapted content follows the new format's natural conventions
- [ ] Voice and key messaging preserved
- [ ] No factual drift from the original

---

## 9. Voice Conflict Resolution Prompt

**Purpose:** Handle cases where stated brand guidance conflicts with actual usage patterns or with a specific channel's norms.

**Inputs:** Style guide, example copy, and/or channel context that appear to conflict.

**Instructions:**
1. Identify the specific point of conflict precisely (e.g., "guide says formal; three of four examples use contractions").
2. Default to actual usage patterns (example copy) over stated aspiration, unless the user indicates the guide reflects an intentional recent change.
3. Flag the conflict explicitly to the user rather than silently picking a side.

**Expected Output:** A resolved voice direction plus an explicit note of the conflict and the reasoning for how it was resolved.

**Validation Checklist:**
- [ ] Conflict is named specifically
- [ ] Resolution reasoning is stated, not assumed
- [ ] User is given the chance to correct the resolution if wrong

---

## 10. Optimization / Iteration Prompt

**Purpose:** Improve a piece that is already roughly on-voice but not yet strong — a polish pass rather than a full rewrite.

**Inputs:** Draft that is already voice-aligned, goal for the piece.

**Instructions:**
1. Identify the 2-4 highest-impact improvements (usually: opening line strength, redundant phrasing, weak verbs, missing specificity).
2. Make targeted edits rather than a full rewrite.
3. Preserve everything that already works.

**Expected Output:** Lightly polished version + short list of what was changed and why.

**Validation Checklist:**
- [ ] Edits are targeted, not a full unnecessary rewrite
- [ ] Voice and meaning fully preserved
- [ ] Each change has a clear rationale
