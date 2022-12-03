"""https://adventofcode.com/2021/day/25"""
from typing import Any
from itertools import count

from aoc import *


def parse(input: str) -> tuple[int, int, dict[tuple[int, int], bool]]:
    """Parse the input"""
    grid: dict[tuple[int, int], bool | None] = {}
    for y, row in enumerate(input.splitlines()):
        for x, char in enumerate(row):
            if char == ".":
                continue
            grid[x, y] = char == ">"
    return len(input.splitlines()[0]), len(input.splitlines()), grid


def wrap(xs: int, ys: int, x: int, y: int, dx: int, dy: int) -> tuple[int, int]:
    x += dx
    y += dy
    x %= xs
    y %= ys
    return x, y


def solve(input: tuple[int, int, dict[tuple[int, int], bool]]) -> int | str | Answer:
    """Solve the puzzle"""
    xs, ys, grid = input
    for step in count():
        old = grid.copy()
        new = grid.copy()
        for (x, y), spot in grid.items():
            if spot is True:
                if wrap(xs, ys, x, y, 1, 0) not in grid:
                    del new[x, y]
                    new[wrap(xs, ys, x, y, 1, 0)] = True
        grid = new
        new = grid.copy()
        for (x, y), spot in grid.items():
            if spot is False:
                if wrap(xs, ys, x, y, 0, 1) not in grid:
                    del new[x, y]
                    new[wrap(xs, ys, x, y, 0, 1)] = False
        if grid == old:
            return Answer(step + 1)
        grid = new


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
