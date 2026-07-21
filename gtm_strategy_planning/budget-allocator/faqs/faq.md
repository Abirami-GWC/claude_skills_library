# Frequently Asked Questions

**Purpose of this file**: Answers common questions about methodology, data requirements, edge cases, output customization, statistical caveats, and how this skill hands off to related skills.

---

### Methodology

**1. What budgeting framework does this skill default to if the user doesn't specify one?**
It defaults to a blended approach: a top-down ceiling for discipline, a bottom-up build for channel-level detail, and zero-based scrutiny applied to the lowest-performing 20-30% of current spend. See `references/budget_planning.md`.

**2. What's the difference between ROI, ROAS, and LTV:CAC, and when should each be used?**
ROI measures overall financial return net of cost (best for cross-channel comparison, ideally margin-based); ROAS measures revenue efficiency of ad spend specifically (best for fast-attribution paid channels); LTV:CAC measures the durability of the customer relationship relative to acquisition cost (best for evaluating long-term unit economics). See `references/roi_framework.md`.

**3. Why does this skill emphasize "marginal return" instead of "average return"?**
A channel's average return can look strong while the next incremental dollar produces a much weaker return due to saturation (e.g., a paid search auction becoming more competitive). Reallocating budget based on average return alone can lead to over-investing in an already-saturated channel. See `references/roi_framework.md`.

**4. What is "fully-loaded CAC" and why is it preferred over "media-only CAC"?**
Fully-loaded CAC includes all costs contributing to acquisition — media, creative, tooling, salaries/commissions, agency fees, events, and partner fees — not just working media spend. Media-only CAC typically understates true acquisition cost by 1.5-3x. See `references/cac_calculation.md`.

**5. How does this skill decide between linear/trend, cohort-based, and pipeline-coverage forecasting?**
It matches the model to the data available and sales motion: linear/trend for channels with consistent multi-period history, cohort-based for recurring-revenue businesses where retention matters, and pipeline-coverage for B2B motions with a defined funnel stage structure. See `references/forecasting_models.md`.

**6. Why does the skill insist on best/base/worst-case scenarios instead of a single forecast number?**
A single point forecast hides the underlying uncertainty in the assumptions. Presenting a range (with stated key drivers) lets stakeholders see what would need to be true for the plan to over- or under-perform, and pre-plan responses. See `references/scenario_planning.md`.

### Data Requirements

**7. What historical data does this skill need at minimum?**
At minimum: total budget for the period, and directional spend/output data per channel (even if approximate). More precise outputs require: fully-loaded cost components, new customers acquired per channel, revenue/margin per customer, and retention data if LTV is needed.

**8. How much historical data is "enough" for a reliable forecast?**
Roughly 6+ consistent periods for linear/trend forecasting, and 4+ comparable cohorts for cohort-based forecasting. Fewer periods can still be used but should be presented as lower-confidence, wider-range estimates.

**9. What if I only have blended (not channel-level) CAC or ROI data?**
The skill will work with blended figures but will explicitly note that channel-level reallocation recommendations carry lower confidence without channel-level attribution, and will recommend establishing channel-level tracking going forward.

**10. Does this skill require access to a live CRM, ad platform, or BI tool?**
No. It works from data supplied directly in the conversation (pasted tables, summarized figures, or uploaded data). It does not perform live data pulls from external systems.

### Edge Cases

**11. What happens if there's no historical data at all (e.g., a brand-new business or new market)?**
The skill uses category/industry-typical benchmark ranges, clearly labels them as estimates rather than facts, and recommends a short initial test period or data-collection checkpoint before committing the full budget. See `references/budget_planning.md` and Example 5 in `examples/examples.md`.

**12. How does the skill handle a brand-new channel with no baseline performance?**
It includes the new channel in the model using benchmark estimates (clearly labeled), sizes an initial test-level allocation rather than a full-scale commitment, and flags that the figures should be replaced with actuals after the first measurement period.

**13. What if the user's stated budget can't realistically achieve their stated growth target?**
The skill states the gap explicitly (e.g., "$490K short of the pipeline required") and presents trade-off options — extend the timeline, increase the budget, or lower the target — rather than silently inflating projected returns to make the numbers appear to work.

