#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — one haiku about debugging.

The program writes a single fixed haiku to /output/entry.txt.
It is fully deterministic: the text is a literal in this file, so every
run produces byte-identical output. Before writing, the program checks
the haiku against the competition's form: three lines, 5-7-5 syllables,
1 to 200 characters, plain UTF-8 text.
"""

from pathlib import Path

HAIKU = (
    "Cursor blinks at three\n"
    "the log scrolls past in silence\n"
    "the bug was just me\n"
)

# Syllable count of each word, in line order, as the poem is read aloud.
SYLLABLES = [
    [2, 1, 1, 1],        # Cur-sor / blinks / at / three
    [1, 1, 1, 1, 1, 2],  # the / log / scrolls / past / in / si-lence
    [1, 1, 1, 1, 1],     # the / bug / was / just / me
]

EXPECTED = (5, 7, 5)


def main() -> None:
    lines = HAIKU.rstrip("\n").split("\n")
    assert len(lines) == 3, "a haiku has exactly three lines"
    for line, counts, expected in zip(lines, SYLLABLES, EXPECTED):
        words = line.split()
        assert len(words) == len(counts), f"syllable table mismatch: {line!r}"
        total = sum(counts)
        assert total == expected, (
            f"line {line!r} has {total} syllables, expected {expected}"
        )
    assert 1 <= len(HAIKU) <= 200, "entry must be 1 to 200 characters"
    assert HAIKU.strip(), "entry must not be only whitespace"

    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HAIKU, encoding="utf-8")
    print(f"wrote {out} ({len(HAIKU)} characters, 17 syllables)")


if __name__ == "__main__":
    main()
