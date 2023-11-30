"""https://adventofcode.com/2015/day/1"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2015, 1, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return input.count("(") - input.count(")")
