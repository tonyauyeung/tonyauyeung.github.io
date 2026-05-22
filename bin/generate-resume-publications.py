#!/usr/bin/env python3
"""Generate LaTeX publication list for the CV from _bibliography/papers.bib."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.customization import convert_to_unicode
except ImportError:
    print(
        "error: bibtexparser is required. Run: pip install bibtexparser",
        file=sys.stderr,
    )
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = ROOT / "_bibliography" / "papers.bib"
OUTPUT_PATH = ROOT / "assets" / "resume" / "publications_generated.tex"

# Match _config.yml scholar settings
SELF_LAST_NAMES = {"ouyang"}
SELF_FIRST_NAMES = {"ruikang", "r", "r."}


def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def load_bib_entries() -> list[dict]:
    raw = BIB_PATH.read_text(encoding="utf-8")
    if raw.startswith("---"):
        raw = raw.split("---", 2)[-1]

    parser = BibTexParser()
    parser.customization = convert_to_unicode
    parser.ignore_nonstandard_types = False
    parser.homogenize_fields = False
    db = bibtexparser.loads(raw, parser=parser)
    return list(db.entries)


def is_self_author(last: str, first: str) -> bool:
    clean_last = strip_accents(last.lower()).replace("*", "").strip()
    clean_first = strip_accents(first.lower()).replace(".", "").strip()
    if clean_last not in SELF_LAST_NAMES:
        return False
    if clean_first in SELF_FIRST_NAMES:
        return True
    return clean_first.startswith("r") and clean_first in ("r", "ruikang")


def split_author(author: str) -> tuple[str, str, str]:
    """Return (last, first, suffix_markers like *)."""
    author = author.strip()
    suffix = ""
    while author and author[-1] in "*∗†‡§¶‖&^":
        suffix = author[-1] + suffix
        author = author[:-1].strip()

    if "," in author:
        last, first = (part.strip() for part in author.split(",", 1))
    else:
        parts = author.rsplit(" ", 1)
        if len(parts) == 2:
            first, last = parts[0].strip(), parts[1].strip()
        else:
            return author, "", suffix

    return last, first, suffix


def format_author(author: str) -> str:
    last, first, suffix = split_author(author)
    if last and first:
        display = f"{last}, {first}{suffix}"
    else:
        display = f"{author}{suffix}"

    if is_self_author(last, first):
        return f"\\textbf{{{display}}}"
    return display


def split_authors(author_field: str) -> list[str]:
    """Split a BibTeX author field on ' and ' without breaking names."""
    parts: list[str] = []
    current: list[str] = []
    tokens = author_field.split()
    i = 0
    while i < len(tokens):
        if tokens[i].lower() == "and":
            parts.append(" ".join(current).strip())
            current = []
            i += 1
            continue
        current.append(tokens[i])
        i += 1
    if current:
        parts.append(" ".join(current).strip())
    return [p for p in parts if p]


def format_authors(author_field: str) -> str:
    formatted = [format_author(name) for name in split_authors(author_field)]
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    return ", ".join(formatted[:-1]) + f", and {formatted[-1]}"


def venue(entry: dict) -> str:
    if entry.get("abbr"):
        return entry["abbr"]
    if entry.get("booktitle"):
        return entry["booktitle"]
    if entry.get("journal"):
        return entry["journal"]
    return "Preprint"


def year_suffix(entry: dict) -> str:
    year = entry.get("year", "").strip()
    if not year:
        return ""
    return f" ({year})"


def format_entry(entry: dict) -> str:
    authors = format_authors(entry["author"])
    title = entry.get("title", "").strip().strip("{}")
    where = venue(entry)
    return (
        f"        \\item {authors}{year_suffix(entry)}. "
        f"{{\\color{{teal}}{title}}}. \\textit{{{where}}}."
    )


def main() -> None:
    entries = load_bib_entries()
    entries.sort(key=lambda e: int(e.get("year", "0")), reverse=True)

    lines = ["    \\begin{itemize}"]
    lines.extend(format_entry(entry) for entry in entries)
    lines.append("    \\end{itemize}")

    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} ({len(entries)} publications)")


if __name__ == "__main__":
    main()
