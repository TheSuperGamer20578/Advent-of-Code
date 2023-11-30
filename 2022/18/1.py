"""https://adventofcode.com/2022/day/18"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return {tuple(map(int, line.split(","))) for line in input.splitlines()}


@solution(2022, 18, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    surface = 0
    for x, y, z in input:
        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            if (x + dx, y + dy, z + dz) not in input:
                surface += 1
    return surface
