#!/usr/bin/env python3
"""
validate_matrix.py

Validates a populated comparison-matrix JSON file (matching
knowledge/comparison_matrix_schema.json, supports N vendors) against the
structural and sourcing rules in instructions/data_validation.md, BEFORE it is
rendered to markdown/CSV/HTML/docx.

Usage:
    python validate_matrix.py <path-to-matrix.json>

Exit code 0 = passes all checks. Exit code 1 = one or more failures printed.
This script checks structure/sourcing presence only — it cannot verify that a
claim is factually true, only that it is not silently unsourced.
"""

import json
import sys

VALID_SUPPORT_LEVELS = {"Full", "Partial", "Add-on", "Unsupported", "Unknown"}


def validate(matrix: dict) -> list[str]:
    errors = []

    if not matrix.get("as_of_date"):
        errors.append("Missing top-level 'as_of_date'.")

    vendors = matrix.get("vendors", [])
    vendor_ids = {v.get("id") for v in vendors}
    if "us" not in vendor_ids:
        errors.append("No vendor with id 'us' found — every matrix must include our own product.")
    if len(vendor_ids) < 2:
        errors.append("Fewer than 2 vendors defined — a comparison needs at least one competitor.")

    dimensions = matrix.get("dimensions", [])
    if not dimensions:
        errors.append("No dimensions defined.")

    for dim in dimensions:
        dim_id = dim.get("id", "<missing id>")
        cells = dim.get("cells", [])
        cell_vendor_ids = {c.get("vendor_id") for c in cells}

        missing = vendor_ids - cell_vendor_ids
        if missing:
            errors.append(f"Dimension '{dim_id}': missing cells for vendor(s) {sorted(missing)}.")

        for cell in cells:
            vendor_id = cell.get("vendor_id", "<missing vendor_id>")
            level = cell.get("support_level")

            if level not in VALID_SUPPORT_LEVELS:
                errors.append(
                    f"Dimension '{dim_id}', vendor '{vendor_id}': invalid support_level "
                    f"'{level}' (must be one of {sorted(VALID_SUPPORT_LEVELS)})."
                )

            if vendor_id != "us" and level not in ("Unknown", None):
                has_source = bool(cell.get("source_note")) or bool(cell.get("source_url"))
                if not has_source:
                    errors.append(
                        f"Dimension '{dim_id}', vendor '{vendor_id}': support_level='{level}' "
                        f"but no source_note/source_url provided. Mark 'Unknown' or add a source."
                    )

            if vendor_id != "us" and level == "Unsupported":
                if not cell.get("source_url"):
                    errors.append(
                        f"Dimension '{dim_id}', vendor '{vendor_id}': marked 'Unsupported' without "
                        f"a source_url. Highest-risk claim type — a URL or explicit confirmation "
                        f"is strongly recommended."
                    )

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_matrix.py <path-to-matrix.json>")
        sys.exit(2)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        matrix = json.load(f)

    errors = validate(matrix)

    if not errors:
        vendor_count = len(matrix.get("vendors", []))
        dim_count = len(matrix.get("dimensions", []))
        print(f"PASS — {vendor_count} vendors, {dim_count} dimensions, structurally sound and sourced.")
        sys.exit(0)

    print(f"FAIL — {len(errors)} issue(s) found:\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)


if __name__ == "__main__":
    main()
