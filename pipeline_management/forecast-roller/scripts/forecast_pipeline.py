#!/usr/bin/env python3
"""
forecast_pipeline.py — Deterministic weighted revenue forecast for an open pipeline.

Computes weighted revenue per deal (value x probability), confidence tiers, period
filtering, and a concentration-risk check, per knowledge/forecasting-rules.md.
Running the same input through this script always produces the same forecast.

USAGE:
    python3 forecast_pipeline.py pipeline.csv
    python3 forecast_pipeline.py pipeline.csv --period-end 2026-09-30
    python3 forecast_pipeline.py pipeline.csv --today 2026-07-16 --concentration-threshold 0.3

EXPECTED CSV COLUMNS (header row required):
    deal_name           (required)
    value               (required, numeric)
    stage               (required — one of: lead, qualified, discovery, demo,
                         proposal, negotiation, closed won, closed lost —
                         case-insensitive)
    probability         (optional, 0-100)
    close_date          (optional, YYYY-MM-DD)
    last_activity_date  (optional, YYYY-MM-DD)

Excluded from the forecast entirely: "lead" and "closed lost" stages.
Tracked separately, not added to the forecast total: "closed won" (already
recognized revenue).
"""

import argparse
import csv
import sys
from datetime import datetime, date

STAGE_MIDPOINT = {
    "qualified": 10,
    "discovery": 23,
    "demo": 40,
    "proposal": 65,
    "negotiation": 88,
}
EXCLUDED_STAGES = {"lead", "closed lost"}
WON_STAGE = "closed won"
FORECASTABLE_STAGES = set(STAGE_MIDPOINT) | {WON_STAGE}


def parse_date(s):
    if not s or not s.strip():
        return None
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()


def normalize_stage(s):
    s = (s or "").strip().lower()
    if s not in FORECASTABLE_STAGES and s not in EXCLUDED_STAGES:
        raise ValueError(
            f"Unknown stage '{s}'. Must be one of: lead, qualified, discovery, "
            f"demo, proposal, negotiation, closed won, closed lost"
        )
    return s


def tier_for(probability):
    if probability >= 70:
        return "High"
    if probability >= 40:
        return "Medium"
    return "Low"


