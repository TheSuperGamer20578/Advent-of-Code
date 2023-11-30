"""https://adventofcode.com/2021/day/7"""
import statistics
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(num) for num in input.split(",")]


@solution(2021, 7, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    position = int(statistics.median(input))
    fuel = 0
    for crab in input:
        fuel += abs(crab - position)
    return fuel
