#!/usr/bin/env python3
"""Two Robots in an Elevator entry: write one line of awkward robot
small talk to /output/entry.txt.

The joke opens like a status report — one robot ran a diagnostic on
the silence, because that is what robots do when a social situation
feels wrong. The verdict then flips the premise: both robots are
avoiding eye contact, which is impossible, because neither of them
has eyes. The awkwardness is real (two machines stuck in a lift
pretending not to notice each other), the machine logic shows
through (diagnostic, verdict), and the punchline is the turn at the
very end.
"""

import os

LINE = (
    "I ran a diagnostic on this silence. Verdict: we are both "
    "avoiding eye contact neither of us has."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. "Diagnostic" and "Verdict"
    # carry the machine voice; the punchline is the final clause,
    # which only works because the setup sounds like a real report.
    # Verified 25 Nov 2026: the line is 96 chars, one line, and two
    # runs produce byte-identical output (sha256 8998ff67...).
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
