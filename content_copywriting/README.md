# Content & Copywriting Skill Library

A modular library of four reusable Claude Skills covering the core content and copywriting workflows: brand voice, advertising, email, and web conversion copy. Each skill is self-contained (its own `SKILL.md` + supporting `references/`, `templates/`, `prompts/`, `examples/`, `faqs/`, `checklists/`, `testing/`) and can be installed individually or as a set.

## Library Structure

```
content_copywriting/
├── README.md                      (this file — library index & routing)
├── brand-voice-writer/
│   ├── SKILL.md
│   ├── references/
│   ├── templates/
│   ├── prompts/
│   ├── examples/
│   ├── faqs/
│   ├── checklists/
│   └── testing/
├── ad-copy-generator/
│   └── (same structure)
├── email-sequence-writer/
│   └── (same structure)
└── landing-page-copywriter/
    └── (same structure)
```

## The Four Skills

| Skill | Core Job | Typical Trigger Phrases |
|---|---|---|
| **Brand Voice Writer** | Makes any piece of copy match a defined brand tone, personality, and messaging framework. The "consistency layer" underneath the other three. | "rewrite this in our brand voice," "does this sound on-brand," "create a style guide" |
| **Ad Copy Generator** | Produces channel-specific paid/organic advertising copy — headlines, hooks, CTAs — optimized per platform. | "write Google/Meta/LinkedIn ad copy," "give me headline variations," "A/B test angles" |
| **Email Sequence Writer** | Builds complete, strategically-sequenced multi-email flows (welcome, nurture, onboarding, win-back, cart-abandon, launch). | "write a welcome sequence," "onboarding emails," "win-back campaign," "email drip" |
| **Landing Page Copywriter** | Produces full conversion-structured page copy (hero → benefits → proof → objections → CTA) for a single conversion goal. | "landing page copy," "sales page," "product page," "hero section + FAQ" |

## How Routing Works (Dynamic Activation)

These four skills are designed to be mutually exclusive in their core job but composable in a real workflow. A single request can call more than one in sequence.

**Decision order when a request could match more than one skill:**

1. **Is the ask about matching a defined tone/voice, with no persuasion-structure or channel-format component?** → Brand Voice Writer.
2. **Is the ask for copy on a specific paid/organic ad channel (Google, Meta, LinkedIn, display)?** → Ad Copy Generator.
3. **Is the ask for two or more emails forming a strategic arc over time?** → Email Sequence Writer.
4. **Is the ask for a page built around one conversion action (signup, purchase, demo, download)?** → Landing Page Copywriter.
5. **Does the request need more than one of the above** (e.g., "write a landing page, then an ad campaign driving traffic to it, all in our brand voice")? → Chain them: build the base copy with the channel-specific skill first (Ad Copy Generator / Email Sequence Writer / Landing Page Copywriter), then pass the result through Brand Voice Writer as a voice-consistency pass.

**Non-overlap rules already encoded in each skill's "When NOT To Use" section:**
- Brand Voice Writer does not own persuasion structure or channel format — it only owns tone/voice/terminology.
- Ad Copy Generator does not own multi-step sequencing (that's Email Sequence Writer) or full-page structure (that's Landing Page Copywriter).
- Email Sequence Writer does not own single one-off emails or non-email channels.
- Landing Page Copywriter does not own ad copy driving traffic to the page, or the emails that might follow a signup on that page.

## Composability Examples

- **New product launch**: Landing Page Copywriter (page) → Email Sequence Writer (launch sequence) → Ad Copy Generator (traffic ads) → Brand Voice Writer (final consistency pass across all three).
- **Brand refresh**: Brand Voice Writer (new voice guide) applied to existing landing page, ad copy, and email sequences without changing their structure.
- **Cart abandonment recovery**: Email Sequence Writer (3-email flow) referencing the same value props already established on the Landing Page Copywriter output for that product.

## Maintainability Notes

- Each skill keeps its own `references/glossary.md` scoped to its domain terms; there is intentionally no single shared glossary file, to keep each skill fully self-contained and independently installable.
- CTA guidance is duplicated in a channel-appropriate form in each skill (`cta_best_practices.md`) rather than centralized, since CTA rules differ meaningfully between email, ads, and landing pages — this is intentional, not accidental duplication.
- If updating shared principles (e.g., a new brand voice standard), update `brand-voice-writer/references/` and note in the other three skills' `SKILL.md` that they should defer to it when a voice guide is supplied.

## Installing

Each skill folder can be zipped individually into a `.skill` file and installed independently via Claude's **Save Skill** flow, or the whole `content_copywriting/` folder can be kept together for editing and version control, packaging skills out of it as needed.

## Status

| Skill | Status |
|---|---|
| Brand Voice Writer | Complete |
| Ad Copy Generator | Complete |
| Email Sequence Writer | Complete |
| Landing Page Copywriter | Complete |
