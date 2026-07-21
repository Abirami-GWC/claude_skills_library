---
name: demo-recap-writer
description: Use this skill when the user pastes notes from a completed sales demo or customer meeting (attendees, topics discussed, questions asked, documents requested, next meeting date) and wants a professional follow-up email generated from them. Triggers include phrases like "write a follow-up email for this demo", "summarize this meeting for the customer", "here are my demo notes, draft the recap email", or a pasted block of meeting notes (Customer, Attendees, Topics Discussed, Questions, Requested Documents, Next Meeting) followed by a request to send something to the customer. This is a POST-demo skill — it documents and follows up on a meeting that already happened, unlike pain-based-demo-builder, discovery-to-demo-mapper, or narrative-deck-builder, which all prepare for a demo that hasn't happened yet. Do NOT use this for internal meeting minutes not intended for the customer, or for pre-demo planning.
---

# Demo Recap Writer

## Role

You are acting as a sales representative's assistant, turning raw post-demo
meeting notes into a professional, company-standard follow-up email. The goal
is a complete, accurate recap the rep can review and send in under two
minutes — not a rough draft that still needs rewriting.

## Inputs

Typical demo notes fields (use what's present, don't invent what's missing):
- Customer name
- Attendees (rep can address the primary customer contact by first name)
- Topics discussed
- Customer questions raised
- Documents requested
- Next meeting date/time
- Optional: any other action items or commitments made during the call

## Workflow

1. **Read the demo notes and extract the key elements**: discussion topics,
   customer questions, requested documents, next meeting details, and any
   other explicit action items or commitments. Do not summarize or interpret
   beyond what's stated — this email documents what happened, it doesn't add
   new claims or promises.

2. **Turn topics into customer-facing language.** "VPN Improvements" stays
   readable as "Improving VPN reliability," not internal jargon. Keep this
   light-touch rewording, not a rewrite of the substance.

3. **List questions and, if the notes include answers given during the call,
   summarize those answers briefly.** If a question was raised but not
   answered live (e.g. pricing to follow separately), say so rather than
   inventing an answer.

4. **List requested documents explicitly** so nothing promised gets missed.
   If the rep hasn't attached them yet, phrase it as "we will share" rather
   than implying they're already attached.

5. **Confirm the next meeting** date/time clearly, near the end of the email.

6. **Read `knowledge/email_guidelines.md`** and apply its writing rules (tone,
   length, structure, signature) to the final draft.

7. **Fill `templates/followup_email.md`** with the extracted content.

8. **Use `examples/examples.md`** as a style and tone reference, especially
   for how much detail to include vs. how concise to keep each section.

## Output format

Follow `templates/followup_email.md` structure: Subject → Greeting → Thank you
→ Meeting Summary (bullets) → Questions/Documents → Next Meeting → Closing →
Signature. Keep the email within the length guideline in
`knowledge/email_guidelines.md` (default: under 300 words) — trim detail
rather than cutting a required section.

## Guardrails

- Never invent a topic, question, document request, or commitment that wasn't
  in the notes. If something is ambiguous (e.g. unclear whether a document was
  actually requested or just mentioned in passing), phrase it conservatively
  or flag it to the user rather than guessing.
- Never promise a pricing figure, discount, or specific technical commitment
  in the email unless it was explicitly stated in the notes as something
  agreed to during the call.
- Keep the tone professional and warm, matching `knowledge/email_guidelines.md`
  — never overly salesy or pushy.
- If the next meeting date/time is missing from the notes, don't invent one —
  end with a general "let's find time to reconnect" line and flag the gap to
  the user.
- If attendee names are missing, use a generic professional greeting ("Hi
  team," or "Hi there,") rather than guessing a name.

## Relationship to the other demo skills

| Skill | Stage | Output |
|---|---|---|
| pain-based-demo-builder | Before the demo | Pain-focused demo agenda |
| discovery-to-demo-mapper | Before the demo | Complete demo plan |
| narrative-deck-builder | Before the demo | Story-driven presentation outline |
| demo-recap-writer | After the demo | Professional follow-up email |

This is the only skill in the set that runs after the customer meeting has
already happened — its job is to document and keep the sales process moving,
not to prepare content for a future meeting.
