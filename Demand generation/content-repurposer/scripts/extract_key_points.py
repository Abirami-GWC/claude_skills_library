#!/usr/bin/env python3
"""
extract_key_points.py

Scans a long-form source text (markdown or plain text) and surfaces candidate
material for repurposing: section headers, sentences containing numbers/stats
(likely candidates for pull-quotes or infographic data points), and the
longest/most declarative sentences per paragraph (candidate hook lines).

This is a heuristic assist, not a final selection — it narrows a long
document down to a shortlist for a human (or Claude, per
instructions/workflow.md Step 1) to review and choose from. It does not
decide what to repurpose; it just speeds up finding candidates.

Usage:
    python extract_key_points.py <path-to-source.md-or-.txt>

Outputs a plain-text report to stdout: section headers, sentences containing
numerals (candidate stats), and the longest sentence per paragraph (candidate
hook/pull-quote lines).
"""

import re
import sys


def strip_headers(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not re.match(r"^#{1,6}\s+", line))


def split_into_paragraphs(text: str) -> list[str]:
    text = strip_headers(text)
    raw_paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    # collapse internal line wraps so sentences aren't split by the source's line width
    return [re.sub(r"\s*\n\s*", " ", p) for p in raw_paragraphs]


def split_into_sentences(paragraph: str) -> list[str]:
    # Simple sentence splitter; good enough for a heuristic assist, not a
    # linguistic-grade tokenizer.
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", paragraph)
    return [s.strip() for s in sentences if s.strip()]


def extract_headers(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if re.match(r"^#{1,6}\s+", line)]


def extract_numeric_sentences(paragraphs: list[str]) -> list[str]:
    numeric_pattern = re.compile(r"\d")
    results = []
    for p in paragraphs:
        for s in split_into_sentences(p):
            if numeric_pattern.search(s) and len(s.split()) <= 40:
                results.append(s)
    return results


def extract_longest_sentence_per_paragraph(paragraphs: list[str]) -> list[str]:
    results = []
    for p in paragraphs:
        sentences = split_into_sentences(p)
        # skip header-only or very short paragraphs
        sentences = [s for s in sentences if len(s.split()) >= 6]
        if not sentences:
            continue
        longest = max(sentences, key=lambda s: len(s.split()))
        results.append(longest)
    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_key_points.py <path-to-source.md-or-.txt>")
        sys.exit(2)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    paragraphs = split_into_paragraphs(text)
    headers = extract_headers(text)
    numeric_sentences = extract_numeric_sentences(paragraphs)
    hook_candidates = extract_longest_sentence_per_paragraph(paragraphs)

    print(f"=== Section headers ({len(headers)}) ===")
    for h in headers:
        print(f"  {h}")

    print(f"\n=== Candidate stat/quote sentences containing numbers ({len(numeric_sentences)}) ===")
    for s in numeric_sentences[:25]:
        print(f"  - {s}")
    if len(numeric_sentences) > 25:
        print(f"  ... and {len(numeric_sentences) - 25} more")

    print(f"\n=== Candidate hook lines (longest sentence per paragraph, first 25) ===")
    for s in hook_candidates[:25]:
        print(f"  - {s}")
    if len(hook_candidates) > 25:
        print(f"  ... and {len(hook_candidates) - 25} more")

    print(
        "\nReminder: this is a heuristic shortlist, not a final selection. "
        "Review against instructions/workflow.md Step 3 (one strong idea per "
        "output piece) before drafting, and verify every stat/quote actually "
        "matches the source's meaning before use."
    )


if __name__ == "__main__":
    main()
