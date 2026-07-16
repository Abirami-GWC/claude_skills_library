# Quality Checklist

**Purpose of this file**: A general quality-assurance checklist applied to any output produced by the Budget Allocator skill (Budget Allocation Model, Channel Recommendations, ROI Forecast, CAC Analysis, Spend Distribution).

---

## Accuracy & Consistency

- [ ] All monetary figures use a single, stated currency throughout the output
- [ ] All percentages sum correctly (e.g., channel allocation percentages sum to 100%)
- [ ] No contradictory figures for the same metric appear in different sections without explanation
- [ ] Calculation formulas used (CAC, ROI, ROAS, LTV:CAC, payback period) match the definitions in the corresponding `references/` file
- [ ] Value basis (revenue vs. margin vs. pipeline-weighted) is consistent within any single comparison table

## Rigor

- [ ] Marginal return, not just average return, is considered before recommending a spend increase
- [ ] Forecasts are presented as a range or with an explicit confidence qualifier, not a false-precision single number, when historical data is limited
- [ ] Scenario analysis (best/base/worst case) varies no more than 3-5 key drivers per set
- [ ] Attribution method is stated and applied consistently across all channels being compared
- [ ] Measurement time windows match each channel's natural sales cycle (short for fast-attribution paid channels, longer for events/ABM/enterprise field)

## Transparency

- [ ] Every assumption is stated explicitly, not left implicit
- [ ] Every benchmark or estimated figure (used in place of missing data) is clearly labeled as such
- [ ] Data gaps are disclosed along with what data would be needed to close them
- [ ] Confidence level is stated for any forecast or projection

## Scope Discipline

- [ ] Output contains no GTM positioning, messaging, or narrative strategy content
- [ ] Output contains no roadmap timeline, milestone sequencing, or launch-plan content
- [ ] Output contains no board narrative, executive storyline, or slide-copy content
- [ ] If the original request spanned out-of-scope territory, the response explicitly notes the handoff to the relevant separate skill

## Usability

- [ ] Output uses the appropriate template(s) from `templates/` rather than an ad-hoc format
- [ ] Tables and figures are complete (no placeholder brackets left unfilled in a delivered output)
- [ ] Recommendations are actionable and specific (e.g., "shift 15% from Channel X to Channel Y because CAC payback improved from 14 to 9 months") rather than vague (e.g., "consider optimizing channels")
- [ ] Output is immediately usable by a marketing or finance stakeholder without further translation or clarification
