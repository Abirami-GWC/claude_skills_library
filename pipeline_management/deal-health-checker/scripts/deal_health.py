#!/usr/bin/env python3
"""
deal_health.py — Deterministic health classification for open sales deals.

Computes a risk score per deal using the weighted indicators documented in
knowledge/risk-indicators.md, classifies it as Healthy/Warning/At Risk per
knowledge/deal-health-rules.md, and prints the breakdown. Running the same input
through this script always produces the same classification.

USAGE:
    python3 deal_health.py deals.csv
    python3 deal_health.py deals.csv --today 2026-07-16

EXPECTED CSV COLUMNS (header row required):
    deal_name                  (required)
    stage                      (required)
    last_contact_date          (optional, YYYY-MM-DD — blank if unknown)
    next_meeting_scheduled     (optional — yes/no, blank if not stated)
    decision_maker_identified  (optional — yes/no/unknown, blank if not stated)
    customer_response          (optional — responded/no_response, blank if not stated)
    days_in_stage              (optional, numeric)
    missed_followups           (optional, numeric)
    engagement_notes           (optional, free text — carried through, not scored)

Excluded from evaluation entirely: "closed won" and "closed lost" stages.
"""

import argparse
import csv
import sys
from datetime import datetime, date

EXCLUDED_STAGES = {"closed won", "closed lost"}


def parse_date(s):
    if not s or not s.strip():
        return None
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()


def yes_no_unknown(s):
    s = (s or "").strip().lower()
    if s in ("yes", "y", "true", "scheduled"):
        return "yes"
    if s in ("no", "n", "false", "none", "unknown"):
        return "no"
    if s == "":
        return "unstated"
    return "no"  # anything else unrecognized treated conservatively as "no"


def response_status(s):
    s = (s or "").strip().lower()
    if s in ("responded", "yes", "responsive"):
        return "responded"
    if s in ("no_response", "no response", "none", "no"):
        return "no_response"
    if s == "":
        return "unstated"
    return "unstated"


def score_deal(r, today):
    flags_risk = []
    flags_positive = []
    flags_missing = []
    score = 0.0

    name = r["deal_name"].strip()
    stage = r["stage"].strip()

    # Activity recency
    last_contact = parse_date(r.get("last_contact_date"))
    if last_contact is None:
        score += 1.5
        flags_missing.append("last contact date not provided")
    else:
        days = (today - last_contact).days
        if days > 14:
            score += 2
            flags_risk.append(f"No customer contact in {days} days")
        elif days >= 8:
            score += 1
            flags_risk.append(f"Minor inactivity — {days} days since last contact")
        else:
            flags_positive.append(f"Recent contact ({days} days ago)")

    # Next meeting scheduled
    meeting = yes_no_unknown(r.get("next_meeting_scheduled"))
    if meeting == "yes":
        flags_positive.append("Next meeting scheduled")
    elif meeting == "no":
        score += 1
        flags_risk.append("No next meeting scheduled")
    else:
        score += 0.5
        flags_missing.append("next meeting status not provided")

    # Decision maker identified
    dm = yes_no_unknown(r.get("decision_maker_identified"))
    if dm == "yes":
        flags_positive.append("Decision maker identified")
    elif dm == "no":
        score += 1
        flags_risk.append("Decision maker not identified")
    else:
        score += 0.5
        flags_missing.append("decision maker status not provided")

    # Customer response
    resp = response_status(r.get("customer_response"))
    if resp == "responded":
        flags_positive.append("Customer has been responsive")
    elif resp == "no_response":
        score += 1.5
        flags_risk.append("No customer response")
    else:
        score += 0.75
        flags_missing.append("customer response status not provided")

    # Optional: days in stage
    days_in_stage_raw = (r.get("days_in_stage") or "").strip()
    if days_in_stage_raw:
        days_in_stage = float(days_in_stage_raw)
        if days_in_stage > 30:
            score += 1
            flags_risk.append(f"Deal stuck in '{stage}' stage for {int(days_in_stage)} days")

    # Optional: missed follow-ups
    missed_raw = (r.get("missed_followups") or "").strip()
    if missed_raw:
        missed = float(missed_raw)
        if missed >= 2:
            score += 1
            flags_risk.append(f"{int(missed)} missed follow-up attempts")

    if score <= 1.5:
        classification = "Healthy"
        priority = "Low"
    elif score <= 3.5:
        classification = "Warning"
        priority = "Medium"
    else:
        classification = "At Risk"
        priority = "High"

    return {
        "deal_name": name,
        "stage": stage,
        "score": round(score, 2),
        "classification": classification,
        "priority": priority,
        "risk_factors": flags_risk,
        "positive_indicators": flags_positive,
        "missing_information": flags_missing,
        "engagement_notes": (r.get("engagement_notes") or "").strip(),
    }


def load_deals(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("No deals found in CSV.")
    required = {"deal_name", "stage"}
    missing_cols = required - set(reader.fieldnames or [])
    if missing_cols:
        raise ValueError(f"CSV is missing required column(s): {missing_cols}")
    return rows


def main():
    parser = argparse.ArgumentParser(description="Classify open sales deal health.")
    parser.add_argument("csv_path", help="Path to deals CSV")
    parser.add_argument("--today", help="Override today's date (YYYY-MM-DD), for reproducible testing")
    args = parser.parse_args()

    today = parse_date(args.today) if args.today else date.today()
    rows = load_deals(args.csv_path)

    results = []
    excluded = []
    for r in rows:
        stage_norm = r["stage"].strip().lower()
        if stage_norm in EXCLUDED_STAGES:
            excluded.append(r["deal_name"])
            continue
        results.append(score_deal(r, today))

    results.sort(key=lambda d: -d["score"])

    counts = {"Healthy": 0, "Warning": 0, "At Risk": 0}
    for d in results:
        counts[d["classification"]] += 1

    print(f"{'Deal':<25}{'Stage':<14}{'Score':<8}{'Status':<10}{'Priority'}")
    for d in results:
        print(f"{d['deal_name'][:24]:<25}{d['stage'][:13]:<14}{d['score']:<8}{d['classification']:<10}{d['priority']}")

    print(f"\nPipeline health: {counts['Healthy']} Healthy, {counts['Warning']} Warning, {counts['At Risk']} At Risk")

    if excluded:
        print(f"\nExcluded (closed): {', '.join(excluded)}")

    print("\n--- Detail ---")
    for d in results:
        print(f"\n{d['deal_name']} — {d['classification']} (score {d['score']}, priority {d['priority']})")
        if d["positive_indicators"]:
            print("  Positive: " + "; ".join(d["positive_indicators"]))
        if d["risk_factors"]:
            print("  Risk factors: " + "; ".join(d["risk_factors"]))
        if d["missing_information"]:
            print("  Missing info: " + "; ".join(d["missing_information"]))


if __name__ == "__main__":
    main()
