"""https://adventofcode.com/2022/day/6#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2022, 6, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    last = list(input[:14])
    for i, char in enumerate(input):
        last.append(char)
        last.pop(0)
        if not any(last.count(c) > 1 for c in last):
            return i + 1
