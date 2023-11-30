"""https://adventofcode.com/2015/day/6"""
from typing import Any
from collections import defaultdict
import re

from aoc import *

REGEX = re.compile(r"^(turn (?:on|off)|toggle) (\d+),(\d+) through (\d+),(\d+)$", re.MULTILINE)


def parse(input: str) -> Any:
    """Parse the input"""
    return [match.groups() for match in REGEX.finditer(input)]


# TODO: Implement irange()
# @solution(2015, 6, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    grid = defaultdict(bool)
    for instruction, x1, y1, x2, y2 in input:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        match instruction:
            case "turn on":
                for x in irange(x1, x2):
                    for y in irange(y1, y2):
                        grid[x, y] = True
            case "turn off":
                for x in irange(x1, x2):
                    for y in irange(y1, y2):
                        grid[x, y] = False
            case "toggle":
                for x in irange(x1, x2):
                    for y in irange(y1, y2):
                        grid[x, y] = not grid[x, y]
    return sum(grid.values())
