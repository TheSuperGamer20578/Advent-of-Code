"""https://adventofcode.com/2023/day/18"""
from shapely import Polygon

from aoc import *


@solution(2023, 18, 1)
def part1(data: str) -> int:
    trench = [(0, 0)]
    length = 1
    x, y = 0, 0
    for line in data.splitlines():
        direction, distance, _ = line.split()
        distance = int(distance)
        dx, dy = {
            "U": (0, -1),
            "D": (0, 1),
            "L": (-1, 0),
            "R": (1, 0),
        }[direction]
        distance = int(distance)
        x += dx * distance
        y += dy * distance
        trench.append((x, y))
        length += distance
    polygon = Polygon(trench)
    return int(polygon.area + length/2 + 1)


@solution(2023, 18, 2)
def part2(data: str) -> int:
    trench = [(0, 0)]
    length = 1
    x, y = 0, 0
    for line in data.splitlines():
        instruction = line.split()[-1][2:-1]
        distance = int(instruction[:5], 16)
        direction = int(instruction[5:], 16)
        dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][direction]
        distance = int(distance)
        x += dx * distance
        y += dy * distance
        trench.append((x, y))
        length += distance
    polygon = Polygon(trench)
    return int(polygon.area + length/2 + 1)
