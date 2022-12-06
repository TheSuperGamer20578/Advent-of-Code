"""https://adventofcode.com/2022/day/6#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    last = list(input[:14])
    for i, char in enumerate(input):
        last.append(char)
        last.pop(0)
        if not any(last.count(c) > 1 for c in last):
            return i + 1


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
