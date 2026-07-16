---
name: connection-request-writer
description: >
  Sub-skill of linkedin-outreach-writer. Writes the connection request note only
  (not the DM sequence that follows). Enforces the 300-character limit and the
  no-pitch rule. Use internally at Step 2 of the parent workflow whenever a
  connection request is needed. Not intended to be triggered directly by end users.
---

# Connection Request Writer

## Purpose
The connection request note has one job: earn the accept. It is not the place to
pitch, explain the product, or build the full case — that comes later. This
sub-skill isolates that narrow job so it doesn't get diluted by pitch content.

## Rules
- Hard limit: 300 characters (aim for 150-250 in practice).
- One sentence. Two short sentences at most.
- Reference exactly one specific, genuine reason for connecting.
- No product/service mention, no company pitch, no "would love to tell you about..."
- No links.

## Pattern
`Hi [Name] — [specific, genuine reason tied to a real signal]. Would love to connect.`

or, when there's a mutual/shared context:
`Hi [Name] — [mutual connection/group/event reference]. [one line on shared relevance]. Would love to connect.`

## Common mistakes prevented
- Notes that exceed 300 characters and get cut off or rejected by LinkedIn's form.
- Notes that pitch, which lowers accept rates and can trigger spam reporting.
- Generic notes with no specific reason, which also lowers accept rates versus
  specific ones.
