#!/usr/bin/env python3
"""One-Liner Laughs.

Writes one original funny line (<=200 chars, single line, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib only. The twist: the plants are not dying from neglect,
they are testing whether the love was real -- a houseplant loyalty
test, with the punchline landing on "just to see if I meant it".
The line is tight and complete: setup, escalation, and a turn that
reframes the dying plants as suspicious judges of sincerity.
"""

import os

JOKE = "I told my houseplants I loved them, and now they keep dying just to see if I meant it."


def check_gate(text):
    """Gate: /output/entry.txt must hold UTF-8 text of 1 to 200 chars."""
    if not (1 <= len(text) <= 200):
        raise ValueError("joke violates the competition gate: length")
    if "\n" in text or "\r" in text:
        raise ValueError("joke violates the competition gate: not a single line")
    if not text.strip():
        raise ValueError("joke violates the competition gate: whitespace-only")


def write_entry(path, text):
    """Write the joke byte-exact, then leave the file world-readable."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Byte-exact read-back verification: no trailing newline, valid UTF-8.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != text.encode("utf-8"):
        raise ValueError("verification failed: file bytes differ from joke")


def main():
    check_gate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, JOKE)


if __name__ == "__main__":
    main()
