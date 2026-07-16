# Prompt Library

Reusable internal prompts Claude can adapt when executing this skill.

---

## 1. Page Architecture Prompt
**Purpose**: Determine page type and section map before writing copy.
**Inputs**: offer, price/commitment level, conversion goal.
**Instructions**: Select short-form/long-form/squeeze architecture from `references/landing_page_frameworks.md`. Output a section map before drafting full copy.
**Expected Output**: Ordered list of sections with one-line purpose each.
**Validation Checklist**: [ ] Page type matches commitment level [ ] Section order follows standard architecture

---

## 2. Hero Headline Prompt
**Purpose**: Generate a hero headline + subheadline that passes the 5-second test.
**Inputs**: product, audience, core outcome.
**Instructions**: Generate 3 headline variants using different patterns from `references/headline_frameworks.md`; select strongest; write a subheadline that adds mechanism/clarification, not repetition.
**Expected Output**: Primary headline + subheadline + 2 alternate headlines.
**Validation Checklist**: [ ] Passes 5-second clarity test [ ] Subheadline doesn't repeat headline

---

## 3. Benefits Section Prompt
**Purpose**: Convert features into benefit-framed copy with proof.
**Instructions**: For each feature, restate as a visitor outcome, then attach available proof (stat, example, testimonial) per `references/conversion_psychology.md`.
**Expected Output**: 3-5 benefit statements, each paired with supporting proof or a placeholder for proof.
**Validation Checklist**: [ ] Framed as outcomes, not just feature lists [ ] Each benefit has proof or a flagged gap

---

## 4. Social Proof Prompt
**Purpose**: Frame testimonials/stats for maximum credibility.
**Instructions**: Use specific numbers over round ones; place each proof point near the claim it supports per `references/conversion_psychology.md`.
**Expected Output**: Formatted testimonial blocks and/or stat callouts.
**Validation Checklist**: [ ] Numbers are specific, not rounded [ ] Proof tied to a specific claim on the page

---

## 5. Objection Handling / FAQ Prompt
**Purpose**: Surface and pre-answer the top objections.
**Instructions**: Identify 3-5 likely objections for this offer/audience; write each as a Q&A pair, ordered from most fundamental to most specific.
**Expected Output**: FAQ block.
**Validation Checklist**: [ ] Objections ordered fundamental-to-specific [ ] No major known objection left unaddressed

---

## 6. CTA Prompt
**Purpose**: Lock a single consistent CTA phrase and write supporting micro-copy.
**Instructions**: Choose one specific CTA phrase per `references/cta_best_practices.md`; reuse it verbatim at every placement; write micro-copy addressing the top hesitation.
**Expected Output**: CTA phrase + micro-copy, applied consistently across all placements.
**Validation Checklist**: [ ] Identical CTA phrase used everywhere [ ] Micro-copy addresses a real hesitation

---

## 7. Closing Section Prompt
**Purpose**: Write a closing section that reiterates value and drives final action.
**Instructions**: Recap the core value proposition in one line, restate the primary CTA, add risk-reversal language if applicable.
**Expected Output**: Closing headline + CTA + risk-reversal line.
**Validation Checklist**: [ ] Not just a bare CTA button with no context [ ] Risk reversal included if offer has a guarantee/trial

---

## 8. Full Page Assembly Prompt
**Purpose**: Assemble all sections into one delivered page.
**Instructions**: Present sections in order with brief rationale notes per section.
**Expected Output**: Complete section-by-section landing page copy.
**Validation Checklist**: [ ] All planned sections present [ ] Rationale note included per section [ ] CTA consistency verified across the full page

---

## 9. Landing Page Audit/Review Prompt
**Purpose**: Diagnose an existing landing page for conversion issues.
**Instructions**: Map existing sections against the standard architecture for that page type; flag missing proof, unaddressed objections, inconsistent CTAs, or unclear hero.
**Expected Output**: Diagnostic table (section / issue / fix) + prioritized recommendations.
**Validation Checklist**: [ ] Every existing section evaluated [ ] Fixes are specific and actionable

---

## 10. Tightening/Editing Prompt
**Purpose**: Tighten overwritten or unfocused section copy.
**Instructions**: Cut to the clearest version that preserves the core claim and its proof; remove redundant adjectives and filler.
**Expected Output**: Tightened section copy.
**Validation Checklist**: [ ] Core claim and proof intact [ ] Reduced word count without losing clarity
