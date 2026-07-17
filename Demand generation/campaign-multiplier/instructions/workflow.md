# Workflow: Building a Campaign Brief

## Step 1 — Elicit core inputs

Confirm or ask:
1. The core idea/asset (what it is, and its actual content or a summary)
2. Target audience/persona
3. Primary goal: awareness | lead generation | product adoption | retention/expansion
4. Available channels (don't assume paid budget or a channel exists unless confirmed)
5. Rough timeframe

If 2+ of these are missing, ask a single consolidated clarifying question
covering the most critical gaps rather than five separate questions.

## Step 2 — Derive messaging pillars

From the core idea, extract 1–3 messaging pillars — the few things every
channel's content must reinforce. See `references/messaging_pillars_guide.md`
for how to derive pillars from a single asset without diluting the narrative.

## Step 3 — Select channels

Using `knowledge/channel_playbook.md`'s selection heuristic, choose channels
that map to the stated goal and are confirmed available. List excluded
channels with a one-line reason (budget, audience mismatch, lead-time
mismatch) — this makes the brief's channel choices legible rather than arbitrary.

## Step 4 — Define each channel's angle

For each selected channel, fill:
- **Angle**: which pillar this channel leads with, and why that channel suits it
- **Format**: what kind of content this becomes (a post, a thread, an email,
  a webinar) — not the finished copy itself
- **Example hook**: one illustrative headline/opening line, to make the angle
  concrete (not a full draft — that's `content-repurposer`'s job)
- **CTA**: what action this channel drives
- **Success metric**: from `knowledge/channel_playbook.md`'s typical metrics,
  or the user's own KPI framework if supplied

Check for redundancy: if two channels have the same angle and CTA, flag it —
one is likely unnecessary or needs a differentiated angle.

## Step 5 — Validate

Run every item in `instructions/validation_rules.md`.

## Step 6 — Assemble

Use `templates/campaign_brief_template.md` for the narrative brief, and
`templates/channel_matrix.csv` if the user wants a spreadsheet-friendly
planning grid alongside it.

## Common mistakes to avoid

- **Channel sprawl**: including every available channel regardless of fit.
  Prevention: Step 3's explicit goal-mapping requirement.
- **Disconnected angles**: each channel telling an unrelated story. Prevention:
  Step 2's shared-pillar requirement, checked again in Step 4.
- **Assuming budget/team capacity**: including paid ads or webinars without
  confirmation. Prevention: Step 1 and Step 3 explicit confirmation requirement.
- **Producing finished copy instead of a brief**: drifting into writing full
  social posts/emails. Prevention: Step 4 explicitly limits to one example
  hook, not full copy — route to `content-repurposer` for execution.
