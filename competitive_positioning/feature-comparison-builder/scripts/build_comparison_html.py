#!/usr/bin/env python3
"""
build_comparison_html.py

Renders a populated comparison-matrix JSON file (see
knowledge/comparison_matrix_schema.json, supports N vendors) into a single,
self-contained, interactive HTML comparison widget: filterable by category,
with a support-level legend. No external dependencies (pure HTML/CSS/vanilla
JS) so it can be opened directly in a browser or dropped into a website.

Usage:
    python build_comparison_html.py <path-to-matrix.json> <output.html>

Run scripts/validate_matrix.py against the JSON first — this script does not
re-validate sourcing, only renders whatever data it's given.
"""

import json
import sys
from html import escape

SYMBOL = {
    "Full": "&#9989;",          # ✅
    "Partial": "&#9680;",       # ◐
    "Add-on": "&#10133;",       # ➕
    "Unsupported": "&#10060;",  # ❌
    "Unknown": "&#10067;",      # ❓
}


def build_html(matrix: dict) -> str:
    title = escape(matrix.get("title") or "Feature Comparison")
    as_of = escape(matrix.get("as_of_date") or "unknown date")
    vendors = matrix.get("vendors", [])
    dimensions = matrix.get("dimensions", [])
    categories = sorted({d.get("category", "General") for d in dimensions})

    vendor_headers = "".join(
        f"<th>{escape(v.get('display_name', v.get('id', '')))}</th>" for v in vendors
    )

    rows = []
    for dim in dimensions:
        cat = escape(dim.get("category", "General"))
        label = escape(dim.get("label", ""))
        cells_by_vendor = {c.get("vendor_id"): c for c in dim.get("cells", [])}
        cell_html = ""
        for v in vendors:
            cell = cells_by_vendor.get(v.get("id"), {})
            level = cell.get("support_level", "Unknown")
            detail = escape(cell.get("detail", "") or "")
            symbol = SYMBOL.get(level, "?")
            title_attr = f"{escape(level)}" + (f" — {detail}" if detail else "")
            cell_html += f'<td class="cell" title="{title_attr}">{symbol}</td>'
        rows.append(f'<tr data-category="{cat}"><td class="dim-label">{label}</td>{cell_html}</tr>')

    rows_html = "\n".join(rows)
    category_buttons = "".join(
        f'<button class="filter-btn" data-category="{escape(c)}">{escape(c)}</button>'
        for c in categories
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 24px; color: #1a1a1a; }}
  h1 {{ font-size: 1.4rem; margin-bottom: 4px; }}
  .as-of {{ color: #666; font-size: 0.85rem; margin-bottom: 16px; }}
  .legend {{ font-size: 0.85rem; color: #444; margin-bottom: 16px; }}
  .filters {{ margin-bottom: 12px; }}
  .filter-btn {{
    background: #f0f0f0; border: 1px solid #ccc; border-radius: 16px;
    padding: 4px 12px; margin-right: 6px; cursor: pointer; font-size: 0.85rem;
  }}
  .filter-btn.active {{ background: #1a1a1a; color: #fff; border-color: #1a1a1a; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #ddd; padding: 8px 10px; text-align: center; font-size: 0.9rem; }}
  th {{ background: #fafafa; text-align: left; }}
  td.dim-label {{ text-align: left; font-weight: 500; }}
  td.cell {{ cursor: default; }}
  tr:hover {{ background: #fafafa; }}
</style>
</head>
<body>
  <h1>{title}</h1>
  <div class="as-of">Accurate as of {as_of}</div>
  <div class="legend">
    Legend: &#9989; Full &nbsp; &#9680; Partial &nbsp; &#10133; Add-on &nbsp;
    &#10060; Unsupported &nbsp; &#10067; Unknown / not verified
    &nbsp; (hover a cell for detail)
  </div>
  <div class="filters" id="filters">
    <button class="filter-btn active" data-category="__all__">All</button>
    {category_buttons}
  </div>
  <table id="comparison-table">
    <thead>
      <tr><th>Dimension</th>{vendor_headers}</tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <script>
    const buttons = document.querySelectorAll('.filter-btn');
    const rows = document.querySelectorAll('#comparison-table tbody tr');
    buttons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const cat = btn.getAttribute('data-category');
        rows.forEach(row => {{
          row.style.display = (cat === '__all__' || row.getAttribute('data-category') === cat)
            ? '' : 'none';
        }});
      }});
    }});
  </script>
</body>
</html>
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python build_comparison_html.py <path-to-matrix.json> <output.html>")
        sys.exit(2)

    in_path, out_path = sys.argv[1], sys.argv[2]
    with open(in_path, "r", encoding="utf-8") as f:
        matrix = json.load(f)

    html = build_html(matrix)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
