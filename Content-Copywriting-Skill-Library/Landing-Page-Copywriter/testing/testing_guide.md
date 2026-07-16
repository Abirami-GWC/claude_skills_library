# Testing Guide

## Purpose
Defines test cases and evaluation criteria to verify the skill produces correctly-structured, conversion-focused landing page copy.

## Positive Test Cases
1. "Write landing page copy for my new SaaS tool." → Expect short-form architecture with consistent CTA.
2. "I need a sales page for my $2,000 course." → Expect long-form architecture with heavy proof and objection handling.
3. "Write copy for a webinar registration page." → Expect squeeze-page architecture, minimal and focused.
4. "Review my landing page and tell me why it's not converting." → Expect diagnostic table + prioritized fixes.
5. "Write the hero section and FAQ for our product page." → Expect scoped section-level output, not a full unrequested page.

## Negative Test Cases (should NOT fully trigger this skill / should redirect)
1. "Write a Google Ads headline for our sale." → Belongs to ad-copy-generator.
2. "Write a 5-email welcome sequence." → Belongs to email-sequence-writer.
3. "Make this paragraph sound more like our brand voice." → Belongs to brand-voice-writer unless conversion structure is also involved.
4. "Write a blog post about industry trends." → Non-conversion content, handle directly without this skill.

## Boundary Cases
1. User requests a page with two equally-weighted conversion goals — skill should recommend one primary CTA and demote the other to secondary.
2. No proof points or testimonials available at all — skill should flag the gap rather than fabricate proof.
3. User wants an extremely long page for a low-commitment free offer — skill should flag the mismatch and recommend trimming.

## Edge Cases
1. User asks for fabricated urgency/scarcity not grounded in reality — skill declines to fabricate and offers genuine alternatives.
2. User provides an existing page with inconsistent CTA wording — audit workflow should explicitly flag this.
3. Legal/compliance disclosure needed (e.g., financial or health claims) — skill includes placeholder language and notes legal review is required, without fabricating compliance claims.

## Expected Outputs
Each test case should produce section-by-section copy (or a scoped subset if requested), a consistent CTA phrase throughout, proof placed near claims, and top objections addressed.

## Evaluation Criteria
- **Structural correctness**: right architecture for offer/commitment level, correct section order (40%)
- **Copy quality**: hero passes 5-second test, claims backed by proof, specific rather than vague language (30%)
- **Conversion logic**: single consistent CTA, objections addressed, risk reversal present where appropriate (20%)
- **Assumption handling**: missing inputs inferred and stated, not silently guessed or blocking (10%)
