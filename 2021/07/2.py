"""https://adventofcode.com/2021/day/7#part2"""
import math
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(num) for num in input.split(",")]


@solution(2021, 7, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    best = math.inf
    for position in range(min(input), max(input) + 1):
        fuel = 0
        for crab in input:
            crab_fuel = abs(crab - position)
            fuel += (crab_fuel * (crab_fuel+1)) // 2
        if fuel < best:
            best = fuel
    return best
