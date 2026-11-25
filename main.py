"""One Star for Monday — entry program (pure stdlib, deterministic).

Writes the one-line review to /output/entry.txt.
The line is judged against the published judge brief: a one-star review of
Monday written as if Monday were a restaurant, at most 25 words, that reads
like a real diner's complaint (a table, a server, a dish or a bill gone
wrong), lands the joke about Monday itself, and is short enough to retype
into a group chat without trimming a word.
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# Every element is a diner's complaint: the server, a wobbly table, the dish
# (cold emails — the Monday special), and the bill (the whole weekend). The
# joke only works for Monday: no other day serves cold emails and charges
# your weekend. 19 words, 100 characters, plain text, no hashtags, no explanation.
ENTRY_TEXT = "One star. The server sat me at a wobbly table, served cold emails, and charged me my entire weekend."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
