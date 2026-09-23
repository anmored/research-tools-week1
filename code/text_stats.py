#!/usr/bin/env python3
"""Print the 10 most frequent words in a text file."""

import argparse
import re
from collections import Counter
from pathlib import Path


# Test method:
# 1. Create a sample file containing:
#      Hello, hello! World.
#      world world
# 2. Run:
#      python code/text_stats.py sample.txt
# 3. Expected output:
#      world   3
#      hello   2

WORD_PATTERN = re.compile(r"[^\W_]+")


def count_words(text: str) -> Counter[str]:
    """Count words after normalizing case and splitting on spaces/punctuation."""
    words = WORD_PATTERN.findall(text.casefold())
    return Counter(words)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print the 10 most frequent words in a text file."
    )
    parser.add_argument("file", type=Path, help="path to the input text file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        text = args.file.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"error: cannot read {args.file}: {exc}") from exc

    counts = count_words(text)
    top_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10]

    for word, count in top_words:
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
