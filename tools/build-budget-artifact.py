"""Write artifact/budget-dashboard.html from budget.html.

The claude.ai Artifact publisher supplies its own <!doctype>, <head> and
<body>, so the artifact copy is budget.html without that wrapper.
Run from the repo root: python3 tools/build-budget-artifact.py
"""
import re
from pathlib import Path

src = Path("budget.html").read_text()
head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", src, re.S).group(1)
head = re.sub(r'\s*<meta charset="UTF-8">|\s*<meta name="viewport"[^>]*>', "", head)
out = "<!-- Generated from budget.html by tools/build-budget-artifact.py. Edit budget.html instead. -->\n"
Path("artifact/budget-dashboard.html").write_text(out + head.strip() + "\n" + body.strip() + "\n")
