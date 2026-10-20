#!/usr/bin/env python3
"""Privacy/leak check for the jibun-de-mamoru repo.

Fails the build when any tracked file carries: inference-provider or
provider-model identifiers, personal webmail addresses, local machine
paths, or hardcoded API key assignments. Also enforces the tool's public
promise that index.html makes zero outbound requests (no fetch/XHR/axios,
no telemetry) - the article tells readers input never leaves the device,
so the code must not be able to break that silently.

Detection blocklist note: listing a vendor here is a rule, not an
admission - it names many vendors across the market and says nothing
about which (if any) the author uses.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PATTERNS = [
    ("provider/model id", re.compile(
        r"openrouter|api\.typesafe|typesafe|integrate\.api\.nvidia|nvidia|"
        r"nemotron|glm-5|z-ai|\bgpt-oss\b|deepseek|\bgroq\b|"
        r"generativelanguage|api\.z\.ai|\bminimax\b|anthropic|\bgemini\b|"
        r"\bqwen\b|mistral", re.I)),
    ("personal email", re.compile(
        r"[A-Za-z0-9._%+-]+@(?:gmail|googlemail|outlook|hotmail|yahoo|icloud)"
        r"\.[a-z.]{2,10}")),
    ("local machine path", re.compile(r"/home/[a-z][a-z0-9_-]{2,20}/", re.I)),
    ("hardcoded key assignment", re.compile(r"_API_KEY\s*=\s*[\"']")),
]

# Files that legitimately carry rule text (the checker names vendors as a
# rule, not an admission; AGENTS.md is the working agreement).
ALLOW_HINTS = ("AGENTS.md", "privacy_check.py")

# The one public promise the page makes that must never regress.
NO_NETWORK_VIOLATIONS = re.compile(r"\bfetch\s*\(|XMLHttpRequest|axios|beacon\(|telemetry", re.I)
NETWORK_ALLOWED = ("index.html",)


def main() -> int:
    leaks = []
    tracked = subprocess_files()
    for name in tracked:
        p = REPO / name
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for label, pat in PATTERNS:
            for i, line in enumerate(text.splitlines(), 1):
                if pat.search(line) and not any(h in name for h in ALLOW_HINTS):
                    leaks.append(f"  {name}:{i}: {label}: {line.strip()[:80]}")
        if name == "index.html" and NO_NETWORK_VIOLATIONS.search(text):
            leaks.append("  index.html: outbound request API found (fetch/XHR/axios/"
                         "beacon) - the page promises everything stays on-device")
        if name == "index.html":
            js_src = re.findall(r'\bsrc\s*=\s*"(https?://[^"]+)"', text)
            for u in js_src:
                leaks.append(f"  index.html: remote <script src> found: {u} "
                             "(single-file, no remote code)")
    if leaks:
        print("PRIVACY LEAKS FOUND:")
        print("\n".join(leaks))
        return 1
    print("privacy check: clean")
    return 0


def subprocess_files():
    import subprocess
    out = subprocess.run(["git", "ls-files"], cwd=REPO,
                         capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if l.strip()]


if __name__ == "__main__":
    sys.exit(main())
