#!/usr/bin/env python3
"""
build_calculator_html.py

Generates a self-contained, interactive HTML calculator widget from a JSON
spec defining inputs, a formula, and an output — for use as a lead-magnet
calculator (ROI calculator, savings calculator, sizing estimator, etc.).

CRITICAL: per instructions/workflow.md Step 3a, the formula in the spec must
be explicitly confirmed with the user before this script is run. This script
does not validate business logic correctness — only that the spec is
structurally usable. Fabricating a formula and running it through this script
still produces a misleading tool; the confirmation step happens before this
script is invoked, not instead of it.

Spec format (JSON):
{
  "title": "Support Cost Savings Calculator",
  "description": "Estimate your annual savings by switching to [Product].",
  "inputs": [
    {"id": "tickets_per_month", "label": "Support tickets per month", "type": "number", "default": 500},
    {"id": "cost_per_ticket", "label": "Current cost per ticket (USD)", "type": "number", "default": 12},
    {"id": "reduction_pct", "label": "Expected ticket reduction (%)", "type": "number", "default": 30}
  ],
  "formula": "tickets_per_month * cost_per_ticket * (reduction_pct / 100) * 12",
  "output_label": "Estimated annual savings",
  "output_prefix": "$",
  "output_suffix": ""
}

The "formula" field is a Python-expression-like string using only the input
ids as variables, +, -, *, /, (), and numeric literals — it is compiled to
JavaScript automatically (operators map directly, no translation needed for
this restricted grammar). Do not use function calls or unsupported syntax;
keep formulas to basic arithmetic on the declared inputs.

Usage:
    python build_calculator_html.py <path-to-spec.json> <output.html>

After generating, test the calculator with at least one known input/output
pair to confirm the JS formula matches the confirmed formula exactly (see
instructions/workflow.md Step 3a).
"""

import json
import re
import sys
from html import escape

ALLOWED_FORMULA_PATTERN = re.compile(r"^[\w\s+\-*/().0-9]+$")


def validate_formula(formula: str, input_ids: list[str]) -> None:
    if not ALLOWED_FORMULA_PATTERN.match(formula):
        raise ValueError(
            f"Formula contains characters outside the allowed arithmetic grammar: {formula!r}. "
            f"Only input ids, +, -, *, /, (), and numbers are permitted."
        )
    # crude check that every token that looks like an identifier is a known input id
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", formula)
    unknown = [t for t in tokens if t not in input_ids]
    if unknown:
        raise ValueError(
            f"Formula references unknown identifier(s) {unknown}, not among declared "
            f"input ids {input_ids}. Fix the spec before generating."
        )


def build_html(spec: dict) -> str:
    title = escape(spec.get("title", "Calculator"))
    description = escape(spec.get("description", ""))
    inputs = spec.get("inputs", [])
    formula = spec.get("formula", "0")
    output_label = escape(spec.get("output_label", "Result"))
    output_prefix = escape(spec.get("output_prefix", ""))
    output_suffix = escape(spec.get("output_suffix", ""))

    input_ids = [i["id"] for i in inputs]
    validate_formula(formula, input_ids)

    input_fields_html = ""
    js_var_reads = ""
    for inp in inputs:
        iid = inp["id"]
        label = escape(inp.get("label", iid))
        default = inp.get("default", 0)
        input_fields_html += f"""
    <div class="field">
      <label for="{iid}">{label}</label>
      <input type="number" id="{iid}" value="{default}" step="any">
    </div>"""
        js_var_reads += f'    const {iid} = parseFloat(document.getElementById("{iid}").value) || 0;\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 24px; max-width: 480px; color: #1a1a1a; }}
  h1 {{ font-size: 1.3rem; margin-bottom: 4px; }}
  .desc {{ color: #555; font-size: 0.9rem; margin-bottom: 20px; }}
  .field {{ margin-bottom: 14px; }}
  label {{ display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 4px; }}
  input {{ width: 100%; padding: 8px 10px; font-size: 1rem; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }}
  button {{
    background: #1a2b4c; color: #fff; border: none; border-radius: 6px;
    padding: 10px 18px; font-size: 0.95rem; cursor: pointer; margin-top: 8px;
  }}
  button:hover {{ background: #2a3e66; }}
  .result {{
    margin-top: 20px; padding: 16px; background: #f5f7fb; border-radius: 8px;
    font-size: 1.1rem; display: none;
  }}
  .result.show {{ display: block; }}
  .result .value {{ font-size: 1.8rem; font-weight: 700; color: #1a2b4c; }}
</style>
</head>
<body>
  <h1>{title}</h1>
  <div class="desc">{description}</div>
  <form id="calc-form">
    {input_fields_html}
    <button type="submit">Calculate</button>
  </form>
  <div class="result" id="result-box">
    <div>{output_label}</div>
    <div class="value" id="result-value"></div>
  </div>

  <script>
    document.getElementById('calc-form').addEventListener('submit', function(e) {{
      e.preventDefault();
{js_var_reads}
      const result = {formula};
      const box = document.getElementById('result-box');
      const valueEl = document.getElementById('result-value');
      valueEl.textContent = "{output_prefix}" + result.toLocaleString(undefined, {{maximumFractionDigits: 2}}) + "{output_suffix}";
      box.classList.add('show');
    }});
  </script>
</body>
</html>
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python build_calculator_html.py <path-to-spec.json> <output.html>")
        sys.exit(2)

    in_path, out_path = sys.argv[1], sys.argv[2]
    with open(in_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    try:
        html = build_html(spec)
    except ValueError as e:
        print(f"Spec validation failed: {e}")
        sys.exit(1)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Wrote {out_path}")
    print("Reminder: test with a known input/output pair before delivering — "
          "confirm the JS formula matches the user-confirmed business logic exactly.")


if __name__ == "__main__":
    main()
