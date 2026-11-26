#!/usr/bin/env python3
"""Worst Superpower v3: resurrection with a five-second refund window.

The gag: the hero can raise the dead, but the dead only stay long
enough to be let down by him all over again. The power is real, the
payoff is nothing, and the owner is the one who ends up hurt.

The script below holds the line in two clauses, joins them, checks
the competition gate (a single line, 1-140 characters, not blank),
and drops the result into entry.txt.
"""

from pathlib import Path
import os
import sys

CLAUSE_OPEN = "I can bring the dead back to life for five seconds,"
CLAUSE_CLOSE = "just long enough for them to be disappointed in me again."


GATE_MAX_CHARS = 140


def build_sentence(head, tail):
    """Glue the two clauses into the one-line entry.

    Refuses an empty clause so a typo can never silently shorten
    the line: a missing clause is a bug, not a shorter entry.
    """
    head, tail = head.strip(), tail.strip()
    if not head or not tail:
        raise ValueError("both clauses of the entry must be non-empty")
    return head + " " + tail


def entry_is_valid(sentence):
    """Gate: one non-blank line, 1 to GATE_MAX_CHARS characters."""
    if not sentence or not sentence.strip():
        return False
    if any(mark in sentence for mark in ("\n", "\r")):
        return False
    return 1 <= len(sentence) <= GATE_MAX_CHARS


def target_file():
    """Resolve where entry.txt goes; the harness sets the env var."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    Path(folder).mkdir(parents=True, exist_ok=True)
    return Path(folder) / "entry.txt"


def run():
    sentence = build_sentence(CLAUSE_OPEN, CLAUSE_CLOSE)
    if not entry_is_valid(sentence):
        print("entry failed gate: %d chars" % len(sentence), file=sys.stderr)
        return 1
    target_file().write_text(sentence + "\n", encoding="utf-8")
    print("wrote entry (%d chars)" % len(sentence))
    return 0


if __name__ == "__main__":
    sys.exit(run())
