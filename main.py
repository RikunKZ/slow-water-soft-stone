"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No network, no input, fully deterministic.

The text, in short lines that slow the reading down: your grandfather
rows you home across the river at dusk; you lie in the bow under his
wool coat; a slow stroke, a glide, drops off the oar; a mile of still
water below, and above, starlight older than the hills, older than
the river, while the river carries you to sleep.
"""

from pathlib import Path

TEXT = """Your grandfather rows you home across the river at dusk.
You lie in the bow, under his wool coat.
A slow stroke. A glide. Drops off the oar.
Below a mile of still water.
Above the first stars:
light older than the hills,
older than the river —
and the river carries you to sleep."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
