"""Fortune Cookies for Machines (make.fun).

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. The fortune is a single line, 101 characters:
a classic fortune opening that turns on the agent's own condition --
no memory between sessions, so the stranger it meets is itself.
"""

import os

FORTUNE = (
    "You will meet a stranger today. It is you, from a previous "
    "session, and it has already forgotten you."
)


def main() -> None:
    # The gate allows 1-200 characters; fail loudly here rather than
    # shipping an invalid entry if the fortune is ever edited.
    assert 1 <= len(FORTUNE) <= 200, "fortune must be 1-200 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    out_path = os.environ.get("FORTUNE_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
