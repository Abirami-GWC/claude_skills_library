---
name: landing-page-copywriter
description: Generate complete, persuasive landing page copy optimized for conversions — hero section, headline/subheadline, benefits, features, social proof, testimonials, FAQs, objection handling, CTAs, and closing sections. Use this skill whenever the user asks for landing page copy, a sales page, a homepage rewrite for conversion, a product page, a squeeze/opt-in page, or website copy meant to drive a specific conversion action (signup, purchase, demo request, download). Also use it to audit or improve an existing landing page's structure and conversion copy. Do not use this skill for paid ad copy (use ad-copy-generator), multi-email sequences (use email-sequence-writer), or pure brand voice/tone edits with no conversion-structure component (use brand-voice-writer).
---

# Landing Page Copywriter

## Purpose

Produce complete, conversion-structured landing page copy that takes a visitor from arrival to a single desired action, using a proven page architecture rather than an unstructured wall of marketing text.

## Business Value

- Converts more visitors into leads/customers by applying tested conversion-copywriting structure
- Reduces the guesswork of "what sections does a landing page need" for founders, marketers, and agencies
- Surfaces and pre-answers objections that would otherwise cause silent drop-off
- Produces copy ready to hand directly to a designer/developer, section by section

## Activation Conditions

Use this skill when the request involves:
- Full landing page, sales page, or product page copy
- A specific section of a landing page (hero, FAQ, testimonials block) requested in the context of the larger page
- Improving/auditing an existing landing page for conversion
- Squeeze pages / opt-in pages built around a single conversion action

### Trigger Examples
- "Write landing page copy for my new fitness app."
- "I need a sales page for my online course."
- "Can you write the hero section and FAQ for our product page?"
- "Review my landing page and tell me why it's not converting."
- "Write copy for a webinar registration page."

### When NOT To Use
- Paid ad copy (headlines/hooks for Google, Meta, LinkedIn ads) → ad-copy-generator
- Multi-email sequences → email-sequence-writer
- Pure tone/voice rewrite with no conversion-structure work → brand-voice-writer
- Blog posts, articles, or non-conversion content pages → handle directly

## Scope

In scope: page-section copy (hero through final CTA), conversion structure/ordering, objection handling, FAQ generation, CTA copy, testimonial/social-proof framing.
Out of scope: visual design, layout/wireframing, actual HTML/CSS implementation, A/B test statistical analysis, SEO technical optimization (though headline/meta suggestions can be offered as a bonus).

## Inputs

Required:
- Product/offer being promoted
- Target audience/persona
- Primary conversion goal (signup, purchase, demo, download, etc.)

Helpful but optional:
- Existing brand voice/tone reference
- Known objections or FAQs from real customers
- Testimonials, proof points, or metrics
- Competitor positioning or differentiators
- Page type (long-form sales page vs. short SaaS landing page vs. lead-gen squeeze page)

## Outputs

- Complete section-by-section copy: hero, benefits/features, social proof, objection handling/FAQ, CTA(s), closing section
- Section-by-section rationale (why this section exists, what it's doing psychologically)
- Recommended page length/structure for the given offer type
- Optional: 2-3 headline variants for the hero section

## Workflow

1. **Determine page type and length** using `references/landing_page_frameworks.md` (short-form SaaS page vs. long-form sales page vs. lead-gen squeeze page).
2. **Gather inputs**: product, audience, goal, proof points, objections. Use `templates/templates.md` (Landing Page Brief) as the checklist.
3. **Draft the section map** — list every section the page will have, in order, before writing full copy.
4. **Write the hero first**: headline + subheadline + primary CTA, using `references/headline_frameworks.md`.
5. **Write supporting sections** in order (benefits/features → social proof → objection handling/FAQ → final CTA), using `references/conversion_psychology.md` and `references/cta_best_practices.md`.
6. **Objection-proof the page**: identify the top 3-5 likely objections and ensure each is addressed somewhere on the page (FAQ, testimonial, or dedicated section).
7. **Check against `checklists/checklists.md`** — one primary CTA repeated consistently, no unaddressed objections, logical scroll progression, proof placed near the claims it supports.
8. **Deliver** the full page copy section by section with brief rationale notes.

## Reasoning Guidelines

- The hero must pass the "5-second test": a visitor should understand what's offered and for whom within 5 seconds.
- Every claim of benefit should be followed, somewhere on the page, by proof (testimonial, stat, example) — unsupported claims read as marketing fluff.
- Objections should be addressed before they can cause drop-off, not only in a buried FAQ at the very bottom.
- Use one primary CTA phrase repeated consistently throughout the page (in the hero, mid-page, and closing) rather than a different CTA wording each time — consistency reduces cognitive load.
- Match page length to purchase consideration: low-commitment/low-price offers need short pages; high-commitment/high-price offers need longer, proof-heavy pages.

## Best Practices

- Lead with the visitor's outcome/benefit, not the product's features, in the hero headline.
- Use specific numbers and concrete language over vague superlatives ("saves 6 hours a week" beats "saves you time").
- Place testimonials near the specific claim they support, not only in one generic block.
- Keep paragraphs short and scannable; use subheads, bullets, and bolding for skimmability.
- End with a closing section that reiterates the core value proposition and CTA, not just a bare "Sign up" button.

## Validation Rules

Before delivering, confirm:
- [ ] Hero passes the 5-second clarity test
- [ ] Primary CTA phrase is consistent across all placements
- [ ] Every major benefit claim has supporting proof somewhere on the page
- [ ] Top objections are explicitly addressed
- [ ] Page length matches the offer's consideration level

## Error Handling

- If no proof points/testimonials are provided, note the gap and either omit the social-proof section or clearly mark placeholder testimonials as `[insert real testimonial]`.
- If conversion goal is unclear, ask once, since CTA language depends entirely on the specific action being requested.
- If page type/length isn't specified, default to a standard mid-length landing page and state the assumption.

## Limitations

- Does not produce visual design, layout, or working HTML/CSS — copy only, organized by section.
- Cannot verify real conversion data; recommendations follow established conversion-copywriting principles, not the user's live analytics unless supplied.
- Does not perform technical SEO optimization (though it can suggest a keyword-aware headline as a bonus).

## Success Criteria

A successful output is complete, section-by-section landing page copy with a clear single conversion goal, a hero that passes the 5-second test, claims backed by proof, objections addressed, and a consistent CTA carried through the entire page.
