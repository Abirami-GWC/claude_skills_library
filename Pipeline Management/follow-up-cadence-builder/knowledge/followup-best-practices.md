# Follow-Up Best Practices

The actual cadence rules: how often to touch a deal, which channel to use, what
message type fits, and when to stop.

## Base cadence by stage (days between touches, when there's been no response)

| Stage | Days between touches | Why |
|---|---|---|
| Early | 5-7 days | Still earning attention — crowding a prospect this early reads as desperate |
| Mid | 3-5 days | Momentum matters once a proposal is out, but give real evaluation time |
| Late | 2-3 days | Time-sensitive — administrative delays here can lose a deal that's basically won |

## Adjusting for how the prospect has responded

- **Prospect engaged/responded positively at last contact**: follow up within 1-2
  days to keep momentum — don't wait out the full base cadence.
- **Prospect went quiet after 1 touch**: use the base cadence above for the next
  attempt, and vary the channel if the first touch was email (e.g., try a call or
  LinkedIn message next, not another email).
- **Prospect has gone quiet for 2+ consecutive touches**: widen the interval
  slightly (add ~50% to the base cadence) and shift the message type toward
  something lower-pressure (see message types below) rather than repeating the
  same ask.
- **Prospect explicitly asked for space** ("check back in a month"): honor it
  exactly — schedule the next touch for the date they gave, not the default
  cadence.

## Channel selection by stage

| Stage | Preferred channel | Notes |
|---|---|---|
| Early | Email, LinkedIn | Call only if there's already a warm signal (they asked to be called, or responded well before) |
| Mid | Email primary | Use a call specifically to walk through the proposal or answer questions, not as a generic check-in |
| Late | Phone/call preferred, email for paper trail | Urgency and human back-and-forth matter more than a written record at this stage, but confirm anything verbal in a follow-up email |

Never stack two channels in the same day (e.g., email and LinkedIn message on the
same date) — it reads as pressure, not persistence.

## Message types

- **Check-in / value-add** (early stage, first or second touch): low-pressure,
  offers something (an article, an answer to something they mentioned), asks a
  light question about timeline.
- **Proposal follow-up** (mid stage): addresses likely questions directly, offers a
  short call, references something specific from the proposal or the champion's
  earlier feedback.
- **Urgency nudge** (late stage): confirms the specific next step and any real
  deadline (e.g., end of quarter pricing, legal review timeline) — factual, not
  artificially urgent.
- **Break-up message** (after the stopping-rule threshold, see below): explicitly
  asks whether to close out the opportunity — often the message that finally gets
  a reply, because it removes pressure rather than adding it.

## Stopping rule

After **3 consecutive touches with no response**, do not schedule a 4th touch in
the same cadence style. Instead:
1. Send one break-up message.
2. If that also goes unanswered, stop the automated cadence and flag the deal —
   point the rep to `deal-health-checker` (a separate skill) to assess whether the
   deal should be marked at-risk or deprioritized, rather than continuing to
   generate follow-ups indefinitely.

This limit applies per "silence streak" — if the prospect responds at any point,
the streak resets and normal cadence resumes.

## Multiple stakeholders

If only one stakeholder (e.g., a champion) is engaged and there's a known
economic buyer or decision maker who hasn't been reached, the best move is often to
loop them in explicitly in the next message ("Would it help to include [role] on
our next call?") rather than continuing to only contact the engaged stakeholder.
