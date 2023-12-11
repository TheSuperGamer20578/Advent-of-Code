"""https://adventofcode.com/2023/day/11"""
from itertools import combinations

from aoc import *


def solve(data: str, scale: int) -> int:
    galaxies = {(x, y) for y, row in enumerate(data.splitlines()) for x, c in enumerate(row) if c == "#"}
    empty_rows = set(range(len(data.splitlines()))) - {y for _, y in galaxies}
    empty_cols = set(range(len(data.splitlines()[0]))) - {x for x, _ in galaxies}

    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        dx = abs(x1 - x2) + (scale-1)*sum(min(x1, x2) <= x <= max(x1, x2) for x in empty_cols)
        dy = abs(y1 - y2) + (scale-1)*sum(min(y1, y2) <= y <= max(y1, y2) for y in empty_rows)
        total += dx + dy
    return total


@solution(2023, 11, 1)
def part1(data: str) -> int:
    return solve(data, 2)


@solution(2023, 11, 2)
def part2(data: str) -> int:
    return solve(data, 1_000_000)
