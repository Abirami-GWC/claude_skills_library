# Worked Examples

## Example 1: ABC Manufacturing (full discovery notes)

**Input**
```
Company: ABC Manufacturing
Industry: Manufacturing
Current Firewall: Cisco ASA
Current VPN: Cisco AnyConnect
Branch Offices: 8
Pain Points:
- VPN disconnects
- Slow threat investigation
- Compliance reporting
Business Goal: Improve security and reduce downtime
Decision Maker: IT Director
Deployment Timeline: 2 Months
```

**Processing notes**
- Current vendor "Cisco ASA" / "Cisco AnyConnect" → Firebox + VPN Migration
  (mappings.yaml → current_vendor)
- Decision maker "IT Director" → lead with security posture, compliance,
  business impact framing (mappings.yaml → decision_maker)
- Industry "Manufacturing" → weight branch connectivity and uptime
  (mappings.yaml → industry)
- Migration path Cisco ASA → Firebox averages 2 weeks (knowledge.md) — well
  within the stated 2-month timeline, so no flag needed.

**Output**
```
Demo Plan

1. Customer Environment Overview
2. Existing Cisco ASA Challenges
3. VPN Connectivity Improvements
4. Centralized Security Management
5. Compliance Reporting
6. Migration Strategy
7. Business Benefits
8. Next Steps
9. Q&A
```

## Example 2: Partial discovery notes (no current vendor stated)

**Input**
```
Company: Riverside Health Clinic
Industry: Healthcare
Pain Points:
- Poor visibility across clinic locations
- Ransomware concerns
Decision Maker: CISO
```

**Processing notes**
- No current vendor stated → skip the "Migration Strategy" section entirely
  rather than inventing a "from" vendor.
- No deployment timeline stated → omit any specific timeline commitment.
- Decision maker "CISO" → lead with threat detection, compliance/audit
  readiness, incident response framing.
- Industry "Healthcare" → weight HIPAA compliance and clinical system uptime.

**Output**
```
Demo Plan

1. Customer Environment Overview
2. Customer Challenges (Visibility, Ransomware Risk)
3. Centralized Monitoring Across Locations
4. Endpoint Detection & Ransomware Containment
5. Compliance Reporting (HIPAA)
6. Business Benefits
7. Next Steps
8. Q&A
```
Note: no "Migration Strategy" section — nothing in the discovery notes
supports one.

## Example 3: Unmapped vendor (flag instead of guessing)

**Input**
```
Company: Northgate Logistics
Current Firewall: SonicWall
Pain Points:
- Slow incident response
```

**Processing notes**
- "SonicWall" is not in mappings.yaml → do not invent a migration path or
  demo angle for it. Flag to the user: "SonicWall isn't in our current vendor
  mappings — I'll build the plan around the stated pain point using
  knowledge.md, but you may want to add a SonicWall entry to mappings.yaml for
  next time."
