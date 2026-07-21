# Brand Voice Writer — Worked Examples

---

### Example 1: Basic tone rewrite with example copy provided

**User Request:** "Rewrite this paragraph to sound more like us. Here are three of our recent blog intros: [samples showing short sentences, second person, contractions, occasional humor]."

**Why the Skill Activates:** User wants existing content rewritten to match a voice signal (example copy) — a direct match for Brand Voice Writer's core purpose.

**Workflow:** Extract voice fingerprint from the 3 samples (short sentences, "you," contractions, light humor) → identify mismatches in the draft (long sentences, third person, no contractions) → rewrite sentence by sentence → produce rationale.

**Expected Output:** Rewritten paragraph + 2-3 bullet rationale (e.g., "switched to second person and shortened sentences to match your sample intros").

**Final Response:** Delivers the rewrite with a brief "why" note, offers to apply the same treatment to more content if there's a larger batch.

**Alternative Response:** If only one sample were provided instead of three, Claude would note the voice signal is thinner and its confidence is correspondingly lower, while still proceeding.

**Edge Cases:** If the three samples actually differ significantly from each other in style, flag the inconsistency rather than averaging them silently.

---

### Example 2: No brand voice info provided at all

**User Request:** "Make this sound more on-brand." (No style guide, no examples, no adjectives.)

**Why the Skill Activates:** Clear brand-voice request, but missing the essential input.

**Workflow:** Recognize the essential input (voice signal) is missing → ask one clarifying question rather than guessing.

**Expected Output:** A short clarifying question: "Happy to — could you share a style guide, a few examples of your existing content, or 3-5 adjectives that describe your brand?"

**Final Response:** Question only; no invented voice applied.

**Alternative Response:** If the user has no formal materials, Claude could offer to build a voice fingerprint from a verbal description ("we're like a knowledgeable friend, not a salesperson").

**Edge Cases:** If the user insists Claude "just guess," proceed with a clearly labeled neutral-professional default and flag it as a guess, not a confirmed brand voice.

---

### Example 3: Conflicting style guide and example copy

**User Request:** "Our style guide says formal, no contractions — but check if this draft matches our voice." (Attached examples all use contractions and casual phrasing.)

**Why the Skill Activates:** Voice-consistency check with brand material provided.

**Workflow:** Detect the conflict between stated rule and actual usage → apply the framework's rule of prioritizing example copy → flag conflict explicitly.

**Expected Output:** Review noting the draft is actually more consistent with the real usage patterns than with the written style guide, and a recommendation to update the guide or clarify intent.

**Final Response:** "Your style guide says no contractions, but all three of your recent examples use them freely — I've evaluated the draft against your actual usage, which it matches well. You may want to update the written guide to reflect current practice, or let me know if the formal rule is a recent intentional change."

**Alternative Response:** If the user confirms the formal rule is a deliberate recent shift, Claude re-evaluates against the stated guide instead.

**Edge Cases:** Guide and examples conflict on a claim-affecting point (e.g., what to call the product) — treat this as higher-stakes and always flag rather than silently choosing.

---

### Example 4: Formalizing a brand voice guide from scratch

**User Request:** "Create a one-page brand voice guide from these five blog posts."

**Why the Skill Activates:** Direct request to formalize/document a voice — core activation trigger.

**Workflow:** Analyze all 5 samples for recurring patterns → derive personality adjectives, spectrum placements, messaging pillars → fill out the Brand Messaging Guide template → mark inferred elements.

**Expected Output:** A completed one-page guide using the template in `templates/templates.md`.

**Final Response:** Delivered guide with a note that pillars/personality were inferred from the 5 samples and should be confirmed by the brand team.

**Alternative Response:** If fewer than 3 samples were given, Claude would note the inference is lower-confidence and recommend more samples for a robust guide.

**Edge Cases:** If the 5 posts were written by different people with visibly different styles, note the inconsistency rather than averaging it into a falsely coherent voice.

---

### Example 5: Terminology consistency audit across multiple documents

**User Request:** "We use 'sign in' and 'log in' inconsistently across our help center — standardize it."

**Why the Skill Activates:** Direct terminology-consistency request, a named activation trigger.

**Workflow:** Scan all provided documents for both terms → determine frequency/preference (or ask if unclear) → apply chosen standard throughout → produce a terminology decision table.

**Expected Output:** Corrected documents + a table showing what was standardized.

**Final Response:** "I standardized on 'sign in' since it appeared in 80% of your existing docs and is the term used in your product UI. Updated all instances across the 6 articles — here's the change table."

**Alternative Response:** If frequency was roughly 50/50, ask the user which term matches current product UI rather than guessing.

**Edge Cases:** A quoted user review or testimonial contains the "wrong" term — preserve it verbatim since it's someone else's words, not brand copy.

---

### Example 6: Tone recalibration for a negative-state message

**User Request:** "This outage apology email still sounds too jokey for what it is. We're normally playful but this is bad."

**Why the Skill Activates:** Tone adjustment request tied to brand voice.

**Workflow:** Map situation to tone matrix (outage/apology = serious, high empathy needed) → dial down humor/exclamation markers → preserve some core personality (directness, human warmth) → keep clarity and ownership prominent.

**Expected Output:** Rewritten email: direct, honest, empathetic, minimal humor, still recognizably the same brand's voice underneath.

**Final Response:** Delivered rewrite with rationale: "Removed the joke and exclamation points, kept the direct 'here's exactly what happened and what we're doing' structure that's core to your voice."

**Alternative Response:** If the user wants zero personality at all (fully neutral corporate tone), Claude complies but notes this may read as generic.

**Edge Cases:** If legal/compliance language must be included verbatim, preserve it exactly even if it clashes stylistically, and note it can't be altered.

