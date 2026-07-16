# Worked Examples

## Example 1
**User input:** "This prospect (CTO at a 50-person fintech) just posted on LinkedIn
about struggling with data pipeline reliability during a migration. Give me some
opener lines."

**Expected output (3-5 ranked candidates):**
1. *"Reaction/Response"* — "Your post on the migration reliability issues hit on
   something we hear a lot from fintech teams crossing that scale — specifically
   the schema-drift-during-cutover problem." *(Strongest — directly engages the
   content of their post, not just its existence.)*
2. *"Sharp Question"* — "Curious whether the reliability issues you mentioned were
   more about the migration itself or the monitoring gap during cutover?"
3. *"Direct Observation"* — "Saw your post about the pipeline reliability
   struggles during the migration — sounds like exactly the cutover-window problem
   most fintech teams hit around 50 people." *(Weaker — closer to restating the
   post than engaging with it; kept as a backup option.)*

## Example 2 — What NOT to do
**User input:** "Give me an opener for this prospect: [LinkedIn URL, no other info]."

**Anti-pattern to avoid:** Fabricating a plausible-sounding but unverified fact
("Saw your recent post about scaling challenges...") when no actual content was
provided or retrieved.

**Correct behavior:** If a research/browsing tool is available, use it to actually
look at the profile before generating openers. If no tool is available and no
content was pasted, tell the user real signals are needed and ask them to paste
relevant research, rather than inventing something plausible-sounding.

## Example 3 — Cliché rejection
**User input:** Draft opener: "I hope this finds you well! I came across your
profile and loved what you're building at Acme!"

**Expected Claude behavior:** Flag this as a rejected pattern (matches multiple
banned clichés, fails the copy-paste test — it would work for literally any
prospect at any company), and rewrite using a real signal from the prospect's
actual profile/content instead.
