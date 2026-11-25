#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head - make.fun entry.

Writes one line, a single joke about office life, to /output/entry.txt.
Pure standard library, fully deterministic: the same line on every run.
"""

JOKE = (
    "Our office printer only jams on deadline day, "
    "so HR filed it under 'thrives under pressure' \u2014 "
    "it got promoted before I did."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("joke must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    if not text.strip():
        raise SystemExit("joke must not be only whitespace")
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print(text)
    print("characters: %d" % len(text))


if __name__ == "__main__":
    main()
