# Input Example 1 — Pasted Pipeline

A sales manager might paste something like this, asking for a Q3 forecast:

---

Can you forecast our Q3 revenue based on this pipeline? Today is July 16th.

ABC Manufacturing — $120,000, Negotiation stage, 85% probability, closing July 28th
XYZ Retail — $50,000, Proposal stage, 45% probability, closing August 5th
Delta Software — $30,000, Discovery stage, no probability given yet, expected to
close around September 10th, haven't logged any recent activity on this one

---

Note the third deal is missing a stated probability and has no logged last-activity
date — Claude should infer probability from `knowledge/sales-probabilities.md`'s
Discovery-stage default, flag both gaps, and still include the deal in the
forecast (at Low confidence) rather than dropping it or asking the manager to fill
in every field before proceeding.
