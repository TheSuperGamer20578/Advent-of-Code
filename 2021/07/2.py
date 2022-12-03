"""https://adventofcode.com/2021/day/7#part2"""
import math
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(num) for num in input.split(",")]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    best = math.inf
    for position in range(min(input), max(input) + 1):
        fuel = 0
        for crab in input:
            crab_fuel = abs(crab - position)
            fuel += (crab_fuel * (crab_fuel+1)) // 2
        if fuel < best:
            best = fuel
    return best


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