**14. What if two data points the user provides contradict each other (e.g., two different CAC figures for the same channel)?**
The skill surfaces the contradiction rather than guessing which is correct, and asks which figure is authoritative if it would materially change the recommendation.

**15. How does the skill handle extreme concentration in one channel (e.g., 90% of budget in one channel)?**
It flags concentration risk explicitly once a single channel exceeds roughly 50-60% of total budget without strong stated justification, since this creates exposure to platform, auction, or partner-relationship risk. See `checklists/quality_checklist.md`.

**16. What happens with a zero or near-zero budget scenario?**
The skill will note that below certain practical minimums (e.g., a channel's minimum effective ad spend threshold), some channels may not be viable at all, and will recommend concentrating on the lowest-CAC, lowest-minimum-spend options rather than spreading an insufficient budget too thin.

### Output Customization

**17. Can I get just the CAC analysis without a full budget model?**
Yes. Each output (Budget Allocation Model, Channel Recommendations, ROI Forecast, CAC Analysis, Spend Distribution) can be requested independently; the corresponding template and prompt in `templates/` and `prompts/` can be used standalone.

**18. Can the skill express recommendations as percentages instead of dollar amounts?**
Yes, the templates support both; percentages are generally recommended alongside dollar figures for easier sensitivity review.

**19. Can I request the model in a different currency or planning horizon (monthly vs. quarterly vs. annual)?**
Yes, both are user-configurable inputs; the templates use bracketed placeholders for currency and horizon so they can be adapted to any planning cycle.

**20. Does the skill support segment-level breakdowns (e.g., SMB vs. Enterprise)?**
Yes, `templates/cac_analysis_template.md` includes an optional segment breakout section for cases where the sales motion or unit economics differ materially by segment.

### Statistical Caveats

**21. How confident should I be in a forecast built from limited data?**
Confidence should scale with the number of historical periods and consistency of the underlying trend. The skill will explicitly qualify forecasts as high/medium/low confidence and state the basis for that qualifier.

**22. Why does the skill avoid presenting a single precise forecast number?**
Because false precision (e.g., "exactly 342 customers") implies a level of certainty the underlying data rarely supports. The skill prefers ranges and explicit confidence qualifiers. See `references/forecasting_models.md`.

**23. How does the skill handle attribution uncertainty across multi-touch customer journeys?**
It states the attribution method used (last-touch, first-touch, multi-touch, or channel-level cohort approximation) explicitly and applies it consistently across channels being compared, rather than silently mixing methods.

### Handoffs to Related Skills

**24. Can this skill write our GTM positioning or messaging strategy?**
No. Positioning and messaging strategy is handled by a separate GTM Strategy Builder skill. This skill will complete any budget/spend/ROI portion of a mixed request and note that the positioning portion should go to that skill.

**25. Can this skill build our quarterly roadmap or launch timeline?**
No. Roadmap timelines and milestone sequencing are handled by a separate Quarterly Roadmap Planner skill. This skill produces the budget inputs (e.g., what spend supports which initiative) but does not sequence the roadmap itself.

**26. Can this skill write our board deck narrative or executive slide copy?**
No. Board-ready narrative and storytelling is handled by a separate Board Deck Narrative skill. This skill can supply the underlying budget/ROI/CAC figures and tables that a board narrative would reference, but does not produce narrative prose or slide copy.

**27. If a request spans budget allocation and one of these other domains, how does the skill respond?**
It completes the budget/spend/ROI portion fully and clearly states that the remaining portion (positioning, roadmap, or narrative) falls to the relevant separate skill, without attempting to produce that content itself or duplicating that skill's methodology.

**28. Does this skill's output feed into those other skills, or is it fully separate?**
Its outputs (Budget Allocation Model, CAC Analysis, ROI Forecast, Spend Distribution) are natural inputs to those other skills — e.g., a Board Deck Narrative skill might reference this skill's ROI Forecast — but this skill does not generate or duplicate their narrative/timeline/positioning content itself.
