"""Write a one-line joke about working beside AI coding agents.

Pure stdlib, deterministic, no network. Writes the joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

JOKE = (
    "My coding agent introduced the demo crash as a feature "
    "and took a bow before the error finished loading."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
