"""https://adventofcode.com/2019/day/1"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(mass) for mass in input.splitlines()]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return sum(mass // 3 - 2 for mass in input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
