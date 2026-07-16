#!/usr/bin/env python3
"""
cliche_checker.py

Screens candidate opener lines against the banned-cliches list and flags
generic-sounding lines. Also runs a rough "copy-paste test" heuristic: openers
with no digits, proper nouns, or quoted terms are flagged as possibly too generic
(a heuristic, not a definitive check — use judgment alongside it).

Usage:
  python3 cliche_checker.py openers.txt
  (one candidate opener per line in the input file)
"""
import sys
import re
from pathlib import Path

CLICHE_FILE = Path(__file__).parent.parent / "knowledge" / "banned-cliches.txt"


def load_cliches():
    lines = CLICHE_FILE.read_text().splitlines()
    return [l.strip().lower() for l in lines if l.strip() and not l.startswith("#")]


def has_specificity_markers(line):
    # crude heuristic: proper nouns (capitalized mid-sentence words), digits,
    # or quoted phrases suggest a concrete, specific reference.
    has_digit = bool(re.search(r"\d", line))
    has_capitalized_word = bool(re.search(r"(?<!^)(?<!\. )[A-Z][a-z]+", line))
    has_quote = '"' in line or "'" in line
    return has_digit or has_capitalized_word or has_quote


def check_line(line, cliches):
    lower = line.lower()
    hits = [c for c in cliches if c in lower]
    specific = has_specificity_markers(line)
    return hits, specific


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cliche_checker.py openers.txt")
        sys.exit(1)

    lines = [l.strip() for l in Path(sys.argv[1]).read_text().splitlines() if l.strip()]
    cliches = load_cliches()

    for i, line in enumerate(lines, 1):
        hits, specific = check_line(line, cliches)
        print(f"\nCandidate {i}: {line}")
        if hits:
            print(f"  FLAGGED — contains cliché phrase(s): {', '.join(hits)}")
        if not specific:
            print("  WARNING — no obvious specificity markers (names/numbers/quotes). "
                  "Double-check this passes the copy-paste test.")
        if not hits and specific:
            print("  OK — no cliché phrases detected, has specificity markers.")


if __name__ == "__main__":
    main()
