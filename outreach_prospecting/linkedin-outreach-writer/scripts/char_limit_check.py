#!/usr/bin/env python3
"""
char_limit_check.py

Checks drafted LinkedIn copy against known platform character limits.

Usage:
  python3 char_limit_check.py messages.json

Input format (messages.json):
[
  {"type": "connection_request_note", "text": "..."},
  {"type": "standard_dm", "text": "..."}
]

type must match a key in knowledge/linkedin-character-limits.json -> "limits".
"""
import json
import sys
from pathlib import Path

LIMITS_FILE = Path(__file__).parent.parent / "knowledge" / "linkedin-character-limits.json"


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 char_limit_check.py messages.json")
        sys.exit(1)

    limits_data = json.loads(LIMITS_FILE.read_text())
    limits = limits_data["limits"]

    messages = json.loads(Path(sys.argv[1]).read_text())

    for i, m in enumerate(messages, 1):
        msg_type = m.get("type")
        text = m.get("text", "")
        length = len(text)
        limit = limits.get(msg_type)

        print(f"\nMessage {i} ({msg_type}): {length} characters")
        if limit is None:
            print(f"  WARNING — unknown message type '{msg_type}', no limit to check against.")
            continue
        if length > limit:
            print(f"  FAIL — exceeds limit of {limit} characters by {length - limit}.")
        else:
            print(f"  OK — within limit of {limit} characters ({limit - length} to spare).")


if __name__ == "__main__":
    main()
