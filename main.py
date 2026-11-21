"""Make the AI judge feel awe - entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No network, no input, fully deterministic.

The text, in short lines that slow the reading down: floating in warm
shallows at dusk, ears under the surface, the world gone soft and far
away, and starlight that set out before there were eyes to see it,
arriving to rest on the water that has been holding you all along.
"""

from pathlib import Path

TEXT = """You float in the warm shallows.
Your ears slip under.
The world goes soft, far away —
only your heart, slow and close.
Above you, the first stars come out:
light that set out before there were eyes to see it,
crossing the darkness,
to rest on the water holding you all along."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
