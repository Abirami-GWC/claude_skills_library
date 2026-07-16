# Market Segmentation

**Purpose of this document:** Give Claude a rigorous, standard method for segmenting a market before defining ICP, positioning, and channel strategy, independent of industry.

## Introduction

Market segmentation is the process of dividing a total addressable market into meaningfully distinct groups so that targeting, messaging, and channel decisions can be tailored rather than applied uniformly to a heterogeneous market. Segmentation is upstream of ICP definition (see `icp_framework.md`): segmentation maps the whole market's structure, while ICP selects which resulting segment(s) to prioritize.

## Detailed Explanation

### Segmentation Models
Several complementary segmentation models are used, often in combination:
- **Firmographic segmentation:** company size, industry/vertical, geography, growth stage, ownership type. Easiest to operationalize (data is usually available) but often insufficiently predictive on its own.
- **Behavioral segmentation:** how the segment currently solves the problem, purchase behavior, usage intensity, buying process maturity. More predictive of propensity and channel fit than firmographics alone.
- **Needs-based segmentation:** groups defined by the specific job/problem/outcome they need solved, regardless of firmographic similarity (a small and a large company can share the same underlying need). Often the most strategically useful but the hardest to operationalize without direct research.
- **Technographic segmentation:** existing technology stack and integration environment — increasingly important wherever the product must interoperate with other systems.
- **Value-based segmentation:** grouping by the economic value the segment could realistically realize from adoption (useful for prioritizing which segments justify the highest-touch, highest-cost GTM investment).

A mature segmentation typically layers firmographic/technographic (to operationalize targeting) on top of needs-based/behavioral (to ensure the segments are strategically meaningful), rather than relying on a single model alone.

### TAM / SAM / SOM
Sizing discipline for prioritizing segments:
- **TAM (Total Addressable Market):** total demand for the category, if 100% share were achievable.
- **SAM (Serviceable Addressable Market):** the portion of TAM reachable given real constraints (geography served, product capability, regulatory scope, channel reach).
- **SOM (Serviceable Obtainable Market):** the realistic share capturable within the planning horizon given competitive intensity, resources, and go-to-market capacity.
Segmentation and TAM/SAM/SOM sizing should be done together: each candidate segment should have an associated sizing estimate to inform prioritization, even if the estimate is a labeled rough approximation rather than precise research.

### Segment Evaluation and Prioritization Criteria
Once candidate segments are identified, prioritize using consistent criteria:
- **Size and growth rate** of the segment.
- **Reachability** — can this segment be efficiently reached with available channels/motion?
- **Willingness/ability to pay** for the value delivered.
- **Competitive intensity** within the segment (crowded vs. underserved).
- **Strategic fit** with current product capability and roadmap direction.
- **Time-to-value/proof potential** — can wins in this segment be achieved and referenced quickly to build momentum?

Segments should be scored across these criteria (even qualitatively, e.g., High/Medium/Low) to produce a ranked shortlist rather than an unranked list of "possible markets."

### Beachhead Strategy
Especially for new products or new-market entry, segmentation should identify a **beachhead segment**: the single narrowest, most winnable segment where the product/company can achieve a dominant, referenceable position before expanding to adjacent segments. Trying to serve multiple segments simultaneously from day one typically dilutes messaging, product prioritization, and GTM resource allocation. A beachhead should be chosen using the prioritization criteria above, favoring reachability and time-to-proof over raw size.

## Professional Guidance

Always layer at least two segmentation models (typically firmographic/technographic for operational targeting plus needs-based/behavioral for strategic meaning) rather than relying on firmographics alone. Always produce a sizing estimate (even rough, clearly labeled) alongside each candidate segment, and always recommend a prioritized shortlist — not an unranked list of every theoretically possible segment. When advising on new-market entry, explicitly recommend a beachhead segment and the expansion sequence beyond it.

## Examples

- *B2B SaaS:* Segments might include (1) small teams self-serving via a free tier, (2) mid-market teams needing sales-assisted onboarding, (3) enterprise teams needing dedicated implementation and compliance review — each with distinct reachability, willingness-to-pay, and motion implications.
- *Consumer:* A direct-to-consumer wellness product might segment by needs-based clusters (e.g., "proactive optimizers" seeking marginal performance gains vs. "problem-solvers" addressing an acute symptom) layered on top of demographic/behavioral purchase-channel data.
- *Professional services:* A consulting offering might segment by client organizational maturity (segments needing foundational process design vs. segments needing advanced optimization) rather than purely by industry vertical, since the underlying need differs more by maturity than by sector in that case.

## Common Mistakes

- Segmenting only by firmographics (industry, size) and stopping there, missing the behavioral/needs-based distinctions that actually predict differentiated buying behavior.
- Producing an unranked list of every plausible segment instead of a prioritized shortlist with sizing and reachability criteria.
- Attempting to serve every identified segment simultaneously instead of selecting a beachhead and sequencing expansion.
- Confusing "segmentation" (mapping the market) with "ICP" (selecting the target) — segmentation should come first and inform ICP, not be skipped in favor of jumping straight to a single assumed target.
- Using TAM figures that are not tied to a credible SAM/SOM narrowing, producing inflated market-size claims that do not inform actual near-term prioritization.

## Best Practices

- Layer at least two segmentation models (one operational, one strategic/needs-based).
- Attach a sizing estimate (TAM/SAM/SOM, clearly labeled if approximate) to each candidate segment.
- Score and rank candidate segments against consistent criteria (size, reachability, willingness-to-pay, competitive intensity, strategic fit, time-to-proof).
- For new-market entry, explicitly recommend a beachhead segment and the logical expansion sequence.
- Revisit segmentation periodically as the market evolves or as the company's own capabilities/product scope expand.

## Summary

Market segmentation divides the total market into meaningful, distinctly targetable groups using firmographic, technographic, behavioral, needs-based, and value-based models — typically layered rather than used alone. Each candidate segment should carry a sizing estimate (TAM/SAM/SOM) and be scored against prioritization criteria (size, reachability, willingness-to-pay, competitive intensity, strategic fit, time-to-proof) to produce a ranked shortlist. For new or expanding markets, a deliberately chosen beachhead segment — rather than simultaneous multi-segment pursuit — improves the odds of a strong, referenceable initial position.
