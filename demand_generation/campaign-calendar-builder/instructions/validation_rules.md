# Validation Rules — Campaign Calendar Builder

Run before delivering any calendar.

## Dependency checks

- [ ] Every activity's `depends_on` list only references activities that
      exist in the dataset (no dangling references).
- [ ] No activity is scheduled to start before an activity it depends on has ended.
- [ ] No circular dependencies (A depends on B, B depends on A).
- [ ] Every dependency is tagged `user-confirmed` or `inferred` — none left ambiguous.

## Lead-time checks

- [ ] Each activity's lead time (time between its start and the anchor/launch
      date, or its dependency's completion) meets or exceeds the relevant
      minimum in `knowledge/timeline_planning_principles.md`, unless the user
      has stated different constraints.
- [ ] Activities with typically long lead times (webinar, PR, paid creative,
      partner content) are flagged if their lead time is tight relative to the norm.

## Buffer checks

- [ ] Dependent activities have at least a minimal buffer (not scheduled to
      start the same day their dependency completes), unless the user has
      explicitly accepted zero buffer.

## Ownership/scheduling checks

- [ ] No owner is double-booked on the same date across activities that both
      require active work that day, where owner data is available.
- [ ] Unknown owners/dates are marked "TBD," not silently left blank or guessed.

## Final gate

If any dependency or lead-time check fails, do not silently resolve it —
present the conflict explicitly to the user with the specific activities and
dates involved, and let them decide the resolution (move a date, accept the
risk, cut an activity).
