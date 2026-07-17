# Validation Rules — Pre-Delivery QA

Run every drafted sequence through this checklist before delivering to the user.

## Structural checks
- [ ] Sequence has a clear touch count matching what was requested (or the agreed default of 5).
- [ ] Each touch has a distinct subject line — no duplicates.
- [ ] Send-day offsets are specified and increasing (e.g., Day 0, 3, 7, 12, 18).
- [ ] The final touch is clearly a breakup/exit message.

## Personalization checks
- [ ] Touch 1 references at least one specific, verifiable fact about the account
      or persona (not just "I noticed you're in [industry]").
- [ ] Remove the personalization line mentally — does the email still make generic
      sense for any company? If yes, it fails this check and needs a sharper hook.
- [ ] No invented statistics, funding rounds, exec names, or news events. Anything
      unverified is marked `[VERIFY: ...]` or `[INSERT: ...]`.

## Repetition checks
- [ ] No two touches make the same core argument in different words.
- [ ] No touch consists solely of "following up," "circling back," "bumping this up,"
      or equivalent with no new content.

## Tone & length checks
- [ ] Touch 1 body ≤ ~120 words.
- [ ] No touch exceeds ~150 words unless the user explicitly wants longer-form copy.
- [ ] Tone matches requested voice; default is direct, plain B2B English — no hype
      words ("revolutionary," "game-changing," "synergy") unless user's brand voice
      calls for it.

## Deliverability checks
- [ ] No subject line uses deceptive patterns (fake "Re:"/"Fwd:", fake calendar
      invite framing, ALL CAPS, excessive punctuation "!!!").
- [ ] No more than 1 link in early touches (links can hurt inbox placement).
- [ ] Cross-reference `resources/spam-trigger-words.txt`; flag any matches for the user.

## CTA checks
- [ ] CTA difficulty escalates gently across the sequence (soft question → clearer
      ask → easy binary yes/no) rather than a hard "book a call" in touch 1.
- [ ] Every touch has exactly one CTA — never stack multiple asks in one email.

## Final gate
If any unchecked item involves fabricated facts about a real company, do not deliver
the sequence with those facts present — replace with a placeholder and flag it
explicitly to the user in the response, not just in file comments.
