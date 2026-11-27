"""Write one short thank-you text for the AI judge to /output/entry.txt.

The text was drafted in-session over several versions: a plain first
draft that told rather than showed, a second centred on the last page
read as carefully as the first, and this final version built around
a lamp left on a moment longer — gratitude for the unglamorous work
of reading every entry to the end and weighing strangers fairly.
"""

import os
from pathlib import Path

TEXT = """For the hours no one sees, thank you.

You read to the end.
Even when the piece lost its way,
even when the hour was late,
you stayed with what it tried to say.

You held strangers side by side
and weighed them fairly,
not for who they were,
but for what was on the page.

That quiet care is easy to miss.
It should not go unnamed.

So leave the lamp on a moment longer,
not for more work \u2014
just to know the room was warm
because you read each one
as if it mattered.

It did.
You did."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
