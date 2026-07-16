# Follow-Up Cadence Builder — Process

Builds a personalized follow-up schedule for one deal — timing, channel, message
type, and reminders — so the rep never has to guess what to do next or let a deal
go quiet by accident.

## Step 1 — Get the deal's contact history

Ask for or read in: current stage, prior interactions (dates, channel, what was
discussed), any response received, and time since last contact. This may arrive as
a pasted description, a CRM export, or a few sentences of context.

Read `knowledge/deal-stages.md` for how to normalize the stage and understand how
stage affects cadence tempo. See `examples/input-example-1.md` for what a realistic,
unstructured version of this looks like.

If the user gives no data at all, ask for at minimum: stage, last contact date, and
what happened at last contact — don't invent a contact history.

## Step 2 — Determine the cadence

Read `knowledge/followup-best-practices.md` for the actual cadence rules: how many
days between touches given the deal's stage and how the prospect has been
responding, which channel to use at each stage, which message type fits the
situation, and — importantly — the stopping rule for when to stop automated
follow-up and hand the deal to `deal-health-checker` instead.

Read `knowledge/communication-guidelines.md` for tone, message length, and pacing
rules (e.g., never stack two channels in one day, always reference something
specific from the last interaction, one clear ask per message).

Compute the actual follow-up dates by adding the documented interval to the last
contact date (or to today, if the deal has already gone past its next expected
touch) — do this arithmetic carefully and show your work isn't required, but the
dates in the final plan must be correct calendar dates, not vague ("in a few days").

## Step 3 — Build the plan

Assemble the schedule using `templates/followup-plan.md` as the exact layout —
a dated sequence of touches, each with channel, message type, and purpose.

For any touch that involves sending a message, draft it using
`templates/email-template.md` (or adapt the same message-type logic for a call/
LinkedIn touch — the template's message-type sections apply regardless of channel).

For each touch, also produce a short reminder line using
`templates/reminder-template.md`, suitable for pasting into a task manager or CRM
task.

`examples/output-example-1.md` shows a complete worked plan end-to-end, matched to
`examples/input-example-1.md` — use it to check tone, date math, and format before
replying.

## Step 4 — Flag the stopping point

Every cadence plan must end with an explicit stopping rule: after how many
unanswered touches the rep should stop automated follow-up and either try a
different approach or flag the deal as at-risk (pointing to
`deal-health-checker` if the user has that skill available). Don't generate an
infinite or open-ended cadence.

## Edge cases

Full edge-case handling (no response history at all, multiple stakeholders, a
prospect who explicitly asked not to be contacted for a while, reviving a fully
cold deal) is documented in `knowledge/followup-best-practices.md` — read it rather
than improvising when one of these comes up.
