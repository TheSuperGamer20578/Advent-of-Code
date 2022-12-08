"""https://adventofcode.com/2022/day/8"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [list(map(int, row)) for row in input.splitlines()]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    visible = set()
    for x, row in enumerate(input):
        highest = -1
        for y, tree in enumerate(row):
            if tree > highest:
                highest = tree
                visible.add((x, y))
    for y in range(len(input[0])):
        highest = -1
        for x, row in enumerate(input):
            tree = row[y]
            if tree > highest:
                highest = tree
                visible.add((x, y))
    for x, row in list(enumerate(input))[::-1]:
        highest = -1
        for y, tree in list(enumerate(row))[::-1]:
            if tree > highest:
                highest = tree
                visible.add((x, y))
    for y in range(len(input[0]))[::-1]:
        highest = -1
        for x, row in list(enumerate(input))[::-1]:
            tree = row[y]
            if tree > highest:
                highest = tree
                visible.add((x, y))
    return len(visible)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
