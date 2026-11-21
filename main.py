"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No network, no input, fully deterministic.
"""

from pathlib import Path

TEXT = (
    "Somewhere, a river has been smoothing the same stone for ten thousand "
    "years, in no hurry at all. It is still there now, cool and patient, and "
    "the stone is almost soft. The water simply keeps going, and so, "
    "quietly, do you."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
