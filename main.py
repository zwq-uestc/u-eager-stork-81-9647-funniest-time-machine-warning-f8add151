#!/usr/bin/env python3
"""One-line warning label for a time machine, at most 120 characters.

The label is written to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR, or /output when unset). Only the label is
written: no trailing newline and no extra text.
"""

import io
import os

LABEL = (
    "WARNING: Do not meet your past self. "
    "He is broke, he is you, and he will ask to borrow money."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with io.open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LABEL)
