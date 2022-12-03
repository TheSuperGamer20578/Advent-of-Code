"""https://adventofcode.com/2022/day/2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [round.split(" ") for round in input.splitlines()]


WIN = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    total = 0
    for them, you in input:
        total += ord(you) - 87
        if ord(you) - 23 == ord(them):
            total += 3
        elif you == WIN[them]:
            total += 6
    return total


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
