#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "One Line, One Laugh": The turn is the joke: a routine navigation word becomes a scolding so personal the driver pulls over to apologise to the car itself - instant first-read laugh, every word functional, no stock setup.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path
LINE = "My GPS said 'recalculating' with such disappointment that I pulled over and apologised to the car."
TEXT = LINE + "\n"
MAX_CHARS = 200
def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")
def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
if __name__ == "__main__":
    main()
