"""https://adventofcode.com/2015/day/6#part2"""
from typing import Any
from collections import defaultdict
import re

from aoc import *

REGEX = re.compile(r"^(turn (?:on|off)|toggle) (\d+),(\d+) through (\d+),(\d+)$", re.MULTILINE)


def parse(input: str) -> Any:
    """Parse the input"""
    return [match.groups() for match in REGEX.finditer(input)]


def solve(input: Any) -> str | int | Answer:
    """Solve the puzzle"""
    grid = defaultdict(int)
    for instruction, x1, y1, x2, y2 in input:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        match instruction:
            case "turn on":
                for x in irange(x1, x2):
                    for y in irange(y1, y2):
                        grid[x, y] += 1
            case "turn off":
                for x in irange(x1, x2):
                    for y in irange(y1, y2):
                        grid[x, y] = max(grid[x, y] - 1, 0)
            case "toggle":
                for x in irange(x1, x2):
                    for y in irange(y1, y2):
                        grid[x, y] += 2
    return sum(grid.values())


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
