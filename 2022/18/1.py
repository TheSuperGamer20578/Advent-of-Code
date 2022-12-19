"""https://adventofcode.com/2022/day/18"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return {tuple(map(int, line.split(","))) for line in input.splitlines()}


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    surface = 0
    for x, y, z in input:
        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            if (x + dx, y + dy, z + dz) not in input:
                surface += 1
    return surface


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
