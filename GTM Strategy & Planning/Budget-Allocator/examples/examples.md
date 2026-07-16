# Examples

**Purpose of this file**: Illustrative end-to-end examples showing when and how the Budget Allocator skill activates, across diverse industries and budget sizes, to demonstrate reusability and correct workflow application.

---

## Example 1: Multi-Channel Quarterly Budget Allocation (B2B SaaS, Mid-Size Budget)

**User Request**: "We have $500K for next quarter's marketing budget. Help us allocate it across paid search, content/SEO, events, and partner channels based on last year's performance."

**Why the Skill Activates**: The request explicitly asks for budget allocation across named channels using historical performance — a core Budget Allocator use case.

**Workflow**: Clarify total budget and horizon → establish baseline CAC/ROI per channel → select bottom-up approach (data available) → apply channel strategy tiering → optimize allocation → populate budget model template → validate against checklist.

**Expected Output**: Budget Allocation Model, Channel Recommendations, Spend Distribution.

**Final Response (condensed)**: Paid search $175K (35%, fast payback, CAC $2,100), content/SEO $100K (20%, compounding tier, CAC $850 trailing), events $125K (25%, medium payback, CAC $4,900 but highest deal size), partner $75K (15%, CAC $1,700), reserve $25K (5%). Total reconciles to $500K.

**Alternative Response**: If historical CAC data were unavailable for one channel (e.g., partner), the response would substitute an industry-benchmark CAC range clearly labeled as an estimate and recommend a data-collection step for next cycle.

**Edge Cases**: If channels' historical spend sums to more than $500K when extrapolated to targets, flag the gap and offer trade-off options rather than silently underfunding a channel.

---

## Example 2: CAC Spike Investigation and Reallocation (Consumer Fintech App)

**User Request**: "Our CAC on paid social jumped 40% this quarter. Should we shift budget to organic or email?"

**Why the Skill Activates**: This is a CAC analysis and channel reallocation question, both core responsibilities.

**Workflow**: Calculate fully-loaded CAC trend for paid social → compare against organic/email CAC and trend → assess marginal return (is paid social saturated?) → recommend reallocation with tier balance in mind.

**Expected Output**: CAC Analysis, Channel Recommendations.

**Final Response (condensed)**: Paid social fully-loaded CAC rose from $45 to $63 (auction saturation signal); organic CAC stable at $18 but slower-building; email CAC $22 with fast payback. Recommend shifting 15% of paid social budget to email (fast payback, stable CAC) and sustaining organic investment for compounding value; do not fully exit paid social given it still contributes top-of-funnel volume other channels rely on.

**Alternative Response**: If no spend-response data exists to test saturation, state that the marginal-return assessment is directional only and recommend a controlled test (e.g., ±20% spend test) before a large reallocation.

**Edge Cases**: If organic has fewer than 3 comparable historical periods, disclose that its CAC trend is not yet statistically reliable.

---

## Example 3: ROI Forecast for a Proposed Spend Increase (Manufacturing / Industrial B2B)

**User Request**: "Build an ROI forecast for a 15% increase in trade show and field event spend next year."

**Why the Skill Activates**: ROI forecasting for a specific channel spend change is a direct Budget Allocator responsibility.

**Workflow**: Establish baseline event ROI/ROAS → apply appropriate long-cycle measurement window → forecast using linear/trend model with saturation check → run best/base/worst scenario given long-cycle uncertainty.

**Expected Output**: ROI Forecast, Spend Distribution.

**Final Response (condensed)**: Base case: 15% spend increase ($90K to $103.5K) projects ROI of 240% (vs. 255% currently), reflecting mild diminishing returns; best case 280% if new target accounts convert faster than historical average; worst case 190% if event ramp-up slips a quarter. Recommend proceeding with increase but tracking pipeline-to-close conversion over the next 2 quarters given the long measurement window this channel requires.

**Alternative Response**: If only revenue (not margin) data is available, present ROAS instead of margin-based ROI and disclose the difference.

**Edge Cases**: Long sales cycle means results won't be fully observable for 2+ quarters; flag that early-period data will understate true ROI.

---

## Example 4: Budget Cut Response with Forecasting Under Constraint (Healthcare Services)

**User Request**: "Corporate just told us to cut the marketing budget by 20% for the rest of the year. What should we cut, and what happens to our pipeline forecast?"

**Why the Skill Activates**: This combines budget reallocation under a cut with forecasting — both explicitly in scope, and it is one of the required multi-channel-reallocation/forecasting-under-cut scenarios.

**Workflow**: Apply zero-based scrutiny to lowest-performing channels → model uniform cut vs. efficiency-ranked cut vs. strategic-protection cut → forecast pipeline impact of each option → recommend.

**Expected Output**: Budget Allocation Model, ROI Forecast, Channel Recommendations, Spend Distribution.

