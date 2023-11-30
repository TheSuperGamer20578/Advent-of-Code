"""https://adventofcode.com/2019/day/1"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(mass) for mass in input.splitlines()]


@solution(2019, 1, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(mass // 3 - 2 for mass in input)
