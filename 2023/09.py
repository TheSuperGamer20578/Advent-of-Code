"""https://adventofcode.com/2023/day/9"""
from aoc import *


def extrapolate(seq: list[int], p2: bool) -> int:
    if all(a == 0 for a in seq):
        return 0
    return seq[-(not p2)] + extrapolate([a - b for a, b in zip(seq[1:], seq)], p2)*(-p2*2+1)


@solution(2023, 9, 1)
def part1(data: str) -> int:
    return sum(
        extrapolate([int(num) for num in line.split()], False)
        for line in data.splitlines()
    )


@solution(2023, 9, 2)
def part2(data: str) -> int:
    return sum(
        extrapolate([int(num) for num in line.split()], True)
        for line in data.splitlines()
    )
