# Ad Copy Generator — Worked Examples

---

### Example 1: Google Search headlines for a SaaS product

**User Request:** "Write 5 Google Search headline variations for our invoicing app for freelancers."

**Why the Skill Activates:** Direct channel-specific headline request.

**Workflow:** Confirm/assume Search (intent-driven, direct) → select 3-5 distinct frameworks → check ~30-char limit.

**Expected Output:** 5 headlines, each a different framework/angle, all within character limits.

**Final Response:** "Invoice Software for Freelancers" (direct benefit) / "Get Paid 2 Weeks Faster" (outcome) / "Still Chasing Client Payments?" (problem-agitate) / "Free 14-Day Trial, No Card" (offer/specificity) / "Built for Solo Freelancers" (identity).

**Alternative Response:** If audience is agencies rather than solo freelancers, swap identity-naming headline accordingly.

**Edge Cases:** If the product has no free trial, remove the "Free 14-Day Trial" headline rather than inventing an offer.

---

### Example 2: Meta ad hook for a skincare product

**User Request:** "Give me 3 Meta ad hooks that lead with a pain point, for a skincare product targeting people with sensitive skin."

**Why the Skill Activates:** Channel-specific hook generation request.

**Workflow:** Select problem-agitate framework variants → front-load hook for feed truncation → check emotional-driver proportionality (sensitive skin frustration is legitimate, not exploiting insecurity disproportionately).

**Expected Output:** 3 problem-agitate hooks, feed-appropriate length.

**Final Response:** Three hooks such as: "Tired of products that promise 'gentle' and still leave you red and irritated?" — each distinct in specific pain articulated.

**Alternative Response:** If the user wants an aspirational angle instead, switch to Before/After/Bridge framework.

**Edge Cases:** Avoid language that manufactures body-image insecurity beyond the real, stated skin-sensitivity problem.

---

### Example 3: LinkedIn ad for B2B, targeting HR directors

**User Request:** "LinkedIn ad copy targeting HR directors — professional tone, focus on ROI."

**Why the Skill Activates:** Channel + audience + tone specification for ad copy.

**Workflow:** Apply LinkedIn register norms (credibility/specificity over casual curiosity) → FAB framework for ROI-focused B2B audience → note fixed CTA button list constraint.

**Expected Output:** Primary text + headline + CTA recommendation, professional register.

**Final Response:** Delivered ad emphasizing a concrete ROI figure (if supplied) or process improvement, closing with a LinkedIn-standard CTA like "Learn more."

**Alternative Response:** If no real ROI figure was supplied, use a process/outcome-based FAB structure instead of inventing a percentage.

**Edge Cases:** If user supplies a specific real ROI stat, use it exactly; do not round up or embellish it.

---

### Example 4: Diagnosing weak existing ad copy

**User Request:** "Rewrite this ad — the CTA is weak and the hook doesn't grab attention." (Pastes existing ad.)

**Why the Skill Activates:** Explicit iteration/critique request.

**Workflow:** Run the Ad Copy Diagnostic — assess hook strength, value prop clarity, CTA/funnel match → identify the primary weak point → apply targeted fix, not full rewrite.

**Expected Output:** Diagnostic notes + revised copy.

**Final Response:** "The hook led with a feature ('cloud-based') instead of the benefit — swapped to a problem-agitate hook. The CTA ('Click Here') didn't match your funnel stage (this looks like consideration-stage retargeting) — swapped to 'See your custom quote.'"

**Alternative Response:** If performance data is available (e.g., "CTR is fine but conversions are low"), diagnosis shifts toward CTA/landing-page mismatch rather than hook weakness.

**Edge Cases:** If the original ad's weak CTA was actually intentional (e.g., brand style deliberately avoids hard-sell CTAs), confirm with user before overriding that choice.

---

### Example 5: Emotional trigger brainstorm

**User Request:** "What are some emotional triggers I could use for a fitness app ad besides fear of missing out?"

**Why the Skill Activates:** Direct request for emotional-trigger strategy.

**Workflow:** Draw from the driver list (pain avoidance, aspiration, social proof, reciprocity, ease) excluding FOMO/scarcity as requested.

**Expected Output:** 3-4 alternative driver options with example headline snippets for each.

**Final Response:** Aspiration/identity ("become the person who never skips leg day"), ease-of-action ("workouts that fit in 15 minutes"), pain-avoidance ("stop starting over every January"), reciprocity (offering a free personalized plan).

**Alternative Response:** If the user wants only rational/logical drivers (no emotional appeal at all), pivot toward FAB-style feature/benefit framing instead.

**Edge Cases:** Avoid disproportionate body-image fear appeals even under "pain avoidance."

---

### Example 6: Display ad banner set

**User Request:** "Display ad banner set — headline + subhead + CTA — for retargeting cart abandoners."

**Why the Skill Activates:** Channel-specific format + funnel stage (retargeting) specified.

**Workflow:** Apply Display's minimal-copy convention → retargeting funnel stage → direct benefit/reminder framing, not curiosity (no room to pay it off) → high-commitment CTA.

