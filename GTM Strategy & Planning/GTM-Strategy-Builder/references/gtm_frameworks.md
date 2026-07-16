# GTM Frameworks Overview

**Purpose of this document:** Provide Claude with a working knowledge of the major, industry-standard Go-To-Market (GTM) frameworks and motions so it can select and apply the right one when drafting or refreshing a GTM strategy. This is foundational reference knowledge — it is not a template and not company-specific.

## Introduction

"Go-To-Market strategy" is the plan for how a product or service reaches and converts its target buyers. A GTM strategy is more than a marketing plan: it synthesizes market definition (segmentation, ICP), value articulation (positioning, messaging), and route-to-market decisions (motion, channels, sales alignment) into one coherent operating plan for a defined period, typically a quarter or a launch window. This document orients Claude on the core frameworks used to structure that synthesis, independent of industry.

## Detailed Explanation

### The GTM Stack (Layered Model)
A useful mental model treats GTM strategy as layers, each depending on the one below it:
1. **Market definition** — segmentation and ICP (who exists in the market and who we target).
2. **Value definition** — positioning and value proposition (why we matter to that target).
3. **Communication** — messaging and personas (how we say it, to whom specifically).
4. **Route to market** — GTM motion and channels (how we reach and convert them).
5. **Alignment** — sales enablement and handoffs (how revenue teams execute consistently).

Each layer should be revisited whenever a layer below it changes; a shift in ICP, for instance, should trigger a review of messaging and channel choice.

### GTM Motions
A "motion" describes the dominant mechanism by which prospects move from awareness to purchase:
- **Sales-led (SLG):** Human sellers drive the buying process, typical for complex, high-consideration, or highly regulated purchases (enterprise software, capital equipment, professional services). Relies on outbound prospecting, discovery calls, and multi-stakeholder deal cycles.
- **Product-led (PLG):** The product itself drives acquisition, activation, and expansion, typically via free trials or freemium tiers with self-serve upgrade paths. Works best for products with fast time-to-value and low initial risk.
- **Marketing-led:** Demand generation and content/brand programs create pipeline that sales converts; common in categories with longer research cycles and multiple influencers.
- **Partner-led / Channel:** Resellers, systems integrators, marketplaces, or embedded/OEM partners carry some or all of the acquisition and delivery motion; common where trust, distribution, or integration complexity favors an intermediary.
- **Hybrid motions:** Most mature companies blend motions (e.g., PLG for smaller accounts, sales-assist or sales-led for larger ones) — this is often the most realistic recommendation for a maturing company rather than a single "pure" motion.

Motion choice should be driven by: deal complexity, average deal size, buyer research behavior, product time-to-value, and the org's current team composition and capacity — not by what is currently fashionable.

### Choosing a Motion — Decision Factors
- **Deal size and complexity:** Small, simple, single-stakeholder purchases suit PLG/self-serve; large, multi-stakeholder, high-risk purchases suit sales-led.
- **Buyer autonomy:** If buyers can evaluate and adopt without procurement/IT/legal involvement, self-serve motions are viable; if compliance, security review, or budget approval gates exist, sales-led or hybrid is required.
- **Time-to-value:** Fast, self-evident value supports product-led growth; value that depends on integration, customization, or organizational change favors sales-led, consultative motions.
- **Market maturity:** In an emerging or uneducated category, marketing-led/thought-leadership investment is often needed before a motion can scale efficiently.
- **Channel economics and trust:** In categories where buyers rely on trusted intermediaries (e.g., regulated industries, capital equipment, specialized industrial buyers), partner-led motion may outperform direct.

### The GTM Funnel / Bowtie Model
Traditional funnel models (Awareness → Interest → Consideration → Purchase) describe acquisition; the "bowtie" model extends this symmetrically post-purchase (Onboarding → Adoption → Expansion → Advocacy), reflecting that in most modern business models (subscription, recurring revenue, land-and-expand), GTM strategy must plan for retention and expansion, not just initial acquisition. A GTM plan restricted to the acquisition funnel is incomplete for any recurring-revenue business model.

### Channel Strategy Principles
Channels are the specific tactical vehicles used within a motion (e.g., outbound email, paid search, industry events, content/SEO, partner marketplaces, direct sales outreach, account-based marketing). Channel selection should:
- Match where the target ICP/persona actually spends attention and does research (see `buyer_persona_guide.md`).
- Be prioritized, not exhaustive — 2-4 well-resourced channels typically outperform ten under-resourced ones.
- Differ by segment/persona and by funnel stage; a channel that is excellent for top-of-funnel awareness may be poor for late-stage conversion.
- Be reassessed each quarter based on measured performance, not left static indefinitely.

## Professional Guidance

When advising on GTM strategy, always state the motion and channel recommendation as a function of the ICP and segmentation already defined — never recommend a motion in isolation. Recommend the smallest set of channels that plausibly reaches the priority segment for the current business goal (e.g., growth vs. retention vs. expansion), and be explicit about tradeoffs (e.g., "sales-led scales revenue predictably but is capacity-constrained; PLG scales cheaply but converts a lower percentage of qualified accounts").

## Examples

- A mid-market SaaS vendor selling a $30/user/month collaboration tool to teams of 5-50 people is well suited to a product-led motion with a sales-assist layer for accounts above a usage threshold.
- A vendor of industrial monitoring equipment sold to plant operations directors, where purchases require capital budget approval and multi-month evaluation, should run an outbound sales-led motion supported by trade-show and industry-publication marketing.
- A healthcare compliance software provider selling into hospital systems, where procurement, security, and legal review are mandatory, should run a sales-led motion with a partner channel for systems-integrator-delivered implementations.

## Common Mistakes

- Choosing a trendy motion (e.g., PLG) because competitors use it, without validating that the buyer behavior and deal complexity actually fit.
- Treating "GTM motion" and "marketing channel" as the same decision — motion is the overall mechanism; channels are tactics within it.
- Building a GTM plan that only addresses acquisition and ignores expansion/retention in a recurring-revenue business.
- Spreading budget and attention across too many channels instead of concentrating on the few that match the ICP's actual behavior.
- Failing to revisit motion/channel choice when the ICP or segment priority changes.

## Best Practices

- Always tie motion and channel choice explicitly back to ICP behavior and deal characteristics.
- Default to a hybrid motion recommendation for maturing companies rather than a single pure motion, and state the segment boundary between them.
- Recommend a focused channel mix (2-4 channels) with a clear primary and secondary channel, and name the metric that will indicate success for each.
- Revisit motion and channel fit at least once per quarter or whenever ICP/segmentation changes.

## Summary

GTM strategy is a layered system: market definition informs value definition, which informs communication, which informs route-to-market. Motion (sales-led, product-led, marketing-led, partner-led, or hybrid) should be chosen based on deal complexity, buyer autonomy, time-to-value, and market maturity — not fashion. Channels are the tactical vehicles within a motion and should be few, prioritized, and tied to where the ICP actually researches and buys. Because most modern business models are recurring-revenue, GTM plans must address the full bowtie (acquisition through expansion), not just the top-of-funnel.
