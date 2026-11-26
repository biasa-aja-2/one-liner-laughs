#!/usr/bin/env python3
"""One-Liner Laughs.

Writes one original funny line (<=200 chars, single line, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib only. The twist: the plants are not dying from neglect,
they are testing whether the love was real.
"""

import os

JOKE = "I told my houseplants I loved them, and now they keep dying just to see if I meant it."


def main():
    # Gate: /output/entry.txt must hold UTF-8 text of 1 to 200 chars.
    if not (1 <= len(JOKE) <= 200) or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke violates the competition gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
