# Industry Playbook: Manufacturing

Manufacturing customers typically care about, in rough priority order:
1. Factory / production uptime
2. Secure branch connectivity (multiple plants/warehouses)
3. Compliance (ISO 27001, industry-specific regulations)
4. Remote/field worker access

## How to use this file

This is an **industry lens**, not a replacement for the category playbooks in
`playbooks/`. Use it to weight and frame the category playbooks when the
customer's industry is known:

- Pull the relevant category playbook(s) for the stated pains (e.g.
  `playbooks/networking_playbook.md` for VPN issues, `playbooks/security_playbook.md`
  for incident response, `playbooks/compliance_playbook.md` for ISO 27001).
- Frame each item using manufacturing-specific language — e.g. "secure branch
  connectivity across your plants" instead of generic "multi-site connectivity."
- Prioritize uptime and branch connectivity ahead of compliance unless the
  customer explicitly signals compliance as their top-of-mind/most urgent pain.

## Recommended case study match

Prefer a manufacturing or industrial case study from `knowledge/case_studies.md`
if one exists. If none exists, use the closest adjacent industry and say so
rather than fabricating a manufacturing-specific one.
