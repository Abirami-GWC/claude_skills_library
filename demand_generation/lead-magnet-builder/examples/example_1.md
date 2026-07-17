# Worked Example 1 — Checklist Lead Magnet

## User input

> "We sell API security tooling. Build a lead magnet for engineering
> leads/security leads at mid-market SaaS companies — something about getting
> ready for a SOC 2 audit. Format: checklist. Also write the landing page copy."

## Claude's internal process (not shown to user)

1. Topic: SOC 2 audit readiness. Persona: engineering/security leads,
   mid-market SaaS. Format: checklist (user-specified).
2. Specific value: not just "SOC 2 checklist" — narrow to "the API-security-
   specific items most commonly flagged in SOC 2 audits," since the company
   sells API security tooling and a generic full-SOC-2 checklist would be
   outside their expertise/credibility zone. Confirm this framing makes sense
   rather than assuming — in this run, proceed with the narrower framing as
   the sensible default and note the assumption.
3. Draft using `templates/checklist_template.md` — every item is a concrete,
   checkable action (e.g. "Rotate all API keys older than 90 days," not
   "Improve API security").
4. Draft landing page copy: headline sells the outcome ("Know exactly which
   API security gaps auditors flag most"), not the format.
5. Validate: no padding, no vague items, no unverifiable claims in the landing copy.

## Output delivered to user (abbreviated)

```
# API Security Checklist for Your Next SOC 2 Audit

Use this before your next SOC 2 audit cycle to catch the API-specific gaps
auditors flag most often.

## Authentication & Access
- [ ] Rotate all API keys older than 90 days
- [ ] Confirm every API endpoint requires authentication (no unauthenticated
  internal-only endpoints exposed externally)
- [ ] Verify rate limiting is enabled on all public-facing endpoints

## Logging & Monitoring
- [ ] Confirm API access logs are retained for at least 90 days
- [ ] Verify failed authentication attempts trigger an alert

## Data Handling
- [ ] Confirm all API responses exclude fields not required by the consuming client
- [ ] Verify PII fields are encrypted in transit and at rest

---
Note: assumed a narrower "API-security-specific" framing rather than a
full general SOC 2 checklist, since that matches your product's expertise —
let me know if you wanted the broader scope instead.
```

```
# Landing Page Copy

Headline: Know exactly which API security gaps auditors flag most
Subheadline: A focused checklist for engineering and security leads prepping
for a SOC 2 audit — built from the API-specific issues that come up again and again.

Value bullets:
- The exact authentication gaps auditors check first
- A logging/monitoring baseline that satisfies most SOC 2 evidence requests
- Data-handling items specific to API responses, not generic security advice

Form: Name, work email (2 fields — matches "send the checklist + one follow-up
resource" as the stated use)
Button: Get the checklist
```

## Why this is a good output

- Narrowed the topic to something the company can credibly speak to, and
  flagged that assumption explicitly rather than silently deciding it.
- Every checklist item is concrete and checkable, not a restated goal.
- Landing page form stayed to 2 fields, matching the stated follow-up use.
- Headline sells the outcome, not "download our checklist."
