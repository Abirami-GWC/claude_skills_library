# Worked Example — Campaign Calendar Builder (Conflict Caught)

## User input

> "We're launching a new feature on August 10th. Blog post needs to be
> written by Dana, then goes through legal review, then publishes on launch
> day. Sam wants to post the LinkedIn announcement the day before launch to
> build anticipation, and send the email on launch day. Build me a calendar
> and flag anything that won't work."

## Claude's internal process (not shown to user)

1. Gather activities: blog draft (Dana), legal review, blog publish (anchor:
   Aug 10), LinkedIn post (Sam, requested for Aug 9 — the day *before*
   launch), email (Sam, Aug 10).
2. Infer the obvious dependency the user didn't state explicitly: the
   LinkedIn and email promotion both logically depend on the blog post being
   live, since they reference it — tagged `dependency_source: "inferred"`,
   not silently treated as user-confirmed.
3. Populate `knowledge/calendar_schema.json` with all 5 activities and dependencies.
4. Run `scripts/validate_calendar.py --min-buffer-days 1` — catches that the
   user's requested LinkedIn date (Aug 9) is *before* the blog publish date
   it depends on (Aug 10), and that the email has zero buffer after publish.
5. Do not silently move the LinkedIn post — flag the conflict and present
   the tradeoff to the user.
6. Render `scripts/build_gantt_chart.py` — the conflict shows as a
   backwards-pointing red arrow, visually confirming the issue before delivery.

## Output delivered to user

```
Built the calendar — found one scheduling conflict worth flagging before we lock this in:

⚠️ LinkedIn announcement is scheduled for Aug 9, but it depends on the blog
post publishing, which isn't until Aug 10. As written, the LinkedIn post
would go out a day before the thing it's announcing is actually live.

This dependency (LinkedIn/email → blog publish) was inferred from context,
not something you stated directly — worth confirming it's correct before I
finalize the calendar.

Options:
1. Move the LinkedIn post to Aug 10 (same day as publish) — safest, but
   loses the "anticipation" framing you mentioned wanting.
2. Change the LinkedIn post's angle to a teaser that doesn't require the
   blog to be live yet (e.g., "something's coming tomorrow") — keeps the
   Aug 9 date but changes what it depends on.
3. Move the blog publish date earlier to Aug 9 so LinkedIn can safely follow it.

Let me know which direction you want and I'll finalize the calendar and Gantt chart.

[Gantt chart image attached — the conflict is visible as a red backwards arrow
between "Publish blog post" and "LinkedIn announcement."]
```

## Why this is a good output

- The conflict was caught programmatically (via the validator script) rather
  than by eyeballing five activities, which is exactly the kind of check that
  gets missed under launch-week pressure.
- Claude did not silently resolve the conflict by moving the LinkedIn date —
  it surfaced the tradeoff and let the user decide, per the skill's explicit rule.
- The inferred dependency was labeled as inferred, not presented as something
  the user had confirmed, so the user has the chance to correct it if the
  actual intended relationship was different.
