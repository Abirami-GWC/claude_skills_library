# Worked Example — Campaign Multiplier

## User input

> "We just shipped a new real-time collaboration feature for our design tool.
> Target audience is product design teams at mid-market SaaS companies. Goal
> is product adoption among existing users, secondary goal is some new-user
> awareness. We have email, blog, LinkedIn, and an in-product announcement
> banner available — no paid budget right now. Launch is in 2 weeks."

## Claude's internal process (not shown to user)

1. All 5 required inputs present: core idea (real-time collaboration
   feature), audience (product design teams, mid-market SaaS), goal (adoption
   primary, awareness secondary), channels (email, blog, LinkedIn, in-product
   — paid explicitly excluded), timeframe (2 weeks).
2. Derive pillars: (1) "See changes as your team makes them — no more
   refresh-and-hope," (2) "Built for design teams that review async across time zones."
3. Channel selection: adoption goal → email (existing users) + in-product
   banner lead the plan; blog supports both goals (SEO/awareness) with a
   secondary CTA; LinkedIn covers the awareness goal for net-new audience.
   Paid social excluded — no budget confirmed.
4. Check for redundancy: email and in-product banner both target existing
   users but serve different moments (email = announcement, banner = point of
   use) — not redundant, kept distinct on purpose, noted in the brief.
5. Validate: metrics defined for each channel, no fabricated benchmarks,
   2-week timeframe checked against each channel's lead time (all four are
   low-lead-time, no flag needed).

## Output delivered to user (abbreviated)

```
# Campaign Brief: Real-Time Collaboration Launch

Goal: Product adoption (primary), new-user awareness (secondary)
Timeframe: 2 weeks

## Messaging Pillars
1. See changes as your team makes them — no more refresh-and-hope
2. Built for design teams reviewing async across time zones

## Channel Plan

### Email (existing users)
Angle: Pillar 1 — direct announcement to people who'll feel the change immediately
Format: Product update email
Example hook: "You'll never refresh a design file waiting for a teammate's
edit again."
CTA: Try it in your next review
Success metric: Click-through to feature, feature adoption rate 2 weeks post-send

### In-Product Banner
Angle: Pillar 1 — same message, delivered at the moment of use rather than
inbox, intentionally distinct touchpoint from email
Format: In-app announcement banner
Example hook: "New: live collaboration is here →"
CTA: Try it now
Success metric: Banner click rate, feature activation rate

### Blog
Angle: Pillar 2 — deeper story for both existing and prospective users
Format: Long-form post with workflow walkthrough
Example hook: "How [Company] Design built real-time review for distributed teams"
CTA: Read the full story / try the feature
Success metric: Organic traffic, scroll depth

### LinkedIn
Angle: Pillar 2 — awareness for net-new audience
Format: Organic post + short video clip
Example hook: "Your design team is in 4 time zones. Your review process
shouldn't be."
CTA: Link to blog post
Success metric: Engagement rate, click-through to blog

## Excluded Channels
- Paid Social — no budget confirmed for this launch

## Open Questions
- [ ] Confirm exact launch date to finalize send/post scheduling
```

## Why this is a good output

- Every channel ties to one of exactly two pillars — no channel invented its own angle.
- Paid social wasn't silently omitted — it's explicitly excluded with a stated reason.
- Email and in-product banner look similar at a glance but were deliberately
  distinguished rather than flagged as redundant, with the reasoning shown.
- Stayed at the hook/angle level — no fully drafted email or blog copy, correctly
  leaving that to `content-repurposer`.
