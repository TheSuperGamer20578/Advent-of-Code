"""https://adventofcode.com/2021/day/7"""
import statistics
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(num) for num in input.split(",")]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    position = int(statistics.median(input))
    fuel = 0
    for crab in input:
        fuel += abs(crab - position)
    return fuel


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
