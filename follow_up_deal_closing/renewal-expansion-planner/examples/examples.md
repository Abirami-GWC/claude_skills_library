# Worked Examples

## 1. Growing usage — Alderbrook Health Network

**Scenario**: 1-year Insight Suite contract ($85K) signed last August, 60 days from ending. Usage up 40%, two more departments onboarded, champion asked about a predictive-analytics module.

**Input**: "Alderbrook's Insight Suite contract ends in 60 days. Usage is up 40%, two more departments came on board, and Priya's asked about predictive analytics. Help me plan the renewal."

**Output**:

```
Renewal plan for Alderbrook Health Network (contract ends [date], usage signal: growing):

| Timing | Action |
|---|---|
| Now (60 days out) | Open the renewal conversation; pitch the predictive-analytics module in the same conversation |
| 30 days out | Send the renewal + expansion proposal/quote |
| 14 days out | Send a reminder; confirm no open objections |
| Contract end | Confirm renewal signed, or trigger a save/escalation plan |

Framing note: usage is growing, so lead with the expansion pitch — the renewal itself is low-risk.
```

(90-day milestone omitted — it's already passed at the 60-day mark.)

## 2. Flat usage — no expansion opportunity yet

**Scenario**: Northline Manufacturing, 90 days from renewal. Usage steady, no growth, no complaints, no stated expansion interest.

**Input**: "Northline's renewal is in 90 days. Usage is steady, nothing's really changed, no complaints. What's the plan?"

**Output**:

```
Renewal plan for Northline Manufacturing (contract ends [date], usage signal: flat):

| Timing | Action |
|---|---|
| Now (90 days out) | Internal account review; schedule a QBR |
| 60 days out | Open the renewal conversation, leading with a value check-in (what's been achieved, what's underused) — hold off on any upsell ask |
| 30 days out | Send the renewal proposal/quote |
| 14 days out | Send a reminder; address any open objection |
| Contract end | Confirm renewal signed, or trigger an escalation/save plan |

Framing note: usage is flat, not growing — lead with a value conversation before considering any expansion ask.
```

## 3. At-risk usage — champion left

**Scenario**: Bristol Logistics, 45 days from renewal. Login frequency down sharply, the original champion left the company two months ago, no clear new point of contact.

**Input**: "Bristol Logistics renews in 45 days. Their champion left two months ago and usage has dropped off a cliff. What do we do?"

**Output**:

```
Renewal plan for Bristol Logistics (contract ends [date], usage signal: at-risk):

| Timing | Action |
|---|---|
| Now (45 days out) | Lead with a save conversation — identify the new point of contact, surface the drop in usage directly, and understand what changed |
| 30 days out | Send the renewal proposal/quote only once the relationship is stabilized; do not lead with pricing if the save conversation is still unresolved |
| 14 days out | Send a reminder; confirm no open objections |
| Contract end | Confirm renewal signed, or trigger an escalation/save plan |

Framing note: usage is at-risk due to champion loss — no expansion pitch, and renewal terms wait until the relationship is stabilized.
```

## Why these are correct

Each timeline only includes milestones still ahead of today (the 90-day milestone was correctly skipped for Alderbrook). The framing note changes entirely by usage signal — expansion-led, value-led, or risk-led — per `mappings/signal_to_framing.yaml`, and expansion is explicitly withheld in the at-risk case per the guardrail in SKILL.md.
