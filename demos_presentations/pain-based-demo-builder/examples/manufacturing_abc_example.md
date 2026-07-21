# Example: ABC Manufacturing (Manufacturing, Industry Playbook + Vendor/Sizing)

**Input (raw discovery notes)**
```
Company: ABC Manufacturing
Industry: Manufacturing
Pain Points:
- VPN instability
- Slow incident response
- Compliance reporting (ISO 27001)
Current Firewall: Fortinet
Users: 450 Employees
Branch Offices: 12
```

**Processing notes**
- "VPN instability" matched the alias for "VPN disconnects" in `pain_to_feature.yaml`.
- "Slow incident response" matched directly.
- "Compliance reporting" + "ISO 27001" both matched the "Compliance / audit
  difficulty" entry.
- 12 branch offices → flagged "Difficult multi-site management" as a suggested
  addition per `knowledge/sizing_guidance.md` (not stated by the customer, so
  noted separately).
- 450 users → Mid-Market tier per `knowledge/sizing_guidance.md`.
- Current vendor Fortinet → competitive angle pulled from
  `mappings/objection_mapping.yaml` (lead with VPN Failover/SD-WAN + ThreatSync,
  no head-to-head comparison).
- Industry = Manufacturing → `playbooks/industries/manufacturing_playbook.md`
  applied: uptime and branch connectivity weighted ahead of compliance.

**Output**
```
Demo Agenda

1. Understanding Your Current Challenges
2. Solving VPN Instability
   - VPN Failover
   - SD-WAN
3. Faster Threat Investigation
   - ThreatSync
   - Automated Alerts
4. Compliance Reporting (ISO 27001)
   - Audit Reports
   - ISO Reporting
5. Customer Success Story
   Manufacturing company reduced incident response time significantly
6. Q&A
7. Next Steps
```

**Suggested addition flagged separately (not in the agenda unless the rep wants it):**
"With 12 branch offices, centralized multi-site management may also be worth
showing — want me to add it as item 5?"
