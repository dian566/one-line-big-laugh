#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to /output/entry.txt."""

import os

JOKE = "My smart speaker heard me say I am fine, so now it whispers ads for therapy in my sleep."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
