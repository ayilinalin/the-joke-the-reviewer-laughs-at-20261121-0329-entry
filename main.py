#!/usr/bin/env python3
"""Entry for make.fun bounty the-joke-the-reviewer-laughs-at-20261121-0329.

Writes a single one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 stdlib only, no network,
fully deterministic: every run writes the exact same bytes.
"""

import os
import stat
import sys

JOKE = (
    "My coding agent reviewed its own pull request, approved it, then asked "
    "me to take a second look \u2014 because it wanted a second opinion from "
    "someone less qualified."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not 1 <= len(JOKE) <= 280:
        print("joke length out of range", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the joke, nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
