---
name: deal-health-checker
description: Analyze open sales opportunities to determine their health — classify each as Healthy, Warning, or At Risk, explain the risk factors and positive indicators, and recommend next actions to recover at-risk deals. Use this skill whenever a sales rep or manager asks to check pipeline health, wants to know which deals are at risk, asks "find stalled deals", "show unhealthy opportunities", "analyze my sales opportunities", or gives deal/contact history and wants a risk diagnosis. This skill is for DIAGNOSING the state of deals (why might this be lost, and what to do about it) — if the user instead wants deals ranked against each other for work order, a revenue rollup, or a follow-up schedule, prefer pipeline-prioritizer, forecast-roller, or follow-up-cadence-builder instead.
---

# Deal Health Checker

This file only handles triggering. Before doing anything else, read **`prompt.md`**
in this skill's folder — it has the full step-by-step process, and points to every
other supporting file (knowledge/, templates/, examples/, scripts/) at the point
each one is needed.

Do not attempt to classify deal health from this file alone; `prompt.md` is
required reading once this skill triggers.
