"""https://adventofcode.com/2015/day/8"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [(line.strip(), eval(line)) for line in input.splitlines()]


@solution(2015, 8, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(len(code) - len(string) for code, string in input)
