#!/usr/bin/env python3
"""Check WoW navigation and metadata; requires Python 3 and PyYAML.

Run from the repository root: python3 maintenance/check_repository.py
This does not validate external URLs, arbitrary Markdown syntax, or policy meaning.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def check(root):
    errors = []
    counts = {"files": 0, "links": 0, "skills": 0, "yaml": 0}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in {".git", "tmp", "__pycache__"} for part in relative.parts):
            continue
        if not path.is_file():
            continue
        counts["files"] += 1
        try:
            content = path.read_text(encoding="utf-8")
            if "\0" in content:
                raise ValueError("NUL byte; inspect binary authorization")
        except (UnicodeError, ValueError) as error:
            errors.append(f"{relative}: {error}")
            continue
        try:
            if path.suffix in {".yaml", ".yml"}:
                yaml.safe_load(content)
                counts["yaml"] += 1
            if path.suffix != ".md":
                continue
            if content.startswith("---\n"):
                parts = content.split("---\n", 2)
                if len(parts) != 3:
                    raise ValueError("unclosed frontmatter")
                metadata = yaml.safe_load(parts[1])
                if path.name == "SKILL.md":
                    counts["skills"] += 1
                    if not isinstance(metadata, dict):
                        raise ValueError("skill metadata must be a mapping")
                    if metadata.get("name") != path.parent.name:
                        raise ValueError("skill name must match directory")
                    if not isinstance(metadata.get("description"), str):
                        raise ValueError("skill description must be a string")
                    if not metadata["description"].strip():
                        raise ValueError("skill description is empty")
            elif path.name == "SKILL.md":
                raise ValueError("skill frontmatter missing")
        except (yaml.YAMLError, ValueError) as error:
            errors.append(f"{relative}: {error}")
        # This repository uses inline Markdown links without optional titles.
        for target in re.findall(r"\]\(([^)]+)\)", content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            counts["links"] += 1
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root) or not destination.exists():
                errors.append(f"{relative}: broken/outside link {target}")
    return counts, errors


if __name__ == "__main__":
    repository = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not repository.is_dir():
        sys.exit(f"Not a directory: {repository}")
    totals, failures = check(repository)
    for failure in failures:
        print(failure)
    print(f"{'FAIL' if failures else 'PASS'}: {totals}; {len(failures)} errors")
    sys.exit(bool(failures))