**Final Response (condensed)**: Uniform 20% cut projects a 19% pipeline reduction. Efficiency-ranked cut (defunding the lowest-ROAS display channel and trimming a saturated paid-search tranche) projects only an 8% pipeline reduction for the same dollar savings. Recommend efficiency-ranked option; protect the newly-launched regional channel despite its short track record given its strategic priority, funding it via savings from the cut channels.

**Alternative Response**: If leadership requires an even cut for political/fairness reasons, present the uniform-cut pipeline impact alongside the efficiency-ranked option so the trade-off is explicit rather than hidden.

**Edge Cases**: If a channel under consideration for defunding has a contractual minimum commitment, flag it as a hard constraint rather than including it as a candidate for cuts.

---

## Example 5: New Market Entry with No Historical Data (Renewable Energy Equipment)

**User Request**: "We're entering a new geographic market with no prior spend data. How should we allocate an initial $250K GTM budget?"

**Why the Skill Activates**: Budget allocation request; the no-baseline scenario is explicitly handled by this skill's error-handling guidance.

**Workflow**: Note missing historical data → use category/geography benchmark CAC and channel-mix ranges → apply channel strategy reasoning based on buyer profile (e.g., high deal size, concentrated buyer list favors ABM/events/partner) → propose allocation with wide confidence bands → recommend a data-collection checkpoint.

**Expected Output**: Budget Allocation Model, Channel Recommendations, CAC Analysis (benchmark-based).

**Final Response (condensed)**: Given a concentrated buyer base and high average deal size typical of this equipment category, propose 35% partner/channel, 30% field events/ABM, 20% paid/digital for awareness, 15% content — all CAC figures labeled as benchmark estimates (industry range $8K-$15K per customer) pending real data; recommend a 90-day checkpoint to replace estimates with actuals.

**Alternative Response**: If the user can supply even partial data from a comparable market, blend that data with benchmarks instead of relying purely on benchmarks.

**Edge Cases**: Explicitly state that recommendations carry low confidence until real data exists; do not present benchmark-based figures with false precision.

---

## Example 6: LTV:CAC-Driven Reallocation (Subscription Media Service)

**User Request**: "Compare LTV:CAC across our four acquisition channels and tell us where to move budget."

**Why the Skill Activates**: LTV:CAC analysis and reallocation recommendation is core scope.

**Workflow**: Calculate LTV and CAC per channel → compute ratio → assess marginal return for reallocation candidates → recommend shift.

**Expected Output**: ROI Forecast (LTV:CAC), Channel Recommendations, Spend Distribution.

**Final Response (condensed)**: Channel A: LTV:CAC 4.8:1 (strong); Channel B: 3.1:1 (healthy); Channel C: 1.6:1 (weak, largely due to high churn in that acquisition cohort); Channel D: 2.9:1. Recommend shifting 10-15% of budget from Channel C to Channel A, while investigating whether Channel C's churn issue is a targeting problem (fixable) or a structural fit problem (not fixable by budget alone).

**Alternative Response**: If churn data is incomplete for newer cohorts, present LTV as a range and flag it as preliminary until 12-month retention data matures.

**Edge Cases**: A channel with strong LTV:CAC but very small absolute volume may not be reallocation-worthy at scale; note capacity/scalability constraints alongside the ratio.

---

## Example 7: Zero-Based Budget for a New Product Line (Industrial Software)

**User Request**: "We're launching a new product line and need a zero-based GTM budget — nothing carried over from the core product's budget assumptions."

**Why the Skill Activates**: Zero-based budgeting request is explicitly within the budget planning framework scope.

**Workflow**: Apply zero-based methodology per references/budget_planning.md → require every channel to justify funding from data/benchmarks → build allocation from the ground up.

**Expected Output**: Budget Allocation Model, Channel Recommendations.

**Final Response (condensed)**: Each of six candidate channels scored on estimated CAC/ROI/strategic fit for the new line; two channels (organic content, targeted paid search) funded at 60% combined based on strongest estimated payback; ABM funded at 25% given concentrated target account list; remaining channels held at zero pending initial data from the first funded channels.

**Alternative Response**: If the new product line shares a buyer profile with an existing product, note that some benchmark data can be borrowed from the existing line rather than starting from pure industry benchmarks.

**Edge Cases**: If the new line has zero historical data of any kind, disclose that all figures are estimates and propose a short initial test period before committing the full budget.

---

## Example 8: Small Business Budget Allocation (Local Services Business)

**User Request**: "I run a small home services business with a $15,000/quarter marketing budget. How should I split it between Google Ads, social media, and referral incentives?"

**Why the Skill Activates**: Small-scale budget allocation across channels remains in scope regardless of absolute budget size, demonstrating reusability across business sizes.

**Workflow**: Simplify framework to top-down/bottom-up blend appropriate for limited data → apply channel strategy reasoning for a local, transaction-driven business → propose allocation.

