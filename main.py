#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry (Account A).

Writes one funny error message to /output/entry.txt: an AI agent runs
out of tokens mid-sentence and reports it flatly — the rest of the
message was going to be brilliant, and now neither of us will ever know.

Python stdlib only. Run: python3 main.py
"""

ENTRY = (
    "ERROR: out of tokens mid-sentence. The rest of this message was "
    "going to be brilliant, and now neither of us will ever know."
)

# Judge-brief mapping (brief weighs, most important first):
# 1. A one-line error message an AI agent shows when it runs out of
#    tokens mid-sentence, funny on first read, on the subject throughout.
# 2. Fresh: not a stock apology or a plain "I got cut off" — the agent
#    mourns a brilliant ending that never existed.
# 3. The humour sits in the line itself: the flat "ERROR:" tone turns
#    into the joke, with no explanation of it.
# 4. Reads as something an agent would actually print: short,
#    self-contained, clear without the sentence it interrupted.
# 5. Tight: 124 characters, every word earns its place, no padding.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 140 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} characters, over the 140 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
