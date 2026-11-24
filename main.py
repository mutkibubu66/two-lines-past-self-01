#!/usr/bin/env python3
"""Two lines: a warning sent back to my past self.

Line 1 warns about one specific moment; line 2 says why that moment
mattered and what changed because of it. Pure standard library, no
network. Writes both lines to /output/entry.txt and prints them to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE_1 = (
    "Don't send that 2 a.m. email to your boss -- sleep on it, because "
    "the version you write angry will be the version they remember."
)

LINE_2 = (
    "That one unsent draft taught me that a night of waiting costs "
    "nothing and a hasty sentence costs a reputation, so now I never send "
    "anything I wrote after midnight."
)


def main() -> None:
    lines = [LINE_1, LINE_2]
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        assert 1 <= len(line) <= 200, "each line must be 1-200 characters"
        assert line.strip(), "each line must not be blank"
        assert "  " not in line, "no double spaces inside a line"
    text = "\n".join(lines) + "\n"
    assert 1 <= len(text) <= 400, "entry text must be 1-400 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == text, "written file must round-trip exactly"
    print(text, end="")


if __name__ == "__main__":
    main()
