# Knowledge Base (placeholder — replace with real, verified WatchGuard content)

This file is the source of truth for anything factual in a generated demo plan.
Do not state a capability, timeline, or certification anywhere else that isn't
backed by an entry here.

**Canonical source note:** This file is the canonical version of the
Firebox/ThreatSync/AuthPoint product facts, migration-time table, and
compliance coverage used across the `demos_presentations` skills.
`narrative-deck-builder/knowledge/knowledge.md` intentionally duplicates the
product facts and migration table (each skill is self-contained and
independently installable), adapted for story-beat framing and extended with
customer success stories. When updating real product facts, migration times,
or compliance language, update this file first and mirror the change into
`narrative-deck-builder/knowledge/knowledge.md`.

## Firebox

**Benefits**
- Secure branch connectivity
- Centralized management across sites
- High availability / automatic failover

**Use when:** Current vendor is being replaced, or branch connectivity /
uptime is a stated pain point.

## ThreatSync

**Benefits**
- Faster threat detection via correlation
- Automated response to common threat patterns

**Use when:** Slow/manual threat investigation is a stated pain point.

## AuthPoint

**Benefits**
- Multi-factor authentication
- Reduces credential-based breach risk

**Use when:** Access control or credential security is a stated pain point.

## Migration Paths

| From | To | Average migration time |
|---|---|---|
| Cisco ASA | Firebox | 2 weeks |
| Fortinet | Firebox | 2–3 weeks |
| Palo Alto | Firebox | 3 weeks |

**Note:** If a customer's stated deployment timeline is shorter than the
average migration time for their specific path, flag this to the user rather
than presenting the timeline as guaranteed achievable.

## Compliance Coverage

Supports reporting and controls relevant to:
- ISO 27001
- PCI DSS
- HIPAA

**Note:** "Supports reporting relevant to X" is not the same as "certified for
X" — do not overstate compliance claims. Confirm exact certification language
with the compliance/legal team before it goes into a customer-facing plan.

## Business Benefits (general framing, tie to stated business goal)

- Reduced downtime → framed as: fewer VPN/firewall-related outages, faster
  incident containment.
- Improved security posture → framed as: faster detection, centralized
  visibility, MFA coverage.
- Reduced operational overhead → framed as: centralized management, fewer
  manual investigation hours.

---
*Replace all of the above with verified WatchGuard product facts, real
migration-time data, and confirmed compliance language before using this in a
live customer-facing deal.*
