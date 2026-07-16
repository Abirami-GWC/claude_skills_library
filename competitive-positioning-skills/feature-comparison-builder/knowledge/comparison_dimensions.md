# Standard Comparison Dimension Categories

Offer these as the default set if the user hasn't specified dimensions. Only
include categories relevant to the request — don't pad in unrelated rows.

## Features
Core product capabilities relevant to the buyer's use case (workflow-specific,
not generic "does stuff" claims).

## Pricing
Pricing model, unit of measure, included vs. add-on tiers, contract flexibility.
See `references/pricing_comparison_guidelines.md`.

## Integrations
Ecosystem breadth — native vs. via-partner/via-Zapier integrations, API
availability and rate limits, webhook support.

## Security & Compliance
Certifications (SOC 2, ISO 27001, HIPAA, FedRAMP, PCI-DSS, etc.), data
residency options, encryption model (at rest / in transit), audit logging,
SSO/SAML/SCIM support.

## Scalability
Documented limits (users, throughput, storage, concurrent operations),
multi-region/multi-tenant support, published uptime SLA, horizontal vs.
vertical scaling model.

## AI Capabilities
Specific AI/ML features (not a generic "has AI" checkbox) — e.g., model
type/provider if disclosed, generally-available vs. beta vs. roadmap status,
data usage/training policy for customer data, explainability/audit features.
See `references/ai_capability_comparison_notes.md` — this category has the
highest rate of marketing-vs-reality gaps, so sourcing discipline matters most here.

## Deployment
Cloud / on-prem / hybrid, time-to-deploy, implementation model (self-serve vs.
requires professional services).

## Support
SLA tiers, support hours, channels (chat/email/phone), named vs. pooled
support, documented first-response times.

## Licensing
Per-seat / per-usage / platform-fee model, minimum contract terms, overage
handling, open-source vs. proprietary components if relevant.

## Adding a custom dimension

If the user needs a dimension outside this set (common in specialized RFPs),
add it under the closest-fitting category, or create a new category heading if
it doesn't fit any existing one — keep the neutral, outcome-based naming
convention from `instructions/data_validation.md`.
