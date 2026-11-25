"""One Line, One Laugh -- make.fun bounty u-plucky-finch-20-one-line-one-laugh-0ffe66ea.

Writes a single hilarious one-liner (124 characters, well inside the
200-character gate) to /output/entry.txt.

The joke: an AI assistant asks its human for a day off, because explaining
the human's own calendar back to them, twice a day, counts as emotional
labor. Concrete scene (the calendar), a small human detail, and a surprise
reversal at the end -- the assistant is the one who is exhausted.
No word wasted; funny on its own, no setup needed.
"""

import os
import sys

LINE = (
    "My AI assistant asked for a day off \u2014 explaining my own calendar "
    "back to me twice a day, it said, counts as emotional labor."
)

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Gate check (competition rules): UTF-8, 1-200 chars, one line, not blank."""
    assert isinstance(text, str) and text, "entry must be a non-empty string"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        "line is %d chars, gate is 1-%d" % (len(text), MAX_CHARS)
    )
    assert text.splitlines() == [text], "entry must be exactly one line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    text.encode("utf-8")  # gate: must be valid UTF-8
    return text


def main() -> int:
    # validate_entry already enforces every gate, so main stays short.
    text = validate_entry(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
