# Social Media Marketing Skill Library

A modular library of four Claude Skills covering the social media content workflow, from planning to publishing: what to post and when, what the post idea should be, how to structure the full post, and how to close it with a CTA that actually drives engagement. Each skill is self-contained (its own `SKILL.md` + supporting `knowledge/`, `mappings/`, `templates/`, `examples/`) and can be installed individually or as a set.

## Library Structure

```
social_media_marketing/
├── README.md                      (this file — library index & routing)
├── social-content-calendar/
│   ├── SKILL.md
│   ├── knowledge/
│   ├── mappings/
│   ├── templates/
│   └── examples/
├── social-post-ideator/
│   └── (same structure)
├── post-structurer/
│   └── (same structure)
└── engagement-cta-writer/
    └── (same structure)
```

## The Four Skills

| Skill | Core Job | Typical Trigger Phrases |
|---|---|---|
| **Social Content Calendar** | Builds the overall posting plan — which pillar, which platform, which day — across a week or month. | "content calendar," "posting schedule," "content plan for the month" |
| **Social Post Ideator** | Turns one topic, product update, or raw idea into a batch of platform-native post ideas with ready-to-use hooks. | "post ideas," "give me hooks," "what should I post about X" |
| **Post Structurer** | Takes one idea or rough draft and writes the complete, ready-to-publish post — hook, body, and CTA. | "turn this into a LinkedIn post," "structure this draft," "write out this idea as a post" |
| **Engagement CTA Writer** | Writes multiple CTA options for a post, each tuned to a specific engagement goal (comments, shares, saves, follows, clicks). | "CTA ideas for this post," "how should I end this post" |

## How Routing Works (Dynamic Activation)

These four skills sit at different stages of the same pipeline and are usually mutually exclusive in the moment, but naturally chain together across a real workflow.

**Decision order when a request could match more than one skill:**

1. **Is the ask about planning what to post across days/weeks, not writing any single post yet?** → Social Content Calendar.
2. **Is the ask for a batch of post ideas/hooks from a topic, with no single post being finalized?** → Social Post Ideator.
3. **Is the ask for one complete, ready-to-publish post (hook + body + CTA) from an idea or rough draft?** → Post Structurer.
4. **Is the ask specifically about the closing line/CTA of a post that's otherwise done or already has a body?** → Engagement CTA Writer.

**Non-overlap rules already encoded in each skill's own description:**
- Social Content Calendar owns the planning grid, not individual post content — it flags where the other three skills should be used to fill a slot.
- Social Post Ideator owns idea generation (many concepts, not fully written), not full single-post drafting.
- Post Structurer owns writing one full post end-to-end, including a CTA — it can hand off to Engagement CTA Writer if the user wants CTA variants specifically rather than the one CTA drafted inline.
- Engagement CTA Writer owns only the closing ask, assuming the post content already exists or is supplied as context.

## Composability Examples

- **Monthly planning cycle**: Social Content Calendar (grid of what/when) → Social Post Ideator (concrete ideas for each slot) → Post Structurer (full draft for a chosen idea) → Engagement CTA Writer (CTA variants if the drafted CTA needs A/B options).
- **One-off post from an announcement**: Social Post Ideator (a few angle options) → Post Structurer (write the chosen angle out in full).
- **Fixing a weak existing post**: Engagement CTA Writer alone, if only the closing line needs work.

## Installing

Each skill folder can be zipped individually into a `.skill` file and installed independently via Claude's **Save Skill** flow, or the whole `social_media_marketing/` folder can be kept together for editing and version control, packaging skills out of it as needed.

## Status

| Skill | Status |
|---|---|
| Social Content Calendar | Complete |
| Social Post Ideator | Complete |
| Post Structurer | Complete |
| Engagement CTA Writer | Complete |
