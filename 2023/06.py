"""https://adventofcode.com/2023/day/6"""
from math import sqrt, floor, ceil, prod

from aoc import *


def solve(time: int, record: int) -> int:
    px = (time + sqrt(time**2 - 4*record))/2
    nx = (time - sqrt(time**2 - 4*record))/2
    return max(floor(max(px, nx) - 1e-10), 0) - ceil(min(px, nx) + 1e-10) + 1


@solution(2023, 6, 1)
def part1(data: str) -> int:
    [times, records] = data.splitlines()
    races = zip(map(int, times.split()[1:]), map(int, records.split()[1:]))
    return prod(solve(time, record) for time, record in races)


@solution(2023, 6, 2)
def part2(data: str) -> int:
    [time, record] = data.splitlines()
    time = int(time.split(" ", 1)[1].replace(" ", ""))
    record = int(record.split(" ", 1)[1].replace(" ", ""))
    return solve(time, record)
