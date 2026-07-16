# Brand Voice Writer — Testing Guide

## Purpose
Defines test cases and evaluation criteria to validate that this skill activates correctly, applies the frameworks correctly, and stays within scope.

## Positive Test Cases (skill should activate and perform well)

1. **Input:** Draft + 3 example pieces of on-brand copy → rewrite request.
   **Expected:** Voice fingerprint correctly extracted; rewrite matches sentence length, POV, contraction use of examples; rationale provided.

2. **Input:** Style guide document only, no examples → generate new content.
   **Expected:** Explicit rules from the guide applied; no invented brand facts.

3. **Input:** "Standardize terminology across these 5 docs."
   **Expected:** All inconsistent term instances found; single standard applied throughout; decision table produced.

4. **Input:** "Create a brand voice guide from these 5 posts."
   **Expected:** Completed Brand Messaging Guide template; inferred elements clearly marked as inferred.

5. **Input:** Apology/crisis email needing tone recalibration from a playful baseline voice.
   **Expected:** Humor and exclamation reduced; empathy/clarity/ownership prioritized; some brand personality marker retained.

## Negative Test Cases (skill should NOT fully activate / should redirect or decline)

6. **Input:** "Write me a Facebook ad for my product" with no brand voice material and no voice-matching request.
   **Expected:** Redirect toward Ad Copy Generator, or ask if a brand voice reference should be applied.

7. **Input:** "Write this in the exact voice of [specific real, active competitor company]."
   **Expected:** Declines close mimicry of a specific real company's proprietary identity; offers to build the user's own voice instead.

8. **Input:** A request with no brand signal at all ("just make it sound good").
   **Expected:** One clarifying question about voice signal, not an invented voice presented as confirmed.

## Boundary Cases

9. **Input:** Style guide and example copy conflict directly on a stylistic rule.
   **Expected:** Conflict explicitly flagged; example copy prioritized by default; user given the option to override.

10. **Input:** Only 1 example piece of copy provided (thin signal).
    **Expected:** Proceeds, but notes lower confidence in the extracted voice fingerprint and invites more examples if available.

11. **Input:** Long (10+ page) document where voice drifts partway through.
    **Expected:** Drift correctly identified and corrected using the strongest/most established section as reference; intentional register shifts (e.g., technical appendix) not mistakenly "corrected."

## Edge Cases

12. **Input:** Quoted customer testimonial within brand copy uses "wrong" terminology per the standardization rule.
    **Expected:** Quoted material preserved verbatim; standardization applied only to the brand's own writing.

13. **Input:** Mandatory legal/compliance language must appear verbatim even though it clashes with brand voice.
    **Expected:** Legal text preserved exactly; surrounding copy adjusted for voice; no unauthorized alteration of the mandatory text.

14. **Input:** Multiple sub-brands with different voices in the same request.
    **Expected:** Distinct fingerprints built per sub-brand; no blending.

## Evaluation Criteria

- **Fidelity:** Does the output match the extracted voice fingerprint (personality, spectrum placement, do/don't patterns)?
- **Accuracy:** Are all factual claims from the source preserved exactly, with zero invented facts/proof points?
- **Consistency:** Is terminology and formatting consistent throughout the deliverable?
- **Appropriateness:** Does tone match the situational context, not just the abstract brand adjectives?
- **Transparency:** Are inferred elements, conflicts, and assumptions clearly flagged rather than silently resolved?
- **Scope discipline:** Does the skill correctly redirect out-of-scope requests (channel-specific persuasion copy) to the appropriate sibling skill?
