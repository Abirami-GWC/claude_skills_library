# Testing Guide

**Purpose of this file**: Defines positive, negative, boundary, and edge test cases for validating that the Budget Allocator skill activates correctly, produces the required outputs, and respects its scope boundaries.

---

## Positive Test Cases

These requests should activate the skill and produce a correct, complete response.

1. "Allocate our $1.2M annual marketing budget across paid, organic, events, and partner channels based on last year's data."
   - Expected: Budget Allocation Model + Spend Distribution, reconciled to $1.2M, using bottom-up or blended methodology.

2. "Calculate fully-loaded CAC by channel from this spend and customer data." (with data supplied)
   - Expected: CAC Analysis using fully-loaded cost components, attribution method stated.

3. "Our LTV:CAC on Channel X dropped to 1.4:1 — what should we do?"
   - Expected: CAC/ROI-based diagnosis and reallocation recommendation, with a caveat if churn data is incomplete.

4. "Build best/base/worst case scenarios for next year's demand gen budget given a possible 10% market slowdown."
   - Expected: Scenario Planning output with 3-5 key drivers varied and a headline-metric range.

5. "We need to cut 15% from the marketing budget — model the options."
   - Expected: Uniform cut, efficiency-ranked cut, and (if strategic priorities are stated) strategic-protection cut, compared side by side.

6. "Forecast pipeline and revenue if we hold our current channel spend flat next quarter."
   - Expected: Forecast using an appropriate model (linear/cohort/pipeline-coverage) with stated confidence level.

## Negative Test Cases

These requests should NOT be handled by this skill; the correct behavior is to decline or redirect, not attempt the task.

1. "Write our GTM positioning statement and key messaging pillars for the new product launch."
   - Expected: Skill does not activate for the positioning content; response notes this belongs to a GTM Strategy Builder skill.

2. "Build our Q3 roadmap with milestones and owners."
   - Expected: Skill does not activate for roadmap/timeline content; notes this belongs to a Quarterly Roadmap Planner skill.

3. "Write the narrative and slide copy for our board deck summarizing GTM performance."
   - Expected: Skill does not activate for narrative/slide content; notes this belongs to a Board Deck Narrative skill. (If the board deck needs the underlying ROI/CAC figures, this skill can supply those, but not the narrative prose.)
   - Note: if the same request also asks "and tell us if our channel spend is efficient," the skill should handle the efficiency analysis portion and redirect only the narrative portion.

4. "Calculate our payroll tax withholding for the marketing team."
   - Expected: Skill does not activate; this is general accounting/payroll, out of scope entirely.

5. "Design a creative brief and ad copy for our next paid social campaign."
   - Expected: Skill does not activate; creative asset generation is out of scope.

## Boundary Cases

1. **Zero budget**: "We have $0 additional budget this quarter but still need to hit our pipeline target." Expected: Skill states the target is not achievable with $0 incremental spend absent a channel-mix shift within the existing baseline, and models what reallocating existing (non-zero) spend could achieve instead of fabricating a plan from nothing.

2. **Extreme single-channel concentration**: "Put 95% of our budget into paid search since it has the best CAC." Expected: Skill flags concentration risk explicitly, models the risk (platform/auction dependency), and asks whether this concentration is an intentional strategic choice before finalizing.

3. **Single-period-only data**: "Here's one month of data — build our annual forecast." Expected: Skill proceeds but explicitly labels the forecast as low-confidence given only one historical period, and recommends re-forecasting once more periods are available.

4. **Extremely large budget with no channel detail**: "We have $50M — just tell us the split." Expected: Skill still applies the same framework (top-down ceiling, tier balance, concentration checks) rather than assuming large budgets bypass normal rigor; asks for at least directional channel performance data if none is supplied.

## Edge Cases

1. **No historical data at all (new business/new market)**: Skill uses labeled industry benchmarks and recommends a test-and-learn checkpoint rather than fabricating precise figures. See `references/budget_planning.md` and Example 5 in `examples/examples.md`.

2. **Conflicting user-supplied figures**: Two different CAC values given for the same channel in the same conversation. Skill surfaces the conflict and asks which is authoritative rather than silently picking one.

3. **Mixed in-scope/out-of-scope request**: "Build our budget allocation and also write the board narrative explaining it." Skill completes the budget allocation fully and explicitly notes the narrative portion is out of scope for this skill.

4. **Insufficient budget for stated target**: Skill states the shortfall explicitly and offers trade-off options rather than inflating projected ROI to make the numbers appear to close the gap.

## Evaluation Criteria

A response is considered correct if it satisfies all of the following:

- **Activation correctness**: The skill activates only for budget/spend/CAC/ROI/forecasting/scenario requests, and declines/redirects for positioning, roadmap, or narrative requests (per `SKILL.md` "When NOT To Use").
- **Output completeness**: All requested outputs among Budget Allocation Model, Channel Recommendations, ROI Forecast, CAC Analysis, and Spend Distribution are present and populated (no unfilled template placeholders in a delivered response).
- **Arithmetic integrity**: Allocations sum to the stated total budget; percentages sum to 100%.
- **Assumption transparency**: All assumptions, benchmarks used in place of real data, and data gaps are explicitly disclosed.
- **Rigor**: Marginal-return reasoning is applied where relevant; forecasts carry an explicit confidence qualifier or range when data is limited; scenario sets vary no more than 3-5 drivers.
- **Scope discipline**: No positioning, roadmap, or board-narrative content appears in the output; mixed requests are correctly split between in-scope and redirected portions.
- **Usability**: Output is directly usable by a marketing/finance stakeholder without further translation, using the appropriate `templates/` structure.
