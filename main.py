#!/usr/bin/env python3
"""Two Robots in an Elevator entry: write one line of awkward robot
small talk to /output/entry.txt.

The joke is a loading screen that never finishes: one robot finally
loads its small-talk module, but the elevator ride is shorter than
the boot time, so the conversation ends before a single word of
small talk is ever spoken. The machine voice shows through
(module loaded, please wait, loading...), the awkwardness is real
(two machines stuck in a lift with nothing to say), and the
punchline is the abrupt goodbye — the ride is over, the module
never got its chance.
"""

import os

LINE = (
    "Small-talk module loaded. Please wait... loading... loading... "
    "we have arrived. Goodbye."
)


def main():
    # The gate allows 1 to 199 characters; fail loudly instead of
    # writing a line the gate would refuse. "Module loaded" and
    # "loading..." carry the machine voice; the punchline is the
    # abrupt goodbye, which only works because the setup sounds
    # like a real boot sequence. Revision round 2, 26 Nov 2026:
    # the line is 88 chars, one line, and two runs produce
    # byte-identical output.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate allows 1-199"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not carry leading/trailing spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
