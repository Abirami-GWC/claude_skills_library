#!/usr/bin/env python3
"""
generate_winloss_charts.py

Generates supporting chart images (PNG) from a deal-records CSV matching
templates/deal_record_schema.csv:
  1. win_rate_by_competitor.png — bar chart of win rate per competitor, with
     sample size labeled on each bar (never shows a percentage without n)
  2. loss_reason_distribution.png — stacked/grouped bar chart of loss reasons
     per competitor

Usage:
    python generate_winloss_charts.py <path-to-deals.csv> <output-directory>

Dependencies: matplotlib (preinstalled).

Bars for any competitor with n < 5 are rendered in a muted/hatched style and
labeled "n<5, anecdotal" directly on the chart, per
references/statistical_significance_notes.md — charts must carry the same
sample-size caution as the text report, since a chart's visual weight can
imply confidence the data doesn't support.
"""

import csv
import sys
import os
from collections import defaultdict, Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_deals(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def win_rate_chart(deals, out_path):
    groups = defaultdict(list)
    for d in deals:
        comp = (d.get("competitor") or "unknown").strip() or "unknown"
        groups[comp].append(d)

    labels, rates, ns, colors = [], [], [], []
    for comp, group_deals in sorted(groups.items()):
        n = len(group_deals)
        wins = [d for d in group_deals if d["outcome"].strip().lower() == "won"]
        rate = 100 * len(wins) / n if n else 0
        labels.append(comp)
        rates.append(rate)
        ns.append(n)
        colors.append("#c9c9c9" if n < 5 else "#2f5aa8")

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(labels, rates, color=colors)
    for bar, n, rate in zip(bars, ns, rates):
        label = f"n={n}" + (" (anecdotal)" if n < 5 else "")
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                label, ha="center", fontsize=8, color="#333")
    ax.set_ylabel("Win rate (%)")
    ax.set_title("Win Rate by Competitor")
    ax.set_ylim(0, max(rates + [10]) + 15)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close(fig)


def loss_reason_chart(deals, out_path):
    losses = [d for d in deals if d["outcome"].strip().lower() == "lost"]
    if not losses:
        return  # nothing to chart

    by_competitor = defaultdict(Counter)
    for d in losses:
        comp = (d.get("competitor") or "unknown").strip() or "unknown"
        reason = (d.get("reason_code") or "OTHER_UNKNOWN").strip()
        by_competitor[comp][reason] += 1

    all_reasons = sorted({r for counts in by_competitor.values() for r in counts})
    competitors = sorted(by_competitor.keys())

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bottom = [0] * len(competitors)
    cmap = plt.get_cmap("tab10")

    for i, reason in enumerate(all_reasons):
        values = [by_competitor[c].get(reason, 0) for c in competitors]
        ax.bar(competitors, values, bottom=bottom, label=reason, color=cmap(i % 10))
        bottom = [b + v for b, v in zip(bottom, values)]

    # annotate total n above each bar
    for x, comp in enumerate(competitors):
        n = sum(by_competitor[comp].values())
        ax.text(x, bottom[x] + 0.3, f"n={n}", ha="center", fontsize=8, color="#333")

    ax.set_ylabel("Losses (count)")
    ax.set_title("Loss Reason Distribution by Competitor")
    ax.legend(fontsize=7, loc="upper right", ncol=2)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close(fig)


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_winloss_charts.py <path-to-deals.csv> <output-directory>")
        sys.exit(2)

    csv_path, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)

    deals = load_deals(csv_path)
    if not deals:
        print("No deal records found in file.")
        sys.exit(1)

    win_rate_path = os.path.join(out_dir, "win_rate_by_competitor.png")
    loss_reason_path = os.path.join(out_dir, "loss_reason_distribution.png")

    win_rate_chart(deals, win_rate_path)
    loss_reason_chart(deals, loss_reason_path)

    print(f"Wrote {win_rate_path}")
    print(f"Wrote {loss_reason_path}")


if __name__ == "__main__":
    main()
