# Example Run

**User input:** "Plan next week for LinkedIn and Instagram. LinkedIn 3x/week, Instagram 2x/week. We have a product update launching Wednesday. Pillars: product education, customer stories, industry takes."

## Output produced

# Content Calendar: Week of [date]

| Date | Platform | Pillar | Topic (concrete) | Format | Notes |
|---|---|---|---|---|---|
| Mon | LinkedIn | Industry commentary | Take on [current industry trend] | Text-only | |
| Wed | LinkedIn | Product/education | New feature launch — what it solves and why | Text-only + link in comment | Fixed date: launch day |
| Wed | Instagram | Product/education | Same launch, visual carousel version | Carousel | Coordinated with LinkedIn |
| Fri | LinkedIn | Customer story | [Specific account] result post | Text-only | Use social-post-ideator for hook |
| Sat | Instagram | Customer story | Same story, visual/quote-card version | Single image | |

**Cadence check:** LinkedIn: 3/week (within sustainable range). Instagram: 2/week (within sustainable range).

**Fixed dates included:** Product launch (Wed) — given priority slot on both platforms, other pillars rotated around it.

**Next steps:** Run `social-post-ideator` for Monday and Friday's hooks, then `post-structurer` to turn each into a finished draft.