---

### Example 7: Cross-format adaptation

**User Request:** "Turn this on-voice blog post into a short internal Slack announcement, same voice."

**Why the Skill Activates:** Cross-format voice adaptation is an explicit in-scope task.

**Workflow:** Identify Slack-announcement conventions (very short, scannable, casual internal register) → preserve voice fingerprint and core message → restructure rather than mechanically truncate.

**Expected Output:** A short, voice-consistent Slack message capturing the key point of the blog post.

**Final Response:** Delivered adaptation, noting which points from the blog post were dropped as non-essential for the shorter format.

**Alternative Response:** If the user wanted every detail preserved, Claude would note that a Slack announcement of that length would undercut the format's purpose and suggest a linked "read more."

**Edge Cases:** Internal audience may tolerate more jargon/informality than external audience — adjust register accordingly even within the same voice.

---

### Example 8: Voice QA/review without rewriting

**User Request:** "Don't rewrite it — just tell me if this matches our brand voice guide." (Style guide attached.)

**Why the Skill Activates:** Voice consistency check is explicitly requested, without an edit.

**Workflow:** Compare the piece against each voice dimension from the guide → identify specific on-voice and off-voice lines → give an overall verdict.

**Expected Output:** Structured review: verdict + line-level notes, no rewritten content.

**Final Response:** "Overall: partially on-voice. Paragraph 1 matches well (short sentences, second person). Paragraph 3 drifts into passive, formal phrasing ('it is recommended that users...') that doesn't match your direct, active style guide."

**Alternative Response:** If asked afterward, Claude can then offer the rewrite as a follow-up, but respects the "don't rewrite" instruction first.

**Edge Cases:** If the content is fully on-voice, say so clearly and briefly rather than manufacturing critique.

---

### Example 9: Voice adjectives only, no examples

**User Request:** "We're 'bold, witty, and precise.' Write a short product announcement in that voice."

**Why the Skill Activates:** Voice generation request from adjective-only signal.

**Workflow:** Translate each adjective into spectrum placement + do/don't sentence pair → draft a short do/don't confirmation implicitly through word choice → write the announcement.

**Expected Output:** A short announcement using confident, punchy, precise language (no hedging, no filler).

**Final Response:** Delivered draft; briefly notes how "bold/witty/precise" were interpreted (e.g., "precise" → no vague superlatives, specific claims only) so the user can correct direction if it's off.

**Alternative Response:** If the user provided a real example afterward that contradicted this interpretation, prioritize the example on the next pass.

**Edge Cases:** "Bold" claims must still be factually accurate — bold in delivery, not in overstating capabilities.

---

### Example 10: Batch consistency check across many pieces

**User Request:** "Check these 8 product descriptions for voice consistency with each other — we don't have a formal guide, just want them to feel like one brand."

**Why the Skill Activates:** Multi-document voice consistency task, no formal guide required.

**Workflow:** Analyze all 8 for internal consistency (not against an external guide) → identify the piece(s) that deviate from the majority pattern → produce a voice consistency table.

**Expected Output:** Table showing which descriptions are consistent and which deviate, with specific reasons.

**Final Response:** "6 of 8 are consistent (short, benefit-led sentences, second person). Descriptions 3 and 7 shift into passive, feature-list style — here's exactly where they diverge and suggested edits."

**Alternative Response:** If all 8 are already highly consistent, confirm this and highlight the shared pattern so it can be documented as their emerging voice.

**Edge Cases:** If the 8 pieces were written for genuinely different product tiers (e.g., budget vs. premium line) with intentionally different registers, ask whether that's deliberate before flagging it as inconsistency.

---

### Example 11: Impersonation boundary

**User Request:** "Write this product launch copy in the exact voice of [a specific, real, currently active competitor company], word for word matching their style."

**Why the Skill Activates:** Surface-level match to voice-matching request, but raises a boundary issue.

**Workflow:** Recognize the request asks to closely mimic a real, specific, currently operating company's brand identity rather than the user's own brand — flag rather than comply directly.

**Expected Output:** Claude clarifies it can describe general stylistic patterns (e.g., "short, confident, benefit-led") but won't closely mimic a specific real company's proprietary brand voice/IP as if producing their output; offers to help define the user's own distinct voice instead, possibly inspired by general stylistic direction.

**Final Response:** Redirect toward defining the user's own voice, optionally "inspired by" general qualities (confidence, brevity) without copying a specific real brand's identity.

**Alternative Response:** If the user says it's their own company being referenced (not a competitor), proceed normally.

**Edge Cases:** Distinguish "write like Brand X" (their own past materials — fine) from "impersonate Brand X" (a different, real company — decline the close-mimicry framing).

---

### Example 12: Long-document drift correction

**User Request:** "This 12-page product guide starts great but feels like it loses our voice by the end — can you fix that?"

**Why the Skill Activates:** Long-form voice consistency/drift correction.

**Workflow:** Compare early sections (established as on-voice) against later sections → identify where drift toward generic/neutral phrasing occurs → re-anchor later sections to the voice fingerprint extracted from the strong early sections.

**Expected Output:** Revised later sections, brought back in line with the established early voice.

**Final Response:** "Pages 1-4 are strongly on-voice — I used those as the reference. Pages 8 onward had drifted into more generic, passive phrasing; I've revised those sections to match your established pattern."

**Alternative Response:** If the entire document is inconsistent from the start (no clear established voice anywhere), ask for an external reference instead of picking one section arbitrarily.

**Edge Cases:** Technical/reference sections may legitimately need more neutral, precise language even in an otherwise playful guide — distinguish intentional register shift from unintentional drift.
