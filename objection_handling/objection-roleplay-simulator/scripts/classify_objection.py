#!/usr/bin/env python3
"""
classify_objection.py

Lightweight, dependency-free rule-based router for sales objections.
Not a model call -- this is a fast first pass. See references/schemas.md "Classifier contract"
for the full spec this implements, and keep the lists below in sync with the relevant
handlers/*.md file whenever competitors or pricing language change.

Usage:
    python classify_objection.py --text "We're also looking at Fortinet, and honestly
    their price is lower too."

    echo "We already have a vendor" | python classify_objection.py

Output: single JSON object on stdout, matching the schema in REFERENCE.md.
"""

import argparse
import json
import re
import sys

# Keep this in sync with handlers/competitor-objection-handler.md "Competitor battlecards" table.
KNOWN_COMPETITORS = [
    "fortinet",
    "palo alto",
    "palo alto networks",
    "sonicwall",
]

# Keep this in sync with handlers/pricing-objection-handler.md "Pricing scenarios" table.
PRICING_KEYWORDS = [
    "price",
    "pricing",
    "cost",
    "costs",
    "budget",
    "expensive",
    "discount",
    "afford",
    "cheaper",
    "cheap",
]

# Keep this in sync with handlers/top-objections-playbook.md "The 10 objections" table (col 2).
PLAYBOOK_KEYWORDS = {
    "existing_vendor": ["already have", "current vendor", "current provider"],
    "timing": ["not a good time", "bad timing", "later this year", "next quarter"],
    "needs_thought": ["think about it", "not sure yet", "need more time"],
    "internal_stakeholder": ["run this by", "check with", "need approval from"],
    "complexity": ["seems complex", "too complicated", "hard to implement"],
    "past_failure": ["tried something like this", "didn't work before", "bad experience"],
    "satisfied": ["happy with what we have", "no complaints", "working fine"],
    "info_request": ["send me some information", "send me info", "email me details"],
    "too_small": ["small team", "don't need enterprise", "too small for this"],
    "procurement": ["procurement", "compliance review", "legal review"],
}


def classify(text: str) -> dict:
    lowered = text.lower()

    # 1. Competitor check takes priority, per REFERENCE.md classifier contract.
    for competitor in KNOWN_COMPETITORS:
        if re.search(r"\b" + re.escape(competitor) + r"\b", lowered):
            return {
                "category": "competitor",
                "matched_competitor": competitor,
                "confidence": "high",
            }

    # 2. Pricing keywords.
    if any(kw in lowered for kw in PRICING_KEYWORDS):
        return {
            "category": "pricing",
            "matched_competitor": None,
            "confidence": "high",
        }

    # 3. Top-objection keyword sets.
    for subcategory, phrases in PLAYBOOK_KEYWORDS.items():
        if any(phrase in lowered for phrase in phrases):
            return {
                "category": "playbook",
                "matched_competitor": None,
                "confidence": "medium",
                "subcategory": subcategory,
            }

    # 4. Default bucket -- low confidence, downstream should re-classify by reasoning.
    return {
        "category": "playbook",
        "matched_competitor": None,
        "confidence": "low",
    }


def main():
    parser = argparse.ArgumentParser(description="Classify a raw sales objection.")
    parser.add_argument("--text", help="Objection text. If omitted, reads from stdin.")
    args = parser.parse_args()

    text = args.text if args.text is not None else sys.stdin.read()
    text = text.strip()

    if not text:
        print(json.dumps({"error": "no objection text provided"}))
        sys.exit(1)

    result = classify(text)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
