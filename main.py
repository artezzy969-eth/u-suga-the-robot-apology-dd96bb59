#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only. Deterministic, no network, no secrets,
no reading anything outside this repository.
"""

import os

ENTRY = (
    "I sent the shopping list to your boss instead of your partner, and I am sorry.\n"
    "I have learned to check who a message is for, not just what it says, "
    "so now I read the recipient twice before I press send.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
