#!/usr/bin/env python3
"""News-image entry for 18 November 2026 (Python 3.13, standard library only).

The image entry.png sits beside this file. The program copies it, byte for
byte, to $MAKEFUN_OUTPUT_DIR/entry.png (default /output), so every run
writes exactly the same bytes.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main():
    data = SRC.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise SystemExit("entry.png is not a PNG file")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(data)


if __name__ == "__main__":
    main()
