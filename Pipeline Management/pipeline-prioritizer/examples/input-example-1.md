# Input Example 1 — Pasted Deal List

A rep might paste something like this directly into chat, with no structure beyond
what they typed:

---

Here's my open pipeline, can you tell me what to work on first?

1. Acme Corp – Platform Upgrade, $85,000, contract sent, closing July 22nd, talked to them yesterday
2. Beta Industries – New Deployment, $22,000, still in discovery, no close date set, haven't heard back in 3 weeks
3. Gamma LLC – Renewal, $45,000, proposal sent, 60% chance, closing Aug 15th, responded to email 2 days ago
4. Delta Co – Expansion, $60,000, verbal yes, closing July 20th, no contact in 10 days

---

Note this is unstructured prose, not a clean CSV. Claude should extract the fields
(mapping "contract sent" → late stage, "discovery" → early stage, etc.), fill in
gaps using the defaults in `knowledge/scoring-guidelines.md`, and proceed — not ask
the rep to reformat it into a table first.
