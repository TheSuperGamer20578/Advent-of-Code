"""https://adventofcode.com/2022/day/9"""
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


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    tx, ty = hx, hy = 0, 0
    visited = {(tx, ty)}
    for (dx, dy), n in input:
        for _ in range(n):
            hx += dx
            hy += dy
            distance = hx - tx, hy - ty
            if abs(distance[0]) > 1 or abs(distance[1]) > 1:
                tx += sign(distance[0])
                ty += sign(distance[1])
            visited.add((tx, ty))
    return len(visited)



if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
