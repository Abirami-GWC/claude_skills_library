# FAQ

**Purpose of this document:** Answer common scope, methodology, edge-case, data, customization, and integration questions about the GTM Strategy Builder skill.

---

### Scope Questions

**1. What exactly does this skill produce?**
Any combination of: Quarterly GTM Plan, Positioning Strategy, ICP Definition, Buyer Persona Set, Messaging Framework, Channel Strategy summary, and Strategic Recommendations. See `SKILL.md` Outputs section.

**2. Does this skill handle pricing strategy?**
No. Pricing may be referenced as an input (e.g., to inform positioning or segmentation), but designing a pricing model or pricing tiers is not this skill's responsibility.

**3. Does this skill write ad copy or campaign creative?**
No. It produces the strategic messaging framework (pillars, proof points, persona variants) that creative copy should be derived from, but it does not produce finished ad creative or campaign assets itself.

**4. Can this skill be used for a product launch instead of a quarterly refresh?**
Yes. The same workflow applies to a launch GTM plan; treat the launch window as the "quarter" being planned for.

**5. Is this skill industry-specific?**
No. It is deliberately industry-agnostic. It has been used illustratively across B2B SaaS, healthcare, fintech, industrial/manufacturing, consumer, and professional services in `examples/examples.md`, but the frameworks apply to any industry.

**6. Does this skill do market research (e.g., primary customer interviews)?**
No. It structures and applies frameworks to information the user provides or that Claude reasons about. It will recommend specific research/validation steps (e.g., win/loss interviews) but does not conduct them.

### Methodology Questions

**7. What positioning methodology does this skill use?**
A competitive-alternative-first method (aligned with widely used approaches like April Dunford's and Geoffrey Moore's positioning work), detailed in `references/positioning_framework.md`.

**8. What ICP methodology does this skill use?**
A fit-versus-propensity model with firmographic/technographic/behavioral/trigger dimensions and a weighted scoring approach, plus an explicit anti-ICP, detailed in `references/icp_framework.md`.

**9. Are buyer personas based on demographics or something else?**
Jobs-To-Be-Done (functional, emotional, social jobs) plus role in the buying committee — not demographic/biographical detail. See `references/buyer_persona_guide.md`.

**10. How does this skill decide on a GTM motion (sales-led vs. product-led, etc.)?**
Based on deal complexity, buyer autonomy, time-to-value, and market maturity, per `references/gtm_frameworks.md` — never based on trend-following.

**11. How does segmentation relate to ICP?**
Segmentation maps the whole market's structure (see `references/market_segmentation.md`); ICP selects which resulting segment(s) to prioritize and defines them in targetable detail (see `references/icp_framework.md`). Segmentation comes first.

**12. What framework grounds competitive analysis?**
A combination of industry-structure analysis (five forces) and buyer-level competitive alternative mapping plus win/loss analysis, detailed in `references/competitive_analysis.md`.

### Edge Case Questions

**13. What if the user's request mixes GTM strategy with budget allocation?**
Complete the GTM-strategy portion (segments, positioning, messaging, motion, prioritized channel list) and explicitly hand off the dollar-allocation portion to the Budget Allocator skill.

**14. What if the user asks for a detailed execution timeline alongside the GTM plan?**
Produce the GTM plan, and note that translating it into a sprint/execution timeline is handled by the Quarterly Roadmap Planner skill.

**15. What if the user asks for a board deck based on the GTM plan?**
Produce or reference the GTM plan content, and note that board-narrative framing and slide structure is handled by the Board Deck Narrative skill, which takes this GTM plan as direct input.

**16. What if existing GTM artifacts (positioning, messaging) are inconsistent with each other?**
Surface the inconsistency explicitly before finalizing a refresh, and resolve it based on the stated current business goal, per the Error Handling section of `SKILL.md`.

**17. What if the user has no existing customers yet (pre-launch)?**
Proceed with hypothesis-driven segmentation, ICP, and personas, clearly labeled as hypotheses, and recommend the specific validation steps (e.g., early customer interviews) needed post-launch.

**18. What if the request is too vague to identify a target segment?**
Propose 2-3 plausible segment options and ask the user to choose, or proceed with the most defensible option clearly labeled as an assumption, per `SKILL.md` Error Handling.

**19. What if the user wants GTM strategy for an internal, non-commercial initiative (e.g., an internal tool)?**
The same segmentation/positioning/messaging logic can apply to internal stakeholder audiences, but this is a stretch use of the skill; confirm the internal "customer" and adapt terminology accordingly.

### Data Requirement Questions

**20. What information does Claude need before starting?**
See `SKILL.md` Inputs section: product/service description, target industry (if known), current/desired segments, known competitors, existing GTM artifacts (if refreshing), business goals, and known constraints.

**21. What happens if most of that information is missing?**
Claude proceeds using clearly labeled placeholder assumptions rather than blocking, and invites the user to correct them, per the Inputs and Error Handling sections of `SKILL.md`.

**22. Does this skill require access to real analytics/CRM data?**
No. It works from whatever qualitative or quantitative information the user provides in conversation; it does not integrate with external systems.

### Output Customization Questions

**23. Can I get just one artifact (e.g., only messaging) instead of a full plan?**
Yes. State which specific artifact is needed; Claude will produce only that artifact using the relevant template and reference files rather than a full Quarterly GTM Plan.

**24. Can the output be tailored to a specific format (e.g., shorter, slide-style bullets)?**
Yes, the underlying strategic content stays the same; formatting/length can be adapted on request, as long as all validation-rule elements (specific segment, complete positioning statement, etc.) remain present.

**25. Can this skill produce content in a language other than English?**
Yes, the frameworks are language-independent; specify the desired output language and Claude will apply the same frameworks and structure in that language.

### Integration with Companion Skills

**26. How does this skill relate to the Budget Allocator skill?**
This skill produces the prioritized channel/motion strategy (which channels, in what priority order, for which segments). The Budget Allocator skill takes that prioritized list and determines specific dollar allocation, CAC/LTV modeling, and spend mix. This skill does not perform that financial modeling itself.

**27. How does this skill relate to the Quarterly Roadmap Planner skill?**
This skill defines the strategic "what and why" (segments, positioning, messaging, motion). The Quarterly Roadmap Planner skill turns strategic priorities into execution timelines, sprint sequencing, and delivery milestones. This skill does not produce execution schedules.

**28. How does this skill relate to the Board Deck Narrative skill?**
This skill produces the substantive GTM strategy content. The Board Deck Narrative skill packages strategic content (including GTM strategy, but also financials and other inputs) into an executive/board-appropriate narrative and slide structure. This skill does not produce board-facing narrative framing or slide decks.

**29. If I only have this skill available, can it just do the adjacent work anyway?**
It can provide lightweight, qualitative adjacent commentary (e.g., a rough channel priority order, a one-paragraph plain-language summary) but should not attempt full budget modeling, execution roadmaps, or formal board narratives — those require dedicated methodology this skill does not own. It should clearly flag when a request has exceeded its intended scope.

**30. Can the outputs of this skill be handed directly into those companion skills?**
Yes — outputs are intentionally structured (named channels, named segments, named goals) so they can be passed as direct inputs to Budget Allocator, Quarterly Roadmap Planner, or Board Deck Narrative without rework.
