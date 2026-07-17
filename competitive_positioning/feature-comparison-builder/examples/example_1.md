# Worked Example — Feature Comparison Builder (3-Vendor, Multi-Category)

## User input

> "Build a comparison of us vs. Flowly and Chainwork, covering real-time event
> triggers, SOC 2 Type II, and our automated workflow summarization AI feature.
> We support all three fully (SOC 2 is certified, summarization is GA). Flowly's
> docs say they poll every 15 minutes instead of real-time, their trust page
> doesn't list SOC 2, and their changelog shows workflow summarization is still
> in beta. I don't know anything about Chainwork on any of these — mark
> unknown. Deliver both an interactive HTML version and a landscape Word doc
> for the deck."

## Claude's internal process (not shown to user)

1. Scope: 3 vendors, 3 dimensions across 3 categories (Features, Security &
   Compliance, AI Capabilities), two output formats.
2. Populate matrix:
   - Real-time triggers: us=Full, Flowly=Partial ("polling every 15 min",
     sourced to public docs), Chainwork=Unknown
   - SOC 2 Type II: us=Full, Flowly=Unsupported ("not listed on trust page",
     sourced to their trust page URL — high-risk claim type, source_url present
     per validation rule), Chainwork=Unknown
   - Workflow summarization (AI): us=Full/GA, Flowly=Partial/beta (sourced to
     changelog — correctly not marked Full since it's beta, per
     `ai_capability_comparison_notes.md`), Chainwork=Unknown
3. Run `scripts/validate_matrix.py` — passes (all non-Unknown claims sourced,
   Unsupported claim has a source_url).
4. Render both formats: `scripts/build_comparison_html.py` for the interactive
   version, `scripts/build_comparison_docx.py` for the deck (auto-landscape
   since 3 vendors).
5. Verify docx visually via PDF conversion — landscape, readable, category-grouped tables confirmed.

## Output delivered to user

- An interactive HTML widget (filterable by category) showing the 3×3 matrix
  with hover-detail tooltips
- A landscape Word document with three tables (one per category), a legend,
  an as-of date, and a sources appendix listing the Flowly public-docs,
  trust-page, and changelog URLs
- Open items flagged: all three Chainwork cells need follow-up before this is
  used in a signed RFP context

## Why this is a good output

- Flowly's beta-status AI feature was correctly marked `Partial`, not `Full` —
  avoided the most common AI-comparison mistake (treating beta as GA).
- The `Unsupported` claim for Flowly's SOC 2 status carries an actual
  source_url, satisfying the highest-risk-claim validation rule.
- Chainwork was left fully `Unknown` across the board rather than guessed at,
  with an explicit open-items flag.
- Landscape orientation was applied automatically for the 3-vendor table and
  visually verified before delivery.
