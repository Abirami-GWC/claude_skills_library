# Board Deck Narrative — Frequently Asked Questions

**Purpose of this file:** Answer common questions about how to use this skill effectively, including tone/length calibration, handling incomplete data, confidentiality, priority compression, and how this skill relates to upstream strategy/budget/roadmap skills.

---

**1. How long should a board narrative be?**
Default to board-standard brevity: a one-page executive summary or one-pager, a 1-3 page memo, or an 8-12 slide presentation outline unless the user specifies a different constraint. When a constraint is stated (e.g., "keep it to 5 slides"), that constraint always overrides the default.

**2. How formal should the tone be?**
Tone should be plain, confident business language — neither casual nor overly technical. Avoid internal jargon, tool names, and team-specific shorthand. Match the register of a document that could be read by someone outside the organization without translation.

**3. What if I only have partial data — some metrics but no clear ask?**
Proceed with what is available, clearly mark missing pieces (e.g., "[ASK NOT SPECIFIED]"), and ask the user directly whether this is meant to be informational only or whether a decision is being requested, since that materially changes the document's structure.

**4. What if the source material is extremely long (e.g., a 40-page strategy document)?**
Read it fully, then compress using the workflow's prioritization and grouping steps — group initiatives by outcome/theme, select only the highest-leverage metrics, and cap strategic priorities at 5. Note in the output if significant detail was omitted for length, so the user can retrieve it from the source if the board asks.

**5. What if the source material is extremely sparse (a sentence or two)?**
Do not fabricate metrics, priorities, or risks to fill gaps. Ask for the minimum viable input (at least one metric, the purpose of the meeting, and 2-3 priorities) or provide a labeled skeleton the user can fill in.

**6. Can this skill decide what our GTM strategy should be?**
No. This skill only narrates and compresses a strategy that already exists or is supplied by the user. Strategy formulation (segmentation, positioning, market entry decisions) belongs to a GTM Strategy Builder skill.

**7. Can this skill build our budget or calculate ROI?**
No. It can reference budget conclusions or asks handed to it (e.g., "we are requesting a 20% increase") but does not model, calculate, or allocate budget. That belongs to a Budget Allocator skill.

**8. Can this skill create our quarterly roadmap?**
No. It compresses an existing roadmap's headline priorities into board-level language but does not sequence, resource, or schedule roadmap items. That belongs to a Quarterly Roadmap Planner skill.

**9. How does this skill avoid duplicating content from those other skills?**
It treats their outputs as inputs: a completed strategy, a finalized budget ask, or a roadmap's priority list are all things this skill consumes and reframes for an executive audience, rather than content it recreates or second-guesses. If asked to originate any of that content itself, it flags the request as out of scope and points to the appropriate upstream skill.

**10. What if I ask this skill to both build the roadmap and summarize it for the board?**
It will separate the two requests, decline the roadmap-building portion (redirecting to a Quarterly Roadmap Planner skill), and offer to proceed with the board narrative once the roadmap exists or is supplied, even partially.

**11. How do I compress a 40-initiative roadmap into 3 strategic priorities?**
Group initiatives by the business outcome they serve (e.g., retention, expansion, efficiency) rather than by team or system. Identify the 2-4 themes that capture the majority of strategic intent, state each as an outcome (not a task list), and use a one-line rationale per priority. If more than 5 themes are truly necessary, that likely signals the material needs further compression or the board conversation needs to be split across sessions.

**12. What if the board only wants 3 priorities, but our real roadmap has 5+ equally important themes?**
Present the top 3 by impact or urgency, and note that additional priorities exist and are available in supporting material or upon request, rather than force-fitting a false ranking.

**13. How does this skill handle confidential or sensitive information (e.g., churn, layoffs, underperformance)?**
It frames sensitive figures at a level of precision appropriate to the audience and likely distribution (e.g., rounded ranges rather than exact figures if material may circulate beyond the room), while still surfacing material risks and bad news honestly rather than omitting them.

**14. Will this skill soften bad news to make the board feel better?**
No. It states underperformance and risk plainly, pairs it with cause and a forward plan, and treats honest framing as more credible to boards than optimistic smoothing. It will resist requests to obscure or omit materially relevant bad news.

