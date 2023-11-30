"""https://adventofcode.com/2019/day/1#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(mass) for mass in input.splitlines()]


@solution(2019, 1, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    fuel = sum(mass // 3 - 2 for mass in input)
    module = fuel
    while module > 0:
        module = module // 3 - 2
        fuel += max(module, 0)
    return fuel
