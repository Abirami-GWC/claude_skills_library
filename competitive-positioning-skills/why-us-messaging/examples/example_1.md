# Worked Example 1 — CTO Persona

## User input

> "We're a workflow-automation platform. Write website 'vs' page copy for a CTO
> comparing us to Competitor Flowly. Our real differentiators: (1) native
> webhook-based architecture vs. their polling-based integration model (public
> docs); (2) our API rate limits are 10x higher on the standard tier (both
> public pricing pages); (3) we're SOC 2 Type II certified, they're not
> (verified via both trust pages)."

## Claude's internal process (not shown to user)

1. Persona = CTO/VP Eng → per `knowledge/persona_priorities.json`, prioritize
   capability/operational differentiators, avoid pure pricing framing as the lead.
2. Channel = website copy → `templates/why_us_one_pager.md`.
3. Map differentiators: webhook vs. polling = capability; rate limits =
   capability/operational; SOC 2 = capability (security posture — CTOs weight this highly).
4. All three sourced (public docs, pricing pages, trust pages) — no fabrication needed.
5. Draft with acknowledge-then-pivot on the lead point (architecture).

## Output delivered to user

```
# Why [Us] vs. Flowly — For Engineering Teams

Flowly's polling-based integration model works fine at low volume — but
engineering teams scaling past a few thousand events a day start feeling it.

**Event-driven, not polling.** Our webhook-based architecture pushes events
in real time; Flowly polls on an interval, which means latency scales with
your integration count, not just your event volume.

**10x the headroom.** Standard-tier API rate limits are 10x higher than
Flowly's published limits — one less thing your team has to architect around
before you've even shipped.

**SOC 2 Type II certified.** Verified on our trust page; Flowly's trust page
does not currently list this certification, worth confirming directly with
them if it's a requirement for your org.

Happy to walk through the API docs side by side if that's useful before you
commit to an architecture decision.
```

## Why this is a good output

- Leads with architecture (capability), not price — matches CTO persona priorities.
- Every claim sourced to public documentation.
- SOC 2 claim phrased carefully ("does not currently list," "worth confirming
  directly") rather than a flat "they don't have it," since certifications can
  be in progress or simply unlisted.
