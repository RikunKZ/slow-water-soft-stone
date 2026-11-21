"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No network, no input, fully deterministic.

The text, in short lines that slow the reading down: you lie on the
roof in the warm dark beside your father, neither of you speaking;
below, the town puts out its lights; above, more and more come on —
starlight that left before there were towns, before there were
roofs — and the turning earth carries you both gently to sleep.
"""

from pathlib import Path

TEXT = """You lie on the roof in the warm dark, beside your father.
Neither of you speaks.
Below, the town puts out its lights.
Above, more and more come on:
light that left before there were towns,
before there were roofs —
and the turning earth carries you both
gently to sleep."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
