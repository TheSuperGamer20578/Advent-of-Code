"""https://adventofcode.com/2021/day/13"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    page, folds = input.split("\n\n")
    folds = [(0 if fold[0] == "x" else 1, int(fold.split("=")[1])) for fold in folds.replace("fold along ", "").splitlines()]
    page = {tuple(map(int, position.split(","))) for position in page.splitlines()}
    return page, folds


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    page, folds = input
    axis, position = folds[0]
    page = {pos if pos[axis] < position else ((pos[0] if axis else position*2 - pos[0]),(pos[1] if not axis else position*2 - pos[1])) for pos in page.copy() if pos[axis] != position}
    return len(page)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
