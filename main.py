#!/usr/bin/env python3
"""One Line of Earned Pride: write one quiet, earned line to /output/entry.txt.

The line is a single sentence. Tomas has practiced the same song for
twenty years on a borrowed guitar, and tonight, in his mother's
kitchen with his sisters listening from the doorway, he plays it
through without stopping once. The long effort is inside the line,
the scene is seen happening, and the pride lands on the last words,
with no trophy, podium, or graduation in sight.
"""

import os

ENTRY = (
    "For twenty years Tomas practiced the same song on a borrowed guitar; "
    "tonight, in his mother's kitchen with his sisters listening from "
    "the doorway, he played it through without stopping once."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry is {len(line)} characters, must be 1-240")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
