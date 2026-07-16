# Prompt Library

Reusable internal prompts Claude can adapt when executing this skill.

---

## 1. Sequence Architecture Prompt
**Purpose**: Determine sequence type and structure before writing copy.
**Inputs**: user's goal, audience, offer.
**Instructions**: Identify the closest standard sequence type from `references/email_sequence_frameworks.md`. State the chosen architecture, number of emails, and one-sentence purpose per email before drafting any copy.
**Expected Output**: A numbered arc outline (not full copy yet).
**Validation Checklist**: [ ] Each email has a distinct purpose [ ] Length matches goal complexity [ ] Cadence stated

---

## 2. Subject Line Generation Prompt
**Purpose**: Generate high-open-rate subject lines for a specific email.
**Inputs**: email's strategic role, audience, tone.
**Instructions**: Generate 3 subject line options using different patterns from `references/subject_line_playbook.md` (curiosity, direct benefit, personal). Pick the strongest as primary, keep one as an A/B alternate.
**Expected Output**: Primary subject + 1 alternate + preview text.
**Validation Checklist**: [ ] Under 50 characters [ ] No spam-trigger words [ ] Preview text extends, doesn't repeat, subject

---

## 3. Body Copy Prompt
**Purpose**: Write the body of a single email.
**Inputs**: strategic role, chosen framework (AIDA/PAS/StoryBrand/value-first), audience, offer.
**Instructions**: Apply the chosen framework from `references/email_copywriting_frameworks.md`. Keep paragraphs to 1-3 sentences. End with exactly one CTA.
**Expected Output**: Full email body with one CTA.
**Validation Checklist**: [ ] One CTA only [ ] Matches chosen framework structure [ ] Mobile-skimmable formatting

---

## 4. CTA Prompt
**Purpose**: Write a specific, ownership-language CTA matched to sequence position.
**Inputs**: email's position in sequence, desired action, commitment level.
**Instructions**: Use first-person or specific phrasing per `references/cta_best_practices.md`. Match commitment level to trust built so far.
**Expected Output**: Button text + optional P.S. reinforcement line.
**Validation Checklist**: [ ] Specific, not generic [ ] Commitment level appropriate to sequence stage

---

## 5. Sequence Review/Diagnostic Prompt
**Purpose**: Review an existing sequence for redundancy or weak structure.
**Inputs**: existing sequence copy.
**Instructions**: Map each existing email to a strategic role; flag duplicated roles, missing arc steps, or multiple competing CTAs. Recommend a revised architecture.
**Expected Output**: Diagnostic table (email # / detected role / issue) + revision recommendation.
**Validation Checklist**: [ ] Every email mapped to a role [ ] Redundancies flagged [ ] Concrete fix suggested per issue

---

## 6. Cadence/Timing Prompt
**Purpose**: Recommend send timing across the sequence.
**Inputs**: sequence type, urgency of goal.
**Instructions**: Use standard cadence from `references/email_sequence_frameworks.md` unless user constraints require compression/expansion.
**Expected Output**: Day-by-day or trigger-based send schedule.
**Validation Checklist**: [ ] Cadence matches sequence type norms [ ] Any deviation explained

---

## 7. Editing/Tightening Prompt
**Purpose**: Tighten an overwritten email.
**Instructions**: Cut to the shortest version that preserves the hook, one core idea, and the CTA. Remove redundant sentences and filler transitions.
**Expected Output**: Tightened body copy, same CTA.
**Validation Checklist**: [ ] Core message intact [ ] Length reduced [ ] CTA unchanged

---

## 8. Personalization Prompt
**Purpose**: Add trigger-specific personalization beyond `{{first_name}}`.
**Instructions**: Reference the specific event that triggered the email (signup, cart abandon, milestone reached) in the opening line.
**Expected Output**: Personalized opening line variants.
**Validation Checklist**: [ ] References actual trigger event [ ] Feels natural, not templated

---

## 9. A/B Variant Prompt
**Purpose**: Produce a true A/B alternate (not a cosmetic tweak) for a critical email.
**Instructions**: Change the underlying angle (e.g., benefit-led vs. curiosity-led), not just wording.
**Expected Output**: Two structurally distinct subject/body variants.
**Validation Checklist**: [ ] Variants differ in angle, not just phrasing

---

## 10. Full Sequence Delivery Prompt
**Purpose**: Assemble and present the complete sequence to the user.
**Instructions**: Present each email in order with subject, preview, body, CTA, and one-line strategic note; close with a cadence summary table.
**Expected Output**: Complete formatted sequence ready for ESP upload.
**Validation Checklist**: [ ] All emails present [ ] Summary table included [ ] Consistent tone throughout
