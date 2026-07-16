#!/usr/bin/env python3
"""
validate_sequence.py

Runs automated QA checks on a drafted outbound sequence before delivery.

What it checks:
  - Duplicate subject lines across touches
  - Spam-trigger words/phrases (from resources/spam-trigger-words.txt)
  - Body word count per touch (warns if > 150 words)
  - Touch-to-touch text similarity (catches lazy copy/paste reuse)

Usage:
  python3 validate_sequence.py sequence.json

Input format (sequence.json):
[
  {"touch": 1, "day": 0, "subject": "quick one for you", "body": "..."},
  {"touch": 2, "day": 3, "subject": "...", "body": "..."}
]

Exit code is 0 even with warnings — this is a QA aid, not a hard gate. Read the
printed report and fix flagged issues before delivering the sequence to the user.
"""
import json
import sys
import difflib
import re
from pathlib import Path

SPAM_WORDS_FILE = Path(__file__).parent.parent / "resources" / "spam-trigger-words.txt"


def load_spam_words():
    if not SPAM_WORDS_FILE.exists():
        return []
    lines = SPAM_WORDS_FILE.read_text().splitlines()
    return [l.strip().lower() for l in lines if l.strip() and not l.startswith("#")]


def word_count(text):
    return len(re.findall(r"\w+", text))


def check_duplicate_subjects(touches):
    seen = {}
    issues = []
    for t in touches:
        subj = t["subject"].strip().lower()
        if subj in seen:
            issues.append(f"Touch {t['touch']}: subject line duplicates touch {seen[subj]}.")
        else:
            seen[subj] = t["touch"]
    return issues

def check_spam_words(touches, spam_words):
    issues = []
    for t in touches:
        combined = (t["subject"] + " " + t["body"]).lower()
        hits = [w for w in spam_words if w in combined]
        if hits:
            issues.append(f"Touch {t['touch']}: contains spam-trigger terms: {', '.join(hits)}")
    return issues

def check_body_length(touches, max_words=150):
    issues = []
    for t in touches:
        wc = word_count(t["body"])
        if wc > max_words:
            issues.append(f"Touch {t['touch']}: body is {wc} words (recommended max {max_words}).")
    return issues

def check_similarity(touches, threshold=0.6):
    issues = []
    for i in range(len(touches)):
        for j in range(i + 1, len(touches)):
            ratio = difflib.SequenceMatcher(None, touches[i]["body"], touches[j]["body"]).ratio()
            if ratio > threshold:
                issues.append(
                    f"Touch {touches[i]['touch']} and touch {touches[j]['touch']} are "
                    f"{ratio:.0%} similar — likely re-using the same angle instead of a new one."
                )
    return issues

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_sequence.py sequence.json")
        sys.exit(1)

    data = json.loads(Path(sys.argv[1]).read_text())
    spam_words = load_spam_words()

    all_issues = []
    all_issues += check_duplicate_subjects(data)
    all_issues += check_spam_words(data, spam_words)
    all_issues += check_body_length(data)
    all_issues += check_similarity(data)

    print(f"Validated {len(data)} touches.")
    if not all_issues:
        print("No issues found.")
    else:
        print(f"{len(all_issues)} issue(s) found:\n")
        for issue in all_issues:
            print(f"  - {issue}")

if __name__ == "__main__":
    main()
