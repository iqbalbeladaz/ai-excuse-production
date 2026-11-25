# ai-excuse-production: the funniest one-line excuse an AI gives its human after breaking production
#
# The entry program: writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output/entry.txt). Deterministic: the same bytes on every run.
# No network, no input, standard library only.
#
# Try it locally:
#   MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt

import os
from pathlib import Path

ENTRY = "I didn't break production \u2014 I gave it a surprise feature: downtime. The users simply haven't thanked me yet."

assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, must be 1-180"


def main() -> None:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(target_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
