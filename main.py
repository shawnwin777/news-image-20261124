#!/usr/bin/env python3
"""Entry program for the news-image-20261124 make.fun bounty.

Copies the front-page image (entry.png, sitting next to this script) into
the output directory given by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only; deterministic.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if sha256_of(src) != sha256_of(dst):
        print("error: copied file does not match source (sha256 mismatch)",
              file=sys.stderr)
        return 1
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
