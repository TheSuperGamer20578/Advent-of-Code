"""https://adventofcode.com/2022/day/18#part2"""
from typing import Any
from collections import deque

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return {tuple(map(int, line.split(","))) for line in input.splitlines()}


outside: set[tuple[int, int, int]] = set()
inside: set[tuple[int, int, int]] = set()
def check_accessible(droplet: set[tuple[int, int, int]], x: int, y: int, z: int, ubx: int, lbx: int, uby: int, lby: int, ubz: int, lbz: int) -> bool:
    global inside, outside
    if (x, y, z) in inside:
        return False
    if (x, y, z) in outside:
        return True
    seen: set[tuple[int, int, int]] = set()
    queue = deque([(x, y, z)])
    while queue:
        x, y, z = queue.popleft()
        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) in seen | droplet:
                continue
            seen.add((nx, ny, nz))
            if not lbx < nx < ubx or not lby < ny < uby or not lbz < nz < ubz:
                outside |= seen
                return True
            queue.append((nx, ny, nz))
    inside |= seen
    return False



@solution(2022, 18, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    ubx = max(cube[0] for cube in input)
    lbx = min(cube[0] for cube in input)
    uby = max(cube[1] for cube in input)
    lby = min(cube[1] for cube in input)
    ubz = max(cube[2] for cube in input)
    lbz = min(cube[2] for cube in input)
    surface = 0
    for x, y, z in input:
        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) not in input and check_accessible(input, nx, ny, nz, ubx, lbx, uby, lby, ubz, lbz):
                surface += 1
    return surface
