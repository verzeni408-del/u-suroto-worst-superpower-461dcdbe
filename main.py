"""Worst Superpower v2: the power that patches up your attacker.

The entry is a single fixed line. The program only assembles it from
separate word groups, checks it against the gate (one line, 1-140
characters, not blank), and writes it to entry.txt.
"""

import os
import sys


def pick_fragments():
    opener = "I can instantly heal anyone who just punched me"
    payoff = "so my bullies leave every fight looking flawless"
    sting = "while I keep the bruises"
    return opener, payoff, sting


def stitch_line(pieces):
    line = pieces[0] + ", " + pieces[1] + " " + pieces[2] + "."
    return line


def gate_ok(line):
    if not line or not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return 1 <= len(line) <= 140


def destination():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main():
    line = stitch_line(pick_fragments())
    if not gate_ok(line):
        print(f"entry failed gate: {len(line)} chars", file=sys.stderr)
        return 1
    with open(destination(), "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(f"wrote entry ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