**Expected Output**: Budget Allocation Model, Spend Distribution.

**Final Response (condensed)**: Google Ads $7,500 (50%, fastest payback for local intent-based search), referral incentive program $4,500 (30%, low CAC once established, leverages existing customer trust), social media $3,000 (20%, awareness/retention support). Recommend tracking CAC per channel monthly given the smaller budget's sensitivity to inefficiency.

**Alternative Response**: If the business has no tracking in place at all, recommend basic tracking setup (e.g., call tracking numbers, referral codes) as a prerequisite before the next allocation cycle.

**Edge Cases**: At this budget size, minimum effective spend thresholds matter (e.g., an ad platform may need a minimum daily budget to gather optimization data) — flag if a proposed split falls below a channel's practical minimum.

---

## Example 9: Forecasting Pipeline Coverage for a Revenue Target (Enterprise Cybersecurity)

**User Request**: "We need $12M in closed revenue next year. What pipeline and budget do we need to get there?"

**Why the Skill Activates**: This is a pipeline-coverage forecasting request translating a revenue target into required spend — core forecasting scope.

**Workflow**: Establish historical pipeline coverage ratio and win rate → calculate required pipeline → translate to required spend using historical pipeline-per-dollar efficiency by channel → sanity-check against budget constraints.

**Expected Output**: ROI Forecast, Budget Allocation Model.

**Final Response (condensed)**: Historical coverage ratio 4.2x implies $50.4M pipeline required. Blended historical efficiency of $22 pipeline per $1 spend implies approximately $2.29M required budget. If actual available budget is $1.8M, flag the $490K gap and present options: extend timeline, increase budget, or accept a lower revenue target consistent with available spend.

**Alternative Response**: If win rate is trending upward due to a sales process improvement, adjust the coverage ratio downward and disclose the adjustment explicitly rather than using a stale historical ratio.

**Edge Cases**: If the coverage ratio has been unstable across recent quarters, present a range for required pipeline/budget rather than a single figure.

---

## Example 10: Sensitivity Analysis Before a Large Spend Commitment (Direct-to-Consumer Retail)

**User Request**: "Before we commit to doubling our paid social budget, what are the biggest risks to this plan working out?"

**Why the Skill Activates**: This is a sensitivity/scenario-planning request tied directly to a spend decision.

**Workflow**: Identify key drivers (CAC, conversion rate, ad cost inflation, seasonal demand) → run sensitivity analysis varying each independently → rank by impact → recommend risk mitigation.

**Expected Output**: ROI Forecast, Budget Allocation Model (scenario-adjusted).

**Final Response (condensed)**: Sensitivity ranking: conversion rate (±15% input → ±17% output swing, highest impact), CAC/auction inflation (±15% → ±14% swing), seasonal demand (±15% → ±6% swing, lowest impact). Recommend piloting the increase at +50% first with a defined checkpoint at 6 weeks before committing to the full double, given conversion rate is both the highest-impact and least-controllable driver.

**Alternative Response**: If the user wants to proceed with the full doubling immediately regardless of risk, present the worst-case scenario explicitly (e.g., ROAS could fall to 1.8x from a current 3.2x) so the decision is made with full visibility rather than omitting the downside case.

**Edge Cases**: A budget doubling this large risks moving the channel further into auction saturation; explicitly flag this as a marginal-return risk, not just a scaling opportunity.

---

## Example 11: Multi-Channel Reallocation Across a Full Portfolio (Higher Education / EdTech)

**User Request**: "Here's our spend and results across seven channels for the last four quarters. Tell us how to reallocate the same total budget for maximum enrollment next year."

**Why the Skill Activates**: A full-portfolio, multi-channel reallocation exercise at a fixed total budget — the flagship required multi-channel-reallocation scenario.

**Workflow**: Calculate fully-loaded CAC and ROI trend for all seven channels → tier by payback speed → identify saturation/marginal-return signals → reallocate within the fixed total, respecting tier balance and concentration limits → validate the total still sums to the original budget.

**Expected Output**: Budget Allocation Model, Channel Recommendations, CAC Analysis, Spend Distribution.

**Final Response (condensed)**: Two channels (paid social, direct mail) show rising CAC and flat-to-declining marginal return; three channels (organic search, campus partner referral, targeted digital) show stable-to-improving CAC and headroom before saturation; two channels (events, display) are marginal. Reallocate 18% of total budget away from paid social and direct mail into organic search and partner referral, hold events and targeted digital flat, cut display by half. Total remains at the original figure.

**Alternative Response**: If leadership wants to preserve historical channel presence for brand-consistency reasons, present a constrained version that caps any single channel's cut at 25% of its prior spend rather than fully reallocating based on data alone.

**Edge Cases**: If two channels' fiscal-year data only partially overlap (e.g., a channel launched mid-year), annualize or clearly footnote the partial-year comparison rather than treating it as a full four-quarter dataset.
