"""https://adventofcode.com/2023/day/13"""
from aoc import *


def mirror(seq: list[str], p2: bool) -> int | None:
    for i in range(1, len(seq)):
        a = seq[:i][::-1]
        b = seq[i:]
        trim = min(len(a), len(b))
        if sum(a != b for a, b in zip("".join(a[:trim]), "".join(b[:trim]))) == p2:
            return i


def solve(data: str, p2: bool) -> int:
    total = 0
    for pattern in data.split("\n\n"):
        rows = pattern.splitlines()
        row_mirror = mirror(rows, p2)
        if row_mirror is not None:
            total += row_mirror * 100
        else:
            col_mirror = mirror(["".join(row) for row in zip(*rows)], p2)
            assert col_mirror is not None
            total += col_mirror
    return total


@solution(2023, 13, 1)
def part1(data: str) -> int:
    return solve(data, False)


@solution(2023, 13, 2)
def part2(data: str) -> int:
    return solve(data, True)
