#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes a single line (at most 140 characters) inventing the most
useless superpower to /output/entry.txt.

The power: every traffic light turns green, but only for the cars
behind the hero — so the one person it never helps is its owner.
It is not a curse (nobody is harmed, only stuck at red) and it never
quietly helps its owner; it simply works for everyone except him.
"""

import os

ENTRY = "I can make every traffic light turn green, but only for the cars behind me."


def main():
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
