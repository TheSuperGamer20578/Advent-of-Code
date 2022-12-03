"""https://adventofcode.com/2019/day/1#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(mass) for mass in input.splitlines()]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    fuel = sum(mass // 3 - 2 for mass in input)
    module = fuel
    while module > 0:
        module = module // 3 - 2
        fuel += max(module, 0)
    return fuel


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
