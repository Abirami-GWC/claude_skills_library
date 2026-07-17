# Input Example 1 — Pasted Pipeline Check

A rep or manager might paste something like this, asking for a health check
across a few deals. Today is July 16, 2026.

---

Can you check the health of these opportunities?

ABC Manufacturing — $150,000, Proposal stage, last talked to them 18 days ago,
no meeting scheduled, don't know who the actual decision maker is, haven't heard
back since sending the proposal.

Beta Corp — Negotiation stage, spoke with them 3 days ago, next meeting is
scheduled, decision maker is confirmed, they've been responsive throughout.

Gamma LLC — Discovery stage, talked 10 days ago, next meeting is on the calendar,
not sure yet who the decision maker is or whether they'll respond to my last
email — still early conversations though.

---

Note this is unstructured prose describing three deals with differing amounts of
information — Claude should extract what's given, explicitly flag what's missing
for Gamma (decision maker, response status) rather than assuming either is fine,
and proceed to classify all three rather than asking for a reformatted table
first.