def load_deals(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("No deals found in CSV.")
    required = {"deal_name", "value", "stage"}
    missing_cols = required - set(reader.fieldnames or [])
    if missing_cols:
        raise ValueError(f"CSV is missing required column(s): {missing_cols}")
    return rows


def process(rows, period_end, today, concentration_threshold):
    included = []
    already_won = []
    next_period = []
    excluded = []

    for r in rows:
        flags = []
        name = r["deal_name"].strip()
        value = float(r["value"])
        stage = normalize_stage(r["stage"])
        close_dt = parse_date(r.get("close_date"))
        last_activity_dt = parse_date(r.get("last_activity_date"))

        if stage in EXCLUDED_STAGES:
            excluded.append({"deal_name": name, "stage": stage, "reason": f"stage '{stage}' excluded from forecast"})
            continue

        if stage == WON_STAGE:
            already_won.append({"deal_name": name, "value": value})
            continue

        prob_raw = (r.get("probability") or "").strip()
        if prob_raw:
            probability = float(prob_raw)
        else:
            probability = STAGE_MIDPOINT[stage]
            flags.append("probability inferred from stage")

        if close_dt is None:
            flags.append("no close date — period assignment unknown")
        elif period_end is not None and close_dt > period_end:
            next_period.append({
                "deal_name": name, "value": value, "stage": stage,
                "probability": probability, "close_date": close_dt.isoformat(),
            })
            continue

        if last_activity_dt is None:
            flags.append("no last-activity date — engagement unknown")
        else:
            days_since = (today - last_activity_dt).days
            if days_since > 21:
                flags.append(f"no activity in {days_since} days — possible stale deal")

        weighted_revenue = round(value * probability / 100, 2)
        included.append({
            "deal_name": name,
            "value": value,
            "stage": stage,
            "probability": probability,
            "close_date": close_dt.isoformat() if close_dt else "",
            "weighted_revenue": weighted_revenue,
            "tier": tier_for(probability),
            "data_quality_flags": "; ".join(flags),
        })

    total = round(sum(d["weighted_revenue"] for d in included), 2)
    by_tier = {"High": 0.0, "Medium": 0.0, "Low": 0.0}
    for d in included:
        by_tier[d["tier"]] += d["weighted_revenue"]
    by_tier = {k: round(v, 2) for k, v in by_tier.items()}

    concentration_flag = None
    if included and total > 0:
        top_deal = max(included, key=lambda d: d["weighted_revenue"])
        share = top_deal["weighted_revenue"] / total
        if share > concentration_threshold:
            concentration_flag = {
                "deal_name": top_deal["deal_name"],
                "share_pct": round(share * 100, 1),
            }

    included.sort(key=lambda d: -d["weighted_revenue"])

    return {
        "included": included,
        "already_won": already_won,
        "next_period": next_period,
        "excluded": excluded,
        "total_expected_revenue": total,
        "by_tier": by_tier,
        "concentration_flag": concentration_flag,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compute a weighted revenue forecast for an open pipeline.",
        epilog=(
            "Expected CSV columns (header row required):\n"
            "  deal_name           (required)\n"
            "  value               (required, numeric)\n"
            "  stage               (required — one of: lead, qualified, discovery, demo,\n"
            "                       proposal, negotiation, closed won, closed lost — case-insensitive)\n"
            "  probability         (optional, 0-100)\n"
            "  close_date          (optional, YYYY-MM-DD)\n"
            "  last_activity_date  (optional, YYYY-MM-DD)\n\n"
            "Excluded from the forecast entirely: 'lead' and 'closed lost' stages.\n"
            "Tracked separately, not added to the forecast total: 'closed won'."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("csv_path", help="Path to pipeline CSV")
    parser.add_argument("--period-end", help="Only count deals closing on/before this date (YYYY-MM-DD)")
    parser.add_argument("--today", help="Override today's date (YYYY-MM-DD), for reproducible testing")
    parser.add_argument("--concentration-threshold", type=float, default=0.30, help="Flag if one deal exceeds this share of the total (default 0.30)")
    args = parser.parse_args()

    today = parse_date(args.today) if args.today else date.today()
    period_end = parse_date(args.period_end) if args.period_end else None

    rows = load_deals(args.csv_path)
    result = process(rows, period_end, today, args.concentration_threshold)

    print("=== Included in forecast ===")
    print(f"{'Deal':<32}{'Value':<12}{'Prob%':<8}{'Weighted':<12}{'Tier':<8}{'Flags'}")
    for d in result["included"]:
        print(
            f"{d['deal_name'][:31]:<32}{d['value']:<12.0f}{d['probability']:<8.0f}"
            f"{d['weighted_revenue']:<12.0f}{d['tier']:<8}{d['data_quality_flags']}"
        )

    print(f"\nTotal Expected Revenue: {result['total_expected_revenue']:.2f}")
    print(f"  High:   {result['by_tier']['High']:.2f}")
    print(f"  Medium: {result['by_tier']['Medium']:.2f}")
    print(f"  Low:    {result['by_tier']['Low']:.2f}")

    if result["concentration_flag"]:
        cf = result["concentration_flag"]
        print(f"\nConcentration risk: '{cf['deal_name']}' is {cf['share_pct']}% of the total forecast.")
    else:
        print("\nConcentration risk: none — no single deal dominates the forecast.")

    if result["already_won"]:
        print("\n=== Already won (not in forecast total) ===")
        for d in result["already_won"]:
            print(f"  {d['deal_name']}: {d['value']:.0f}")

    if result["next_period"]:
        print("\n=== Next period (excluded from this total) ===")
        for d in result["next_period"]:
            print(f"  {d['deal_name']}: closes {d['close_date']}")

    if result["excluded"]:
        print("\n=== Excluded ===")
        for d in result["excluded"]:
            print(f"  {d['deal_name']}: {d['reason']}")


if __name__ == "__main__":
    main()
