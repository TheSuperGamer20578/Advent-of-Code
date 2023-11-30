"""https://adventofcode.com/2022/day/9#part2"""
from typing import Any

from aoc import *


DIRECTIONS = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def parse(input: str) -> Any:
    """Parse the input"""
    return [(lambda d, n: (DIRECTIONS[d], int(n)))(*instruction.split(" ")) for instruction in input.splitlines()]


def sign(n: int) -> int:
    if n < 0:
        return -1
    if n > 0:
        return 1
    return 0


def adjust(head, tail):
    hx, hy = head
    tx, ty = tail
    dx, dy = tx - hx, ty - hy
    if abs(dx)<=1 and abs(dy)<=1:
        pass
    elif abs(dx) > 1 < abs(dy):
        tx = hx + sign(dx)
        ty = hy + sign(dy)
    elif abs(dx) > 1:
        tx = hx + sign(dx)
        ty = hy
    elif abs(dy) > 1:
        tx = hx
        ty = hy + sign(dy)
    return tx, ty


@solution(2022, 9, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    hx, hy = 0, 0
    tail = [(hx, hy)] * 9
    visited = {(hx, hy)}
    for (dx, dy), n in input:
        for _ in range(n):
            hx += dx
            hy += dy
            tail[0] = adjust((hx, hy), tail[0])
            for i in range(1, len(tail)):
                tail[i] = adjust(tail[i-1], tail[i])
            visited.add((*tail[-1],))
    return len(visited)