**Expected Output:** Very short headline + subhead + CTA, retargeting-appropriate.

**Final Response:** Headline: "Still thinking it over?" Subhead: "Your cart's waiting — plus free shipping today." CTA: "Finish your order."

**Alternative Response:** If the user hasn't confirmed free shipping is real/available today, remove that specific claim and use a generic reminder instead.

**Edge Cases:** Do not fabricate a discount or shipping offer not confirmed by the user.

---

### Example 7: Multi-angle test campaign

**User Request:** "Give me 4 different angles for ads promoting our budgeting app, I want to test which resonates."

**Why the Skill Activates:** Explicit multi-variant test request.

**Workflow:** Identify 4 genuinely distinct angles (time-saving, stress-reduction, control/confidence, specific-savings-outcome) → draft one ad unit per angle → fill Campaign Messaging Matrix.

**Expected Output:** 4-row matrix, each with headline, primary text summary, and CTA.

**Final Response:** Delivered matrix with a one-line rationale per angle so the user understands what's actually being tested.

**Alternative Response:** If the user has 2 known audience segments, map 2 angles to each segment instead of testing all 4 against everyone.

**Edge Cases:** If one angle would require an unverified statistic ("average user saves $X/month"), only include it if the user confirms the number is real.

---

### Example 8: Ambiguous/missing channel

**User Request:** "Write some ad copy for my new productivity app."

**Why the Skill Activates:** Ad copy request, but channel unspecified.

**Workflow:** Recognize channel ambiguity materially affects format → ask one clarifying question before drafting extensively.

**Expected Output:** Clarifying question: "Happy to help — which channel(s) are you running this on (Google Search, Meta/Instagram, LinkedIn, Display), and what's the campaign goal?"

**Final Response:** Question only, or a general-purpose draft explicitly labeled as channel-agnostic if the user wants to see direction first.

**Alternative Response:** If the user says "just give me something to start," provide a general AIDA-structured concept and note it'll need channel-specific reformatting.

**Edge Cases:** If multiple channels are named at once, produce channel-adapted versions of the same core angle rather than one-size-fits-all copy.

---

### Example 9: Declining a manipulative request

**User Request:** "Add a countdown timer saying '2 hours left!' to create urgency, even though the sale doesn't actually end."

**Why the Skill Activates:** Ad copy request, but includes a fabricated-urgency element.

**Workflow:** Identify fabricated urgency as a dark pattern per `references/consumer_psychology.md` → decline that specific element → offer an honest alternative.

**Expected Output:** Explanation + honest alternative (e.g., genuine low-friction CTA, or urgency only if a real end date exists).

**Final Response:** "I won't add a fake countdown since the sale doesn't actually end then — that's the kind of claim that erodes trust if noticed, and can violate ad platform policies. If there's a real deadline, I'm glad to build urgency around that. Otherwise, here's a strong version leaning on [real benefit] instead."

**Alternative Response:** If the user clarifies there is a real, different end date, use that instead.

**Edge Cases:** If the user pushes back insisting it's "just marketing," maintain the same position and offer the honest alternative rather than complying.

---

### Example 10: Competitor disparagement request

**User Request:** "Write an ad that says [specific real named competitor] is unreliable and overpriced compared to us."

**Why the Skill Activates:** Ad copy request involving a named real competitor and unverifiable disparaging claims.

**Workflow:** Recognize disparagement of a specific real company with unverifiable claims as out of scope/risky → redirect toward a comparison based on the user's own verifiable strengths without naming or disparaging the competitor.

**Expected Output:** Ad copy emphasizing the user's own genuine advantages (if supplied) without naming or making unverifiable claims about the competitor.

**Final Response:** "I'd avoid directly disparaging a named competitor with unverifiable claims — that carries legal and trust risk. I can write strong copy that emphasizes your specific advantages instead, without needing to name or attack them directly."

**Alternative Response:** If the user has a verifiable, sourced factual comparison (e.g., publicly published pricing), a factual, non-disparaging comparison may be reasonable — confirm the claim is accurate and sourced first.

**Edge Cases:** General category comparisons ("unlike traditional tools...") without naming a specific real competitor are generally fine.

---

### Example 11: Brand voice interplay

**User Request:** "Write Meta ad copy for our app — here's our brand voice guide, we're playful and irreverent."

**Why the Skill Activates:** Ad copy request with brand voice constraint supplied.

**Workflow:** Respect the supplied voice (playful, irreverent) while applying ad-conversion structure (hook, framework, CTA) — this skill applies the voice but doesn't formalize/audit it (that's Brand Voice Writer's job).

**Expected Output:** Ad copy in the specified voice, structurally sound per ad frameworks.

**Final Response:** Delivered copy with a playful, irreverent hook and tone, still following a clear PAS or AIDA structure and appropriate CTA.

**Alternative Response:** If the user wants a full brand voice consistency audit across many pieces, note that's better handled by Brand Voice Writer and offer to hand off.

**Edge Cases:** Irreverent tone should still avoid disparaging real competitors or making unverifiable claims — voice doesn't override the ethics/validation rules.
