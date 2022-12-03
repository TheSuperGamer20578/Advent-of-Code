"""https://adventofcode.com/2022/day/3"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [(set(sack[:len(sack) // 2]), set(sack[len(sack) // 2:])) for sack in input.splitlines()]


def priority(char: str) -> int:
    """Get the priority of an item"""
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return sum(priority((first & last).pop()) for first, last in input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
