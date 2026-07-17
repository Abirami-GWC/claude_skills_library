#!/usr/bin/env python3
"""
validate_calendar.py

Validates a populated campaign-calendar JSON file (matching
knowledge/calendar_schema.json) for:
  - dangling dependency references
  - circular dependencies
  - an activity scheduled to start before a dependency has ended
  - insufficient buffer between a dependency's end and the dependent
    activity's start
  - owner double-booking on overlapping date ranges (if owner data present)

Usage:
    python validate_calendar.py <path-to-calendar.json> [--min-buffer-days N]

Exit code 0 = no conflicts found. Exit code 1 = one or more conflicts,
printed with the specific activities and dates involved so they can be
surfaced to the user rather than silently resolved.
"""

import json
import sys
import argparse
from datetime import date, timedelta


def parse_date(s: str) -> date:
    return date.fromisoformat(s)


def find_circular_dependencies(activities: dict) -> list[list[str]]:
    """Returns a list of cycles (each a list of activity ids) if any exist."""
    cycles = []
    visiting = set()
    visited = set()
    path = []

    def dfs(node_id):
        if node_id in visiting:
            cycle_start = path.index(node_id)
            cycles.append(path[cycle_start:] + [node_id])
            return
        if node_id in visited:
            return
        visiting.add(node_id)
        path.append(node_id)
        for dep_id in activities.get(node_id, {}).get("depends_on", []):
            if dep_id in activities:
                dfs(dep_id)
        path.pop()
        visiting.discard(node_id)
        visited.add(node_id)

    for aid in activities:
        if aid not in visited:
            dfs(aid)

    return cycles


def validate(calendar: dict, min_buffer_days: int) -> list[str]:
    errors = []
    activities_list = calendar.get("activities", [])
    activities = {a["id"]: a for a in activities_list}

    # dangling references
    for a in activities_list:
        for dep_id in a.get("depends_on", []):
            if dep_id not in activities:
                errors.append(
                    f"Activity '{a['id']}' ({a.get('name','')}) references unknown "
                    f"dependency '{dep_id}'."
                )

    # circular dependencies
    cycles = find_circular_dependencies(activities)
    for cycle in cycles:
        errors.append(f"Circular dependency detected: {' -> '.join(cycle)}")

    # date ordering + buffer checks
    for a in activities_list:
        if not a.get("start_date"):
            errors.append(f"Activity '{a['id']}' ({a.get('name','')}) has no start_date.")
            continue
        try:
            a_start = parse_date(a["start_date"])
        except ValueError:
            errors.append(f"Activity '{a['id']}': invalid start_date format (expected YYYY-MM-DD).")
            continue

        for dep_id in a.get("depends_on", []):
            dep = activities.get(dep_id)
            if not dep or not dep.get("end_date"):
                continue
            try:
                dep_end = parse_date(dep["end_date"])
            except ValueError:
                continue

            if a_start < dep_end:
                errors.append(
                    f"Activity '{a['id']}' ({a.get('name','')}) starts {a_start} but its "
                    f"dependency '{dep_id}' ({dep.get('name','')}) doesn't end until {dep_end}."
                )
            else:
                buffer_days = (a_start - dep_end).days
                if buffer_days < min_buffer_days:
                    errors.append(
                        f"Activity '{a['id']}' ({a.get('name','')}) starts only {buffer_days} "
                        f"day(s) after dependency '{dep_id}' ends — below the recommended "
                        f"minimum buffer of {min_buffer_days} day(s)."
                    )

        # flag whether dependency_source is tagged
        if a.get("depends_on") and not a.get("dependency_source"):
            errors.append(
                f"Activity '{a['id']}' has dependencies but no 'dependency_source' "
                f"(user-confirmed vs inferred) — tag it before delivering."
            )

    # owner double-booking (only checks activities with the same owner and overlapping dates)
    owner_activities = {}
    for a in activities_list:
        owner = a.get("owner")
        if not owner:
            continue
        owner_activities.setdefault(owner, []).append(a)

    for owner, acts in owner_activities.items():
        for i in range(len(acts)):
            for j in range(i + 1, len(acts)):
                a1, a2 = acts[i], acts[j]
                try:
                    s1, e1 = parse_date(a1["start_date"]), parse_date(a1.get("end_date", a1["start_date"]))
                    s2, e2 = parse_date(a2["start_date"]), parse_date(a2.get("end_date", a2["start_date"]))
                except (ValueError, KeyError):
                    continue
                if s1 <= e2 and s2 <= e1:
                    errors.append(
                        f"Owner '{owner}' is double-booked: '{a1['id']}' ({s1}-{e1}) overlaps "
                        f"with '{a2['id']}' ({s2}-{e2})."
                    )

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("calendar_path")
    parser.add_argument("--min-buffer-days", type=int, default=0,
                         help="Minimum days required between a dependency's end and the "
                              "dependent activity's start (default: 0, since same-day "
                              "publish-then-promote is a common valid pattern). Raise this "
                              "for higher-stakes campaigns where same-day sequencing is risky.")
    args = parser.parse_args()

    with open(args.calendar_path, "r", encoding="utf-8") as f:
        calendar = json.load(f)

    errors = validate(calendar, args.min_buffer_days)

    if not errors:
        print(f"PASS — {len(calendar.get('activities', []))} activities, no conflicts found.")
        sys.exit(0)

    print(f"FAIL — {len(errors)} conflict(s) found:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)


if __name__ == "__main__":
    main()
