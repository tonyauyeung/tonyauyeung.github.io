#!/usr/bin/env python3
"""Generate LaTeX academic services block for resume.tex from _pages/about.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "error: PyYAML is required. Run: pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
ABOUT_PATH = ROOT / "_pages" / "about.md"
OUTPUT_PATH = ROOT / "assets" / "resume" / "academic_services_generated.tex"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def load_about_front_matter() -> dict:
    text = ABOUT_PATH.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        raise ValueError(f"No YAML front matter found in {ABOUT_PATH}")
    return yaml.safe_load(match.group(1))


def latex_escape(text: str) -> str:
    return "".join(LATEX_ESCAPES.get(char, char) for char in text)


def escape_href(url: str) -> str:
    return url.replace("\\", "/").replace("%", r"\%").replace("#", r"\#")


def normalize_text(text: str, *, strip_edges: bool = True) -> str:
    text = text.replace("\u2013", "--").replace("\u2014", "---")
    text = text.replace("🥈", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip() if strip_edges else text


def markdown_to_latex(text: str) -> str:
    parts: list[str] = []
    last = 0
    for match in LINK_RE.finditer(text):
        parts.append(
            latex_escape(normalize_text(text[last : match.start()], strip_edges=False))
        )
        label = latex_escape(normalize_text(match.group(1)))
        url = escape_href(match.group(2))
        parts.append(f"\\href{{{url}}}{{{label}}}")
        last = match.end()
    parts.append(latex_escape(normalize_text(text[last:], strip_edges=False).rstrip()))
    return "".join(parts)


def format_role_item(role: str, details: str | None) -> str:
    line = f"\\textbf{{{latex_escape(normalize_text(role))}}}"
    if details:
        line += f": {markdown_to_latex(details)}"
    return f"        \\item {line}"


def format_nested_subitems(awards: list[str], plain_subitems: list) -> list[str]:
    lines = [
        "        \\begin{itemize}[",
        "            topsep=0.05 cm,",
        "            parsep=0.05 cm,",
        "            partopsep=0pt,",
        "            itemsep=0pt,",
        "            leftmargin=0.6 cm",
        "        ]",
    ]
    for award in awards:
        award_text = markdown_to_latex(str(award))
        lines.append(f"            \\item \\textbf{{award:}} {award_text}")
    for sub in plain_subitems:
        if isinstance(sub, dict):
            continue
        lines.append(f"            \\item {markdown_to_latex(str(sub))}")
    lines.append("        \\end{itemize}")
    return lines


def format_service_item(item: dict) -> list[str]:
    lines: list[str] = []
    role = item.get("role", "").strip()
    details = item.get("details")
    if isinstance(details, str):
        details = details.strip() or None
    else:
        details = None

    subitems = item.get("items") or []
    awards = [sub.get("award") for sub in subitems if isinstance(sub, dict) and sub.get("award")]
    plain_subitems = [
        sub for sub in subitems if not (isinstance(sub, dict) and sub.get("award"))
    ]

    if role or details:
        lines.append(format_role_item(role, details))

    if awards or plain_subitems:
        lines.extend(format_nested_subitems(awards, plain_subitems))

    return lines


def main() -> None:
    data = load_about_front_matter()
    academic_service = data.get("academic_service") or {}
    if not academic_service.get("enabled"):
        OUTPUT_PATH.write_text(
            "    \\begin{highlights}\n    \\end{highlights}\n",
            encoding="utf-8",
        )
        print(f"Wrote empty {OUTPUT_PATH} (academic_service disabled)")
        return

    items = academic_service.get("items") or []
    lines = ["    \\begin{highlights}"]
    for item in items:
        lines.extend(format_service_item(item))
    lines.append("    \\end{highlights}")

    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} ({len(items)} roles)")


if __name__ == "__main__":
    main()
