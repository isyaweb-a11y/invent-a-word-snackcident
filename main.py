"""Invent a Word We Need.

One new English word that does not exist yet, defined in one clear line
of at most 140 characters. The word names a small daily moment with no
name: opening the fridge for one thing and leaving with a full meal, a
sense of shame, and no memory of deciding. Gate: 1-140 characters.
"""

ENTRY = (
    "snackcident (n.) — opening the fridge for one thing and leaving "
    "with a full meal, a sense of shame, and no memory of deciding."
)


def check_definition(text: str) -> str:
    """A new word needs its name, its part of speech, and a clear definition."""
    assert text.startswith("snackcident (n.)"), "entry must open with the new word"
    assert "fridge" in text, "definition must name the scene"
    assert "no memory of deciding" in text, "definition must land on the punchline"
    return text


def main() -> None:
    text = check_definition(" ".join(ENTRY.split()))
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
