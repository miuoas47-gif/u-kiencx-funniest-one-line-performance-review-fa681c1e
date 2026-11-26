#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun bounty entry.

Prints exactly one line: a performance review, no arguments needed.
Fully deterministic: no time, no randomness, no network.
"""

REVIEW = (
    "A model employee: punctual to every meeting, allergic to every "
    "deadline, and the only person who can make 'per my last email' "
    "sound like a threat."
)


def main() -> None:
    print(REVIEW)


if __name__ == "__main__":
    main()
