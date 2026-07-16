# Risk and Dependency Management: RAID Logs, Critical Path, and Cross-Functional Dependency Mapping

> **Purpose:** Explain how to track risks, assumptions, issues, and dependencies (RAID), understand critical path awareness, and map dependencies across marketing, sales, and product for a quarterly roadmap.

## Introduction

A quarterly roadmap is only as reliable as its understanding of what could disrupt it. Risk and dependency management is the discipline of surfacing what could go wrong (risks), what is being assumed without proof (assumptions), what has already gone wrong (issues), and what one team is waiting on another team to deliver (dependencies) — before these become missed milestones. This reference covers the RAID log method, critical path awareness, and cross-functional dependency mapping.

## Detailed Explanation

### The RAID Log

A RAID log is a structured, living document with four categories:
- **Risks:** potential future events that could negatively affect the roadmap (e.g., "key vendor integration may not be ready in time"). Each risk should have a likelihood, an impact, an owner, and a mitigation or contingency plan.
- **Assumptions:** things being treated as true without current proof (e.g., "assumes current headcount is retained through the quarter"). Assumptions should be tracked because if they prove false, dependent plans must be revisited.
- **Issues:** risks that have already materialized into current problems requiring action (e.g., "the vendor integration is now confirmed delayed"). Issues need an owner and a resolution plan with urgency proportional to their impact on the critical path.
- **Dependencies:** work in one team or workstream that requires an input, decision, or deliverable from another team or workstream before it can proceed.

The RAID log should be reviewed at every planning checkpoint (kickoff, mid-quarter review, close-out) and updated whenever a new risk, assumption, issue, or dependency is identified — not only at the start of the quarter.

### Critical Path Awareness

The critical path is the sequence of dependent milestones that determines the minimum possible completion time for the roadmap's key outcomes — if any milestone on the critical path slips, the overall timeline slips by the same amount, while a delay to a milestone with float (spare time before it affects downstream work) does not. Critical path awareness means:
- Identifying which milestones are truly on the critical path (their delay directly delays a committed outcome) versus which have float.
- Prioritizing risk mitigation and monitoring attention on critical-path items first.
- Recognizing that adding resources to a non-critical-path item does not speed up the overall roadmap; only critical-path acceleration does.
- Re-evaluating the critical path whenever a milestone's status changes, since the critical path can shift during the quarter.

### Cross-Functional Dependency Mapping

Most quarterly roadmap delays originate at the handoff between functions, not within a single function's own work. Dependency mapping across marketing, sales, and product requires:
- **Explicit direction:** for every dependency, name the upstream team (the one delivering) and the downstream team (the one waiting), never leave it ambiguous which way the dependency runs.
- **A required-by date**, not just a "sometime this quarter" expectation — the downstream team needs a specific date by which the input must arrive to protect their own milestones.
- **A single dependency register** visible to all functions, rather than dependencies scattered across separate team-level plans where they are easy to miss.
- **Common dependency patterns to watch for:** product feature completion gating sales enablement content; sales enablement gating a go-to-market launch date; marketing campaign assets gating a lead-generation milestone; legal or compliance review gating any customer-facing launch; data or analytics instrumentation gating measurement of a key result.

## Professional Guidance

- Build the RAID log during initial roadmap planning, not after a problem has already occurred; a RAID log created reactively has already missed its main value.
- Flag every dependency with a required-by date, since "later this quarter" is not an actionable commitment for the downstream team.
- Distinguish clearly between a risk (has not happened yet, still preventable) and an issue (has happened, now needs remediation) — conflating them slows response.
- Recompute the critical path at every review checkpoint; a milestone that was not critical at kickoff can become critical if an earlier item slips.
- Assign a single accountable owner to each risk and dependency; a risk "owned by everyone" is effectively owned by no one.

## Examples

*Illustrative and generic — no real company implied.*

- Risk: "Confidence in the [NEW SEGMENT] messaging is unvalidated; may require a mid-quarter pivot." Owner: Marketing Lead. Mitigation: validate messaging with a small pilot audience by week 3.
- Assumption: "Assumes the sales team retains current headcount through the quarter." If this proves false, the pipeline generation key result should be revisited.
- Issue: "The product feature required for the sales demo script is now confirmed delayed by two weeks." Owner: Product Lead. Resolution: sales enablement milestone is re-sequenced two weeks later; the launch milestone (on the critical path) is flagged at risk.
- Dependency mapping example: Product's feature completion (upstream) is required by Sales Enablement's script finalization (downstream) with a required-by date of week 4; if product slips, the required-by date for enablement slips in lockstep, and the launch milestone — being on the critical path — is placed at risk.

## Common Mistakes

- Creating a RAID log once at kickoff and never revisiting it during the quarter.
- Treating every milestone as equally critical, which dilutes attention away from the items that actually determine the timeline.
- Leaving dependencies as vague expectations ("marketing will need something from product eventually") instead of dated, owned commitments.
- Assigning risk ownership to a team rather than a specific accountable role, causing risks to go unmanaged.
- Failing to distinguish risks from issues, leading to delayed escalation on problems that have already occurred.

## Best Practices

- Maintain a living RAID log reviewed at every planning checkpoint.
- Explicitly identify the critical path and re-evaluate it whenever milestone status changes.
- Record every cross-functional dependency with upstream owner, downstream owner, and required-by date in a single shared register.
- Assign one accountable owner per risk, assumption, issue, and dependency.
- Prioritize mitigation effort on critical-path risks over non-critical-path risks.

## Summary

Risk and dependency management protects a quarterly roadmap from the handoff failures and unexpected disruptions that a purely optimistic plan ignores. The RAID log structures risks, assumptions, issues, and dependencies into an owned, dated, living document; critical path awareness focuses mitigation effort where delays actually matter; and explicit cross-functional dependency mapping — with named upstream/downstream owners and required-by dates — closes the gap where most quarterly plans actually break down.
