"""https://adventofcode.com/2023/day/21"""
from collections import deque
from math import ceil
from typing import Callable

from aoc import *


def parse(data: str) -> tuple[set[tuple[int, int]], int, int, int, int]:
    rows = data.splitlines()
    start = data.index("S")
    sx, sy = start % (len(rows[0])-1), start // len(rows[0])
    garden = {(x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c == "."}
    garden.add((sx, sy))
    return garden, sx, sy, len(rows[0]), len(rows)


def solve(garden: set[tuple[int, int]], start_x: int, start_y: int, width: int, height: int, steps: int, check: Callable[[int, int, int], None]):
    queue = deque([(start_x, start_y, 0)])
    seen = set()
    while queue:
        x, y, d = queue.popleft()
        check(x, y, d)
        if d == steps:
            continue
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if (nx % width, ny % height) not in garden:
                continue
            queue.append((nx, ny, d + 1))


@solution(2023, 21, 1)
def part1(data: str) -> int:
    garden, sx, sy, width, height = parse(data)
    accessible = set()

    def check(x: int, y: int, d: int):
        if d % 2 == 0:
            accessible.add((x, y))

    solve(garden, sx, sy, width, height, 64, check)
    return len(accessible)


@solution(2023, 21, 2)
def part2(data: str) -> int:
    garden, sx, sy, width, height = parse(data)
    assert width == height
    assert sx == sy
    assert (26501365 - sx) % width == 0
    t = [set(), set(), set()]

    def check(x: int, y: int, d: int):
        ti = ceil((d-sx)/width)
        if d % 2 == 1:
            t[2 if ti == 1 else ti].add((x, y))
        elif ti <= 1:
            t[1].add((x, y))

    solve(garden, sx, sy, width, height, sx + 2*width, check)
    n = 26501365 // width
    t[2] |= t[0]
    t = list(map(len, t))
    return (n**2 - n) * ((t[2]+t[0])//2 - t[1]) + n*(t[1]-t[0]) + t[0]
