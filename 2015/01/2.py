"""https://adventofcode.com/2015/day/1#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


def solve(input: Any) -> Answer:
    """Solve the puzzle"""
    floor = 0
    for i, char in enumerate(input):
        match char:
            case "(":
                floor += 1
            case ")":
                floor -= 1
        if floor < 0:
            return i + 1


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
