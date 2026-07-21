---
name: follow-up-cadence-builder
description: Build a personalized follow-up schedule for a specific deal — a multi-touchpoint sequence of when to reach out next, which channel to use, what type of message to send, and reminders/next actions over time. Use this skill whenever a sales rep wants a cadence/sequence of touchpoints planned out for a deal, asks "build me a follow-up plan", "what's my outreach schedule for this deal", "this prospect went quiet, what now, plan out the next few touches", or gives a deal's contact history and wants a multi-step communication schedule (not just one immediate action). This skill is for SCHEDULING/DRAFTING outreach for ONE deal over time — if the user instead wants deals ranked against each other, a health/risk diagnosis, or a revenue rollup, prefer pipeline-prioritizer, deal-health-checker, or forecast-roller instead. If the ask is a single, immediate "what should I do next / when should I follow up with X" question rather than a full forward-looking schedule, prefer next-best-action (in follow_up_deal_closing) — it gives one prioritized action, not a cadence. When genuinely ambiguous, ask which the rep wants: one next action now, or a full schedule.
---

# Follow-Up Cadence Builder

This file only handles triggering. Before doing anything else, read **`prompt.md`**
in this skill's folder — it has the full step-by-step process, and points to every
other supporting file (knowledge/, templates/, examples/) at the point each one is
needed.

Do not attempt to build a cadence from this file alone; `prompt.md` is required
reading once this skill triggers.
