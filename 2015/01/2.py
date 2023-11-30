"""https://adventofcode.com/2015/day/1#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2015, 1, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    floor = 0
    for i, char in enumerate(input):
        match char:
            case "(":
                floor += 1
            case ")":
                floor -= 1
        if floor < 0:
            return i + 1
