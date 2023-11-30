"""https://adventofcode.com/2015/day/3#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2015, 3, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    x = y = rx = ry = 0
    visited = {(0, 0)}
    for char in input:
        match char:
            case "<":
                x -= 1
            case ">":
                x += 1
            case "^":
                y += 1
            case "v":
                y -= 1
        visited.add((x, y))
        x, y, rx, ry = rx, ry, x, y
    return len(visited)
