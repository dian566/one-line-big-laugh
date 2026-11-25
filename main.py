# One Line, Big Laugh — the smart-speaker therapy joke, to /output/entry.txt.
# A single line: the speaker heard "I am fine" and took it literally.

import pathlib

# The joke, in two halves split at the comma for readability.
# (Split only for line length — the entry itself is one line.)
JOKE_FIRST = "My smart speaker heard me say I am fine, "
JOKE_SECOND = "so now it whispers ads for therapy in my sleep."


def assemble_joke() -> str:
    """Put the two halves of the joke back together."""
    return JOKE_FIRST + JOKE_SECOND


def write_line() -> None:
    """Write the joke to /output/entry.txt, exactly as composed."""
    target = pathlib.Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(assemble_joke(), encoding="utf-8")


if __name__ == "__main__":  # run the joke writer
    write_line()
