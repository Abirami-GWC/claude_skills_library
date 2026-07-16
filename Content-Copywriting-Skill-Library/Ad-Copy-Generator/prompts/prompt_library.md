# Ad Copy Generator — Internal Prompt Library

---

## 1. Headline Generation Prompt

**Purpose:** Generate multiple genuinely distinct headline variations.

**Inputs:** Product/offer, value proposition, audience, channel, funnel stage.

**Instructions:**
1. Select 3-5 different frameworks from `references/headline_frameworks.md` appropriate to the funnel stage and channel.
2. Draft one headline per framework, each testing a distinct angle.
3. Check character limits for the specified channel.
4. Label each with its framework and angle.

**Expected Output:** 3-5 headlines, each labeled with framework/angle.

**Validation Checklist:**
- [ ] Each headline represents a genuinely different angle, not a reworded duplicate
- [ ] Character limits respected for the channel
- [ ] No invented statistics or claims

---

## 2. Full Ad Unit Prompt

**Purpose:** Produce a complete, channel-formatted ad (headline + body + CTA).

**Inputs:** Creative brief (see template), channel, chosen or requested angle(s).

**Instructions:**
1. Select a body-copy framework (AIDA/PAS/FAB/Before-After-Bridge/4 Ps) matching offer type.
2. Draft hook, body, and CTA following that framework.
3. Match CTA to funnel stage (see `references/cta_best_practices.md`).
4. Confirm channel format compliance.

**Expected Output:** Complete ad unit, channel-formatted, with brief rationale.

**Validation Checklist:**
- [ ] Body copy framework applied coherently start to finish
- [ ] CTA matches funnel stage
- [ ] Format fits channel constraints
- [ ] No fabricated proof points or urgency

---

## 3. CTA Generation Prompt

**Purpose:** Produce CTA options matched to funnel stage and channel.

**Inputs:** Funnel stage, channel, offer type, whether urgency/scarcity is genuinely real.

**Instructions:**
1. Identify appropriate commitment level (low-friction vs. high-commitment) for the funnel stage.
2. Draft 3-4 verb-led CTA options.
3. Only include urgency/scarcity language if confirmed real by the user.

**Expected Output:** 3-4 CTA options with funnel-stage rationale.

**Validation Checklist:**
- [ ] Commitment level matches funnel stage
- [ ] No fabricated urgency/scarcity
- [ ] CTAs are short, verb-led, specific where possible

---

## 4. Value Proposition Extraction Prompt

**Purpose:** Distill a clear, single-sentence value proposition from a longer product description.

**Inputs:** Product description, target audience.

**Instructions:**
1. Identify the single strongest benefit most relevant to the stated audience (not necessarily the most technically impressive feature).
2. State it as a concrete, specific outcome, not a vague superlative.
3. Offer 2-3 alternative value prop framings if the product has multiple strong angles.

**Expected Output:** 1-3 candidate value proposition statements.

**Validation Checklist:**
- [ ] Value prop is concrete and specific, not vague
- [ ] Matches audience's actual priorities, not just product features
- [ ] Traceable to information provided, nothing invented

---

## 5. Emotional Trigger Selection Prompt

**Purpose:** Identify appropriate emotional/psychological drivers for a given offer and audience, within ethical bounds.

**Inputs:** Offer, audience, funnel stage.

**Instructions:**
1. Consider pain avoidance, aspiration, social proof, authority, scarcity, reciprocity, ease (see `references/consumer_psychology.md`).
2. Select drivers proportionate to the actual stakes of the offer.
3. Flag and decline any driver that would require fabrication (fake urgency, invented proof) or disproportionate exploitation of fear/insecurity.

**Expected Output:** 2-3 recommended emotional angles with brief rationale, and explicit notes on any requested tactic that was declined and why.

**Validation Checklist:**
- [ ] All recommended drivers are usable with only real, supplied information
- [ ] No disproportionate fear/insecurity exploitation
- [ ] Declined tactics are explained with an honest alternative offered

---

## 6. Channel Adaptation Prompt

**Purpose:** Adapt one core ad concept across multiple channels correctly.

**Inputs:** Core ad concept/angle, list of target channels.

**Instructions:**
1. Identify each channel's format constraints and register norms (see `references/advertising_frameworks.md`).
2. Restructure (not just shorten/lengthen) the concept to fit each channel's natural conventions.
3. Preserve the core angle/value proposition across all versions.

**Expected Output:** One ad version per requested channel, each correctly formatted.

**Validation Checklist:**
- [ ] Each version respects its channel's format and register norms
- [ ] Core angle/value prop consistent across versions
- [ ] No copy-paste reuse that ignores channel differences

---

## 7. Ad Copy Critique / Diagnostic Prompt

**Purpose:** Diagnose why existing ad copy may be underperforming and recommend specific fixes.

**Inputs:** Existing ad copy, channel, funnel stage, (performance data if available).

**Instructions:**
1. Evaluate hook strength, value prop clarity, CTA/funnel match, and channel format compliance.
2. Identify the single most likely weak point rather than a scattershot list.
3. Recommend a specific, testable fix.

**Expected Output:** Structured diagnostic (see Ad Copy Diagnostic Template) + recommended fix.

**Validation Checklist:**
- [ ] Diagnosis is specific, not generic ("make it punchier")
- [ ] Recommended fix is concrete and testable
- [ ] Existing genuine strengths in the copy are noted, not just weaknesses

---

## 8. Multi-Angle Campaign Prompt

**Purpose:** Generate a full set of distinct angles for a multi-variant test campaign.

**Inputs:** Offer, audience (possibly multiple segments), channel, number of angles needed.

**Instructions:**
1. Identify 3-5 genuinely distinct value propositions or emotional angles for the offer.
2. Draft one full ad unit per angle.
3. Map angles to audience segments if segments are provided.

**Expected Output:** Campaign Messaging Matrix (see template) with one row per angle.

**Validation Checklist:**
- [ ] Angles are substantively different, not superficial rewordings
- [ ] Each angle-to-segment mapping is logical
- [ ] All ad units are channel-format-compliant

---

## 9. Compliance & Ethics Screening Prompt

**Purpose:** Screen a drafted or requested ad concept for manipulative tactics, unverifiable claims, or targeting concerns before finalizing.

**Inputs:** Draft ad copy or request description.

**Instructions:**
1. Check for fabricated urgency/scarcity, invented statistics/testimonials, disparagement of named real competitors, or disproportionate exploitation of fear/insecurity targeting vulnerable groups.
2. If found, do not include it; offer an honest alternative achieving a similar persuasive goal.
3. Note the substitution briefly to the user.

**Expected Output:** Cleared ad copy, or a flagged note plus an honest alternative.

**Validation Checklist:**
- [ ] No fabricated claims present in final copy
- [ ] No named-competitor disparagement
- [ ] Any declined tactic is explained with an alternative offered

---

## 10. Optimization / Iteration Prompt

**Purpose:** Improve copy that's already reasonably strong with targeted refinements.

**Inputs:** Current ad copy, goal for improvement (e.g., "improve CTR," "reduce bounce after click").

**Instructions:**
1. Identify the 1-2 highest-leverage changes (usually hook strength or CTA/funnel mismatch).
2. Make targeted edits; preserve what's already working.
3. Explain the specific hypothesis behind each change (what it should improve and why).

**Expected Output:** Refined copy + hypothesis-based rationale for each change.

**Validation Checklist:**
- [ ] Changes are targeted, not a full unnecessary rewrite
- [ ] Each change has a clear, testable hypothesis
- [ ] Original strengths preserved
