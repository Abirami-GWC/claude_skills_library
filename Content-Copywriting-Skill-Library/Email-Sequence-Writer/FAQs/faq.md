# FAQ

1. **What counts as an "email sequence" versus a single email?** Two or more emails with a shared strategic arc sent over time to move the recipient toward a goal.
2. **How many emails should a sequence have?** Use the standard length in `references/email_sequence_frameworks.md` for that sequence type unless the user specifies otherwise; shorten if the goal doesn't justify the standard length.
3. **Can this skill write a single standalone email?** It can, but for a truly standalone one-off email, no skill is needed — just write it directly.
4. **Does this skill handle HTML/ESP-specific code?** No, it produces copy only; formatting for a specific ESP is out of scope.
5. **Should every email include a discount?** No — only when a genuine incentive exists; manufactured discounts in every sequence erode brand trust and margin.
6. **How is this different from Ad Copy Generator?** Ad Copy Generator writes paid ad copy for channels like Google/Meta/LinkedIn Ads; this skill writes owned-channel email sequences.
7. **How is this different from Brand Voice Writer?** Brand Voice Writer adjusts tone/voice on existing copy; this skill builds new multi-email strategic sequences from scratch.
8. **What if the user only gives a goal, no audience?** Ask one clarifying question about audience, since tone and objection-handling depend heavily on who's reading.
9. **Can sequences include images or visual design notes?** The skill produces copy; visual/design notes can be added as bracketed suggestions but aren't the primary deliverable.
10. **What's the ideal subject line length?** Roughly 30-50 characters for mobile-heavy audiences; see `references/subject_line_playbook.md`.
11. **Should CTAs repeat across emails in a sequence?** The commitment level should escalate, not repeat identically, across the sequence.
12. **How many CTAs per email?** Exactly one.
13. **What if the user wants a sequence longer than the framework recommends?** Accommodate it, but note where redundancy risk increases.
14. **Can this skill review an existing sequence instead of writing a new one?** Yes — see the diagnostic workflow in `prompts/prompt_library.md`.
15. **Does the skill guarantee open/click rates?** No — it applies established best practices but cannot guarantee performance without live data.
16. **What tone should be used by default?** Warm and conversational for B2C, professional-but-human for B2B, unless the user specifies otherwise.
17. **Should urgency language be used in every promotional sequence?** Only where a real deadline or constraint exists.
18. **How does the skill handle personalization beyond first name?** It references the specific trigger event (signup, cart abandon, milestone) in the opening line.
19. **What if the sequence type doesn't match any standard framework?** Adapt the closest framework and note the adaptation.
20. **Can this skill generate A/B subject line variants?** Yes, especially recommended for the first and final emails in a sequence.
21. **Is cadence (send timing) part of the output?** Yes, a recommended schedule (day-based or trigger-based) is included.
22. **What if the brand has no existing testimonials for social-proof emails?** Ask if any exist; if not, either omit social proof or use a clearly-labeled illustrative example.
23. **Should every sequence end with a hard sell?** No — nurture and welcome sequences often end with a soft CTA; only launch/promotional and cart-abandon sequences typically end with a hard, direct offer.
24. **Can the skill shorten an existing overlong sequence?** Yes, using the tightening/editing prompt to merge redundant emails.
25. **What if compliance/legal requirements (e.g., unsubscribe language) are needed?** The skill can include standard unsubscribe/compliance placeholders but does not provide legal review.
26. **How does the skill decide between AIDA, PAS, or StoryBrand for a given email?** Based on that email's strategic role — see `references/email_copywriting_frameworks.md`.
27. **Can this be used for internal/employee email sequences?** The frameworks are built for external marketing sequences; internal comms would need different structures.
