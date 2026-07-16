# Testing Guide

## Purpose
Defines test cases and evaluation criteria to verify the skill produces correctly-structured, on-strategy email sequences.

## Positive Test Cases
1. "Write a 5-email welcome sequence for new SaaS subscribers." → Expect 5-email welcome architecture with escalating CTAs.
2. "Give me a cart abandonment flow for an online store." → Expect 3-email flow (reminder/objection/incentive) over 24-72 hrs.
3. "Create a win-back campaign for lapsed customers." → Expect 3-4 email re-engagement architecture ending in a clean exit CTA.
4. "Draft a product launch sequence for a 10-day campaign." → Expect teaser-through-last-call architecture spanning 10 days.
5. "Write an onboarding series for new app users." → Expect trigger/milestone-based cadence, not purely calendar-based.

## Negative Test Cases (should NOT fully trigger this skill / should redirect)
1. "Write me one email announcing our office closure." → Single standalone email; skill may assist but doesn't need full sequence architecture.
2. "Make this email sound more like our brand voice." → Should defer to brand-voice-writer logic, not sequence architecture.
3. "Write a Google Ads headline for our sale." → Out of scope; belongs to ad-copy-generator.
4. "Write our landing page hero section." → Out of scope; belongs to landing-page-copywriter.

## Boundary Cases
1. User asks for a "sequence" of exactly 1 email — clarify that a sequence implies multiple emails, or treat as a request to plan a future sequence starting with this one.
2. User asks for an extremely long sequence (15+ emails) — comply but flag redundancy risk and suggest consolidation points.
3. No audience given at all — infer generically but flag the assumption; do not block delivery entirely.

## Edge Cases
1. Conflicting instructions (e.g., "make it urgent" for an evergreen, non-deadline offer) — flag the tension and recommend authentic alternatives (scarcity via limited spots, not fake deadlines).
2. User provides an existing sequence with duplicate CTAs — diagnostic workflow should catch and flag this explicitly.
3. Sequence type not covered by standard frameworks (e.g., "internal employee sequence") — adapt closest framework and note limitations.

## Expected Outputs
Each test case should produce: correctly-numbered emails in send order, one CTA per email, subject+preview+body for each, and a cadence summary table.

## Evaluation Criteria
- **Structural correctness**: right number of emails, right architecture for sequence type (40%)
- **Copy quality**: subject lines earn opens, body follows chosen framework cleanly, CTAs are specific (30%)
- **Strategic coherence**: no redundant emails, clear progression toward the goal (20%)
- **Assumption handling**: missing inputs are inferred and stated, not silently guessed or blocking (10%)
