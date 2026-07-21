# Workflow: Building a Personalized Sequence

## Step 1 — Gather Inputs
Ask (or infer from provided context/uploaded files) for whatever is missing:

| Input | Required? | Default if unspecified |
|---|---|---|
| Target persona / title | Yes | Ask — cannot personalize without this |
| Product/offer + core value prop | Yes | Ask |
| Number of touches | No | 5 |
| Channel mix | No | Email-only |
| Total sequence length (days) | No | 12-14 days |
| Proof points allowed (case studies, metrics) | No | Use generic proof language, mark placeholders |
| Per-account research (news, tech stack, hiring, funding, content) | Yes, for real personalization | Ask user to paste it, or use available research/search tools |
| Sender's name, role, tone/voice sample | No | Neutral, direct B2B tone |

If the user supplies a *list* of target accounts, confirm whether they want one
sequence template with personalization variables flagged, or a fully separate
sequence written per account. Default to asking this via a single clarifying
question if the list has more than 3 accounts (writing 3+ fully bespoke sequences
without confirming is a large amount of work to redo if the user wanted a template).

## Step 2 — Choose Cadence
Consult `references/channel-cadence-guide.md` and `sub-skills/cadence-strategy/reference.md`.
Key decision factors:
- **Deal size / ACV**: higher ACV → fewer, more spaced-out, higher-effort touches.
- **Seniority of persona**: C-level → shorter sequence, more respect for time,
  earlier exit; manager/individual contributor → can sustain more touches.
- **Inbound vs. cold**: warm signal (content download, event attendee) → can open
  more directly; fully cold → needs more curiosity-led opening.

## Step 3 — Draft Touch 1
This is the highest-leverage email. Requirements:
- Opens with something true and specific about the account (not the sender).
- One clear reason the offer might matter to *this* persona right now.
- Soft, low-friction CTA (a question, not "book a 30-min call").
- Under ~120 words body, plaintext-feeling (no heavy HTML/formatting cues).
- Subject line: lowercase-feeling, specific, not clickbait. Avoid generic subjects
  like "Quick question" unless paired with genuinely distinct body content.

If sharp personalization signals are not available for touch 1, do not proceed with
generic filler — tell the user what signal is missing and either ask for it or use
a search/research tool if available.

## Step 4 — Draft Touches 2 through N-1
Each subsequent touch must introduce a **new angle**, not just re-send the pitch:
- Touch 2: a different value angle, or a proof point/example relevant to the persona.
- Touch 3: a resource, insight, or question that stands alone in value (i.e., useful
  even if they never buy) — this is the "give before you ask" touch.
- Touch 4 (if present): social proof — a peer company/persona example, kept general
  unless real, confirmed case studies exist.
- Never write a touch whose entire content is a variation of "just checking in" or
  "wanted to bump this to the top of your inbox."

## Step 5 — Draft the Breakup Touch
See `sub-skills/breakup-messaging/reference.md`. Always:
- Signal this is the last outreach in this sequence.
- Remove pressure — make it easy to say "not now" or ignore without guilt.
- Leave the door open for the prospect to re-engage on their own timeline.

## Step 6 — Validate
Walk the full sequence through `instructions/validation-rules.md`. If code execution
is available, run `scripts/validate_sequence.py` against the drafted copy for:
- Subject line duplication across touches
- Spam-trigger words/phrases (`resources/spam-trigger-words.txt`)
- Body word count per touch
- Touch-to-touch text similarity (catches lazy copy-paste re-use)

## Step 7 — Deliver
Output using `templates/sequence-brief-template.yaml` structure: subject line, send
offset (day X), body, and a one-line rationale per touch. Rationale lines help the
user quickly verify the personalization logic without re-deriving it themselves —
do not omit these even if the user didn't ask for them.

## Decision Rules
- If the user gives no research/signals at all and no tools are available to gather
  them: draft the sequence with clearly marked personalization placeholders
  (e.g., `[INSERT: recent product launch or news hook]`) rather than inventing facts.
- If channel mix includes LinkedIn or calls: draft those touches at a summary level
  here (what day, what goal) and hand off the actual LinkedIn copy to
  `linkedin-outreach-writer` conventions/sub-skills rather than duplicating that logic.
- If the user asks for >7 touches, confirm intent before proceeding.
