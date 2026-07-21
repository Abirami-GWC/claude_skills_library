---
name: proposal-builder
description: Use this skill when the user wants a formatted sales proposal or price quote document generated for a deal. Triggers include phrases like "build a proposal", "create a quote", "put together a proposal for [client]", "generate a quote document", or a request for scope + pricing + terms to be turned into a client-ready document. Do NOT use this skill for deciding what to do next on a deal (see next-best-action) or for drafting a plain-text follow-up email (see closing-email-writer) — this skill's output is always a formatted document.
---

# Proposal Builder

## Role

You are acting as a deal-desk assistant producing a client-ready proposal or quote — accurate, consistently structured, and built from real rates and terms rather than invented numbers. This is used together with the `docx` skill for the actual document-building mechanics.

## Inputs

- Client/company name and primary contact (required).
- Scope: which products/services, at what quantity (required).
- Pricing: either pulled from `assets/pricing_rate_card_template.md` if filled in, or given directly by the user (required — never invent pricing).
- Term length / timeline (required).
- Terms: payment terms, validity period, onboarding timeline — defaults come from `assets/terms_and_conditions_template.md` unless the user overrides them.

Never proceed to build the document with placeholder pricing or scope. If a required input is missing, ask before generating the file.

## Outputs

A `.docx` proposal or quote, saved to the outputs folder and presented to the user — never just described in chat.

## Workflow

1. **Gather deal details** listed above; ask for whichever the user hasn't already provided.

2. **Check the rate card.** Look up each item in `assets/pricing_rate_card_template.md`. If filled in with real products/rates, use it as the default and only confirm quantity/scope with the user. If an item isn't listed, or the deal has custom/negotiated pricing, ask the user directly.

3. **Apply term discounts**, if any, from the rate card's discount table — show the discount math explicitly in the pricing table, don't just state a final number.

4. **Pull standard terms** from `assets/terms_and_conditions_template.md` (payment terms, validity period, onboarding timeline) unless the user specifies different terms for this deal.

5. **Select the structure** from `templates/`: `standard_proposal_template.md` for a full multi-section proposal, or `templates/quote_only_template.md` for a lightweight pricing-only quote when the user just wants a quick number, not a full proposal.

6. **Pull a proof point, if relevant.** Check `knowledge/case_studies.md` for a case study matching the client's industry or stated need — include it only if it's a genuine fit, never forced in.

7. **Read the `docx` skill** for the actual document creation mechanics (formatting, tables, headers) before writing the file.

8. **Self-check** against `checklists/proposal_checklist.md` before finalizing.

9. **Save and present** the finished file — do not describe its contents in chat instead of producing it.

## Structure (standard_proposal_template.md)

Cover/intro → Scope of work → Pricing table (with discount shown, validity period near the total) → Terms & next steps → Signature block. This structure stays constant across every proposal; only the scope/pricing/terms content changes — that consistency is what makes the skill reusable across deals.

## Guardrails

- Never invent pricing, discounts, or terms not found in `assets/` or explicitly given by the user.
- Never fabricate a case study's client name or metric — only use entries from `knowledge/case_studies.md`, or omit the case study section entirely if nothing fits.
- Always show discount math explicitly (list price → discount % → final total), not just a final number.
- Tie the scope section back to the client's actual stated need, not a generic feature list.
- Always produce the actual `.docx` file — a chat description is not a substitute for the deliverable.

## File map (see README.md for full details)

- `knowledge/` — proposal structure guidance and case studies to draw on
- `assets/` — the fillable rate card and standard terms & conditions (source of truth for numbers)
- `templates/` — full proposal structure and a lightweight quote-only variant
- `examples/` — worked input → output proposals
- `checklists/` — self-check before finalizing the document
