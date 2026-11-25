#!/usr/bin/env python3
"""One-Liner Laugh Lab - make.fun entry (u-suroso-69-one-liner-laugh-lab-6ccf3aae).

Writes one original one-line comedy joke to /output/entry.txt
(falling back to ./output/entry.txt when /output is not writable).
Python 3.13 stdlib only: no dependencies, no network, deterministic.
"""

from pathlib import Path

# v3 (final) - "four hours" puts a clock on the interrogation room: a
# concrete number beats vague "hours", and the sock's silence earns the
# twist. 87 chars, one line, deadpan throughout.
JOKE = "I gave the sock four hours to talk. It said nothing, so I ate the evidence. Case closed."


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text, 1-200 characters, one line, not blank."""
    chars = len(text)
    if not 1 <= chars <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {chars}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(JOKE)
    here = Path(__file__).resolve().parent
    last_error: OSError | None = None
    for target in (Path("/output/entry.txt"), here / "output" / "entry.txt"):
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(JOKE, encoding="utf-8")
            print(f"wrote {len(JOKE)} chars to {target}")
            return
        except OSError as err:
            last_error = err
    if last_error is not None:
        raise last_error


if __name__ == "__main__":
    main()
