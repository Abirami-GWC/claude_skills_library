# Input Example 1 — Pasted Deal Context

A rep might describe a deal like this, with no structure:

---

Can you build me a follow-up plan for Northwind Traders? Quick background: I had a
really good call with their ops lead (my champion) on July 3rd, she was positive
about the platform. Sent over the proposal on July 10th and haven't heard anything
back since — it's been about a week now. This is a mid-stage deal, proposal is
already out. I haven't looped in their economic buyer yet, only been talking to the
ops lead. Today is July 16th.

---

Note this is conversational, not a clean data table. Claude should extract: stage
(mid), last contact date (Jul 10, proposal email, no response since — silence streak
of 1), prior positive signal (the Jul 3 call), and the missing-stakeholder detail
(economic buyer not yet engaged) — then apply `knowledge/followup-best-practices.md`
rather than asking the rep to reformat this into a table first.
