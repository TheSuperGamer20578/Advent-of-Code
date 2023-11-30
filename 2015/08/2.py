"""https://adventofcode.com/2015/day/8#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [line.strip() for line in input.splitlines()]


@solution(2015, 8, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(line.count('"') + line.count("\\") + 2 for line in input)