**15. What if my board wants more operational detail than a typical board?**
Calibrate to the specific board's known preferences if stated, but default to higher altitude with detail available on request or in an appendix, since board norms trend toward strategic rather than operational detail.

**16. How many metrics should be in a board narrative?**
Five to seven at most, chosen to answer whether performance is on track, why (leading indicators), and whether the underlying business economics are healthy (unit economics). More than that typically indicates the set has not been curated.

**17. What is a "north star" metric and do I need one?**
It's the single measure best capturing the core value being delivered, which other metrics ladder up to. It's recommended but not mandatory — if the business or situation doesn't have an obvious single north star, a small, clearly connected set of metrics can substitute.

**18. What if the data I provide conflicts with itself (e.g., two different totals for the same metric)?**
The conflict is surfaced directly to the user rather than silently resolved by picking one number, since silently choosing could introduce inaccuracy into board-facing material.

**19. Can this skill produce a full slide deck with visual design?**
No — it produces the narrative content and a slide-by-slide outline (headlines and bullet points), not visual design, layout, or a finished presentation file. The outline is meant to be built into a deck using whatever presentation tooling the user prefers.

**20. What's the difference between the "Board Summary," "Executive Narrative," "One-page Strategy," "Decision Summary," and "Presentation Outline" outputs?**
Board Summary and Executive Narrative are close variants of a condensed overview (memo-style vs. narrative-style); One-page Strategy is a single-page distillation focused on priorities and rationale; Decision Summary is narrowly focused on a specific ask; Presentation Outline is a slide-by-slide structure. Which to use depends on the requested format and occasion — see the Outputs section of SKILL.md.

**21. How should risks be phrased for a board audience?**
In business and financial impact terms, not technical or process terms — e.g., "risk of missing the annual retention target by [X]%" rather than "risk of a system migration delay," unless the technical detail directly explains the business impact.

**22. What if there's no explicit ask — the update is purely informational?**
That's fine; not every board interaction requires a decision. State clearly that the material is for information, and use a plain next-steps section instead of an options/recommendation structure.

**23. How should I handle a request to present a pivot the board hasn't been prepared for?**
Use the pivot narrative arc: state the original rationale (context), the evidence that conditions changed (conflict), and the new direction with a specific ask (resolution). Reference relevant prior board decisions to maintain continuity rather than presenting the pivot as disconnected from history.

**24. Should I include appendix/backup detail in the main narrative?**
No — keep backup detail in a clearly separated appendix or offer it as available on request. The main narrative should stay at board altitude throughout.

**25. What if the user wants the narrative to be much longer than typical board material (e.g., 10 pages)?**
Honor the user's stated constraint, but note if the length exceeds typical board norms and suggest an executive summary be added at the front so the core message is still accessible even at that length.

**26. Can this skill be used for investor updates as well as board meetings?**
Yes — the same narrative and framing disciplines apply to investor audiences, with additional attention to confidentiality and precision given typically wider distribution.

**27. What happens if the user's request is really about building the underlying strategy, not narrating it?**
The skill states plainly that strategy origination is out of scope, explains the distinction, and points to the appropriate upstream skill (GTM Strategy Builder), rather than attempting to originate strategic decisions itself.

**28. How does this skill decide which narrative arc (steady progress, course correction, underperformance, pivot, investment ask) to use?**
By assessing the situation described in the source material and the user's stated purpose for the board interaction — each arc type is described with its context/conflict/resolution shape in `references/strategic_narrative_design.md`.

**29. What if I need the same content in multiple formats (e.g., both a memo and a slide outline)?**
The skill can produce both from the same underlying compressed content, using `templates/board_memo_template.md` and `templates/presentation_outline_template.md` respectively, keeping the narrative consistent across formats.

**30. Does this skill fact-check the numbers I provide?**
No — it cannot independently verify figures. It can flag internal inconsistencies, missing data, or implausible-looking claims for the user to confirm, but accuracy of the underlying data remains the user's responsibility.
