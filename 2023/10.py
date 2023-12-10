"""https://adventofcode.com/2023/day/10"""
from itertools import product

from shapely import Polygon, Point
from aoc import *

CONNECTIONS = {
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
    "L": {(0, -1), (1, 0)},
    "J": {(0, -1), (-1, 0)},
    "7": {(0, 1), (-1, 0)},
    "F": {(0, 1), (1, 0)},
}


def follow(data: str) -> tuple[Polygon, set[tuple[int, int]]]:
    lines = data.splitlines()
    start = data.find("S")
    lx, ly = x, y = start % (len(lines[0]) + 1), start // (len(lines[0]) + 1)
    for dx, dy in {(0, 1), (1, 0), (0, -1), (-1, 0)}:
        if (-dx, -dy) in CONNECTIONS[lines[y + dy][x + dx]]:
            x, y = x + dx, y + dy
            break
    else:
        raise ValueError("Invalid start")
    loop = [(lx, ly)]
    while True:
        loop.append((x, y))
        if lines[y][x] == "S":
            break
        for dx, dy in CONNECTIONS[lines[y][x]]:
            if (x + dx, y + dy) != (lx, ly):
                lx, ly = x, y
                x, y = x + dx, y + dy
                break
    return Polygon(loop), set(loop)


@solution(2023, 10, 1)
def part1(data: str) -> int:
    _, loop = follow(data)
    return len(loop) // 2


@solution(2023, 10, 2)
def part2(data: str) -> int:
    polygon, loop = follow(data)
    x1, y1, x2, y2 = polygon.bounds
    return sum(
        polygon.contains(Point(x, y))
        for x, y in product(range(int(x1), int(x2) + 1), range(int(y1), int(y2) + 1))
        if (x, y) not in loop
    )
