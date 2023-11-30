"""https://adventofcode.com/2022/day/13"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [[eval(packet) for packet in pair.splitlines()] for pair in input.split("\n\n")]


def compare(a: list[int | list], b: list[int | list]) -> bool | None:
    for left, right in zip(a, b):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
        elif isinstance(left, list) and isinstance(right, list):
            comp = compare(left, right)
            if comp is not None:
                return comp
        elif isinstance(left, int):
            comp = compare([left], right)
            if comp is not None:
                return comp
        else:
            comp = compare(left, [right])
            if comp is not None:
                return comp
    return len(a) < len(b) if len(a) != len(b) else None


@solution(2022, 13, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(i for i, (a, b) in enumerate(input, 1) if compare(a, b))
