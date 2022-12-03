"""https://adventofcode.com/2015/day/3#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


def solve(input: Any) -> Answer:
    """Solve the puzzle"""
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
    return Answer(len(visited))


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
