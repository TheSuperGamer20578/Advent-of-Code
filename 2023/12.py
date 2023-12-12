"""https://adventofcode.com/2023/day/12"""
from itertools import repeat
from functools import cache

from aoc import *


@cache
def solve(springs: tuple[bool | None], counts: tuple[int], block_length: int = 0):
    if len(springs) == 0:
        if len(counts) == 0 and block_length == 0:
            return 1
        if len(counts) == 1 and block_length == counts[0]:
            return 1
        return 0
    count = 0
    for value in [True, False] if springs[0] is None else [springs[0]]:
        if value:
            count += solve(springs[1:], counts, block_length + 1)
        else:
            if block_length == 0:
                count += solve(springs[1:], counts, 0)
            elif len(counts) > 0 and block_length == counts[0]:
                count += solve(springs[1:], counts[1:], 0)
    return count


@solution(2023, 12, 1)
def part1(data: str) -> int:
    total = 0
    for row in data.splitlines():
        springs, counts = row.split()
        springs = [{".": False, "#": True, "?": None}[char] for char in springs]
        counts = [int(count) for count in counts.split(",")]
        total += solve(tuple(springs), tuple(counts))
    return total


@solution(2023, 12, 2)
def part2(data: str) -> int:
    total = 0
    for row in data.splitlines():
        springs, counts = row.split()
        springs = [{".": False, "#": True, "?": None}[char] for char in "?".join(repeat(springs, 5))]
        counts = [int(count) for count in counts.split(",")]*5
        total += solve(tuple(springs), tuple(counts))
    return total
