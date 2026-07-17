#!/usr/bin/env python3
"""
build_gantt_chart.py

Renders a populated campaign-calendar JSON file (matching
knowledge/calendar_schema.json) into a visual Gantt-style timeline PNG:
one horizontal bar per activity, color-coded by channel/type, with
dependency arrows drawn from each prerequisite's end to its dependent's
start, and the anchor date marked with a vertical line.

Always run scripts/validate_calendar.py first — this script renders
whatever data it's given and does not re-check for conflicts, though
unresolved conflicts (e.g. an activity starting before its dependency ends)
will typically be visually obvious as a backwards-pointing arrow in the
resulting chart, which is itself a useful signal something is wrong.

Usage:
    python build_gantt_chart.py <path-to-calendar.json> <output.png>

Dependencies: matplotlib (preinstalled).
"""

import json
import sys
from datetime import date
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

TYPE_COLORS = {
    "content_creation": "#7a9cc6",
    "approval": "#e0a458",
    "publish": "#2f5aa8",
    "promotion": "#4caf7d",
    "reminder": "#b07cc6",
    "other": "#999999",
}


def parse_date(s):
    return date.fromisoformat(s)


def build_gantt(calendar: dict, out_path: str):
    activities = calendar.get("activities", [])
    if not activities:
        raise ValueError("No activities found in calendar JSON — nothing to render.")

    # sort by start date for a readable top-to-bottom flow
    activities = sorted(activities, key=lambda a: a.get("start_date", "9999-99-99"))
    by_id = {a["id"]: a for a in activities}

    fig_height = max(3, 0.5 * len(activities) + 1.5)
    fig, ax = plt.subplots(figsize=(11, fig_height))

    y_positions = {}
    for i, a in enumerate(activities):
        y = len(activities) - i
        y_positions[a["id"]] = y

        start = parse_date(a["start_date"])
        end = parse_date(a.get("end_date", a["start_date"]))
        duration = max((end - start).days, 1)
        color = TYPE_COLORS.get(a.get("type", "other"), TYPE_COLORS["other"])

        ax.barh(y, duration, left=start, height=0.5, color=color, edgecolor="#333", linewidth=0.5)

        label = f"{a.get('name', a['id'])}" + (f" ({a.get('owner')})" if a.get("owner") else "")
        ax.text(start, y + 0.32, label, fontsize=8, va="bottom", ha="left", color="#222")

    # dependency arrows: from dependency's end to this activity's start
    for a in activities:
        for dep_id in a.get("depends_on", []):
            dep = by_id.get(dep_id)
            if not dep:
                continue
            dep_end = parse_date(dep.get("end_date", dep["start_date"]))
            a_start = parse_date(a["start_date"])
            y_from = y_positions[dep_id]
            y_to = y_positions[a["id"]]
            style = "-" if a_start >= dep_end else "-"
            arrow_color = "#c0392b" if a_start < dep_end else "#888888"
            ax.annotate(
                "", xy=(a_start, y_to), xytext=(dep_end, y_from),
                arrowprops=dict(arrowstyle="->", color=arrow_color, lw=1, linestyle=style,
                                 connectionstyle="arc3,rad=0.15"),
            )

    # anchor date line
    anchor = calendar.get("anchor_date")
    if anchor:
        anchor_d = parse_date(anchor)
        ax.axvline(anchor_d, color="#c0392b", linestyle="--", linewidth=1)
        ax.text(anchor_d, len(activities) + 0.8, "Anchor date", color="#c0392b",
                fontsize=8, ha="center")

    ax.set_yticks([])
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    fig.autofmt_xdate()
    ax.set_title(calendar.get("campaign_name", "Campaign Timeline"))
    ax.set_ylim(0, len(activities) + 1.5)

    # legend
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in TYPE_COLORS.values()]
    ax.legend(handles, TYPE_COLORS.keys(), loc="upper left", bbox_to_anchor=(1.01, 1),
              fontsize=7, title="Type", title_fontsize=8)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    if len(sys.argv) != 3:
        print("Usage: python build_gantt_chart.py <path-to-calendar.json> <output.png>")
        sys.exit(2)

    in_path, out_path = sys.argv[1], sys.argv[2]
    with open(in_path, "r", encoding="utf-8") as f:
        calendar = json.load(f)

    try:
        build_gantt(calendar, out_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Wrote {out_path}")
    print("Note: a red dependency arrow pointing backwards indicates an unresolved "
          "conflict — run validate_calendar.py to confirm before delivering.")


if __name__ == "__main__":
    main()
