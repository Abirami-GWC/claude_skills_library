---
name: forecast-roller
description: Analyze the current sales pipeline and generate a realistic revenue forecast — expected revenue, high/medium/low confidence deal breakdown, and forecast risks. Use this skill whenever a sales manager or leader asks to forecast revenue, predict pipeline revenue, wants expected sales for a month/quarter, asks "what revenue can we expect", "generate a sales forecast", "roll up the pipeline", or provides pipeline data and wants a revenue projection. This skill is for AGGREGATE, manager-facing revenue estimation across the whole pipeline — if the user instead wants deals ranked against each other, a single deal's health/risk diagnosis, or a follow-up schedule, prefer pipeline-prioritizer, deal-health-checker, or follow-up-cadence-builder instead.
---

# Forecast Roller

This file only handles triggering. Before doing anything else, read **`prompt.md`**
in this skill's folder — it has the full step-by-step process, and points to every
other supporting file (knowledge/, templates/, examples/, scripts/) at the point
each one is needed.

Do not attempt to build a forecast from this file alone; `prompt.md` is required
reading once this skill triggers.
