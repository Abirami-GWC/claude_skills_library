#!/usr/bin/env python3
"""
analyze_winloss.py

Computes win rates and reason-code distributions from a deal-records CSV
matching templates/deal_record_schema.csv (columns: deal_id, close_date,
outcome, competitor, deal_size_usd, segment, industry, region, product_line,
reason_code, reason_detail).

Supports multi-dimension cuts (--cut) in addition to the base
competitor breakdown. Applies the sample-size caution rules from
references/statistical_significance_notes.md automatically.

Usage:
    python analyze_winloss.py <path-to-deals.csv>
    python analyze_winloss.py <path-to-deals.csv> --cut industry
    python analyze_winloss.py <path-to-deals.csv> --cut region --cut industry

Outputs a plain-text summary to stdout. Intended to be run before drafting the
narrative report so every percentage shown to the user is backed by an actual
computed count, not hand-arithmetic.
"""

import csv
import sys
import argparse
from collections import defaultdict, Counter


def significance_label(n: int) -> str:
    if n < 5:
        return "TOO SMALL — anecdotal only, do not report as a pattern"
    if n < 15:
        return "directional / early signal"
    if n < 30:
        return "emerging pattern"
    return "clear pattern"


def load_deals(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def win_rate_block(deals, group_field=None):
    """Print win rate broken out by group_field (e.g. 'competitor'), or overall if None."""
    if group_field is None:
        total = len(deals)
        wins = [d for d in deals if d["outcome"].strip().lower() == "won"]
        rate = 100 * len(wins) / total if total else 0
        print(f"Overall win rate: {rate:.1f}% ({len(wins)}/{total}) — [{significance_label(total)}]")
        return

    groups = defaultdict(list)
    for d in deals:
        key = (d.get(group_field) or "unknown").strip() or "unknown"
        groups[key].append(d)

    for key, group_deals in sorted(groups.items()):
        n = len(group_deals)
        wins = [d for d in group_deals if d["outcome"].strip().lower() == "won"]
        rate = 100 * len(wins) / n if n else 0
        print(f"{key}: {rate:.1f}% ({len(wins)}/{n}) — [{significance_label(n)}]")


def reason_distribution(deals, outcome_filter, group_field="competitor"):
    groups = defaultdict(list)
    for d in deals:
        if d["outcome"].strip().lower() != outcome_filter:
            continue
        key = (d.get(group_field) or "unknown").strip() or "unknown"
        groups[key].append(d)

    for key, group_deals in sorted(groups.items()):
        n = len(group_deals)
        counts = Counter((d.get("reason_code") or "OTHER_UNKNOWN").strip() for d in group_deals)
        print(f"\n{key} (n={n} {outcome_filter}) — [{significance_label(n)}]")
        for reason, count in counts.most_common():
            pct = 100 * count / n
            print(f"  {reason}: {count} ({pct:.0f}%)")


def multi_dimension_cut(deals, dimensions):
    """Cut by an arbitrary combination of dimension fields (e.g. ['competitor','industry'])."""
    groups = defaultdict(list)
    for d in deals:
        key = tuple((d.get(dim) or "unknown").strip() or "unknown" for dim in dimensions)
        groups[key].append(d)

    print(f"\n=== Cut by {' x '.join(dimensions)} ===")
    for key, group_deals in sorted(groups.items()):
        n = len(group_deals)
        wins = [d for d in group_deals if d["outcome"].strip().lower() == "won"]
        rate = 100 * len(wins) / n if n else 0
        label = " / ".join(key)
        sig = significance_label(n)
        flag = "  [SKIP: n<5, not reportable]" if n < 5 else ""
        print(f"{label}: {rate:.1f}% win rate ({len(wins)}/{n}) — [{sig}]{flag}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument(
        "--cut", action="append", default=[],
        help="Dimension field to cut by (competitor, industry, region, segment, product_line). "
             "Repeat --cut to combine dimensions, e.g. --cut competitor --cut industry."
    )
    args = parser.parse_args()

    deals = load_deals(args.csv_path)
    if not deals:
        print("No deal records found in file.")
        sys.exit(1)

    print("=== Overall ===")
    win_rate_block(deals)
    print()

    print("=== Win rate by competitor ===")
    win_rate_block(deals, group_field="competitor")
    print()

    print("=== Loss reason distribution by competitor ===")
    reason_distribution(deals, "lost", group_field="competitor")

    print("\n=== Win reason distribution by competitor ===")
    reason_distribution(deals, "won", group_field="competitor")

    if args.cut:
        multi_dimension_cut(deals, args.cut)


if __name__ == "__main__":
    main()
