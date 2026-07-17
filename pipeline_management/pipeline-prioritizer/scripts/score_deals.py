#!/usr/bin/env python3
"""
score_deals.py — Deterministic priority scoring for open sales deals.

Computes a 0-100 Priority Score for each deal using the weighted model documented
in knowledge/scoring-guidelines.md and knowledge/priority-rules.md, and prints a
ranked table. Running the same input through this script always produces the same
scores and order.

USAGE:
    python3 score_deals.py deals.csv
    python3 score_deals.py deals.csv --weights value=0.3,probability=0.2,urgency=0.2,engagement=0.2,stage=0.1
    python3 score_deals.py deals.csv --today 2026-07-16

EXPECTED CSV COLUMNS (header row required):
    deal_name           (required)
    value               (required, numeric)
    stage               (required, one of: early, mid, late — case-insensitive)
    probability         (optional, 0-100)
    close_date          (optional, YYYY-MM-DD)
    last_activity_date  (optional, YYYY-MM-DD)
    engagement_notes    (optional, free text — carried through to output only)

Missing optional fields are filled with documented defaults and flagged in the
"data_quality_flags" output column.
"""

import argparse
import csv
import sys
from datetime import datetime, date

DEFAULT_WEIGHTS = {
    "value": 0.25,
    "probability": 0.20,
    "urgency": 0.20,
    "engagement": 0.20,
    "stage": 0.15,
}

STAGE_PROBABILITY_DEFAULT = {"early": 20, "mid": 50, "late": 80}
STAGE_SCORE = {"early": 35, "mid": 65, "late": 100}


def parse_weights(raw):
    if not raw:
        return dict(DEFAULT_WEIGHTS)
    weights = dict(DEFAULT_WEIGHTS)
    for pair in raw.split(","):
        key, _, val = pair.partition("=")
        key = key.strip()
        if key not in weights:
            raise ValueError(f"Unknown weight key '{key}'. Valid keys: {list(weights)}")
        weights[key] = float(val)
    total = sum(weights.values())
    if abs(total - 1.0) > 0.01:
        print(f"Warning: weights sum to {total:.2f}, not 1.0 — normalizing.", file=sys.stderr)
        weights = {k: v / total for k, v in weights.items()}
    return weights


def parse_date(s):
    if not s or not s.strip():
        return None
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()


def normalize_stage(s):
    s = (s or "").strip().lower()
    if s not in STAGE_SCORE:
        raise ValueError(f"Unknown stage '{s}'. Must be one of: early, mid, late")
    return s


def urgency_score(close_dt, today):
    if close_dt is None:
        return 40, True
    days = (close_dt - today).days
    if days <= 7:
        return 100, False
    if days <= 30:
        return 75, False
    if days <= 90:
        return 50, False
    return 25, False


def engagement_score(last_activity_dt, today):
    if last_activity_dt is None:
        return 50, True
    days = (today - last_activity_dt).days
    if days <= 3:
        return 100, False
    if days <= 14:
        return 70, False
    if days <= 30:
        return 40, False
    return 15, False


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


def score_deals(rows, weights, today):
    values = [float(r["value"]) for r in rows]
    max_value = max(values) if values else 1
    max_value = max_value or 1  # avoid divide-by-zero if all values are 0

    scored = []
    for r in rows:
        flags = []
        name = r["deal_name"].strip()
        value = float(r["value"])
        stage = normalize_stage(r["stage"])

        prob_raw = (r.get("probability") or "").strip()
        if prob_raw:
            probability = float(prob_raw)
        else:
            probability = STAGE_PROBABILITY_DEFAULT[stage]
            flags.append("probability inferred from stage")

        close_dt = parse_date(r.get("close_date"))
        last_activity_dt = parse_date(r.get("last_activity_date"))

        value_score = (value / max_value) * 100
        urg_score, urg_unknown = urgency_score(close_dt, today)
        if urg_unknown:
            flags.append("no close date — urgency treated as unknown")
        eng_score, eng_unknown = engagement_score(last_activity_dt, today)
        if eng_unknown:
            flags.append("no last-activity date — engagement treated as unknown")
        stage_score = STAGE_SCORE[stage]

        priority = (
            value_score * weights["value"]
            + probability * weights["probability"]
            + urg_score * weights["urgency"]
            + eng_score * weights["engagement"]
            + stage_score * weights["stage"]
        )

        scored.append({
            "deal_name": name,
            "value": value,
            "stage": stage,
            "probability": probability,
            "close_date": close_dt.isoformat() if close_dt else "",
            "last_activity_date": last_activity_dt.isoformat() if last_activity_dt else "",
            "engagement_notes": r.get("engagement_notes", "").strip(),
            "priority_score": round(priority, 1),
            "sub_scores": {
                "value": round(value_score, 1),
                "probability": round(probability, 1),
                "urgency": urg_score,
                "engagement": eng_score,
                "stage": stage_score,
            },
            "data_quality_flags": "; ".join(flags),
            "_close_dt": close_dt,
        })

    # Sort: priority desc, then nearer close date, then higher value
    far_future = date.max
    scored.sort(
        key=lambda d: (
            -d["priority_score"],
            d["_close_dt"] or far_future,
            -d["value"],
        )
    )
    for d in scored:
        del d["_close_dt"]
    return scored


def main():
    parser = argparse.ArgumentParser(description="Score and rank open sales deals.")
    parser.add_argument("csv_path", help="Path to deals CSV")
    parser.add_argument("--weights", help="Comma-separated overrides, e.g. value=0.3,probability=0.2,urgency=0.2,engagement=0.2,stage=0.1")
    parser.add_argument("--today", help="Override today's date (YYYY-MM-DD), for reproducible testing")
    args = parser.parse_args()

    weights = parse_weights(args.weights)
    today = parse_date(args.today) if args.today else date.today()

    rows = load_deals(args.csv_path)
    scored = score_deals(rows, weights, today)

    print(f"{'Rank':<5}{'Score':<8}{'Deal':<32}{'Value':<12}{'Stage':<8}{'Close Date':<12}{'Flags'}")
    for i, d in enumerate(scored, 1):
        print(
            f"{i:<5}{d['priority_score']:<8}{d['deal_name'][:31]:<32}"
            f"{d['value']:<12.0f}{d['stage']:<8}{d['close_date'] or '-':<12}"
            f"{d['data_quality_flags']}"
        )


if __name__ == "__main__":
    main()
