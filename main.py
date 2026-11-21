"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No network, no input, fully deterministic.

The text, in short lines that slow the reading down: your grandfather
rows you home across the river at dusk; you lie in the bow under his
jacket; a slow stroke, a glide, water against wood; the river older
than any village, and the first stars coming out in it.
"""

from pathlib import Path

TEXT = """Your grandfather rows you across the river at dusk.
You lie in the bow, under his jacket.
A slow stroke. A glide. Water against wood.
The river was old before any village,
and the first stars come out in it,
one here, one there,
as if the sky were drifting home to sleep."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
