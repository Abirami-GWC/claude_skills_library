# AI Capability Comparison Notes

AI/ML capability rows have the highest rate of marketing-vs-reality gaps of
any comparison dimension. Extra discipline required.

## Always verify release status explicitly

"Has AI-powered X" is not a single fact — distinguish:
- **GA (generally available)**: shipped, in the standard product, any customer
  can use it today
- **Beta / preview**: shipped but limited access, waitlist, or flagged
  "preview" by the vendor
- **Roadmap-announced**: publicly stated intent, not yet shipped

Never mark a roadmap announcement as `Full` support — mark it `Partial` with
`detail: "roadmap-announced, not yet GA"`, or `Unknown` if the actual status
can't be confirmed.

## Avoid generic "has AI" checkboxes

A dimension like "AI-powered" is not useful or checkable. Break it into
specific, named capabilities (e.g., "automated summarization," "anomaly
detection," "natural-language query") so each cell reflects something a buyer
can actually verify or test.

## Data usage and training policy

If relevant to the buyer (common in enterprise/regulated deals), include
whether customer data is used to train the vendor's models by default, and
whether that's opt-out or opt-in — this is a frequent differentiator and
frequent source of buyer concern. Only state a policy if sourced to the
vendor's actual terms/trust documentation, never assumed.

## Model provenance

If disclosed, note whether the AI capability is built on a third-party
foundation model or a proprietary one — only include if the vendor has made
this public; don't speculate.

## Common mistake this section prevents

Treating a competitor's blog post or press release about an AI feature as
equivalent to a shipped, generally-available capability. Always check the
actual product documentation or release notes, not just marketing
announcements, before marking a cell `Full`.
