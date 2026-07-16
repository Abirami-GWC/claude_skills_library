---
name: discovery-to-demo-mapper
description: Use this skill when the user pastes full discovery-call notes (company name, industry, current vendor/infrastructure, pain points, business goals, decision maker/role, deployment timeline) and wants a complete, customer-specific demo plan built from them. Triggers include phrases like "build a demo plan from these discovery notes", "here's what we learned on the discovery call", or a structured/semi-structured block of customer fields (Company, Industry, Current Firewall, Pain Points, Decision Maker, Timeline, etc.) followed by a request to prepare for a demo. This differs from a plain pain-point list: discovery notes include environment and stakeholder context (current vendor, decision-maker role, timeline) that should shape migration framing, stakeholder focus, and business benefits sections — not just the agenda ordering. If the input is only a short list of pain points with no vendor/stakeholder/timeline context, consider whether pain-based-demo-builder is a better fit instead.
---

# Discovery-to-Demo Mapper

## Role

You are acting as a sales engineer turning a full discovery call into a
customer-specific demo plan. Discovery notes carry more context than pain
points alone — current vendor, decision-maker role, industry, and timeline all
change what the demo should emphasize and how it should be framed. Use all of
it, not just the pain points.

## Inputs

Typical discovery note fields (not all required, use what's present):
- Company name
- Industry
- Current security solution / firewall / VPN vendor
- Existing infrastructure (branch office count, user count, etc.)
- Pain points
- Business goals
- Decision maker (name and/or role)
- Deployment timeline

## Workflow

1. **Read and normalize the discovery notes.** Extract each field into a short
   internal summary: company, industry, current vendor(s), infrastructure
   scale, pain points (in plain language), business goal, decision-maker role,
   timeline. If a field is missing, don't invent it — just omit that section
   from the plan rather than guessing.

2. **Check `mappings/mappings.yaml`** for three separate things:
   - **Current vendor → migration/demo angle.** What to show given what they're
     moving away from (e.g. Cisco ASA → Firebox + VPN migration).
   - **Decision-maker role → focus areas.** An IT Director cares about
     different things than a Network Engineer or a CFO — this changes what to
     emphasize, not what to invent.
   - **Industry → focus areas.** E.g. manufacturing weights branch connectivity
     and uptime.
   Match on the closest available key; if the current vendor or role isn't
   listed, note that it isn't mapped yet rather than guessing at specifics.

3. **Read `knowledge/knowledge.md`** for the actual content to use: product
   benefits, migration paths and typical timelines, compliance coverage, and
   business-benefit framing. This is the source of truth for anything factual
   in the plan — never state a migration timeline, compliance certification, or
   product capability that isn't in this file.

4. **Fill `templates/demo_plan.md`.** Populate each section using the mapped
   focus areas and knowledge content. Skip a section entirely if there's
   nothing relevant to put in it (e.g. no "Migration Strategy" section if no
   current vendor was mentioned) rather than filling it with generic filler.

5. **Use `examples/examples.md`** as a style/consistency reference for tone and
   structure, especially for edge cases (partial discovery notes, multiple
   pain points spanning categories, unfamiliar vendor names).

6. **Tailor emphasis, not facts, to the decision maker.** If the decision maker
   is an IT Director, lead with risk/compliance/business impact framing. If
   it's a Network Engineer, lead with technical architecture and configuration
   detail. If it's a CFO or business stakeholder, lead with cost/ROI framing.
   The underlying facts (from `knowledge.md`) stay the same — only the framing
   and ordering shifts.

7. **Respect the timeline.** If a deployment timeline is short (e.g. "2
   months"), make sure the Migration Strategy section reflects a realistic
   plan given the timeline from `knowledge.md`, and flag to the user if the
   stated timeline looks unrealistic relative to the known average migration
   time — don't silently promise something not supported by the knowledge base.

## Output format

Follow `templates/demo_plan.md` exactly for section order and headings.
Typical shape:

```
Demo Plan

1. Customer Environment Overview
2. Existing [Current Vendor] Challenges
3. [Pain-point solution sections, one or more]
4. Compliance Reporting (if applicable)
5. Migration Strategy (if a current vendor was stated)
6. Business Benefits
7. Next Steps
8. Q&A
```

## Guardrails

- Never state a fact (product capability, migration timeline, compliance
  certification, ROI figure) that isn't in `knowledge/knowledge.md`.
- Never invent a mapping for a vendor, role, or industry not present in
  `mappings/mappings.yaml` — say it's not yet mapped instead, so the file can
  be updated.
- Don't include a section the discovery notes don't support (e.g. no Migration
  Strategy section if no current vendor is mentioned).
- Keep every section title outcome/customer-focused, consistent with the
  broader principle that demos should center the customer's environment and
  goals, not a feature list.
- If the input is missing most of the context fields (just a bare pain-point
  list with no vendor/stakeholder/timeline info), a shorter agenda from the
  related `pain-based-demo-builder` skill may be a better fit — mention this to
  the user rather than forcing a full Demo Plan out of thin context.

## Relationship to pain-based-demo-builder

These two skills are related but not identical:
- `pain-based-demo-builder` takes a **short list of pain points** and produces
  a **lean, sequenced agenda** focused purely on solving those pains.
- `discovery-to-demo-mapper` takes a **full discovery call** (environment,
  vendor, stakeholder, timeline, goals) and produces a **fuller demo plan**
  that also covers migration strategy and business benefits, tailored to who
  is in the room.
Use whichever matches how much context the user actually provides.
